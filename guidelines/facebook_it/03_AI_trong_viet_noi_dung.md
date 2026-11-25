# AI trong viết nội dung · Claude và ChatGPT

Viet Cone Travel · Bản 1.0 · 25/11/2026 · Tài liệu nội bộ
Đi kèm 01 Kế hoạch và 02 Content Guideline.

---

## 1. Nguyên tắc

- AI giúp viết nháp nhanh hơn, không thay người chịu trách nhiệm.
- AI chỉ viết từ dữ kiện đã xác minh do người đưa vào. Không để AI tự thêm tên, số, ngày, địa điểm.
- Mọi bài tiếng Ý có một người đọc tiếng Ý tốt duyệt trước khi đăng.
- Ưu tiên ảnh, video thật. Ảnh AI không dùng để mô tả nơi thật, người thật, trải nghiệm thật.
- Không đưa dữ liệu cá nhân của khách, liên hệ đối tác vào công cụ AI.
- Viết theo kỹ thuật, không theo tên model: model đổi nhanh, kỹ thuật bền hơn.

---

## 2. Thiết lập công cụ

### 2.1 Một Project dùng chung

Tạo một Project (Claude hoặc ChatGPT) tên "VCT – Facebook IT", chứa:

| Tài liệu đưa vào | Mục đích |
|---|---|
| 02 Content Guideline | Giọng, từ ngữ, chuỗi bài, Patto con i partner |
| `VCT_Marketing_Context.md` mục 4, 5, 9 | Định vị, sản phẩm, câu chuẩn RAI, Travelife |
| 3–5 bài tiếng Ý tốt nhất đã đăng (hoặc bài mẫu 02 Guideline mục 12) | Ví dụ để AI bắt chước giọng |
| Bảng "từ nên thay" (02 Guideline mục 6.3) | Tránh sáo ngữ |

Instructions của Project (dán nguyên):

```
Sei un copywriter italiano madrelingua per Viet Cone Travel, un DMC di Hanoi.
Scrivi per viaggiatori italiani dai 50 anni in su e per agenzie di viaggio italiane.
Segui la guida nei file del progetto. Usa solo i fatti che ti fornisco nel messaggio.
Se manca un dato, scrivi [DA VERIFICARE] invece di inventarlo.
Frasi brevi e concrete: chi, dove, cosa, quanto dura. Pochi aggettivi.
Non usare prezzi di viaggi su misura. Non nominare agenzie o clienti se non te lo chiedo.
```

### 2.2 Tính năng nên dùng (11/2026)

| Công cụ | Nên dùng | Lưu ý |
|---|---|---|
| Claude | Projects (file kiến thức + instructions); Styles (tạo style từ bài mẫu); Skills (có thể đóng gói guideline thương hiệu); web search có nguồn | Team/Enterprise: chia sẻ Project cho cả đội; memory tách theo Project |
| ChatGPT | Projects (instructions của Project ghi đè custom instructions chung) | Custom GPTs ngừng hoạt động 11/12/2026: không xây quy trình mới trên GPTs. Canvas đã bị thay bằng khối viết trong chat ở model mới |

Nguồn: support.claude.com (Projects, Memory, Styles, Skills); help.openai.com (Projects, Custom GPT retirement FAQ, release notes). Tính năng thay đổi nhanh; kiểm tra lại mỗi quý.

### 2.3 Dữ liệu

- Claude Free/Pro/Max: có tùy chọn cho phép dùng hội thoại để huấn luyện model. Tắt tùy chọn này trong cài đặt quyền riêng tư.
- Claude Team/Enterprise và ChatGPT Business/Enterprise: mặc định không dùng dữ liệu doanh nghiệp để huấn luyện (theo điều khoản thương mại).
- Ở mọi gói: không dán tên khách, email, số điện thoại, hộ chiếu, ghi chú khách, liên hệ đối tác. Thay bằng mô tả chung ("una coppia di Bologna, 60 anni").

---

## 3. Quy trình 7 bước

