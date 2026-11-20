"""Xuất logo SVG trong assets/logo sang PNG nền trong suốt (cạnh dài 2000 px) và PDF vector (rộng 200 mm).

Chạy: python scripts/export_logo_assets.py
Cần: pip install playwright, rồi playwright install chromium.
Kết quả: assets/logo/png/, assets/logo/pdf/ (sinh lại được, không commit).
PDF ở hệ RGB; bản CMYK để in cần designer hoặc nhà in chuyển đổi.
"""
import re
from pathlib import Path
from playwright.sync_api import sync_playwright

LOGO = Path(__file__).resolve().parent.parent / "assets" / "logo"
PNG, PDF = LOGO / "png", LOGO / "pdf"
WIDTH_PX, WIDTH_MM = 2000, 200


def view_box(svg):
    m = re.search(r'viewBox="([-\d.]+) ([-\d.]+) ([\d.]+) ([\d.]+)"', svg)
    return float(m.group(3)), float(m.group(4))


def main():
    PNG.mkdir(exist_ok=True)
    PDF.mkdir(exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        for f in sorted(LOGO.glob("*.svg")):
            svg = f.read_text(encoding="utf-8")
            w, h = view_box(svg)
            pw, ph = WIDTH_PX, round(WIDTH_PX * h / w)
            page.set_viewport_size({"width": pw, "height": ph})
            sized = svg.replace("<svg ", '<svg width="%d" height="%d" ' % (pw, ph), 1)
            page.set_content('<html><body style="margin:0;background:transparent">' + sized + '</body></html>')
            page.screenshot(path=str(PNG / f"{f.stem}.png"), omit_background=True,
                            clip={"x": 0, "y": 0, "width": pw, "height": ph})
            mh = round(WIDTH_MM * h / w, 2)
            boxed = svg.replace("<svg ", '<svg style="display:block;width:%smm;height:%smm" ' % (WIDTH_MM, mh), 1)
            page.set_content('<html><head><style>@page{size:%smm %smm;margin:0}html,body{margin:0}</style></head><body>%s</body></html>'
                             % (WIDTH_MM, mh, boxed))
            page.pdf(path=str(PDF / f"{f.stem}.pdf"), width=f"{WIDTH_MM}mm", height=f"{mh}mm",
                     print_background=True, page_ranges="1")
            print(f.stem)
        browser.close()


if __name__ == "__main__":
    main()
