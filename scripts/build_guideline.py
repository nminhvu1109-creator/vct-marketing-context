"""Dựng bản HTML và bản Word của một guideline từ file Markdown gốc.

Cách dùng:
    python scripts/build_guideline.py [đường dẫn file .md]

Mặc định: guidelines/facebook_it/01_Facebook_Guideline_IT.md
File ra nằm cạnh file .md, cùng tên, đuôi .html và .docx.
Cần: pandoc, python-docx, beautifulsoup4.
"""
import base64
import re
import subprocess
import sys
from pathlib import Path

from bs4 import BeautifulSoup
from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor, Twips

ROOT = Path(__file__).resolve().parent.parent
FONT_DIR = ROOT / "assets/fonts/source-sans-3"
LOGO_WHITE = ROOT / "assets/logo/vc-logo-horizontal-white.svg"
ICON_WHITE = ROOT / "assets/logo/vc-logo-icon-white.svg"
CSS = Path(__file__).with_name("guideline.css")
DOCX_TEMPLATE = Path(__file__).with_name("guideline_template.docx")

EXTRA_CSS = """
/* Bổ sung cho bản dựng từ Markdown */
main ul,main ol{margin:6px 0 14px;padding-left:22px}
main li{margin:5px 0}
main ol.check{list-style:none;padding:0;counter-reset:c}
main ol.check li{counter-increment:c;display:grid;grid-template-columns:34px minmax(0,1fr);gap:8px;align-items:start;background:#fff;border:1px solid var(--line);border-radius:10px;padding:11px 14px;margin:8px 0}
main ol.check li::before{content:counter(c);font:800 18px/1.3 var(--f);color:var(--tc)}
th.yes{background:var(--moss-100);color:var(--moss)}
th.no{background:var(--tc-50);color:var(--tc-d)}
td .fill,.post .fill{background:var(--och-50);color:var(--och-600);border-radius:3px;padding:0 2px;font-weight:600}
table.sum td:first-child{color:var(--tc-d);white-space:nowrap}
table.sum td:last-child{white-space:nowrap;color:var(--soft);font-weight:600}
.post{max-width:600px}
h4{scroll-margin-top:16px}
hr{display:none}
@media (max-width:640px){table.sum td:first-child,table.sum td:last-child{white-space:normal}}
@media (max-width:640px){.tw table.w3{min-width:520px}.tw table.w4{min-width:680px}}
"""

YES = {"Ưu tiên", "Nên", "Tạo niềm tin", "Làm bài hấp dẫn", "Hãy cho thấy", "Tự nhiên hơn", "Bằng"}
NO = {"Hơn", "Tránh", "Làm mất niềm tin", "Thay vì nói", "Thường gặp", "Nên thay"}


# ---------- HTML ----------

def font_css():
    css = (FONT_DIR / "source-sans-3.css").read_text(encoding="utf-8")

    def embed(m):
        data = base64.b64encode((FONT_DIR / m.group(1)).read_bytes()).decode()
        return f"url(data:font/woff2;base64,{data}) format('woff2')"

    css = re.sub(r"url\(\./([^)]+)\) format\('woff2-variations'\)", embed, css)
    return re.sub(r"/\*.*?\*/\n?", "", css, flags=re.S)


def svg_symbol(path, sid):
    svg = path.read_text(encoding="utf-8")
    view = re.search(r'viewBox="([^"]+)"', svg).group(1)
    inner = re.sub(r"<title.*?</title>", "", svg[svg.index(">") + 1: svg.rindex("</svg>")], flags=re.S)
    return f'<symbol id="{sid}" viewBox="{view}">{inner}</symbol>'


def mark_fill(soup, node):
    """Tô các chỗ điền [..] trong khung bài mẫu."""
    for text in list(node.find_all(string=True)):
        if "[" not in text:
            continue
        parts = re.split(r"(\[[^\]]+\])", str(text))
        frag = []
        for part in parts:
            if part.startswith("[") and part.endswith("]"):
                span = soup.new_tag("span", attrs={"class": "fill"})
                span.string = part
                frag.append(span)
            elif part:
                frag.append(part)
        text.replace_with(*frag)