| Bước | Ai | Việc | Kết quả |
|---|---|---|---|
| 1 | Trưởng nhóm | Brief tiếng Việt: trụ cột, chuỗi, người đọc chính, một ý chính, CTA | 3–5 dòng |
| 2 | TTS nội dung | Fact sheet: chỉ dữ kiện có nguồn (người, nơi, giờ, số, câu chuẩn) | Danh sách dữ kiện + link nguồn |
| 3 | AI | Viết 3 phương án caption tiếng Ý từ brief và fact sheet (prompt 4.1) | 3 bản nháp |
| 4 | AI | Tự phê bình theo guideline và dấu hiệu văn AI, rồi sửa (prompt 4.2) | Bảng lỗi + bản sửa |
| 5 | Người duyệt tiếng Ý | Đọc to, sửa giọng, kiểm từng dữ kiện, chịu trách nhiệm biên tập | Bản cuối |
| 6 | Trưởng nhóm | Soát checklist 02 Guideline mục 9.2; kiểm hình ảnh (mục 6 dưới đây) | Đạt / chưa đạt |
| 7 | TTS nội dung | Đăng; lưu prompt, nguồn, tên người duyệt vào sheet nội dung | Dòng lưu trữ |

- Bước 3–4 có thể chạy 2–3 lần rồi chọn bản tốt nhất.
- Bước 5 không bỏ được. AI tiếng Ý thường đúng ngữ pháp nhưng sai sắc thái, hoặc nghe như catalogue.

---

## 4. Prompt mẫu

Kỹ thuật dựa trên hướng dẫn chính thức của Anthropic (viết rõ, giải thích lý do, đưa ví dụ, tách phần bằng thẻ XML, cho phép trả lời "không biết", kiểm từng tuyên bố bằng trích dẫn) và OpenAI (nêu kết quả cần đạt trước, nói rõ độ dài, giọng, định dạng).

### 4.1 Viết nháp caption

```
<brief>
Trụ cột: [01/02/03/04] · Chuỗi: [tên chuỗi]
Người đọc: [viaggiatori 50+ / agenzie]
Ý chính: [một câu]
CTA: [Scriveteci su WhatsApp / link Partenze / ...]
</brief>

<facts>
[Dữ kiện đã xác minh, mỗi dòng một ý, kèm nguồn]
</facts>

<task>
Scrivi 3 varianti di post Facebook in italiano.
- Prima riga: un dettaglio concreto o una domanda vera, che faccia fermare chi scorre.
- 60–150 parole, paragrafi di 1–3 frasi, "voi".
- Usa SOLO i fatti in <facts>. Se ti serve un dato che non c'è, scrivi [DA VERIFICARE].
- Massimo 2 emoji, 2–4 hashtag tra cui #VietConeTravel.
- Evita: autentico, immergersi, indimenticabile, mozzafiato, paradiso, gemma nascosta,
  "non solo… ma anche", elenchi di tre aggettivi, trattini lunghi.
- Le tre varianti devono essere diverse nell'attacco, non solo nelle parole.
Se il brief non è chiaro, fammi prima al massimo 3 domande.
</task>
```

### 4.2 Phê bình và sửa

```
<draft>[bản nháp]</draft>
<facts>[fact sheet]</facts>

Valuta la bozza secondo la guida del progetto:
1. Ogni affermazione: indica il fatto in <facts> che la sostiene. Se non c'è, segnala da togliere.
2. Tono: suona come un amico vietnamita che parla bene l'italiano, o come un catalogo?
3. Segnali di testo scritto da un'IA (frasi generiche, triadi, contrasti "non X ma Y",
   chiusure ad effetto, troppi aggettivi, emoji decorative).
4. Naturalezza per un lettore italiano di 60 anni: c'è qualcosa che non direbbe mai?
5. Rispetto dei partner: prezzi, nomi di agenzie o clienti, inviti a prenotare direttamente.
Restituisci una tabella (problema | frase | proposta), poi una versione rivista.
```

### 4.3 Chuyển bài tiếng Việt sang tiếng Ý

