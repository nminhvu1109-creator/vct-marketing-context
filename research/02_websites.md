# 02 – Hiện diện web của Viet Cone Travel

Rà soát 20/11/2026: đọc HTML (title, meta, hreflang, heading, link), tra mạng xã hội và báo chí.
Không gửi form. Không gồm ttg.vietconetravel.com.
Trích dẫn giữ ngôn ngữ gốc. Câu chữ chuẩn (RAI, Travelife, năm thành lập): xem bối cảnh mục 9.

## 0. Tổng quan

| Site | Nền tảng | Vai trò | Ngôn ngữ | Giá | CTA |
|---|---|---|---|---|---|
| vietconetravel.com | Wix | Site thương hiệu, catalog, blog | IT (mặc định), EN, ES | Không | "Richiedi Un Preventivo" |
| immersion | Vite, Cloudflare | Bộ trải nghiệm văn hóa | IT, EN | Không | "Programma su misura" → ttg/#brief; WhatsApp, email |
| vivivietnam | Astro, Cloudflare | Proposal white label, 1 đoàn | IT, EN | Không | Không (cố ý) |
| vietnamangkor | Astro, Cloudflare | Proposal white label, 1 đoàn | IT, EN | Không | Không (cố ý) |
| partenze | Astro, Cloudflare + API | Landing Partenze 2027 | IT | Có (USD) | Form đăng ký + WhatsApp |

- Subdomain dùng chung một hệ thiết kế mới: sạch, nhanh, biên tập kỹ.
- Site chính Wix cũ hơn: nhiều lỗi chính tả, trang rác từ template, trang trùng.
- Hai hệ trông như của hai công ty khác nhau.

## 1. vietconetravel.com (site chính)

### 1.1 Nội dung và thông điệp
- Đối tượng: khách lẻ Ý. hreflang `it-it` (x-default), `en-gb`, `es-es`. Chưa có bản tiếng Pháp.
- Menu: DESTINAZIONI (Vietnam, Laos, Cambogia, Thailandia) · TEMI/VIAGGI (Esperienziali, Classici, Responsabili, Trekking, Combinati) · SU DI NOI · BLOG · CONTATTACI.
- Trang chủ: "local DMC ... con oltre 20 anni di esperienza tra Vietnam, Laos, Cambogia e Thailandia." Lệch bối cảnh: thành lập 2019; Thái Lan (bối cảnh mục 5).
- Su di noi: "La nostra agenzia nasce nel 2010". Lệch năm thành lập 2019.
- Missione: "Mostrare il vero Vietnam in modo sostenibile"; giá trị Creatività, Passione, Solidarietà, Responsabilità.
- Số liệu trang chủ: "100% Viaggi personalizzati", "99% Clienti soddisfatti" (không nguồn), "20+ Anni".

### 1.2 Tín hiệu tin cậy
- Travelife: IT "tra le 13 agenzie", EN "Among only 14", Su di noi "tra le 14 aziende". Ba con số khác nhau, đều lệch chuẩn.
- RAI: "ha inoltre collaborato ... alla realizzazione di uno speciale". Lệch câu chuẩn "accompagnato la troupe"; đã có link RaiPlay.
- Tripadvisor: chỉ có badge; mục "COSA DICONO I NOSTRI CLIENTI" không có review bằng chữ.
- CAPTOUR DMCs Club: có badge.
- Trang bền vững: Sostenibilità, Politica di sostenibilità, Rapporto di sostenibilità, Carbon offset policy, Politica sociale e diritti umani. Nên rà "Carbon offset policy" theo bối cảnh mục 10.
- Footer có số giấy phép lữ hành quốc tế.

### 1.3 Sản phẩm
- Tour riêng 8–12 ngày (Esperienziali 6 tour, Classici khoảng 6 tour); không giá, không ngày khởi hành.
- Lỗi nội dung:
  - Mekong autentico: thiếu ngày 4 (nhảy từ Giorno 3 sang 5).
  - Vespa tour: "Itinerario in breve" lặp 3 lần IT, 1 lần EN.
  - copy-of-vespa-tour ("CULTURAL JOURNEY"): tóm tắt bắt đầu ở Saigon, chi tiết bắt đầu ở Hà Nội; lẫn IT/EN.
  - viaggi-esperienziali dùng nhầm mô tả "viaggi avventura".
  - viaggi-combinati lặp 4 thẻ "HOANG SU PHI CAMMINATE TRA LE MINORANZE".
- FAQ hậu cần trên trang chủ (điểm đón "Colonna 4" Nội Bài, SIM, cấm thuốc lá điện tử từ 1/1/2025, tip 6–8 USD/ngày): hữu ích, cho thấy kinh nghiệm vận hành.

