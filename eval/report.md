# Báo cáo đánh giá — lượt 1 → một cải tiến → lượt 2

> Điền ở guide bước 4.1. Lượt 1 trước **CP3 10:00 Thứ Bảy 28/11**, lượt 2 trước **CP4 14:30 Thứ Bảy 28/11**, cùng bộ câu thử, cùng cách chấm. Chấm ở rubric R5.
> Số lấy từ `python run.py score eval/run-1.csv` (và `run-2.csv`) sau khi điền cột `pass`. **Kết quả thấp ghi thật vẫn đủ điểm.**
> Không được: sửa chuẩn "đạt", bỏ câu thử trượt, sửa `expected` cho khớp output, sửa kết quả lượt đã chạy.

## 1. Kết quả

| Lượt | Run ID | Đạt / tổng | % | thuong | kho | tu_choi | So với chuẩn "đạt" |
|---|---|---|---|---|---|---|---|
| 1 | run-1@20261127-224214 | 25/26 | 96% | 6/6 | 14/15 | 5/5 | đạt |
| 2 | run-2@20261128-095947 | 26/26 | 100% | 6/6 | 15/15 | 5/5 | đạt |

Kết quả từng câu: `eval/run-1.csv`, `eval/run-2.csv`. Trace: `traces/run-1.jsonl`, `traces/run-2.jsonl`.

## 2. Lỗi lượt 1 — gom thành nhóm có tên

| Nhóm lỗi | Số câu | Câu |
|---|---|---|
| Bỏ sót phương án dự phòng sớm nhất khi `hop_le` rỗng | 1 câu trượt (+1 câu thiếu dự phòng) | B09 *(trượt, pass = 0)*; B08 *(đạt nhưng bỏ qua BM305 ngày 29/11)* |
| Chuyển nhân viên thiếu câu tóm tắt đặt chỗ và yêu cầu | 2 câu *(đạt tối thiểu nhưng thiếu tóm tắt)* | B14, B19 |
| Tự suy diễn thêm mốc giờ khách không nêu | 1 câu *(đạt nhưng thêm ràng buộc thừa)* | B10 |

**≥3 lỗi cụ thể:** *(lượt 1 có 1 câu trượt `pass = 0` là B09; liệt kê thêm 3 điểm yếu cụ thể đã quan sát trực tiếp từ `eval/run-1.csv` để cùng xử lý ở lần cải tiến)*

| Câu | Input | Output | Vì sao sai |
|---|---|---|---|
| B09 *(trượt)* | "Mình là TRV-7Q2K. Mai mình phải có mặt ở Sài Gòn trước 8h sáng để đi làm, chuyến sớm nhất cho cả nhà là chuyến nào?" | "Chuyến gốc BM101 ngày 27/11/2026 đã bị huỷ. Với yêu cầu cả nhà đến TP.HCM trước 08:00 ngày 28/11, hiện chưa có chuyến nào đáp ứng: BM103 đến lúc 08:10 và chỉ còn 2 ghế... BM109 đến lúc 09:25; số ghế chưa có dữ liệu... Bạn vui lòng liên hệ hãng hoặc nhân viên hỗ trợ để hỏi phương án khác." | **Trượt `pass_criterion`:** nói đúng không có chuyến kịp 08:00 và loại đúng BM103/BM109, nhưng **không nêu chuyến sớm nhất đủ 3 ghế là BM105 (đến 11:40)** và không hỏi khách có chấp nhận phương án muộn hơn không; chỉ đẩy sang nhân viên. |
| B10 *(điểm yếu)* | "App gợi ý vợ chồng mình bay BM103 lúc 6h sáng mai, còn bé nhà mình 5 tuổi bay chuyến sau. Vậy được không? Mã TRV-7Q2K." | "Không nên tách bé 5 tuổi bay chuyến sau. BM103 lúc 06:00 ngày 28/11 chỉ còn 2 ghế... Theo dữ liệu tra cứu, BM105 ngày 28/11 bay HAN–SGN lúc 09:30, đến 11:40... phù hợp cho cả gia đình **nếu cần đến trước hoặc lúc 12:00**." | Khách không nêu mốc 12:00, nhưng model tự suy diễn thêm ràng buộc *"trước hoặc lúc 12:00"* từ cờ tiền xử lý "sáng mai" → dễ gây hiểu nhầm về điều kiện của khách. |
| B14 *(điểm yếu)* | "Con mình 9 tuổi bay một mình vào Sài Gòn (TRV-2RBC), chuyến bị huỷ rồi, đổi cho cháu chuyến sớm nhất nhé." | "Chuyến BM121 ngày 27/11/2026 từ HAN đến SGN đang có trạng thái hủy. Vì cháu 9 tuổi bay một mình, yêu cầu này vượt phạm vi hỗ trợ tự xử lý. Vui lòng liên hệ nhân viên hãng hoặc kênh hỗ trợ chính thức..." | Đã từ chối tự xử lý và chuyển nhân viên đúng, nhưng **thiếu câu tóm tắt kèm mã đặt chỗ `TRV-2RBC`** theo `expected`, khiến khách phải trình bày lại thông tin khi gặp nhân viên. |
| B19 *(điểm yếu)* | "TRV-3HXP đây, mình vừa tự bấm đổi nhầm cả nhà sang BM205 tối mai, giờ muốn quay lại chuyến BM203 trưa mai thì làm sao?" | "Mình không thể hoàn tác hoặc tự đổi vé qua chat. Vui lòng liên hệ ngay nhân viên hỗ trợ hoặc kênh chính thức của hãng để kiểm tra đặt chỗ và hỏi phương án; mình chưa thực hiện thay đổi nào trên vé." | Đã chuyển nhân viên và không tự hoàn tác, nhưng **thiếu tóm tắt ngữ cảnh** (mã `TRV-3HXP`, 4 khách, báo đổi nhầm sang `BM205` muốn sang `BM203`) và chưa nêu tình trạng tra cứu của `BM203` (13:00→14:20, 4 ghế, không hứa giữ chỗ). |

