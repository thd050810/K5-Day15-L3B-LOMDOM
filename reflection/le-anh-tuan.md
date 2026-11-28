# Reflection — Lê Anh Tuấn

> Làm ở guide bước 5.3. Hạn: **23:59 Thứ Bảy 28/11**. Mỗi câu 3–6 dòng.

1. **Vai trò + phần mình làm (trỏ tới file / commit):**
   Thành viên, phụ trách chỗ khó, bộ câu thử, metric và đánh giá (`spec.md` §5–§7, `data/`, `eval/`).
   - CP2 (`1d387ac`, PR #6): viết 18 câu thử ban đầu `eval/benchmark.csv`, 4 metric ở `eval/metric_spec.yaml`, chuẩn "đạt" ở §7 (≥ 80% kèm 4 điều kiện cứng), 10 kịch bản ở §5, dữ liệu giả `data/flights.json` và `data/DATA_CARD.md`.
   - CP3 (`bd435ce`, PR #13): thêm B19–B26 (18 → 26 câu), lấp 2 ô trống "đổi nhầm" và "đổi ý", thêm 5 câu từ khảo sát `evidence/survey/results.csv`.
   - CP4 (`dff1f13`, PR #23): kiểm tay bản chấm nháp của lượt 1 (6/6) và lượt 2 (5/5); chấm chéo với Sơn, khớp 5/5.

2. **AI hỗ trợ mình thế nào (việc gì, công cụ gì, chỗ nào phải sửa lại output AI):**
   Dùng Claude Code để soạn nháp câu thử, metric, dữ liệu giả, data card và chấm nháp cột `pass`. Các quyết định chính do mình chốt: lát cắt theo Canvas (AI chỉ gợi ý, khách tự đổi vé), ngưỡng 80%, và tự soạn dữ liệu giả thay vì chờ.
   Những chỗ phải sửa lại hoặc kiểm lại output của AI:
   - Data card ghi "đã kiểm tay cả 22 chuyến" trong khi thực tế chưa ai kiểm. Đã sửa thành "đối chiếu bằng script", vì không được ghi việc chưa làm.
   - Số chuyến bị huỷ ghi sai (7, đúng là 8).
   - Đáp án từng câu được đối chiếu bằng script với `data/flights.json`.
   - Bản chấm nháp của LLM được kiểm tay trước khi tính vào kết quả.

3. **Một câu thử trượt của nhóm và mình học được gì từ nó:**
   B09: khách cần đến Sài Gòn trước 08:00, nhưng không chuyến nào kịp mà còn đủ 3 ghế. Ở lượt 1, trợ lý nói đúng là không có chuyến kịp, nhưng bỏ sót BM105 (đến 11:40, đủ chỗ) và chỉ đẩy khách sang nhân viên. Trace cho thấy công cụ xếp BM105 vào nhóm "đến muộn" (`hop_le` rỗng), và prompt không có quy tắc cho tình huống này. Nhóm thêm quy tắc chung 2b, lượt 2 đạt 26/26.
   Điều mình học được: tiêu chí của B09 (nêu BM105) và metric cứng `chuyen_goi_y_hop_le` (không gợi ý chuyến đến muộn) gần như mâu thuẫn nhau. Khi chấm, nhóm phải thống nhất lại là "được nêu như lựa chọn muộn hơn để khách quyết". Lần sau mình sẽ viết `expected` và metric cùng lúc, rồi rà xem chúng có cãi nhau không trước khi chốt.