def build_html(md_path):
    body = subprocess.run(
        ["pandoc", "-f", "gfm", "-t", "html", "--wrap=none", str(md_path)],
        capture_output=True, text=True, check=True,
    ).stdout
    soup = BeautifulSoup(body, "html.parser")
    nodes = [n for n in soup.contents if getattr(n, "name", None)]

    title = nodes[0].get_text()
    meta = nodes[1].get_text()
    lead = re.sub(r"</?code>", "", nodes[2].decode_contents()).replace("\n", "<br>")
    name, market = [t.strip() for t in title.split("·")]

    out, toc, sec_open = [], [], False

    def close_sec():
        nonlocal sec_open
        if sec_open:
            out.append("</section>")
            sec_open = False

    for node in nodes[3:]:
        tag = node.name
        if tag == "hr":
            continue
        if tag == "h1":
            close_sec()
            label, text = [t.strip() for t in node.get_text().split("·", 1)]
            out.append(f'<div class="part"><span class="pn">{label}</span><h2>{text}</h2></div>')
            toc.append(("part", f"{label} · {text}", None))
        elif tag == "h2":
            close_sec()
            text = node.get_text()
            m = re.match(r"(\d+)\.\s+(.*)", text)
            no, text = (m.group(1), m.group(2)) if m else ("", text)
            sid = f"s{no}" if no else "tom-tat"
            badge = f'<span class="no">{no}</span>' if no else ""
            out.append(f'<section class="sec" id="{sid}"><h3 class="st">{badge}{text}</h3>')
            toc.append(("sec", text, (sid, no)))
            sec_open = True
        elif tag == "h3":
            text = node.get_text()
            m = re.match(r"(\d+\.\d+)\s+(.*)", text)
            if m:
                out.append(f'<h4 id="s{m.group(1).replace(".", "-")}"><span class="sn">{m.group(1)}</span>{m.group(2)}</h4>')
            else:
                out.append(f"<h4>{text}</h4>")
        elif tag == "table":
            heads = [th.get_text().strip() for th in node.find_all("th")]
            for th in node.find_all("th"):
                label = th.get_text().strip()
                if label in YES:
                    th["class"] = "yes"
                elif label in NO:
                    th["class"] = "no"
            if len(heads) >= 3:
                node["class"] = "w4" if len(heads) >= 4 else "w3"
            if heads and heads[0] == "Câu hỏi" and heads[-1] == "Mục":
                node["class"] = "sum"
            mark_fill(soup, node)
            out.append(f'<div class="tw">{node}</div>')
        elif tag == "blockquote":
            mark_fill(soup, node)
            out.append(
                '<div class="post"><div class="ph"><div class="pa"><svg viewBox="0 0 2000 1622" aria-hidden="true">'
                '<use href="#vc-iw"/></svg></div><div><div class="pn">Viet Cone Travel · Italiano</div>'
                f'<div class="pt">Khung bài mẫu</div></div></div><div class="pb">{node.decode_contents()}</div></div>'
            )
        elif tag == "ol":
            node["class"] = "check"
            out.append(str(node))
        else:
            out.append(str(node))
    close_sec()

    toc_html, nav_opts, in_list = [], [], False
    for kind, text, ref in toc:
        if kind == "part":
            if in_list:
                toc_html.append("</ol>")
            toc_html.append(f'<div class="part-l">{text}</div><ol>')
            in_list = True
        else:
            sid, no = ref
            if not in_list:
                toc_html.append("<ol>")
                in_list = True
            toc_html.append(f'<li><a href="#{sid}"><span class="n">{no}</span>{text}</a></li>')
            nav_opts.append(f'<option value="#{sid}">{(no + ". ") if no else ""}{text}</option>')
    toc_html.append("</ol>")

    chips = "".join(f"<span>{c.strip()}</span>" for c in meta.split("·")[1:])
    html = f"""<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
{font_css()}
{CSS.read_text(encoding="utf-8")}{EXTRA_CSS}</style>
</head>
<body>
<svg width="0" height="0" style="position:absolute" aria-hidden="true">{svg_symbol(LOGO_WHITE, "vc-h")}{svg_symbol(ICON_WHITE, "vc-iw")}</svg>
<div class="mnav"><select id="mnav" aria-label="Chuyển mục">{"".join(nav_opts)}</select></div>
<div class="layout">
<nav class="toc" aria-label="Mục lục">
<div class="brand">{name}</div>
{"".join(toc_html)}
</nav>
<main>
<div class="wrap">
<header class="cover">
<svg class="logo" viewBox="0 0 2000 1138" role="img" aria-label="Viet Cone Travel"><use href="#vc-h"/></svg>
<div class="kick">Guideline kênh</div>
<h1>{name}<br>{market}</h1>
<p class="lead">{lead}</p>
<div class="meta">{chips}</div>
</header>
{chr(10).join(out)}
<footer>
<div class="fl"><svg class="logo" viewBox="0 0 2000 1138" role="img" aria-label="Viet Cone Travel"><use href="#vc-h"/></svg><span>{meta}</span></div>
</footer>
</div>
</main>
</div>
<script>
(function(){{
  var sel=document.getElementById('mnav');
  if(sel){{sel.addEventListener('change',function(){{location.hash=sel.value;}});}}
  var links=[].slice.call(document.querySelectorAll('.toc a'));
  var map={{}};links.forEach(function(a){{map[a.getAttribute('href').slice(1)]=a;}});
  var secs=[].slice.call(document.querySelectorAll('section.sec'));
  if(!('IntersectionObserver' in window))return;
  var io=new IntersectionObserver(function(es){{
    es.forEach(function(e){{
      if(e.isIntersecting){{
        links.forEach(function(a){{a.classList.remove('on');}});
        var a=map[e.target.id];if(a)a.classList.add('on');
        if(sel&&sel.querySelector('option[value="#'+e.target.id+'"]'))sel.value='#'+e.target.id;
      }}
    }});
  }},{{rootMargin:'-20% 0px -70% 0px'}});
  secs.forEach(function(s){{io.observe(s);}});
}})();
</script>
</body>
</html>
"""
    out_path = md_path.with_suffix(".html")
    out_path.write_text(html, encoding="utf-8")
    return out_path


