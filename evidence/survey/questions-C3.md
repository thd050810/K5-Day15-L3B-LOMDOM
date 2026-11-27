# Khảo sát — Trải nghiệm xử lý khi chuyến bay nội địa bị huỷ / đổi lịch

> Điền ở guide bước 1.2.
> Ngưỡng: **≥20 người ngoài nhóm, đúng người dùng**, giữ log đủ câu hỏi và từng câu trả lời.

## Bộ câu hỏi (`*` = bắt buộc)

| # | Câu hỏi | Kiểu trả lời |
|---|---|---|
| 1 | Bạn là:* | Chọn một (Học viên L3A · Học viên L3B · Bạn bè / người thân (đi làm) · Sinh viên · Khác) |
| 2 | Lần gần nhất chuyến bay nội địa của bạn bị huỷ hoặc hãng tự đổi giờ bay là khi nào?* | Chọn một (Trong 1 tháng qua · 1–6 tháng trước · 6–12 tháng trước · Lâu hơn 1 năm · Chưa bao giờ) |
| 3 | Trong 12 tháng qua, bạn gặp tình trạng chuyến bay nội địa bị huỷ hoặc tự đổi giờ mấy lần? (Nhập số, vd: 0, 1, 2...)* | Số |
| 4 | Lần gần nhất đó, bạn đã làm thế nào để xử lý (đổi chuyến / hoàn vé)? | Chọn nhiều (Tự thao tác trên app/web hãng bay hoặc OTA (Traveloka, Booking...) · Gọi tổng đài hãng bay / OTA · Nhắn chat hỗ trợ · Ra quầy sân bay · Nhờ đại lý / người quen · Bỏ vé / chấp nhận lịch mới · Khác) |
| 5 | Lần đó bạn mất khoảng bao lâu để xử lý xong? | Chọn một (Dưới 15 phút · 15–30 phút · 30–60 phút · 60–90 phút · Trên 90 phút) |
| 6 | Lần đó bạn có xong việc không? | Chọn một (Xong (đổi được chuyến phù hợp / hoàn vé suôn sẻ) · Xong một phần (chấp nhận giờ xấu, mất thêm phí hoặc phải chờ hoàn tiền lâu) · Bỏ (không xử lý được / bỏ vé)) |
| 7 | Điều gì khó chịu hoặc lo lắng nhất ở lần xử lý đó? | Đoạn văn |
| 8 | (Tuỳ chọn) Bạn có sẵn lòng cho nhóm hỏi thêm 10 phút không? Nếu có, vui lòng để lại cách liên hệ (không bắt buộc) | Đoạn văn ngắn (không bắt buộc) |

Không thu tên, email, mã học viên trong form (trừ câu 8 nếu người trả lời tự để lại — **phải xoá cột câu 8 trước khi commit `results.csv`**).

## Lưu vào thư mục này

- `questions.md` — nguyên bộ câu hỏi + kênh đã gửi + giờ mở / chốt (file này).
- `results.csv` — bản xuất **đã xoá** mọi cột nhận ra người trả lời (cột câu 8 nếu có thông tin liên hệ). Bản gốc còn thông tin cá nhân đặt tên `raw-*.csv` (đã có trong `.gitignore`) và **không** commit.
- Số chính + ≥3 câu trả lời nguyên văn → chép vào `evidence/summary.md`. Dưới khoảng 10 người thì chỉ ghi `x/n`, không ghi `%`.