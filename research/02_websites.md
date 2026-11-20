# 02 – Hiện diện web của Viet Cone Travel (VCT)

Ngày thu thập: 20/11/2026. Phương pháp: tải HTML thô (curl) và phân tích title, meta, hreflang, heading, nội dung, link, CSS, JS; WebFetch/WebSearch cho mạng xã hội và báo chí. Không gửi form nào. Không bao gồm https://ttg.vietconetravel.com (agent khác phụ trách).

Trích dẫn giữ nguyên ngôn ngữ gốc.

---

## 0. Tóm tắt nhanh

| Site | Nền tảng | Vai trò | Ngôn ngữ | Giá công khai | CTA chính |
|---|---|---|---|---|---|
| vietconetravel.com | Wix | Site thương hiệu, catalog tour, blog | IT (mặc định), EN, ES | Không | "Richiedi Un Preventivo" (form báo giá) |
| immersion.vietconetravel.com | Static (Vite) trên Cloudflare | Bộ sưu tập trải nghiệm văn hóa | IT, EN | Không | "Programma su misura" → ttg.vietconetravel.com/#brief; WhatsApp/email |
| vivivietnam.vietconetravel.com | Astro static trên Cloudflare | Trang chương trình riêng cho 1 đoàn (8–21/11/2026) | IT, EN | Không | Không có CTA, không có liên hệ |
| vietnamangkor.vietconetravel.com | Astro static trên Cloudflare | Trang chương trình riêng cho 1 đoàn (22/02–07/03/2027) | IT, EN | Không | Không có CTA, không có liên hệ |
| partenze.vietconetravel.com | Astro static trên Cloudflare + API riêng | Landing page tour ghép đoàn 2027 | IT | Có (USD) | Form "Richiedi la tua iscrizione" + WhatsApp |

Nhận định chung: các subdomain mới (immersion, partenze, vivi, vietnamangkor) dùng chung một hệ thiết kế hiện đại, sạch và nhanh. Site chính trên Wix thì cũ hơn, nhiều lỗi chính tả, có trang rác từ template và trang trùng lặp. Hai hệ thống trông như của hai công ty khác nhau.

---

## 1. vietconetravel.com (site chính)

URL: https://www.vietconetravel.com/ (IT), https://www.vietconetravel.com/en, https://www.vietconetravel.com/es

### 1.1 Mục đích và đối tượng
- Site thương hiệu và catalog tour cho khách lẻ Ý (B2C), tự định vị là DMC địa phương.
- Ngôn ngữ mặc định là tiếng Ý (`lang="it"`, hreflang `it-it` = x-default). Có thêm bản EN (`en-gb`) và ES (`es-es`). Không có bản tiếng Pháp hay Đức.