```
Riscrivi in italiano questo testo per la nostra pagina Facebook.
Non tradurre parola per parola: scrivi come lo direbbe un redattore italiano,
mantenendo tutti i fatti e nessun fatto in più.
Segnala tra [ ] i punti in cui il significato vietnamita non è chiaro.
<testo>[bài tiếng Việt]</testo>
```

### 4.4 Câu trả lời bình luận

```
Un utente ha scritto questo commento: <commento>[...]</commento>
Proponi 2 risposte brevi in italiano, calde e concrete, firmate "[Nome], Viet Cone Travel".
Regole: niente prezzi in pubblico; se chiede un preventivo, invitalo in privato o su WhatsApp;
se cita un'agenzia, ringrazia e non invitarlo a prenotare con noi.
```

---

## 5. Dấu hiệu văn AI trong tiếng Ý

Đây là dấu hiệu để soát, không phải danh sách cấm. Người đọc thật chỉ đoán đúng văn AI khoảng một nửa số lần; vấn đề không nằm ở việc "bị phát hiện" mà ở bài nghe chung chung, giống mọi Page du lịch khác.

| Dấu hiệu | Ví dụ | Sửa |
|---|---|---|
| Phép đối "non solo… ma…" | "Non solo un viaggio, ma un'esperienza" | Nói thẳng điều khách làm |
| Bộ ba tính từ, bộ ba vế | "autentico, sostenibile e indimenticabile" | Một chi tiết thật thay cả ba |
| Văn quảng cáo phô trương | "incastonato nel cuore di", "ricco patrimonio culturale" | Tên nơi, tên người, việc cụ thể |
| Câu mở, câu kết khuôn mẫu | "Oggi vi parliamo di…", "In conclusione…" | Mở bằng chi tiết; kết bằng câu hỏi thật hoặc CTA |
| Gạch ngang dài liên tục | "Hoi An — città di lanterne — vi aspetta" | Dấu phẩy, dấu chấm |
| Danh từ hóa, giọng hành chính | "la valorizzazione della fruizione del territorio" | Động từ: "visitare", "cucinare con" |
| Emoji trang trí mọi dòng | ✨🌿🏮💫 | 0–2 emoji, có chức năng |
| Sáo ngữ du lịch | immergersi, autentico, viaggio indimenticabile | Quan sát biên tập, chưa có số đo; thay theo 02 Guideline mục 6.3 |

Nguồn: Wikipedia, "Signs of AI writing" (trang hướng dẫn của WikiProject AI Cleanup); Pangram (bản tiếng Ý, có xung đột lợi ích vì bán công cụ phát hiện); Agenda Digitale; Punto Informatico.

---

## 6. Hình ảnh AI và quy định

### 6.1 Quy tắc dùng ảnh, video

| Trường hợp | Cách làm |
|---|---|
| Ảnh, video thật của đội ngũ, khách (có đồng ý) | Ưu tiên số 1 |
| Chỉnh sáng, cân bằng trắng, cắt khung | Được (Brand Guideline 5.4) |
| Xóa, thêm người hoặc vật thể | Không (Brand Guideline 5.4) |
| Ảnh, video AI giống thật về nơi thật (Hạ Long, phố cổ, bản làng) | Không dùng |
| Minh họa AI rõ ràng không phải ảnh thật (bản đồ vẽ, icon, hình minh họa) | Được; ghi rõ khi có thể gây hiểu nhầm |
| Giọng đọc AI cho Reels | Ưu tiên giọng người trong đội; nếu dùng giọng AI giống người thật, bật nhãn AI của Meta |

### 6.2 Vì sao

