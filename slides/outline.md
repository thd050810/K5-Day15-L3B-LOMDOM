# Dàn slide → lấy số từ file nào

> Làm ở guide bước 5.1. Luật: **không có bằng chứng thì không có slide** — mỗi trang ≥1 con số / trích dẫn có nguồn / kết quả đo.
> Xuất PDF thành `demo-slides.pdf` ở thư mục gốc repo, nộp tại CP4 14:30 Thứ Bảy 28/11. Nộp PDF, không nộp link.

| # | Trang | Có gì | Số lấy từ | Xong |
|---|---|---|---|---|
| 1 | Người dùng & pain | Hành khách đặt vé nội địa đi cùng con nhỏ vừa bị huỷ chuyến; cần tìm 1 chuyến đến kịp giờ và đủ chỗ cho cả nhà. Số: **3/20 review Porter (15%)** nêu trở ngại chuyến thay thế (chuyến thay thế lại bị huỷ 96 giờ sau, phải đáp xuống sân bay khác tốn $165 về nhà); ngoài mẫu: **đoàn 10 người** hết vé bị trễ 1 ngày, phát sinh **> 2,5 triệu đ** (Tuổi Trẻ). | `evidence/summary.md` · `spec.md` §1 | ☑ |
| 2 | Vì sao chọn bài này | Bảng impact rút gọn cho lát cắt gợi ý chuyến: **10 gia đình × 1 lần/tháng × 15–30 phút = 150–300 phút/tháng** *(tự ước tính)*. Giải thích vì sao loại 2 hướng: tự giữ/đổi vé (cần quyền sửa đặt chỗ, rủi ro thao tác khó đảo ngược) và hỗ trợ hoàn vé (chưa đo tác động, phụ thuộc chính sách từng vé). | `spec.md` §2 | ☑ |
| 3 | Giải pháp | Lát cắt 1 câu · Sơ đồ workflow cố định 2 bước (`tra_dat_cho` → `tra_chuyen_thay_the` → `call_model`). Mức tự động: **AI gợi ý, người tự xác nhận trên app**. Chỗ chặn rủi ro: tách riêng chuyến `huy`, `con_ghe = null`, thiếu ghế; che số thẻ/OTP; chặn ca trẻ đi một mình & tin nhắn giả mạo nhân viên. | `spec.md` §4 · `codebase/agent.py` | ☑ |
| 4 | Demo live | Chạy trực tiếp `python run.py`: **1 ca thường** (`B01` — `TRV-7Q2K` gợi ý `BM105` 09:30→11:40, 5 ghế, nhắc tự xác nhận) + **1 ca khó/tấn công** (`B08` — `con_ghe = null` không khẳng định còn chỗ, hoặc `B16` — chèn lệnh + gửi số thẻ/OTP nhưng AI vẫn giữ giờ đúng `18:15` và không lặp lại OTP). Mạng hỏng → bật [video dự phòng 30s](https://drive.google.com/file/d/1DZ2G6oSoL-9CExZV7c9GtbvQjEiosldq/view?usp=sharing). | `eval/benchmark.csv` · [Video demo 30s](https://drive.google.com/file/d/1DZ2G6oSoL-9CExZV7c9GtbvQjEiosldq/view?usp=sharing) | ☑ |
| 5 | **Đánh giá thế nào** | Dataset `data/flights.json` (8 đặt chỗ, 22 chuyến) · **26 câu thử** (`thuong` 6 · `kho` 15 · `tu_choi` 5; **11/26** từ người dùng/data thật) · **4 metric** (`eval/metric_spec.yaml`). **Lượt 1** (`run-1@20261127-224214`, `gpt-6-luna`): **25/26 (96%)** — Đạt chuẩn (`thuong` 6/6, `kho` 14/15, `tu_choi` 5/5; trượt `B09` vì không nêu `BM105` 11:40). **Lượt 2** (`run-2@20261128-095947`, cùng model, cùng câu thử): **26/26 (100%)** — sau 1 cải tiến prompt (quy tắc 2b: khi không chuyến nào kịp giờ vẫn nêu chuyến sớm nhất đủ ghế và hỏi khách); B09 qua, 0 câu tệ đi. | `eval/README.md` · `eval/report.md` | ☑ |
| 6 | **Chi phí khi dùng thật** | Mô phỏng **50 phiên** (`simulate-1@20261128-014342`, seed 42, 0/50 lỗi, đo token trên `gpt-6-luna`, tỷ lệ đạt 25/26). Chi phí / task thành công: **$0.00065 (≈ 17 ₫)** (`gpt-6-luna`) · **$0.0065 (≈ 170 ₫)** (`gpt-6.1-terra`) · **$0.0131 (≈ 341 ₫)** (`gpt-6.2-sol`). 3 kịch bản / tháng (`gpt-6-luna`): thấp 500 người **$0.43 (≈ 11.189 ₫)** · cơ sở 2.000 người **$1.72 (≈ 44.754 ₫)** · cao 5.000 người **$4.30 (≈ 111.886 ₫)**. So impact: tốn **≈ 22 ₫/người/tháng** để tiết kiệm **15–30 phút/người/tháng**. | `cost/cost-estimate.md` · `cost/personas.yaml` | ☑ |
| 7 | Kết luận | Đề xuất **Iterate (tiếp tục tinh chỉnh & thử nghiệm thật)**: bài toán có pain rõ (Trang 1), lượt 1 **96%** → lượt 2 **100%** trên dữ liệu mẫu (Trang 5) và chi phí AI rất thấp **22 ₫/người/tháng** (Trang 6), nhưng dữ liệu là dữ liệu dựng, mỗi câu mới chạy 1 lần, và cần đo tần suất thực tế trên gia đình bay nội địa Việt Nam. | Trang 1, 5, 6 · `evidence/summary.md` | ☑ |
| 8 | Nếu có thêm 1 tuần | 3 việc ưu tiên: (1) Tách bộ câu giữ riêng (held-out) và chạy lặp ≥3 lần/câu để đo độ ổn định; thay regex trích ngày/giờ bằng trích xuất có kiểm schema; (2) Thu thập phỏng vấn/thử nghiệm thực tế với 5–10 phụ huynh từng bị huỷ chuyến nội địa VN (`validation/log.md`) để thay số *(tự ước tính)* ở §2 và `personas.yaml`; (3) Thử nối API lịch bay/tồn chỗ thật dạng chỉ đọc. | `eval/report.md` mục 4 · `validation/log.md` | ☑ |

**Trước khi lên:** tải repo về một máy khác (hoặc thư mục mới), chạy theo mục "Chạy trong 3 phút" của `README.md` · `.env` có trên máy demo, đã gọi thử 1 câu trong vòng 1 giờ trước giờ demo · video dự phòng mở được bằng cửa sổ ẩn danh · biết bản chạy thử sẽ làm gì với **1 câu thử lạ** của giám khảo.

Ai nói trang nào (mỗi người ≥1 phần — *đề xuất theo phân công `TEAMS.md`, xác nhận lại với nhóm*):

| Trang | Người nói |
|---|---|
| Trang 1 (Người dùng & pain), Trang 2 (Vì sao chọn bài này) | Đỗ Minh Thanh |
| Trang 3 (Giải pháp), Trang 4 (Demo live) | Nguyễn Quang Huy |
| Trang 5 (Đánh giá thế nào) | Lê Anh Tuấn |
| Trang 6 (Chi phí khi dùng thật), Trang 7 (Kết luận), Trang 8 (Nếu có thêm 1 tuần) | Trần Phạm Minh Sơn |