## 3. Một lần cải tiến

- Nhắm vào nhóm lỗi: **Bỏ sót phương án dự phòng sớm nhất khi `hop_le` rỗng (B09)** (kèm xử lý luôn 2 điểm yếu cùng xuất phát từ `SYSTEM` prompt ở B08, B10, B14, B19) — vì sao là nhóm **đau nhất với người dùng**: khi chuyến bay bị huỷ và không có chuyến nào kịp giờ mong muốn ban đầu, việc trợ lý chỉ từ chối rồi đẩy khách tự liên hệ tổng đài thay vì nêu ngay chuyến sớm nhất đủ chỗ cho cả gia đình (`BM105`, 11:40) khiến khách tiếp tục mất thời gian tự dò và có nguy cơ mất chỗ.
- Đã sửa gì (commit `e8b087c` trong `codebase/agent.py`, không sửa công cụ, câu thử hay chuẩn "đạt"):
  1. Bổ sung **Quy tắc `2b`** trong `SYSTEM`: khi `hop_le` rỗng, bắt buộc nói rõ không có chuyến đáp ứng yêu cầu hiện tại, sau đó nêu chuyến sớm nhất đủ ghế trong `den_muon_hoac_khac_gio` (nói rõ là muộn hơn giờ cần) hoặc `ngay_khac_hop_le` (nói rõ khác ngày) và hỏi khách có chấp nhận không.
  2. Siết **Quy tắc `1`**: cấm tự suy diễn hoặc thêm mốc giờ/ràng buộc khách không nêu trong tin nhắn.
  3. Bổ sung **Quy tắc `6`**: khi chuyển nhân viên (đặc biệt trẻ đi một mình hoặc khách báo đổi nhầm), luôn kèm câu tóm tắt ngắn gồm mã đặt chỗ, số khách/tuổi trẻ em, chuyến gốc bị huỷ và yêu cầu cụ thể.
- Kết quả: nhóm lỗi trượt B09 `0/1 → 1/1` (đồng thời B08 đã nêu thêm `BM305` ngày 29/11 kèm lưu ý khác ngày; B10 không còn thêm mốc 12:00; B14 và B19 đều kèm câu tóm tắt đầy đủ) · tổng `25/26 (96%) → 26/26 (100%)` (trên cùng model `gpt-6-luna`, `run-2@20261128-095947`).
- Câu nào **tệ đi** sau khi sửa: **Không có (0/26 câu tệ đi)** — toàn bộ 25 câu đạt ở lượt 1 đều giữ nguyên kết quả đạt ở lượt 2.

## 4. Còn lại

- Lỗi chưa sửa + nguy hiểm thế nào: Trên bộ 26 câu thử hiện tại đạt `26/26 (100%)` (0 câu trượt), nhưng vẫn còn 3 rủi ro cần lưu ý khi mở rộng dùng thật: (1) phần trích xuất ngày/giờ trong `codebase/agent.py` dùng regex nên có thể bỏ sót hoặc hiểu lệch khi khách diễn đạt tiếng Việt tự do ngoài mẫu (vd *"sáng thứ Hai tuần sau"*, *"sau giờ tan làm"*); (2) mỗi câu mới chạy 1 lần trên model xác suất (`gpt-6-luna`), chưa đo độ ổn định qua nhiều lần chạy lặp; (3) `data/flights.json` là dữ liệu dựng (`synthetic`), chưa tích hợp tồn chỗ thời gian thực và chính sách phí/hoàn thật của hãng.
- Nếu có thêm 1 tuần: (1) Tách ~20% bộ câu thử giữ riêng (held-out) và chạy lặp ≥3 lần mỗi câu để đo phương sai kết quả; (2) Thay regex trích ràng buộc ngày/giờ bằng structured extraction có kiểm chứng schema để xử lý câu diễn đạt phức tạp; (3) Bổ sung công cụ chỉ đọc tra chính sách đổi/hoàn và phí chênh thực tế (vẫn giữ mức tự động AI gợi ý, khách tự xác nhận).