### 1.2 Thông điệp định vị (trang chủ IT)
- Slogan (tiếng Anh, giữ nguyên ở cả 3 bản): **"Immerse. Not just observe."**
- "Viet Cone Travel è un local DMC specializzato nella creazione di viaggi culturali autentici in Vietnam e Indocina, con oltre 20 anni di esperienza tra Vietnam, Laos, Cambogia e Thailandia."
- "viaggiare non significhi semplicemente "visitare" un Paese, ma entrare in connessione con la sua anima, le sue persone e il suo ritmo di vita reale."
- "Disegniamo esperienze profonde, lente e autentiche, dove il viaggiatore non rimane un osservatore esterno, ma diventa parte della storia."
- Trang Su di noi (https://www.vietconetravel.com/su-di-noi): "La nostra agenzia nasce nel 2010 dall'esperienza e dalla passione per il viaggio della nostra fondatrice, la Sig.ra Nga Nguyen." Tên gọi lấy từ "nón lá", gắn với những người phụ nữ đã xây dựng công ty.
- Trang Missione (https://www.vietconetravel.com/la-nostra-missione): "Mostrare il vero Vietnam in modo sostenibile"; tầm nhìn "Essere leader nel turismo esperienziale in Vietnam"; giá trị: Creatività, Passione, Solidarietà, Responsabilità.

### 1.3 Tín hiệu tin cậy (dải badge đầu trang chủ)
- **Travelife Partner**: IT "Viet Cone Travel è tra le 13 agenzie in Vietnam", EN "Among only 14 Travelife Partner agencies in Vietnam", trang Su di noi IT "tra le 14 aziende". Con số không thống nhất. Trang chủ nói Travelife đạt "oltre 100 criteri". Immersion có file PDF chứng nhận: https://immersion.vietconetravel.com/downloads/travelife-partner-certificate.pdf
- **Speciale Tg1 / RAI UNO**: "Nel 2025, Viet Cone Travel ha inoltre collaborato con la televisione nazionale italiana RAI UNO alla realizzazione di uno speciale dedicato al Vietnam, in onda a dicembre 2025 "Vietnam: dalle ferite alla luce"". Có link RaiPlay (puntata 28/12/2025). Đây là tài sản PR mạnh nhất cho thị trường Ý.
- **Tripadvisor**: "Eccellenza riconosciuta dai viaggiatori", link tới https://www.tripadvisor.it/Attraction_Review-g293924-d20899025-Reviews-Viet_Cone_Travel-Hanoi.html (WebFetch bị chặn 403 nên chưa xác minh được điểm và số review).
- **CAPTOUR DMCs Club**: thành viên.
- Số liệu: "100% Viaggi personalizzati", "99% Clienti soddisfatti", "20+ Anni di esperienza locale". Con số 99% không có nguồn.
- Giấy phép lữ hành quốc tế ở footer: "01-1532/2019/TCDL-GP LHQT".
- Có các trang về bền vững: Sostenibilità, Politica di sostenibilità, Rapporto di sostenibilità, Carbon offset policy, Politica sociale e diritti umani…
- Có mục "COSA DICONO I NOSTRI CLIENTI" nhưng HTML không chứa nội dung review (có thể là widget tải bằng JS). Trên trang không có trích dẫn đánh giá nào bằng chữ.

### 1.4 Sản phẩm
Menu: DESTINAZIONI (Vietnam, Laos, Cambogia, Thailandia), TEMI/VIAGGI (Esperienziali, Classici, Responsabili, Trekking, Combinati), SU DI NOI, BLOG, CONTATTACI.

Các tour xem được (đều là tour riêng, may đo; **không có giá**, không có ngày khởi hành):
- Esperienziali (https://www.vietconetravel.com/viaggi-esperienziali): "MEKONG AUTENTICO" 8N7Đ; "UN TUFFO NELLA NATURA" 9N8Đ; "UN GIORNO IN VESPA" 10N9Đ; "FINO ALL'ESTREMO SUD DEL PAESE" 12N11Đ; "DOVE SCORRE IL MEKONG" 12N11Đ; "EMOZIONI TRA CULTURA E MARE" 12N11Đ.
- Classici (https://www.vietconetravel.com/viaggi-classici): "VIETNAM E L'ISOLA DI PHU QUOC" 12N11Đ; "VIETNAM IN FAMIGLIA TRA NATURA, SORRISSI E SCOPERTE" 12N11Đ; "CAMBOGIA E KOH RONG" 12N11Đ; các tour 10N9Đ và 11N10Đ.
- Tour mẫu đã xem:
  - Mekong autentico (https://www.vietconetravel.com/mekong-autentico): Saigon – Cu Chi – Tây Ninh – Bến Tre (homestay) – Trà Vinh (Khmer) – Cần Thơ – Châu Đốc – Saigon. **Mất ngày 4** trong phần chi tiết (nhảy từ Giorno 3 sang Giorno 5).
  - Vespa tour (https://www.vietconetravel.com/vespa-tour): Saigon → Huế → Hội An → Hà Nội → Lan Hạ, 10 ngày. "Itinerario in breve" lặp lại 3 lần bằng IT và 1 lần bằng EN trên cùng trang.
  - Viaggio di nozze (https://www.vietconetravel.com/viaggio-di-nozze): Hà Nội – Hạ Long – Ninh Bình – Mai Châu – Huế – Hội An – Saigon – Bến Tre, 10 ngày.
  - https://www.vietconetravel.com/copy-of-vespa-tour, title "CULTURAL JOURNEY": tóm tắt bắt đầu ở Saigon nhưng chi tiết lại bắt đầu ở Hà Nội. Nội dung tự mâu thuẫn và lẫn IT/EN.
- Trang FAQ hậu cần ngay trang chủ (Pre-Arrival Information, nhập cảnh, điểm đón "Colonna 4" sân bay Nội Bài, SIM, cấm thuốc lá điện tử từ 1/1/2025, tip 6–8 USD/người/ngày). Phần này hữu ích và cho thấy công ty có kinh nghiệm vận hành thật.

### 1.5 CTA và thu lead
- Nút "Richiedi Un Preventivo" trên header → https://www.vietconetravel.com/richietsa-preventivo (slug sai chính tả "richietsa"). Form song ngữ IT/EN: Nome, Cognome, Email, Telefono (WhatsApp), Tipologia di viaggio, Periodo indicativo, Richieste; checkbox privacy. Không hỏi số người, ngân sách hay điểm đến.
- Có trang newsletter (https://www.vietconetravel.com/newsletter) nhưng không thấy liên kết trên trang chủ.
- WhatsApp +84 37 358 2398, email, địa chỉ văn phòng Hà Nội (Ecolife Capitol, 58 Tố Hữu).
- Footer có email sai **"infor@vietconetravel.com"** (mailto cũng sai), nghĩa là có thể mất lead.
- GA4 `G-920ET70RTL`. Không thấy Meta Pixel hay GTM.

### 1.6 Phong cách hình ảnh
Template Wix ảnh lớn, heading viết hoa toàn bộ, có video "SCOPRI IL VIETNAM AUTENTICO". Dùng nhiều thẻ H1 làm style (mỗi badge, mỗi con số đều là H1).

### 1.7 Kỹ thuật và SEO
- Meta generator: "Wix.com Website Builder"; server Pepyaka (Wix).
- Title trang chủ: "HOME | VIETCONE TRAVEL | VIETNAM". Title của bản EN và ES cũng y hệt nên không tối ưu theo ngôn ngữ.
- Meta description IT viết thường toàn bộ, kiểu nhồi từ khóa: "home della nostra agenzia viaggi viet cone travel. tour operator di lunga esperienza…". EN: "sustainable travel agency in vietnam, sustainable tourism in vietnam, …". ES: "viajes vietnam, turismo sostenible vietnam, hanoi".
- Nhiều trang không có meta description (su-di-noi, la-nostra-missione, mekong-autentico, vespa-tour, viaggio-di-nozze, richietsa-preventivo).
- Sitemap (https://www.vietconetravel.com/sitemap.xml) có 146 URL, trong đó **khoảng 20 trang "copy-of-…"/"copia-di-…"** bị index (copy-of-vespa-tour-2/3/4, copy-of-trekking-in-hoang-su-phi-2, copia-di-estimate-english…), gây nội dung trùng lặp và trang rỗng.
- **Trang rác từ template Wix**: https://www.vietconetravel.com/book-online (title "Booking") đăng các dịch vụ "Weddings, Bar Mitzvahs, Christenings, Corporate Parties, Conferences – 1 h – 150 USD – Prenota". Nằm trong sitemap. Nếu khách thấy trang này thì uy tín bị ảnh hưởng nặng.
- Slug của bản EN và ES vẫn là tiếng Ý (/en/viaggi-classici, /es/i-nostri-viaggi…).
- Bản EN và ES còn sót nhiều đoạn tiếng Ý: toàn bộ FAQ, khối "Dalle baie spettacolari del Vietnam…", nút "Scopri di pìu", nút header ES "Richiedi Un Preventivo". Blog trên bản EN chỉ có 4 bài cũ (Cai Rang, Phu Quoc "After 2 years of pandemic…").
- Blog IT: 75 bài, bài mới nhất ngày 04/02/2026, tức khoảng 9 tháng không cập nhật. Chủ đề tốt (làng nghề, dân tộc, lễ hội, lưu trú bền vững). Mô tả blog viết vụng: "addirittura dirci quel che volete che sappiamo!"
- Lỗi chính tả tiếng Ý lặp lại ở vị trí dễ thấy: "Scopri di **pìu**" (đúng: più), "**RESPONSIBILI**" (đúng: RESPONSABILI), "**I NOSTRO BLOG**" (đúng: I NOSTRI), "SORRISSI" (đúng: SORRISI), "Statunensi", "atuo", "quotadina". Trang viaggi-esperienziali dùng nhầm đoạn mô tả của "viaggi avventura". Trang viaggi-combinati lặp 4 thẻ "HOANG SU PHI CAMMINATE TRA LE MINORANZE", trông như nội dung giữ chỗ chưa thay.
- Mâu thuẫn dữ liệu: "oltre 20 anni" nhưng "nasce nel 2010" (16 năm); Travelife "13" và "14"; Instagram ghi số điện thoại +84 24 3204 5077 còn site ghi +84 37 358 2398.

### 1.8 Điểm yếu và cơ hội
1. Xóa hoặc ẩn trang book-online và các trang copy-of-*, sửa slug richietsa và email infor@.
2. Sửa chính tả trên các nút lặp (più, RESPONSABILI, I NOSTRI). Đây là việc nhỏ nhưng ảnh hưởng nhiều tới cảm nhận của khách Ý.
3. Viết lại title và meta theo từ khóa tiếng Ý ("viaggio in Vietnam su misura", "tour Vietnam con guida italiana"…), mỗi trang một H1.
4. Thêm "giá từ…" hoặc khoảng giá cho tour mẫu. Hiện chỉ partenze có giá.
5. Đưa RAI và Travelife lên thành câu chuyện riêng: trang landing, nhúng clip, logo chính thức. Hiển thị review Tripadvisor bằng chữ.
6. Hoàn thiện bản EN/ES hoặc tạm ẩn. Bản dịch dở dang hiện gây hại nhiều hơn lợi.
7. Liên kết site chính sang các subdomain mới (Immersion, Partenze). Hiện trang chủ không trỏ tới subdomain nào.

---

## 2. immersion.vietconetravel.com/it/

URL: https://immersion.vietconetravel.com/it/ (EN: https://immersion.vietconetravel.com/en/)

### 2.1 Mục đích và đối tượng
"Bộ sưu tập" các buổi gặp gỡ văn hóa có thể ghép vào hành trình may đo. Đối tượng chính là khách Ý, có thể cả agency/đối tác Ý vì CTA trỏ sang TTG.

### 2.2 Thông điệp
- Title: "La collezione di esperienze culturali | Immersion · Viet Cone Travel"
- H1: "Immersion – La collezione di esperienze culturali"
- "Incontrare chi tramanda la cultura del Vietnam e capire il significato di un mestiere, di un rito o di una storia di famiglia."
- "Viet Cone visita i luoghi e prepara ogni esperienza con chi vi abita. Scegliamo insieme gli incontri e le attività, con tempo per le domande e attenzione al lavoro delle famiglie."
- Footer: "Destination Management Company specializzata in viaggi culturali su misura in Vietnam per il mercato italiano."

### 2.3 Sản phẩm (8 trải nghiệm, bản đồ chia 3 miền)
- Bắc: Lào Cai (Mường Bo, "Canti e credenze"), Mù Cang Chải ("Ingegno Hmong"), Phú Thọ ("Canto Xoan" + gia đình Mường ở Xuân Sơn), Hà Nội (Phù Gia, Đường Lâm).
- Trung: Huế ("Un dialogo sulla vita buddhista", Kim Đài), Hội An ("La cultura Cham, a casa di Maily").
- Nam: Trà Vinh (Khmer, Cồn Hô), Sóc Trăng ("Ospitalità del delta").
- Trang chi tiết mẫu (https://immersion.vietconetravel.com/it/esperienze/hoi-an/): nhân vật thật là "Kieu Maily è una scrittrice, artista e ricercatrice Cham". Có hai hình thức: "pasto culturale" khoảng 2,5 giờ hoặc "incontro con il tè" khoảng 90 phút. VCT lo phiên dịch. Có hướng dẫn ứng xử: "Chiedi il permesso prima di fotografare o registrare." **Không có giá.**
- Bản đồ có ghi Hoàng Sa và Trường Sa, phù hợp chuẩn Việt Nam.

### 2.4 CTA
- "Il tuo programma Immersion – Indica le esperienze di tuo interesse…" → nút "Programma su misura" dẫn tới https://ttg.vietconetravel.com/#brief.
- WhatsApp có tin nhắn soạn sẵn ("Buongiorno Viet Cone, vorrei informazioni su: Immersion…"), email được Cloudflare làm rối để chống spam.

### 2.5 USP
Kể chuyện qua con người thật (Maily, nhà sư, nghệ nhân), giọng văn tiết chế, tôn trọng, không cường điệu. Đây là trang thể hiện rõ nhất lời hứa "Immerse. Not just observe." Có tải được chứng nhận Travelife.

### 2.6 Hình ảnh và kỹ thuật
- Palette: cream `#FDFBF5`, xanh rừng `#183C27`, vàng `#C99A2E`, mực `#20251F`. Ảnh WebP, layout biên tập kiểu tạp chí.
- Cloudflare, CSP chặt, `robots: index, follow`, canonical và hreflang IT/EN chuẩn, sitemap 18 URL, OG đầy đủ, mỗi trang chi tiết có title và description riêng.
- Không thấy analytics.

### 2.7 Điểm yếu và cơ hội
- Không có giá hay khoảng giá, không có thời lượng ở trang tổng, không có ảnh và tên đối tác ở trang tổng.
- CTA đưa khách lẻ sang trang TTG (nhắm B2B?) khiến hành trình không rõ ràng. Nên có form riêng hoặc tách luồng B2B và B2C.
- Chưa có liên kết từ site chính. Nên làm "Immersion" thành mục menu trên vietconetravel.com.

---

## 3. vivivietnam.vietconetravel.com

URL: https://vivivietnam.vietconetravel.com/ (EN: /en/)

### 3.1 Mục đích
Trang chương trình (proposal) cho **một đoàn cụ thể**: "Vietnam in treno – 14 giorni · 13 notti – Date del viaggio 8–21 novembre 2026". Đoàn này đang đi đúng thời điểm thu thập. Trang dùng để gửi cho khách hoặc agency thay cho file PDF.

### 3.2 Nội dung
- "Un viaggio di quattordici giorni da Hanoi al delta del Mekong, con una notte in treno per raggiungere Hue."
- Lịch trình: Hà Nội – Đường Lâm (dự án Planeterra, múa rối bóng "Roi bong", ngâm chân) – Hạ Long (Milalux Cruise) – Ninh Bình/Tam Cốc – Pù Luông (trekking với người Thái) – tàu đêm Hà Nội–Huế (khoang 4 giường) – Huế – Hội An – Saigon – Củ Chi – Cần Thơ (homestay, xe đạp) – Cái Răng/Vĩnh Long/Cái Bè.
- Khách sạn kèm link: Lion Boutique Hotel, Milalux Cruise, Tam Coc Orchid, Valley Home (Pu Luong Retreat), Huong Giang, Cozy An Boutique, Sky Gem, Vam Xang Rustic Home.
- Bao gồm / không bao gồm rõ ràng. Hướng dẫn viên: ngày 1 ghi "Guida in italiano", các ngày còn lại "Guida in inglese".

### 3.3 CTA, tin cậy, thương hiệu
- **Không có logo hay tên Viet Cone Travel** trong HTML (0 lần nhắc), không có liên hệ, không có CTA, không có giá. Title chỉ là "Vietnam in treno".
- Không có `noindex`. robots.txt của Cloudflare cho phép `search=yes`, nghĩa là trang riêng của khách có thể bị Google index.

### 3.4 Kỹ thuật và hình ảnh
Astro, Cloudflare, CSP rất chặt (`form-action 'none'`), font Source Sans 3. Palette giống Immersion, thêm màu đất `#B0412F`. Có hreflang IT/EN và OG.

### 3.5 Cơ hội
- Thêm `noindex` cho các trang proposal riêng, hoặc ngược lại, chủ động biến chúng thành "itinerario d'esempio" có thương hiệu.
- Thêm footer có logo, liên hệ, Travelife và WhatsApp. Mỗi proposal được chuyển tiếp qua tay khách hay agency đều là một lần quảng bá thương hiệu bị bỏ phí.
- Định dạng này rất mạnh: đẹp, đọc tốt trên điện thoại, có link khách sạn. Nên chuẩn hóa thành sản phẩm chủ lực cho cả kênh B2B.

---

## 4. vietnamangkor.vietconetravel.com

URL: https://vietnamangkor.vietconetravel.com/ (EN: /en/)

### 4.1 Mục đích
Cùng template với vivivietnam: proposal cho đoàn "Viaggio in Vietnam e Angkor – 14 giorni · 13 notti – 22 febbraio – 7 marzo 2027".

### 4.2 Nội dung
- "Un viaggio di quattordici giorni da Hanoi a Siem Reap, attraverso la baia di Lan Ha, Hue, Hoi An, Saigon e il delta del Mekong."
- Điểm nhấn: Thủy Biều (thuyền rồng, nhà vườn, lớp nấu ăn), Mỹ Sơn, nếm rum ở Hội An, Bến Tre, Roluos/Angkor, trung tâm APOPO (rà phá bom mìn), lễ "Srouch Teok", Artisans d'Angkor, Kampong Pluk trên Tonle Sap.
- Có các lựa chọn "Alternativa" tính phụ phí: workshop cà phê với "cultural storyteller", "Cena reale a Hue", "Cena con danza Apsara". Đây là mô hình upsell tốt.
- Khách sạn: Mercure Hanoi La Gare, La Casta Cruise, Huong Giang, Sen Village Hoi An, Hotel Continental Saigon, Tara Angkor. Ăn ba bữa đầy đủ. **Hướng dẫn viên tiếng Ý suốt hành trình.**
- Không có giá, không có thương hiệu VCT, không có liên hệ, không có CTA (giống vivivietnam).

### 4.3 Nhận xét
Chất lượng biên tập rất tốt. Ngày và thứ chính xác (đã kiểm tra 22/02/2027 là thứ Hai). Điểm yếu giống vivivietnam: thiếu thương hiệu và chưa chặn index.

---

## 5. partenze.vietconetravel.com (tour ghép đoàn)

URL: https://partenze.vietconetravel.com/

### 5.1 Mục đích và đối tượng
Landing page bán tour ghép đoàn (group departure) cho khách lẻ Ý. Đây là site duy nhất **công khai giá** và có form đăng ký.

### 5.2 Thông điệp
- Title: "Vietnam Essenziale · Partenze 2027 | Viet Cone Travel"
- Meta: "Vietnam Essenziale in 10 giorni, da Hanoi al Delta del Mekong. Tre partenze garantite nel 2027: marzo, agosto e dicembre. Quote Standard e Superiore da 1.470 USD."
- H1: "Vietnam essenziale in 10 giorni". Các ý chính: "Guide parlanti italiano secondo il programma", "Da 2 partecipanti – Partenza garantita", "Massimo 12 partecipanti nel gruppo".

### 5.3 Ngày khởi hành và giá (USD/người, phòng đôi)

| Khởi hành | Ngày | Standard | Superiore | Phụ thu đơn Std | Phụ thu đơn Sup | Hạn đăng ký |
|---|---|---|---|---|---|---|
| Marzo 2027 | 8–17/03 | $1.480 | $1.580 | +$322 | +$423 | 06/01/2027 |
| Agosto 2027 | 8–17/08 | $1.470 | $1.560 | +$312 | +$403 | 15/06/2027 |
| Dicembre 2027 | 27/12–05/01/2028 | $1.545 | $1.695 | +$353 | +$476 | 25/10/2027 |

Chuyến tháng 12 bao gồm "Cenone di Capodanno".

### 5.4 Lịch trình 10 ngày / 9 đêm
1. Đến Hà Nội (phố cổ 36 phố, tùy chọn lớp làm bánh mì) · 2. Ninh Bình (Hang Múa, Tràng An, Hoa Lư) · 3–4. Hạ Long, ngủ trên du thuyền (Tai Chi lúc bình minh) · 5. Cà phê trứng, Văn Miếu, Lăng, Chùa Một Cột, Hỏa Lò → bay Đà Nẵng → Hội An · 6. Phố cổ Hội An (tùy chọn đạp xe) · 7. Đèo Hải Vân, lăng Khải Định, chùa Thiên Mụ, Đại Nội · 8. Bay vào Saigon (Bảo tàng Chứng tích Chiến tranh, Bưu điện, Catinat) · 9. Bến Tre (kẹo dừa, chiếu, xe lôi) · 10. Về (tùy chọn Củ Chi).

Khách sạn Standard / Superiore: Skylark / Le Jardin Haute Couture (Hà Nội); Victory Cruise / Victory Star (Hạ Long); Hoi An Emotion / Cozy An; Thanh Lịch / Thanh Lịch Royal (Huế); Calista / The Odys (Saigon).

Bao gồm 2 chặng bay nội địa (Hà Nội–Đà Nẵng, Huế–Saigon, kèm hành lý 23 kg), 9 đêm có ăn sáng, 1 đêm du thuyền, vé tham quan. Không gồm vé quốc tế, bảo hiểm, các hoạt động tùy chọn, tip.

### 5.5 Form và lead
- Form "Richiedi la tua iscrizione": chọn chuyến (được chọn nhiều), họ tên, email (không bắt buộc), **WhatsApp (bắt buộc)**, số người lớn, trẻ em dưới 12 tuổi, hạng khách sạn, loại phòng (có lựa chọn "doppia condivisa con 1 altro eventuale partecipante" để ghép người đi một mình), nhu cầu kéo dài trước/sau tour, dị ứng/hạn chế đi lại, checkbox xác nhận tham gia. POST tới `/api/register`.
- Hệ thống analytics tự viết (`/analytics.js` → `/api/analytics`): đo thời gian hoạt động, nguồn UTM (google/facebook/instagram/whatsapp…), thiết bị, trình duyệt, ngôn ngữ. Không dùng cookie bên thứ ba, phù hợp GDPR.
- Nhãn "Iscrizioni chiuse" có sẵn trong HTML nhưng bị `hidden` và JS sẽ bật lên sau hạn chót. Các công cụ đọc text hoặc bot AI có thể hiểu nhầm là đã đóng đăng ký (công cụ trích xuất của tôi thấy 9 lần "Iscrizioni chiuse").

### 5.6 Kỹ thuật và hình ảnh
Astro, Cloudflare, CSP, font Source Sans 3, gallery ảnh 10 ngày. robots.txt có `Content-Signal: search=yes, ai-train=no`. **Không có sitemap.xml, không hreflang, chỉ có tiếng Ý.** Footer: "Destination Management Company specializzata nel mercato italiano per viaggi inbound in Vietnam."

### 5.7 Điểm yếu và cơ hội
- Giá bằng USD. Khách Ý quen nghĩ bằng EUR. Nên hiển thị EUR hoặc kèm quy đổi ước tính.
- "Guide parlanti italiano **secondo il programma**" là cách nói mơ hồ. Nên nói rõ những ngày nào có HDV tiếng Ý.
- Không có review, không có badge RAI/Travelife, không có FAQ (thanh toán, đặt cọc, hủy, bảo hiểm), không nêu điều kiện thanh toán.
- Chỉ có một sản phẩm. Có thể nhân rộng thành các dòng "Partenze" khác: Vietnam + Angkor, Nord autentico, Capodanno.
- Thêm sitemap và schema `TouristTrip`/`Offer` để Google hiển thị giá và ngày.

---

## 6. Mạng xã hội, đánh giá, báo chí

| Kênh | URL | Kết quả |
|---|---|---|
| Instagram | https://www.instagram.com/vietconetravel/ | 369 follower, 309 following. Bio "🌿Responsible tourism", SĐT (+84)24 3204 5077 (khác số WhatsApp trên site) |
| Facebook | https://www.facebook.com/VietConeTravel (và một page cũ https://www.facebook.com/Viet-Cone-Travel-112882640072400/) | Tên page "Viet Cone Travel - Italiano \| Hanoi". Không đọc được số like. Có 2 page nên thương hiệu bị phân tán |
| YouTube | https://www.youtube.com/@vietconetravel7356 | Kênh "VIET CONE TRAVEL", handle có đuôi số mặc định, không đọc được số liệu |
| LinkedIn | https://vn.linkedin.com/in/viet-cone-travel-755b64378 | Là **hồ sơ cá nhân** (/in/), không phải Company Page. Không fetch được |
| Tripadvisor | link ở trên | Bị chặn 403, chưa xác minh điểm và số review |

WebSearch ("Viet Cone Travel" recensioni, "Viet Cone Travel" tour operator, vietconetravel.com, "Speciale Tg1 Vietnam dalle ferite alla luce") **không trả về kết quả nào về VCT**. Công cụ tìm kiếm còn gợi ý nhầm sang "Conical Travel". Đây là dấu hiệu độ phủ thương hiệu và backlink rất thấp ngoài site của chính VCT. Kể cả chương trình RAI cũng không tìm thấy trang nào nhắc tới VCT. Các kết quả tiếng Ý trả về là đối thủ: OVET Viaggi, WeRoad, Threeland ("Migliore agenzia di viaggi del Vietnam"). Lưu ý: công cụ tìm kiếm dùng ở đây có giới hạn (chỉ US), nên cần kiểm tra lại bằng Google Italia và Search Console.

---

## 7. So sánh giữa các site

### 7.1 Tính nhất quán thương hiệu
- **Hai hệ nhận diện**: Wix (chữ hoa, template, nhiều lỗi) và hệ "cream/xanh rừng/vàng + Source Sans 3" của các subdomain (tiết chế, biên tập kỹ). Tên gọi cũng lẫn lộn: "VIETCONE TRAVEL", "Viet Cone Travel", "VietCone", "Viet Cone".
- Định vị trên subdomain rõ hơn: "DMC specializzata … per il mercato italiano". Site chính lại tự nhận phủ 4 nước, 3 ngôn ngữ, nên thông điệp loãng hơn.
- Slogan "Immerse. Not just observe." chỉ xuất hiện trên site chính, trong khi Immersion là nơi thể hiện nó rõ nhất.
- Thông tin không khớp nhau: 20+ năm / thành lập 2010; Travelife 13/14; hai số điện thoại; email infor@.

### 7.2 Trùng lặp
- Lịch trình Partenze, Vespa tour, Viaggio di nozze, vivivietnam và vietnamangkor dùng chung "xương sống" Hà Nội – Hạ Long – Huế – Hội An – Saigon – Bến Tre, với cùng đoạn mô tả Bến Tre (kẹo dừa, chiếu, xe lôi) và Củ Chi "200 km di gallerie".
- Trải nghiệm Immersion (Đường Lâm, Trà Vinh Khmer, Hội An) trùng với nội dung tour và blog trên site chính, nhưng hai bên không liên kết với nhau.

### 7.3 Khoảng trống
1. **Không có điều hướng liên site.** Site chính không trỏ tới Immersion hay Partenze. Subdomain chỉ trỏ về trang chủ chính. Proposal không trỏ đi đâu cả.
2. **Giá**: chỉ có Partenze. Site chính và Immersion hoàn toàn không có giá.
3. **Review và social proof**: không site nào có trích dẫn đánh giá bằng chữ. Tripadvisor chỉ là một badge.
4. **RAI/Tg1**: chỉ nhắc trên site chính, chưa có trang riêng, chưa có trên Partenze và Immersion, chưa có báo chí bên ngoài.
5. **Đo lường**: site chính dùng GA4, Partenze dùng analytics riêng, Immersion/vivi/angkor không thấy tracking. Không có cái nhìn chung về funnel.
6. **Thu lead**: ba luồng khác nhau (form Wix, form Partenze, brief TTG) cộng WhatsApp. Không có lead magnet nào (PDF guide, newsletter được quảng bá).
7. **Ngôn ngữ**: chiến lược chính là tiếng Ý nhưng bản EN/ES của site chính còn dở dang. Subdomain có EN tốt hơn.
8. **SEO**: site chính có lượng nội dung lớn (146 URL, 75 bài blog) nhưng kém về kỹ thuật. Subdomain kỹ thuật tốt nhưng ít nội dung và proposal có thể bị index ngoài ý muốn.

### 7.4 Ưu tiên đề xuất (ngắn)
1. Dọn site chính trong 1–2 ngày: xóa book-online và copy-of-*, sửa infor@ và chính tả nút, viết lại title/meta.
2. Thêm khối "Immersion" và "Partenze 2027" lên menu và trang chủ chính. Thêm footer thương hiệu và liên hệ cho mọi proposal, kèm `noindex`.
3. Đưa giá (EUR) và review vào các trang tour. Làm một trang riêng cho RAI và Travelife.
4. Thống nhất số điện thoại, tên thương hiệu và số năm kinh nghiệm. Chuyển LinkedIn sang Company Page, gộp 2 page Facebook.
5. Lâu dài: cân nhắc chuyển site chính sang cùng stack Astro/Cloudflare với subdomain để có một hệ thiết kế duy nhất.