### 1.4 Thu lead và đo lường
- Form báo giá ở slug sai `richietsa-preventivo`: Nome, Cognome, Email, Telefono (WhatsApp), Tipologia, Periodo, Richieste, privacy. Không hỏi số khách, ngân sách, điểm đến.
- Trang newsletter có nhưng không được liên kết từ trang chủ.
- Liên hệ hiển thị: WhatsApp +84 37 358 2398, email, địa chỉ. Footer ghi sai "infor@" (cả mailto), có thể mất lead.
- GA4 `G-920ET70RTL`. Không thấy Meta Pixel, GTM.

### 1.5 Kỹ thuật và SEO
- Title trang chủ "HOME | VIETCONE TRAVEL | VIETNAM", giống hệt ở EN, ES. Meta nhồi từ khóa; nhiều trang không có meta.
- Mỗi badge, mỗi con số là một thẻ H1.
- Sitemap 146 URL, khoảng 20 trang "copy-of-…/copia-di-…" được index.
- Trang rác Wix `book-online`: "Weddings, Bar Mitzvahs ... 150 USD – Prenota", có trong sitemap.
- Bản EN, ES: slug vẫn tiếng Ý; còn nhiều đoạn tiếng Ý (FAQ, nút "Scopri di pìu"); blog EN chỉ 4 bài cũ.
- Blog IT: 75 bài, bài mới nhất 04/02/2026. Chủ đề tốt (làng nghề, dân tộc, lễ hội, lưu trú bền vững).
- Lỗi chính tả tiếng Ý ở vị trí dễ thấy: "pìu" (più), "RESPONSIBILI" (RESPONSABILI), "I NOSTRO BLOG" (I NOSTRI), "SORRISSI" (SORRISI), "Statunensi", "atuo", "quotadina".

## 2. immersion.vietconetravel.com

- Bộ sưu tập các buổi gặp gỡ văn hóa để ghép vào hành trình may đo. Đối tượng: khách Ý, có thể cả agency.
- H1: "Immersion – La collezione di esperienze culturali".
- Câu chính: "Viet Cone visita i luoghi e prepara ogni esperienza con chi vi abita."
- Footer: "Destination Management Company specializzata in viaggi culturali su misura in Vietnam per il mercato italiano."
- 8 trải nghiệm theo 3 miền:
  - Bắc: Lào Cai (Mường Bo), Mù Cang Chải (Ingegno Hmong), Phú Thọ (hát Xoan, gia đình Mường Xuân Sơn), Hà Nội (Phù Gia, Đường Lâm).
  - Trung: Huế (chùa Kim Đài), Hội An (văn hóa Chăm, nhà Maily).
  - Nam: Trà Vinh (Khmer, Cồn Hô), Sóc Trăng.
- Trang Hội An: Kieu Maily, nhà văn, nghệ sĩ, nhà nghiên cứu Chăm; "pasto culturale" khoảng 2,5 giờ hoặc "incontro con il tè" khoảng 90 phút; Viet Cone lo phiên dịch; có hướng dẫn ứng xử khi chụp ảnh. Không giá.
- Giọng văn tiết chế, có người thật: thể hiện rõ nhất "Immerse. Not just observe." Bản đồ có Hoàng Sa, Trường Sa; có file Travelife tải về.
- Ảnh WebP, layout kiểu tạp chí.
- Kỹ thuật tốt: CSP, index/follow, canonical, hreflang IT/EN, sitemap 18 URL, OG đầy đủ. Không thấy analytics.
- Điểm yếu: trang tổng không có giá, thời lượng, tên host; CTA đưa khách lẻ sang trang TTG (B2B); site chính chưa liên kết tới.

## 3. Trang proposal white label: vivivietnam, vietnamangkor

- Trang chương trình cho từng đoàn, gửi đối tác thay file PDF.
- Cố ý không logo, không tên Viet Cone, không liên hệ, không CTA, không giá: đúng mô hình white label (bối cảnh mục 12).
- Việc cần: đặt `noindex`. Hiện chưa có; robots.txt Cloudflare cho `search=yes`.
- Kỹ thuật: Astro, Cloudflare, CSP `form-action 'none'`, Source Sans 3, hreflang IT/EN, OG.
- Định dạng mạnh: đẹp, đọc tốt trên điện thoại, có link khách sạn. Ưu tiên dùng làm mẫu proposal chuẩn cho kênh B2B.

### vivivietnam: "Vietnam in treno", 14N13Đ, 8–21/11/2026
- Hà Nội – Đường Lâm (Planeterra, rối bóng) – Hạ Long (Milalux) – Tam Cốc – Pù Luông (trekking với người Thái) – tàu đêm đi Huế – Hội An – Saigon – Củ Chi – Cần Thơ – Cái Răng, Vĩnh Long, Cái Bè.
- HDV: ngày 1 tiếng Ý, các ngày còn lại tiếng Anh.

