# Data card — dữ liệu bản chạy thử dùng

> Điền ở guide bước 2.4 (bản đầu ở CP2, đủ ở CP3). Ôn lại: ngày 6 · lab ngày 6. Chấm ở rubric R4.
> Bản đầu CP2: Lê Anh Tuấn soạn, Đỗ Minh Thanh rà mục Dataset 2.

## Dataset 1 · Chuyến bay và đặt chỗ giả (`data/flights.json`)

| | |
|---|---|
| Dùng để làm gì | Nguồn cho công cụ tra đặt chỗ và tra chuyến thay thế; căn cứ để chấm `eval/benchmark.csv` (metric `chuyen_goi_y_hop_le`, `so_lieu_khop_du_lieu`) |
| Từ đâu | Nhóm tự viết tay. Hãng dựng "Bay Mẫu" (mã BM), mã đặt chỗ dựng (TRV-xxxx, theo kiểu đặt chỗ TRV-7Q2K của lab ngày 5) |
| Xử lý những bước gì | Không lọc, không ẩn danh vì không có người thật. Mỗi đặt chỗ dựng cho một kịch bản ở `spec.md` §5 |
| Số dòng / số đoạn | 8 đặt chỗ · 22 chuyến bay (8 chuyến bị huỷ, gồm 1 chuyến thay thế cũng bị huỷ) · 6 sân bay |
| Phủ các ca | Đến kịp và đủ chỗ (BM105, BM145, BM203) · đến muộn (BM107) · thiếu ghế (BM103: 2 ghế, BM153: 1 ghế, BM201: 0 ghế) · không có dữ liệu số ghế (BM109, BM303) · chuyến thay thế bị huỷ (BM143) · sân bay khác điểm đến (BM171 đến Cam Ranh) · đoàn 10 người không chuyến nào đủ chỗ · trẻ bay một mình · chuyến khách nói bị huỷ nhưng dữ liệu báo đúng giờ (BM411) |
| Phiên bản / ngày lấy | v1 · 27/11/2026 · ngày tham chiếu "hôm nay" = 27/11/2026 |
| Nhãn | `synthetic` |
| Cách sinh / seed | Viết tay, không sinh ngẫu nhiên nên không có seed. Đã đối chiếu bằng script phương án đúng của từng câu thử với file này (lọc theo chặng, ngày, trạng thái, số ghế, giờ đến): khớp `expected`. Chưa có người thứ hai kiểm tay |
| Giới hạn | Ít chuyến mỗi chặng, không có giá vé, phí đổi, chính sách hoàn; giờ theo một múi giờ. Không phản ánh tình trạng chỗ thật của hãng nào. **Không phải bằng chứng pain.** |

Phối hợp: issue #5 (Sơn, Huy) dựng công cụ tra cứu trên file này. Nếu đổi dữ liệu thì phải đổi `expected` trước CP2, sau CP2 chỉ được **thêm** chuyến mới cho câu thử mới.

## Dataset 2 · Review công khai C3 (`evidence/c3-reviews.csv`)

| | |
|---|---|
| Dùng để làm gì | Đào bằng chứng pain; nguồn tình huống cho các câu thử có `source = data_that` |
| Từ đâu | 20 review trang 7 của Porter Airlines trên Trustpilot, kèm các ca công khai khác trong `evidence/data-mining.md` (Trustpilot, AirAdvisor, Tuổi Trẻ) |
| Xử lý những bước gì | Lấy đủ 20 review theo thứ tự hiển thị, mọi mức sao · bỏ tên người viết · tóm tắt tiếng Việt · gắn 2 nhãn theo định nghĩa trong `evidence/data-mining.md` |
| Số dòng / số đoạn | 20 review + 7 ca ví dụ ngoài mẫu |
| Phiên bản / ngày lấy | Xem ngày 27/11/2026; review hiển thị ngày 08/02–20/03/2026 |
| Nhãn | thật (công khai, đã bỏ tên) |
| Giới hạn | Một trang của một hãng quốc tế; người viết review thường đang bực nên mẫu nghiêng về phàn nàn. Câu thử `data_that` chỉ lấy **tình huống** từ các ca này rồi viết lại vào đặt chỗ giả, không chép lời người viết |