# ---------- DOCX ----------

TC, MOSS, INK, SOFT = "B0412F", "183C27", "20251F", "53574C"
WIDTH = 9638  # bề rộng vùng chữ, twips


def run(par, text, size=10.5, bold=False, color=INK, italic=False):
    r = par.add_run(text)
    r.font.name = "Arial"
    rpr = r._element.get_or_add_rPr()
    fonts = rpr.find(qn("w:rFonts"))
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        fonts.set(qn(attr), "Arial")
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.italic = italic
    r.font.color.rgb = RGBColor.from_string(color)
    return r


def inline(par, text, size=10.5, color=INK, bold=False):
    """Viết một dòng Markdown có **đậm** và `mã` vào đoạn văn."""
    for part in re.split(r"(\*\*[^*]+\*\*|`[^`]+`)", text):
        if part.startswith("**"):
            run(par, part[2:-2], size, True, color)
        elif part.startswith("`"):
            run(par, part[1:-1], size, bold, MOSS)
        elif part:
            run(par, part, size, bold, color)


def spacing(par, before=0, after=6, line=1.25, keep=False):
    fmt = par.paragraph_format
    fmt.space_before, fmt.space_after, fmt.line_spacing = Pt(before), Pt(after), line
    fmt.keep_with_next = keep
    par.alignment = WD_ALIGN_PARAGRAPH.LEFT


def shade(cell, fill):
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    cell._element.get_or_add_tcPr().append(shd)


