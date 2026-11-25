# Asset thương hiệu

Lấy từ repo cũ `vietcone-marketing` (20/11/2026).

## logo/
- Tên file: `vc-logo-[phiên bản]-[màu].svg`. Phiên bản: horizontal (chính), tagline, icon, icon-compact.
- Màu: `color` cho nền sáng; `white` cho nền đậm và trên ảnh; `ink`, `green` cho in một màu, khắc, thêu.
- SVG được vector hóa từ PNG gốc trong `source/` (khớp 99%+). Khi có file vector gốc từ designer, ưu tiên thay bằng bản đó.
- `favicon/`: favicon web (favicon.svg, .ico, PNG), avatar 1080 px. `vc-logo-email-260.png`: chữ ký email.
- `icon-compact` và favicon là bản dựng tạm; nhờ designer kiểm tra trước khi dùng chính thức.
- PNG nền trong suốt và PDF: chạy `python scripts/export_logo_assets.py` (cần Playwright và Chromium), file ra ở `logo/png/`, `logo/pdf/` (không commit). PDF ở hệ RGB; bản CMYK để in cần designer hoặc nhà in chuyển đổi.

## brand-tokens.css
- Mã màu, thang sắc độ, cỡ chữ, thẻ và nút cho web, theo Brand Guideline mục 3, 4, 6.
- Mã màu và font là điểm cố định (Guideline 0.3); cỡ chữ, bo góc, khoảng cách là mặc định, chỉnh khi cần.
- Nạp sẵn font Source Sans 3 tự host.

## fonts/source-sans-3/
- `*.woff2`: font web, có bộ tiếng Việt.
- `ttf/`: bản cài trên máy (Canva, file thiết kế), lấy từ bản phát hành chính thức của Adobe (v3.052, 25/11/2026).
  - Đứng: Light, Regular, Semibold, Bold, Black.
  - Nghiêng (từ tiếng Ý): It, SemiboldIt, BoldIt.
  - Bộ cũ bị ghi sai tên họ font ("Source Sans 3 ExtraLight" cho cả 4 file); máy đã cài bộ cũ nên gỡ ra rồi cài lại.
- Giấy phép OFL: dùng, chia sẻ tự do.

## partners/travelife/
- `travelife-partner.png`: huy hiệu chính thức, tải từ trang Travelife ngày 10/11/2026.
- Không tự vẽ lại huy hiệu. Bản vector lấy từ trang thành viên Travelife.
- Trên trang bán cho người tiêu dùng EU, ưu tiên dòng chữ "Travelife Partner dal 06/2025" cho đến khi luật sư Ý xác nhận dùng huy hiệu.