### vietnamangkor: "Viaggio in Vietnam e Angkor", 14N13Đ, 22/02–07/03/2027
- Hà Nội – Lan Hạ – Huế – Hội An – Saigon – Mekong – Siem Reap.
- Điểm nhấn: Thủy Biều, Mỹ Sơn, Bến Tre, Roluos, APOPO, lễ "Srouch Teok", Artisans d'Angkor, Kampong Pluk.
- Lựa chọn "Alternativa" có phụ phí (workshop cà phê, "Cena reale a Hue", "Cena con danza Apsara"): mô hình upsell tốt.
- HDV tiếng Ý suốt hành trình. Khách sạn có link (Mercure La Gare, La Casta Cruise, Tara Angkor…).

## 4. partenze.vietconetravel.com

- Landing Partenze cho khách lẻ Ý. Site duy nhất công khai giá và có form đăng ký.
- Title: "Vietnam Essenziale · Partenze 2027 | Viet Cone Travel".
- Ý chính: "Guide parlanti italiano secondo il programma", "Da 2 partecipanti – Partenza garantita", "Massimo 12 partecipanti".

| Khởi hành | Ngày | Standard | Superiore | Phụ thu đơn Std/Sup | Hạn đăng ký |
|---|---|---|---|---|---|
| Marzo 2027 | 8–17/03 | $1.480 | $1.580 | +$322 / +$423 | 06/01/2027 |
| Agosto 2027 | 8–17/08 | $1.470 | $1.560 | +$312 / +$403 | 15/06/2027 |
| Dicembre 2027 | 27/12–05/01/2028 | $1.545 | $1.695 | +$353 / +$476 | 25/10/2027 |

- Giá USD/khách, phòng đôi; chuyến tháng 12 có "Cenone di Capodanno".
- Lịch trình 10N9Đ: Hà Nội – Ninh Bình – Hạ Long (ngủ du thuyền) – Hà Nội – bay Đà Nẵng, Hội An – Huế – bay Saigon – Bến Tre – về.
- Khách sạn Std/Sup: Skylark/Le Jardin (Hà Nội); Victory Cruise/Victory Star; Hoi An Emotion/Cozy An; Thanh Lịch/Thanh Lịch Royal (Huế); Calista/The Odys (Saigon).
- Gồm 2 chặng bay nội địa (23 kg), 9 đêm có ăn sáng, vé tham quan. Không gồm vé quốc tế, bảo hiểm, tùy chọn, tip.
- Form: chọn chuyến, họ tên, email (không bắt buộc), WhatsApp (bắt buộc), số người lớn, trẻ dưới 12, hạng KS, loại phòng (có ghép phòng cho người đi một mình), kéo dài trước/sau, dị ứng. POST `/api/register`.
- Analytics tự viết (`/api/analytics`): thời gian, UTM, thiết bị, ngôn ngữ; không cookie bên thứ ba.
- Nhãn "Iscrizioni chiuse" có sẵn trong HTML (ẩn, JS bật sau hạn): bot đọc text dễ hiểu nhầm là đã đóng.
- Không sitemap, không hreflang, chỉ tiếng Ý.
- Điểm yếu:
  - Giá USD: ưu tiên EUR cho khách Ý.
  - "secondo il programma" mơ hồ: ưu tiên ghi rõ ngày nào có HDV tiếng Ý.
  - Chưa có review, dòng RAI/Travelife, FAQ thanh toán, cọc, hủy, bảo hiểm.
  - Mới một sản phẩm: có thể thêm ngày/tuyến Partenze (Vietnam + Angkor, Nord autentico).
  - Chưa có schema `TouristTrip`/`Offer`.

## 5. Mạng xã hội, đánh giá, báo chí

| Kênh | Hiện trạng | Nguồn |
|---|---|---|
| Instagram | 369 follower, 309 following; bio "Responsible tourism"; số điện thoại cũ, khác site | https://www.instagram.com/vietconetravel/ |
| Facebook | Page "Viet Cone Travel - Italiano \| Hanoi" và một page cũ: thương hiệu bị phân tán | https://www.facebook.com/VietConeTravel · https://www.facebook.com/Viet-Cone-Travel-112882640072400/ |
| YouTube | Handle có đuôi số mặc định | https://www.youtube.com/@vietconetravel7356 |
| LinkedIn | Hồ sơ cá nhân (/in/), chưa phải Company Page | https://vn.linkedin.com/in/viet-cone-travel-755b64378 |
| Tripadvisor | Chặn 403 khi tra; số đánh giá: bối cảnh mục 9 | https://www.tripadvisor.it/Attraction_Review-g293924-d20899025-Reviews-Viet_Cone_Travel-Hanoi.html |