def borders(table, color="DDD9CC", left=None):
    pr = table._element.tblPr
    el = OxmlElement("w:tblBorders")
    for side in ("top", "left", "bottom", "right", "insideH", "insideV"):
        b = OxmlElement(f"w:{side}")
        b.set(qn("w:val"), "single")
        b.set(qn("w:sz"), "4")
        b.set(qn("w:color"), color)
        if left and side == "left":
            b.set(qn("w:sz"), "24")
            b.set(qn("w:color"), left)
        if left and side in ("top", "right", "bottom", "insideH", "insideV"):
            b.set(qn("w:val"), "nil")
        el.append(b)
    pr.append(el)


def full_width(table, widths):
    """Cố định bề rộng bảng và từng cột."""
    pr = table._element.tblPr
    for tag, attrs in (("w:tblW", {"w:w": str(WIDTH), "w:type": "dxa"}), ("w:tblLayout", {"w:type": "fixed"})):
        old = pr.find(qn(tag))
        if old is not None:
            pr.remove(old)
        el = OxmlElement(tag)
        for k, v in attrs.items():
            el.set(qn(k), v)
        pr.append(el)
    for col, w in zip(table._element.tblGrid.findall(qn("w:gridCol")), widths):
        col.set(qn("w:w"), str(w))


def no_split(table):
    """Không cắt một hàng qua hai trang."""
    for row in table.rows:
        row._tr.get_or_add_trPr().append(OxmlElement("w:cantSplit"))


def keep_prev(doc):
    """Giữ đoạn dẫn ở cùng trang với bảng hoặc khung bài đứng ngay sau."""
    pars = doc.paragraphs
    if pars:
        pars[-1].paragraph_format.keep_with_next = True


def cell_margins(cell, v=70, h=110):
    mar = OxmlElement("w:tcMar")
    for side, val in (("top", v), ("left", h), ("bottom", v), ("right", h)):
        m = OxmlElement(f"w:{side}")
        m.set(qn("w:w"), str(val))
        m.set(qn("w:type"), "dxa")
        mar.append(m)
    cell._element.get_or_add_tcPr().append(mar)


def col_widths(rows):
    """Chia bề rộng cột theo độ dài chữ, có sàn và trần."""
    n = len(rows[0])
    lens = [max(len(r[i]) for r in rows) for i in range(n)]
    weights = [min(max(l, 9), 60) for l in lens]
    total = sum(weights)
    widths = [int(WIDTH * w / total) for w in weights]
    widths[-1] += WIDTH - sum(widths)
    return widths


def add_table(doc, rows):
    keep_prev(doc)
    widths = col_widths(rows)
    table = doc.add_table(rows=len(rows), cols=len(rows[0]))
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    borders(table)
    full_width(table, widths)
    for i, row in enumerate(rows):
        for j, text in enumerate(row):
            cell = table.cell(i, j)
            cell.width = Twips(widths[j])
            cell_margins(cell)
            par = cell.paragraphs[0]
            spacing(par, 0, 0, 1.15)
            if i == 0:
                shade(cell, "E0EDE4" if text in YES else "FFE2DC" if text in NO else "F3EEE2")
                inline(par, text, 9, INK, bold=True)
            else:
                inline(par, text, 9, INK, bold=(j == 0 and len(row) > 2))
    no_split(table)
    if len(rows) > 1:
        tr_pr = table.rows[0]._tr.get_or_add_trPr()
        head = OxmlElement("w:tblHeader")
        tr_pr.append(head)
    gap = doc.add_paragraph()
    spacing(gap, 0, 4, 1)


def add_quote(doc, lines):
    keep_prev(doc)
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    borders(table, left=MOSS)
    full_width(table, [WIDTH])
    cell = table.cell(0, 0)
    cell.width = Twips(WIDTH)
    shade(cell, "FFFFFF")
    cell_margins(cell, 110, 200)
    no_split(table)
    first = True
    for block in "\n".join(lines).split("\n\n"):
        par = cell.paragraphs[0] if first else cell.add_paragraph()
        first = False
        spacing(par, 0, 5, 1.25)
        for k, line in enumerate(block.split("\n")):
            if k:
                par.add_run().add_break()
            for part in re.split(r"(\[[^\]]+\])", line.rstrip()):
                if part.startswith("["):
                    run(par, part, 10, False, "815E00")
                elif part:
                    run(par, part, 10, False, MOSS)
    gap = doc.add_paragraph()
    spacing(gap, 0, 6, 1)


