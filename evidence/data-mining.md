# Bằng chứng pain · C3 — Đổi chuyến sau khi bị hủy

**Pain đang kiểm chứng.** Khi chuyến bay bị hủy, người đặt vé cho cả gia đình cần tìm chuyến thay thế kịp giờ và còn đủ chỗ cho mọi người. Phương án đổi có thể đến quá muộn, chuyển sang sân bay khác hoặc xếp nhóm lên các chuyến khác nhau.

## Mẫu review và cách đếm

- Nguồn là [trang 7 review công khai của Porter Airlines trên Trustpilot](https://au.trustpilot.com/review/flyporter.com?page=7), xem ngày **27/11/2026**. Dùng toàn bộ 20 review của bản trang đọc được, theo thứ tự hiển thị, gồm mọi mức sao, không lọc từ khóa. Trang được phát hiện qua truy vấn về đổi vé sau hủy chuyến. Ngày hiển thị trên các review trong mẫu từ 08/02 đến 20/03/2026, gồm cả ngày cập nhật.
- Mỗi dòng là một review, gồm ngày hiển thị, số sao, link và tóm tắt đã bỏ tên. [Bảng CSV](c3-reviews.csv) lưu các mã review cố định vì phân trang có thể thay đổi và trang từng review có thể khó mở.
- `kho_tim_chuyen_thay_the = 1` khi nội dung xác nhận chuyến bị hủy và nêu một trở ngại cụ thể với hành trình thay thế, như chờ nhiều giờ, lại bị hủy, hoặc phải bay sang sân bay khác. Chỉ có chậm chuyến, khách tự lỡ chuyến hoặc chỉ nhắc hủy ở tiêu đề thì ghi 0.
- `tach_nhom_hoac_khong_du_cho = 1` khi có hủy chuyến và review nói rõ nhóm bị chuyển sang các chuyến khác nhau hoặc không còn đủ chỗ để đi cùng chuyến. Tách ghế trên cùng một chuyến là tình huống khác. Giá trị 0 có nghĩa là review không nêu đủ điều kiện để gắn nhãn.

| Chỉ số | Số review | Tỷ lệ trong mẫu |
| --- | ---: | ---: |
| Nêu trở ngại với chuyến thay thế sau hủy chuyến | 3/20 | 15% |
| Nêu rõ tách nhóm sang chuyến khác hoặc thiếu chỗ cho cả nhóm | 0/20 | 0% |

Chạy lại phép đếm từ thư mục gốc repo:

```sh
awk -F, 'NR > 1 { n++; kho += $4; tach += $5 } END { if (n) printf "Kho doi: %d/%d (%.1f%%)\nTach nhom/thieu cho: %d/%d (%.1f%%)\n", kho, n, 100*kho/n, tach, n, 100*tach/n }' evidence/c3-reviews.csv
```

## Ví dụ từ nguồn công khai

Tất cả nguồn được xem ngày 27/11/2026. Các ca tìm theo từ khóa bên ngoài mẫu Porter không nằm trong mẫu số 20.

| Ca | Trích ngắn và hệ quả được kể lại | Nguồn |
| --- | --- | --- |
| Mẫu #8 | “rebooked on another flight 96 hours later”. Chuyến thay thế cũng bị hủy. | [Trustpilot, trang mẫu Porter](https://au.trustpilot.com/review/flyporter.com?page=7) |
| Mẫu #20 | “get on a flight to Hamilton”. Khách kể phải trả thêm 165 đô la tiền xe về nhà. | [Trustpilot, trang mẫu Porter](https://au.trustpilot.com/review/flyporter.com?page=7) |
| Nhóm 10 người tại Việt Nam | “nhân viên ở đây cho biết đã hết vé”. Chuyến đi kéo dài thêm một ngày và gia đình kể phát sinh hơn 2,5 triệu đồng. | [Tuổi Trẻ, 2014](https://tuoitre.vn/se-cong-khai-ly-do-cham-huy-chuyen-bay-622561.htm) |
| Cặp đôi bị xếp sang hai chuyến | “on separate flights 11 days and 13 days out”. Đoạn này xuất hiện trong bản Trustpilot do công cụ tìm kiếm lập chỉ mục, khác với bản trang 7 dùng để đếm. | [Trustpilot, Porter Airlines](https://au.trustpilot.com/review/flyporter.com?page=7) |
| Hai khách đi cùng sự kiện | “placed them on separate return flights”. Người tổ chức kể họ liên hệ hỗ trợ ít nhất 5 lần. | [Trustpilot, ITA Airways](https://www.trustpilot.com/review/www.ita-airways.com?page=5) |
| Gia đình có trẻ nhỏ | “I had to manually rebook our flights through the AA website”. Người đăng kể gia đình tới nơi muộn 48 giờ. Hai bản đăng cùng nội dung trên trang được xem là một ca. | [AirAdvisor, American Airlines](https://airadvisor.com/en-us/airline-complaints/american-airlines/comments/page/5) |
| Người thân đổi vé từ Phần Lan về Việt Nam | “Ba ngày gần như chỉ lo tìm đường bay cho mẹ.” Theo bài báo, vé mới cuối cùng được xác nhận sau khi liên hệ hãng khai thác chặng đầu. | [Tuổi Trẻ, 2026](https://tuoitre.vn/du-khach-viet-chay-dua-thoat-khoi-vung-chien-su-ve-may-bay-tang-tung-gio-20260305225348807.htm) |

## Bảng trích xuất theo tình huống

[Bảng 25 bản ghi](c3-public-cases.csv) gồm 20 review trong bảng mã hoá gốc và 5 trường hợp minh hoạ ngoài mẫu chọn theo nội dung. Cột `nhom_du_lieu` đánh dấu hai nhóm. Mỗi dòng có URL nguồn. Hai trường hợp khác nhau từ cùng một bài báo được ghi hai dòng. Những gì nguồn không nêu rõ để trống, kể cả số người, trẻ nhỏ, hành trình và cách xử lý.

Chỉ dùng 20 dòng `mau_porter` để tính các tỷ lệ trên. Năm dòng `ngoai_mau` minh hoạ các trở ngại như thiếu chỗ, phải đổi sân bay, tách nhóm và tự đổi vé. Bảng này là dữ liệu trích từ nguồn công khai. Số người trả lời khảo sát được tính riêng từ bản xuất form sau khi đối chiếu nguồn và điều kiện sàng lọc.

## Kết luận cho C3

Mẫu review cho thấy khó khăn khi tìm phương án thay thế sau hủy chuyến. Các ví dụ ngoài mẫu cho thấy tình huống hết vé hoặc bị tách sang chuyến khác đã xảy ra. Mẫu gồm một trang review của một hãng quốc tế và có thiên lệch tự chọn, nên chưa ước tính được tần suất pain trong các gia đình đi máy bay tại Việt Nam. Có thể dùng ca nhóm hết vé để minh họa tác động và hỏi thêm gia đình từng bị hủy chuyến về thời gian tìm được chuyến mới, số lần liên hệ hỗ trợ và chi phí phát sinh.
