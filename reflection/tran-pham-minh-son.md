# Reflection — Trần Phạm Minh Sơn

> Làm ở guide bước 5.3. Hạn: **23:59 Thứ Bảy 28/11**. Mỗi câu 3–6 dòng.

1. **Vai trò + phần mình làm (trỏ tới file / commit):**
   Thành viên, cặp với Huy dựng bản chạy thử ở CP2 và phụ trách mô phỏng chi phí, dàn ý slide, video demo ở CP3–CP4 (`cost/`, `spec.md` §8, `slides/outline.md`, video demo 30s).
   - CP2 (`045418c`, PR #8): dựng công cụ tra cứu dữ liệu giả (`codebase/tools.py`), luồng chính `codebase/agent.py` và hoàn thiện thiết kế `spec.md` §4, §6 cùng Huy.
   - CP3–CP4 (`a6b06b2`, PR #22): chạy kiểm tra `eval --try`, `simulate --try` (10 phiên) và mô phỏng 50 phiên trên `gpt-6-luna` (`cost/simulate-1.csv`, `cost/simulate-1-summary.md`, `traces/simulate-1.jsonl`, 0/50 lỗi); hoàn thiện `cost/personas.yaml`, `cost/cost-estimate.md` §1–§3, `spec.md` §8 & §10, dàn ý `slides/outline.md`; quay video demo 30s gắn vào `README.md`; chấm độc lập 5 câu lượt 1 (`B01, B05, B08, B09, B17`) trong `eval/README.md` mục 3 (khớp 5/5 với Tuấn ở `dff1f13`).

2. **AI hỗ trợ mình thế nào (việc gì, công cụ gì, chỗ nào phải sửa lại output AI):**
   Dùng Antigravity để soạn nháp `codebase/tools.py`, `codebase/agent.py`, `spec.md` §4/§6, cấu hình `cost/personas.yaml`, `cost/cost-estimate.md`, dàn ý `slides/outline.md` và bảng đối chiếu 5 câu chấm chéo lượt 1. Những chỗ mình kiểm và sửa lại:
   - Kiểm lại nguồn công khai (Cục Hàng không VN) cho quy mô người dùng trong `cost/personas.yaml` và yêu cầu gắn rõ *(tự ước tính)* cho mọi số persona/kịch bản chưa có dữ liệu đo trực tiếp.
   - Sửa lỗi ký hiệu tiền tệ AI viết nháp kiểu LaTeX (`\$`) trong `slides/outline.md` thành `$` để hiển thị đúng trên GitHub; giữ nguyên tắc không điền thay phần chấm chéo của Tuấn mà chờ Tuấn tự đối chiếu.
   - Đối chiếu lại toàn bộ số chi phí trong `cost/cost-estimate.md` và `spec.md` §8 trực tiếp với `cost/simulate-1-summary.md` do `python run.py simulate` sinh ra, đồng thời tự chạy `python run.py` để quay video demo 30s (đóng `.env` tránh lộ key).

3. **Một câu thử trượt của nhóm và mình học được gì từ nó:**
   `B09` (`TRV-7Q2K` cần đến Sài Gòn trước 08:00 nhưng không chuyến nào kịp và đủ 3 ghế): ở lượt 1 (`run-1@20261127-224214`), trợ lý nói đúng không có chuyến kịp và loại `BM103` (2 ghế), `BM109` (`con_ghe = null`), nhưng bỏ sót không nêu chuyến sớm nhất đủ chỗ `BM105` (đến 11:40) để hỏi khách có chấp nhận muộn hơn không. Sau khi nhóm thêm quy tắc chung `2b` trong `SYSTEM` prompt (`e8b087c`), lượt 2 đạt `26/26` và 0 câu tệ đi.
   Bài học từ góc nhìn chi phí & sản phẩm: một lỗi bỏ sót phương án dự phòng như B09 buộc khách phải hỏi thêm lượt hoặc gọi tổng đài, làm tăng trực tiếp số lượt và token mỗi phiên (trong `simulate-1`, nhóm `khach_ca_kho` tốn ~4 lượt và gấp gần 4 lần token so với `khach_doi_nhanh`). Ngoài ra, chi phí thật luôn phải tính theo **chi phí / task thành công** (chia cho tỉ lệ đạt) và lần sau nên chạy đồng bộ lại `simulate` ngay khi chốt tỉ lệ đạt lượt 2.
