# Tổng hợp bằng chứng pain

## 1. Nguồn và tiến độ CP3

| Nguồn | Tiến độ | Tài liệu |
|---|---|---|
| Đào dữ liệu công khai | Nguồn chính cho CP3. Đã mã hoá 20 review Porter Airlines trên một trang Trustpilot, có cách đếm chạy lại và 6 trích dẫn đối chiếu được | [Cách đếm và nguồn](data-mining.md) · [Bảng mã hoá](c3-reviews.csv) · [Bảng trích xuất 25 bản ghi](c3-public-cases.csv) |
| Phỏng vấn | Chưa có biên bản hoặc lịch hẹn được ghi nhận | [Mẫu phỏng vấn](interviews/TEMPLATE.md) |
| Khảo sát | Đã có tệp CSV trong repo. Chưa đối chiếu bản xuất form gốc và điều kiện sàng lọc | [Bộ câu hỏi](survey/questions-C3.md) · [Tệp CSV hiện có](survey/results.csv) |

## 2. Số chính

- **3/20 review (15%)** nêu trở ngại với chuyến thay thế sau khi bị huỷ.
- **0/20 review** nói rõ nhóm bị xếp sang các chuyến khác nhau hoặc chuyến thay thế thiếu chỗ cho cả nhóm.
- Hai tỷ lệ dùng chung mẫu 20 review của một hãng, gồm mọi mức sao. Mẫu chưa cho biết tần suất gặp vấn đề của gia đình đi chuyến nội địa tại Việt Nam.

## 3. Trích dẫn đối chiếu với nguồn công khai ngày 27/11/2026

| Ca | Trích dẫn hoặc hệ quả |
|---|---|
| Review #8 trong mẫu | “rebooked on another flight 96 hours later”. Chuyến thay thế cũng bị huỷ. [Trustpilot, trang mẫu Porter](https://au.trustpilot.com/review/flyporter.com?page=7) |
| Review #20 trong mẫu | “get on a flight to Hamilton”. Khách kể phát sinh 165 đô la tiền xe. [Trang mẫu Trustpilot](https://au.trustpilot.com/review/flyporter.com?page=7) |
| Nhóm 10 người tại Việt Nam, ngoài mẫu | “nhân viên ở đây cho biết đã hết vé”. Theo bài báo, đoàn đi muộn thêm một ngày và phát sinh hơn 2,5 triệu đồng. [Tuổi Trẻ](https://tuoitre.vn/se-cong-khai-ly-do-cham-huy-chuyen-bay-622561.htm) |
| Review #11 trong mẫu | “I spent 21 hours sitting in Halifax airport”. Khách kể đã lỡ việc sau đợt huỷ và hoãn chuyến. [Trustpilot, trang mẫu Porter](https://au.trustpilot.com/review/flyporter.com?page=7) |
| Gia đình có trẻ nhỏ, ngoài mẫu | “I had to manually rebook our flights through the AA website”. Khách kể đến nơi muộn 48 giờ. [AirAdvisor](https://airadvisor.com/en-us/airline-complaints/american-airlines/comments/page/5) |
| Người thân đổi vé từ Phần Lan, ngoài mẫu | “Ba ngày gần như chỉ lo tìm đường bay cho mẹ.” Người thân xác nhận được vé mới khi liên hệ hãng khai thác chặng đầu. [Tuổi Trẻ](https://tuoitre.vn/du-khach-viet-chay-dua-thoat-khoi-vung-chien-su-ve-may-bay-tang-tung-gio-20260305225348807.htm) |

## 4. Kết luận

**Kết luận về giả thuyết: phải thu hẹp.** Dữ liệu công khai ghi nhận khó khăn khi tìm chuyến thay thế, nên nhóm tập trung gợi ý một chuyến đến kịp giờ và đủ chỗ cho cả nhà. Khách tự quyết định đổi vé.

[Giả thuyết gốc](hypothesis.md) dự kiến dùng review Google Play/App Store 1–3 sao và phỏng vấn. Mẫu đã thu là review Trustpilot của Porter, gồm mọi mức sao. Vì khác nền tảng, bộ lọc và điều kiện gắn nhãn, 15% trong mẫu Porter chưa kiểm được ngưỡng giả thuyết ban đầu. Cần hỏi đúng nhóm gia đình đi chuyến nội địa Việt Nam để đo tần suất và thời gian họ tự tìm chuyến.

## Lịch hẹn CP2

Chưa có lịch hẹn được ghi nhận trong repo.
