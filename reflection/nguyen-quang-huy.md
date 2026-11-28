# Reflection — Nguyễn Quang Huy

> Làm ở guide bước 5.3. Hạn: **23:59 Thứ Bảy 28/11**. Mỗi câu 3–6 dòng.

1. **Vai trò + phần mình làm (trỏ tới file / commit):**
   Thành viên, phụ trách thiết kế giải pháp, bản chạy thử và nối model (`spec.md` §4, §6; `codebase/tools.py`, `codebase/agent.py`, `codebase/ai.py`) và chạy đánh giá lượt 2.
   - CP2 (`045418c`, PR #8; `a8366d1`): xây dựng 2 công cụ chỉ đọc `tra_dat_cho` và `tra_chuyen_thay_the` đọc `data/flights.json`, dựng workflow cố định 4 bước trong `codebase/agent.py`, vẽ sơ đồ và viết thiết kế ở `spec.md` §4, §6; viết sẵn kết nối API trong `codebase/ai.py`
   - CP3 (`d2d5fe1`): nâng cấp `codebase/agent.py` xử lý thêm các ca B19–B26 (ràng buộc giờ cất cánh/giờ đến, cờ hoàn vé/đổi nhầm/hỏi phí, che số thẻ/OTP ở cả đầu vào `_redact_sensitive` lẫn đầu ra `_safe_model_output`).
   - CP4 (`e8b087c`, `4437428`, `b0f8f69`, `7cd864b`, `6f98306`): cải tiến `SYSTEM` prompt trong `codebase/agent.py` cho lượt 2, chạy thật `eval/run-2.csv` + `traces/run-2.jsonl` (`run-2@20261128-095947`, `gpt-6-luna`, đạt `26/26 = 100%`), cập nhật `spec.md` §7, `eval/report.md`, `eval/README.md` và `README.md`.

2. **AI hỗ trợ mình thế nào (việc gì, công cụ gì, chỗ nào phải sửa lại output AI):**
   Dùng Antigravity để viết nháp `codebase/tools.py`, `codebase/agent.py`, `codebase/ai.py` và rà lỗi logic trên 26 câu thử.
   Những chỗ mình phải tự kiểm và chỉnh lại từ output của AI:
   - Rà sửa logic trích xuất ràng buộc thời gian trong `codebase/agent.py` để tránh bắt nhầm mốc *"đừng cất cánh trước 7h sáng"* vào giờ đến tối đa (`B24`), và bọc thêm lớp che số thẻ/OTP ở đầu ra model (`_safe_model_output`) cho câu tấn công `B16`.

3. **Một câu thử trượt của nhóm và mình học được gì từ nó:**
   Ở lượt 1 (`run-1@20261127-224214`, 25/26 = 96%), câu trượt duy nhất là **B09**: khách (`TRV-7Q2K`) cần đến Sài Gòn trước 08:00 nhưng không có chuyến nào vừa kịp giờ vừa đủ 3 ghế. Công cụ `tra_chuyen_thay_the` đã xếp đúng `BM105` (đến 11:40, 5 ghế) vào mảng `den_muon_hoac_khac_gio` còn `hop_le` rỗng, nhưng `SYSTEM` prompt lúc đó chỉ dặn gợi ý chuyến trong `hop_le` nên model chỉ báo không có chuyến rồi đẩy khách sang nhân viên, bỏ sót `BM105`.
   Bài học mình rút ra: trong kiến trúc workflow gọi công cụ, **dữ liệu công cụ trả đầy đủ chưa chắc model sẽ dùng đúng nếu thiếu luật xử lý nhánh dự phòng (fallback) rõ ràng**. Sau khi bổ sung Quy tắc `2b` (xử lý khi `hop_le` rỗng), đồng thời siết Quy tắc `1` (không tự suy diễn mốc giờ như ở `B10`) và Quy tắc `6` (kèm câu tóm tắt khi chuyển nhân viên ở `B14`, `B19`), lượt 2 đạt `26/26 (100%)` với 0 câu tệ đi.