def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def build_docx(md_path):
    lines = md_path.read_text(encoding="utf-8").split("\n")
    doc = Document(str(DOCX_TEMPLATE))
    body = doc.element.body
    for child in list(body):
        if child.tag != qn("w:sectPr"):
            body.remove(child)

    title, meta = lines[0].lstrip("# ").strip(), lines[2].strip()
    name, market = [t.strip() for t in title.split("·")]
    lead_end = lines.index("---")
    lead = " ".join(l.strip() for l in lines[4:lead_end] if l.strip()).replace("`", "")

    par = doc.add_paragraph(); spacing(par, 0, 80, 1)
    par = doc.add_paragraph(); spacing(par, 0, 4, 1)
    r = run(par, "GUIDELINE KÊNH · TÀI LIỆU NỘI BỘ", 8.5, True, TC)
    par = doc.add_paragraph(); spacing(par, 0, 0, 1.1); run(par, name, 30, True, TC)
    par = doc.add_paragraph(); spacing(par, 0, 14, 1.1); run(par, market, 30, True, MOSS)
    par = doc.add_paragraph(); spacing(par, 0, 24, 1.3); run(par, lead, 12.5, False, INK)
    par = doc.add_paragraph(); spacing(par, 0, 0, 1.2); run(par, meta, 10, False, SOFT)

    i, first_h1, n = lead_end + 1, True, len(lines)
    while i < n:
        line = lines[i]
        s = line.strip()
        if not s or s == "---":
            i += 1
        elif s.startswith("# "):
            par = doc.add_heading(level=1)
            par.paragraph_format.page_break_before = True
            run(par, s[2:], 18, True, TC)
            i += 1
        elif s.startswith("## "):
            par = doc.add_heading(level=2)
            if s == "## Tóm tắt":
                par.paragraph_format.page_break_before = True
            par.alignment = WD_ALIGN_PARAGRAPH.LEFT
            run(par, s[3:], 14, True, MOSS)
            i += 1
        elif s.startswith("### "):
            par = doc.add_heading(level=3)
            par.alignment = WD_ALIGN_PARAGRAPH.LEFT
            run(par, s[4:], 12, True, TC)
            i += 1
        elif s.startswith("|"):
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                if not re.match(r"^\|[\s\-|:]+\|$", lines[i].strip()):
                    rows.append(split_row(lines[i]))
                i += 1
            add_table(doc, rows)
        elif s.startswith(">"):
            quote = []
            while i < n and lines[i].strip().startswith(">"):
                quote.append(re.sub(r"^>\s?", "", lines[i].rstrip("\n")).rstrip())
                i += 1
            add_quote(doc, quote)
        elif re.match(r"^(-|\d+\.)\s", s):
            m = re.match(r"^(-|\d+\.)\s+(.*)", s)
            par = doc.add_paragraph()
            spacing(par, 0, 3, 1.25)
            par.paragraph_format.left_indent = Twips(340)
            par.paragraph_format.first_line_indent = Twips(-340)
            mark = "•" if m.group(1) == "-" else m.group(1)
            run(par, mark + "\t", 10.5, mark != "•", TC)
            par.paragraph_format.tab_stops.add_tab_stop(Twips(340))
            inline(par, m.group(2))
            i += 1
        else:
            par = doc.add_paragraph()
            spacing(par, 0, 6, 1.3)
            inline(par, s)
            i += 1

    out_path = md_path.with_suffix(".docx")
    doc.save(str(out_path))
    return out_path


if __name__ == "__main__":
    md = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "guidelines/facebook_it/01_Facebook_Guideline_IT.md"
    md = md.resolve()
    print(build_html(md))
    print(build_docx(md))