- Meta: bắt buộc tự gắn nhãn "AI info" cho video giống thật, âm thanh giống thật do AI tạo hoặc chỉnh; ảnh có thể bị Meta tự gắn nhãn khi phát hiện metadata C2PA/IPTC (ảnh tạo bằng ChatGPT có metadata C2PA). Thiếu nhãn khi bắt buộc có thể bị phạt theo Community Standards.
- EU AI Act, Điều 50 (áp dụng từ 2/8/2026): người dùng hệ thống AI phải công bố deepfake; định nghĩa deepfake gồm cả ảnh, video giống địa điểm có thật. Áp dụng cả với doanh nghiệp ngoài EU khi nội dung dùng tại EU.
- Văn bản AI: nghĩa vụ công bố áp cho văn bản nhằm thông tin cho công chúng về vấn đề lợi ích chung, và được miễn khi có người xem xét, kiểm soát biên tập. Caption quảng cáo tour nhiều khả năng nằm ngoài phạm vi này (suy luận, chưa có hướng dẫn xác nhận). Bước 5 của quy trình là kiểm soát biên tập thực chất.
- Ý, Luật 132/2025: không thấy nghĩa vụ gắn nhãn riêng cho nội dung marketing; có tội danh phát tán deepfake gây hại.
- Quảng cáo gây hiểu lầm (Codice del Consumo): ảnh làm điểm đến đẹp hơn thực tế có thể bị coi là gây hiểu lầm. Chưa tìm thấy vụ AGCM nào về ảnh AI trong du lịch; Cơ quan quảng cáo Anh (ASA, 6/2026) khẳng định nhà quảng cáo chịu trách nhiệm với quảng cáo làm bằng AI.
- Hiệu quả: nghiên cứu cho thấy nhãn AI có thể làm giảm tương tác, nhất là với nội dung cảm xúc. Thêm một lý do ưu tiên ảnh thật.

### 6.3 Facebook có phạt bài viết bằng AI không

- Meta không phạt bài chỉ vì dùng AI.
- Từ 3/2026 Meta hạ thấp nội dung không gốc, đăng lại, chỉnh sửa sơ sài. Rủi ro với AI là bài na ná nhau, sản xuất hàng loạt.
- Cách giữ tính gốc: dữ kiện riêng của Viet Cone, người thật có tên, ảnh tự chụp, giọng của người duyệt.

---

## Nguồn

| Nội dung | Link |
|---|---|
| Anthropic, prompting best practices | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices |
| Anthropic, giảm bịa thông tin | https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations |
| Claude Projects | https://support.claude.com/en/articles/9517075-what-are-projects |
| Claude Skills | https://support.claude.com/en/articles/12512176-what-are-skills |
| Claude, điều khoản người dùng cá nhân | https://www.anthropic.com/news/updates-to-our-consumer-terms |
| Anthropic, điều khoản thương mại | https://www.anthropic.com/legal/commercial-terms |
| OpenAI, prompt guidance | https://developers.openai.com/api/docs/guides/prompt-guidance.md |
| ChatGPT Projects | https://help.openai.com/en/articles/10169521 |
| Custom GPT ngừng hoạt động | https://help.openai.com/en/articles/20001519-custom-gpt-retirement-and-migration-faq |
| OpenAI, dữ liệu doanh nghiệp | https://openai.com/business-data/ |
| Meta, nhãn AI | https://www.meta.com/help/artificial-intelligence/1783222608822690/ |
| Meta, nội dung gốc (3/2026) | https://about.fb.com/news/2026/03/rewarding-original-creators/ |
| EU AI Act | https://eur-lex.europa.eu/eli/reg/2024/1689/oj |
| Điều 50 AI Act và Luật 132/2025 | https://www.assolombarda.it/servizi/diritto-di-impresa/informazioni/intelligenza-artificiale-art-50-ai-act-e-art-13-legge-132-2025-a-confronto |
| ASA, AI và deepfake trong quảng cáo | https://www.asa.org.uk/news/ai-and-deepfakes-four-things-advertisers-need-to-know-before-they-hit-run.html |
| Dấu hiệu văn AI | https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing · https://www.pangram.com/it/signs-of-ai-writing |
| Nhãn AI và tương tác | https://www.cbs.dk/en/articles/ai-labels-reduce-social-media-engagement |

Một số trang chính thức (Meta, OpenAI, EU) chỉ đọc được qua kết quả tìm kiếm trong lúc soạn. Kiểm tra lại trước khi trích nguyên văn ra ngoài.
