# Reflection — Đỗ Minh Thanh

> Làm ở guide bước 5.3. Hạn: **23:59 Thứ Bảy 28/11**. Mỗi câu 3–6 dòng.

1. **Vai trò + phần mình làm (trỏ tới file / commit):**
   Đội trưởng, phụ trách bằng chứng pain, impact, Canvas, `spec.md` §0–§2 và nộp checkpoint.
   - CP1 (`64110e2`, `199c454`, `995368d`): điền `TEAMS.md`, chia việc cho 4 người, viết Canvas, `spec.md` §1/§4/§10, giả thuyết và bằng chứng review C3.
   - CP2–CP3 (`972a098`, `1fb7894`, `ec366a6`, PR #7, #14, #15): tổng hợp `evidence/summary.md`; thay bộ ca giả lập bằng 25 bản ghi trích từ nguồn công khai (`evidence/c3-public-cases.csv`); mã hoá 20 review Porter; ước tính impact ở §2.
   - CP3–CP4 (`0ee30eb`, PR #17; `5578a9b`, PR #25): chấm lượt 1 (25/26), đối chiếu trích dẫn (5/6 khớp nguyên văn), làm slide và `demo-slides.pdf`; mở các issue #9–#12, #18–#21 để chia việc.

2. **AI hỗ trợ mình thế nào (việc gì, công cụ gì, chỗ nào phải sửa lại output AI):**
   Mình dùng Claude Code (và Codex cho nhánh `codex/c3-public-evidence`) để soạn nháp Canvas, spec, tổng hợp bằng chứng, chia việc thành issue, chấm nháp và dựng slide. Những chỗ phải sửa lại hoặc kiểm lại output của AI:
   - Trích dẫn phải mở lại trang gốc để đối chiếu. Một ca (AirAdvisor) không còn trên trang nên mình ghi "chưa đối chiếu được" và không dùng nó, thay vì giữ lại.
   - Số impact không có nguồn nên ghi rõ *(tự ước tính)*.
   - Nội dung PR do AI viết có `@` + tên thật của bạn trong nhóm, có thể gọi nhầm một tài khoản GitHub khác, nên mình đã bỏ đi.

3. **Một câu thử trượt của nhóm và mình học được gì từ nó:**
   B09: khách cần đến Sài Gòn trước 08:00 nhưng không chuyến nào kịp. Ở lượt 1, trợ lý chỉ chuyển khách sang nhân viên, bỏ sót BM105 (đến 11:40, đủ ghế). Nhóm thêm một quy tắc chung (2b) chứ không viết riêng cho câu này; lượt 2 đạt 26/26 và không câu nào tệ đi.
   Ở vai trò đội trưởng, điều mình học được là: 100% trên 26 câu do nhóm tự dựng, mỗi câu chạy 1 lần, chưa đủ để nói "Go". Vì vậy kết luận trên slide là *Iterate*, kèm giới hạn ghi rõ. Lần sau mình sẽ tìm người dùng thật (phụ huynh từng bị huỷ chuyến) ngay từ CP1, vì phần impact và phần phỏng vấn của mình vẫn đang thiếu chính dữ liệu đó.
