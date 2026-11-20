# Asset thương hiệu

Lấy từ repo cũ `vietcone-marketing` (20/11/2026).

## logo/
- Tên file: `vc-logo-[phiên bản]-[màu].svg`. Phiên bản: horizontal (chính), tagline, icon, icon-compact.
- Màu: `color` cho nền sáng; `white` cho nền đậm và trên ảnh; `ink`, `green` cho in một màu, khắc, thêu.
- SVG được vector hóa từ PNG gốc trong `source/` (khớp 99%+). Khi có file vector gốc từ designer, ưu tiên thay bằng bản đó.
- `favicon/`: favicon web, avatar 1080 px. `vc-logo-email-260.png`: chữ ký email.
- `icon-compact` và favicon là bản dựng tạm; nhờ designer kiểm tra trước khi dùng chính thức.
- PNG nền trong suốt và PDF: chạy `python scripts/export_logo_assets.py`, file ra ở `logo/png/`, `logo/pdf/` (không commit). PDF ở hệ RGB; bản CMYK để in cần designer hoặc nhà in chuyển đổi.

## brand-tokens.css
- Mã màu, thang sắc độ, cỡ chữ, thẻ và nút cho web, theo Brand Guideline mục 3, 4, 6.
- Nạp sẵn font Source Sans 3 tự host.

## fonts/source-sans-3/
- `*.woff2`: font web, có bộ tiếng Việt.
- `ttf/`: bản Regular, SemiBold, Bold, Black để cài trên máy (Canva, file thiết kế). Chưa có bản nghiêng.
- Giấy phép OFL: dùng, chia sẻ tự do.

## partners/travelife/
- `travelife-partner.png`: huy hiệu chính thức, tải từ trang Travelife ngày 10/11/2026.
- Không tự vẽ lại huy hiệu. Bản vector lấy từ trang thành viên Travelife.
- Trên trang bán cho người tiêu dùng EU, ưu tiên dòng chữ "Travelife Partner dal 06/2025" cho đến khi luật sư Ý xác nhận dùng huy hiệu.

## Còn thiếu
- File logo gốc từ designer (AI/EPS/PDF), bản CMYK để in.
- Huy hiệu Travelife bản vector.
- Giấy chứng nhận và huy hiệu Tripadvisor Travelers' Choice.
- Logo CAPTOUR DMCs Club (nếu được phép dùng).
- Thư viện ảnh gốc độ phân giải cao, kèm người chụp và tình trạng đồng ý.
