"""Xuất logo SVG trong assets/logo sang PNG nền trong suốt (cạnh dài 2000 px) và PDF vector (rộng 200 mm).

Chạy: python scripts/export_logo_assets.py  (cần Python Playwright + Chromium)
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
            page.set_content(f'<html><body style="margin:0;background:transparent">'
                             f'{svg.replace("<svg ", f"<svg width=\"{pw}\" height=\"{ph}\" ", 1)}</body></html>')
            page.screenshot(path=str(PNG / f"{f.stem}.png"), omit_background=True,
                            clip={"x": 0, "y": 0, "width": pw, "height": ph})
            mh = round(WIDTH_MM * h / w, 2)
            page.set_content(f'<html><head><style>@page{{size:{WIDTH_MM}mm {mh}mm;margin:0}}html,body{{margin:0}}</style></head>'
                             f'<body>{svg.replace("<svg ", f"<svg style=\"display:block;width:{WIDTH_MM}mm;height:{mh}mm\" ", 1)}</body></html>')
            page.pdf(path=str(PDF / f"{f.stem}.pdf"), width=f"{WIDTH_MM}mm", height=f"{mh}mm",
                     print_background=True, page_ranges="1")
            print(f.stem)
        browser.close()


if __name__ == "__main__":
    main()
