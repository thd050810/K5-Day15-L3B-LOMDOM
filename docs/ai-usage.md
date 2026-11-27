# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | Antigravity (AI assistant) | Viết nháp `codebase/tools.py` (`tra_dat_cho`, `tra_chuyen_thay_the`) và `codebase/agent.py` (`answer`, trích xuất ràng buộc, kiểm tra an toàn) | Trần Phạm Minh Sơn, Nguyễn Quang Huy kiểm tra chạy thử `python run.py` | Trần Phạm Minh Sơn, Nguyễn Quang Huy |
| Prompt / thiết kế lời gọi mô hình | Antigravity (AI assistant) | Soạn nháp `SYSTEM` prompt và hoàn thiện sơ đồ/bảng công cụ ở `spec.md` §4, §6 khớp với `codebase/` | Nguyễn Quang Huy, Trần Phạm Minh Sơn rà khớp `metric_spec.yaml` | Nguyễn Quang Huy, Trần Phạm Minh Sơn |
| Đào data (viết script đếm, gợi ý nhãn) | | | Kiểm tay __ dòng, khớp __ | |
| Rà câu hỏi phỏng vấn / khảo sát | | Chỉ rà câu dẫn dắt | | |
| Viết câu thử (benchmark) | | | Mỗi câu thử có `source`; câu thử AI viết được ghi rõ | |
| Sinh data `synthetic` (nếu có) | | | Seed __ · kiểm tay __ dòng | |
| Chấm cột `pass` bằng LLM (nếu có) | Claude Code | Chấm nháp 26 câu lượt 1 theo `pass_criterion` + 4 metric, ghi lý do ở `ghi_chu` | Chờ Lê Anh Tuấn kiểm tay ≥ 5 câu (gồm B09 trượt), khớp __/__ | Lê Anh Tuấn |
| Slide, văn bản | Claude Code | Soạn nháp CP1: canvas, giả thuyết, bài toán, lát cắt | ____ | ____ |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