- Tìm kiếm "Viet Cone Travel" recensioni, tour operator, "Speciale Tg1 Vietnam dalle ferite alla luce": không có kết quả nào về Viet Cone.
- Công cụ còn gợi ý nhầm sang "Conical Travel". Kết quả tiếng Ý là đối thủ: OVET, WeRoad, Threeland.
- Dấu hiệu độ phủ và backlink ngoài site rất thấp. Công cụ tra chỉ dùng vùng US: cần kiểm tra lại bằng Google Italia và Search Console.

## 6. Nhận xét chung

- Tên viết lẫn lộn: "VIETCONE TRAVEL", "Viet Cone Travel", "VietCone", "Viet Cone". Ưu tiên "Viet Cone Travel".
- Subdomain định vị rõ hơn ("per il mercato italiano"); site chính nhận phủ 4 nước, thông điệp loãng.
- Partenze, Vespa tour, Viaggio di nozze, hai proposal dùng chung xương sống Hà Nội – Hạ Long – Huế – Hội An – Saigon – Bến Tre.
- Không có điều hướng liên site; giá chỉ có trên Partenze; không site nào có review bằng chữ.
- Đo lường rời rạc: GA4 (site chính), analytics riêng (Partenze), còn lại không tracking.
- Ba luồng lead (form Wix, form Partenze, brief TTG) cộng WhatsApp; chưa có lead magnet.

## 7. Việc cần làm (gộp)

Site chính:
1. Xóa hoặc ẩn `book-online` và các trang copy-of-*; sửa slug `richietsa`, email footer "infor@".
2. Thailandia: ưu tiên đưa xuống vị trí phụ trong menu hoặc ghi "su richiesta"; câu giới thiệu trang chủ ưu tiên Vietnam, Laos, Cambogia.
3. Sửa "20+ anni", "nasce nel 2010", "99% clienti soddisfatti": ghi "fondata nel 2019".
4. Travelife: theo câu chuẩn bối cảnh mục 9.
5. RAI: câu chuẩn + link RaiPlay; có thể dùng logo RAI và nhúng trích đoạn phóng sự. Ưu tiên một trang riêng cho RAI và Travelife.
6. Sửa chính tả trên nút lặp (più, RESPONSABILI, I NOSTRI).
7. Viết lại title, meta theo từ khóa tiếng Ý; mỗi trang một H1.
8. Thêm "da €…" cho tour mẫu; hiển thị review Tripadvisor bằng chữ.
9. Hoàn thiện bản EN, ES hoặc tạm ẩn.
10. Thêm Immersion và Partenze vào menu và trang chủ.

Liên hệ (mọi kênh):
11. Dùng hai số theo vai trò: +84 988 550 733 (chung), +84 37 358 2398 (B2B, WhatsApp).
12. Instagram: gỡ số +84 24 3204 5077, thay bằng hai số trên.
13. Gộp 2 page Facebook; chuyển LinkedIn sang Company Page.

Subdomain:
14. vivivietnam, vietnamangkor và proposal sau này: thêm `noindex`, giữ white label.
15. Immersion: tách luồng B2C và B2B thay vì đưa khách lẻ sang trang TTG.
16. Partenze: giá EUR, ghi rõ ngày có HDV tiếng Ý, thêm FAQ và dòng uy tín, sitemap, schema; thêm ngày/tuyến Partenze.

Lâu dài:
17. Cân nhắc chuyển site chính sang Astro/Cloudflare để dùng một hệ thiết kế.

## Nguồn

### vietconetravel.com (site chính)
- https://www.vietconetravel.com/
- https://www.vietconetravel.com/en
- https://www.vietconetravel.com/es
- https://www.vietconetravel.com/su-di-noi
- https://www.vietconetravel.com/la-nostra-missione
- https://www.vietconetravel.com/viaggi-esperienziali
- https://www.vietconetravel.com/viaggi-classici
- https://www.vietconetravel.com/mekong-autentico
- https://www.vietconetravel.com/vespa-tour
- https://www.vietconetravel.com/viaggio-di-nozze
- https://www.vietconetravel.com/copy-of-vespa-tour
- https://www.vietconetravel.com/richietsa-preventivo
- https://www.vietconetravel.com/newsletter
- https://www.vietconetravel.com/book-online
- https://www.vietconetravel.com/sitemap.xml

### immersion.vietconetravel.com
- https://immersion.vietconetravel.com/it/
- https://immersion.vietconetravel.com/en/
- https://immersion.vietconetravel.com/it/esperienze/hoi-an/
- https://immersion.vietconetravel.com/downloads/travelife-partner-certificate.pdf

### Trang proposal white label: vivivietnam, vietnamangkor
- https://vivivietnam.vietconetravel.com/
- https://vietnamangkor.vietconetravel.com/

### partenze.vietconetravel.com
- https://partenze.vietconetravel.com/
