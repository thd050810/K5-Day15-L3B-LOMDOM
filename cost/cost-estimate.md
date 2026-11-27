# Chi phí khi dùng thật

> Điền ở guide bước 4.2, nộp ở CP4 14:30 Thứ Bảy 28/11. Ôn lại: ngày 13, ngày 1, ngày 14 · lab ngày 13, lab ngày 14. Chấm ở rubric R6.
> Số **không điền tay**: điền `cost/personas.yaml` → `python run.py simulate` → chép bảng trong `cost/simulate-N-summary.md` vào đây.
> Lúc build dùng gói miễn phí vẫn tính theo **giá gói trả phí** — đây là chi phí cho lúc đưa vào dùng thật.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`): 3 kiểu người dùng:
  - `khach_doi_nhanh` (50% · 1 phiên/tháng · 1 lượt/phiên · câu `thuong`)
  - `khach_hoi_nhieu_luot` (35% · 1 phiên/tháng · 3 lượt/phiên · câu `thuong`, `kho`)
  - `khach_ca_kho` (15% · 2 phiên/tháng · 4 lượt/phiên · câu `kho`, `tu_choi`)
  - Nguồn: *(tự ước tính)* theo kịch bản `spec.md` §2, 4 lớp chỗ khó `spec.md` §5 và ca huỷ nối tiếp (`evidence/summary.md` Review #8).
- **Số người dùng thật** 3 kịch bản: thấp **500** · cơ sở **2.000** · cao **5.000** người/tháng. Nguồn: Cục Hàng không Việt Nam ([caa.gov.vn](https://caa.gov.vn), xem 28/11/2026: 10 tháng 2026 hãng nội địa vận chuyển 33,8 triệu lượt khách, ~3,38 triệu lượt/tháng) và tỷ lệ huỷ chuyến nội địa toàn ngành ~0,7% (báo cáo Cục Hàng không VN qua [nhandan.vn](https://nhandan.vn)) tương đương ~23.660 lượt khách gặp huỷ chuyến/tháng; 3 mức 500 / 2.000 / 5.000 người đặt vé gia đình/tháng là *(tự ước tính)* theo quy mô triển khai trên một kênh app/hãng.
- **Giá** 3 mức model ([openai.com/api/pricing](https://openai.com/api/pricing/), xem 28/11/2026; tỷ giá 1 USD = 26.020 ₫ theo [Vietcombank](https://www.vietcombank.com.vn), xem 28/11/2026):
  - `gpt-6-luna`: vào **$0.10** · ra **$0.50** / 1M token
  - `gpt-6.1-terra`: vào **$1.00** · ra **$5.00** / 1M token
  - `gpt-6.2-sol`: vào **$2.00** · ra **$10.00** / 1M token
- **Tỉ lệ đạt** dùng để tính: **25/26 (96%)** — lượt `run-1@20261127-224214` (lượt 1, chạy cùng model `gpt-6-luna`; khi nhóm chạy và chấm xong lượt 2 `eval/run-2.csv` thì chạy lại `python run.py simulate --rate-from eval/run-2.csv` để cập nhật).
- Đo token trên model **`gpt-6-luna`**, tính giá model **`gpt-6-luna`**, **`gpt-6.1-terra`** và **`gpt-6.2-sol`** *(lưu ý: khác họ/bộ tách token thì số token thật có thể lệch)*.

## 2. Kết quả mô phỏng

Lượt mô phỏng: `cost/simulate-1.csv` · run ID `simulate-1@20261128-014342` · **50 phiên** · seed **42** · phiên lỗi **0/50**.

*(chép từ `cost/simulate-1-summary.md`)*

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| khach_doi_nhanh | 28 | 1 | 1882 | 208 | 1.0 | 2.0 |
| khach_hoi_nhieu_luot | 15 | 3 | 5392 | 859 | 3.0 | 5.3 |
| khach_ca_kho | 7 | 4 | 7179 | 1063 | 4.0 | 6.9 |

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (500 người) | Chi phí / tháng — cơ sở (2.000 người) | Chi phí / tháng — cao (5.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-6-luna (vào 0.1 · ra 0.5 $/1M) | $0.00063 (≈ 16 ₫) | $0.00065 (≈ 17 ₫) | $0.00032 (≈ 8 ₫) | $0.4300 (≈ 11.189 ₫) | $1.72 (≈ 44.754 ₫) | $4.30 (≈ 111.886 ₫) | $0.00086 (≈ 22 ₫) |
| gpt-6.1-terra (vào 1.0 · ra 5.0 $/1M) | $0.0063 (≈ 164 ₫) | $0.0065 (≈ 170 ₫) | $0.0032 (≈ 84 ₫) | $4.30 (≈ 111.886 ₫) | $17.20 (≈ 447.544 ₫) | $43.00 (≈ 1.118.861 ₫) | $0.0086 (≈ 224 ₫) |
| gpt-6.2-sol (vào 2.0 · ra 10.0 $/1M) | $0.0126 (≈ 327 ₫) | $0.0131 (≈ 341 ₫) | $0.0065 (≈ 169 ₫) | $8.60 (≈ 223.772 ₫) | $34.40 (≈ 895.089 ₫) | $86.00 (≈ 2.237.722 ₫) | $0.0172 (≈ 448 ₫) |

Chi phí / task thành công = chi phí trung bình mỗi phiên ÷ tỉ lệ đạt (25/26 = 96%) — **không coi như đạt 100%**.

## 3. So với impact

- Impact / người / tháng (`spec.md` §2): **15–30 phút tìm và đối chiếu chuyến / người / tháng** *(tự ước tính; 1 lần/tháng trong kịch bản thử 10 gia đình = 150–300 phút/tháng)*. Ngoài mẫu, ca hết vé làm kéo dài hành trình và phát sinh chi phí phụ trội (ví dụ >2,5 triệu đồng cho đoàn 10 người ở `evidence/summary.md`).
- Chi phí / người / tháng (cơ sở, model `gpt-6-luna`): **$0.00086 (≈ 22 ₫)** (hoặc $0.0086 ≈ 224 ₫ với `gpt-6.1-terra`; $0.0172 ≈ 448 ₫ với `gpt-6.2-sol`).
- **Kết luận một dòng — đáng làm không:** **Đáng làm về chi phí AI** — chỉ tốn khoảng **22 ₫/người/tháng** (1,72 USD ≈ 44.754 ₫/tháng cho 2.000 người dùng cơ sở trên `gpt-6-luna`) để giảm 15–30 phút tìm chuyến và tránh rủi ro tách gia đình/chọn nhầm chuyến; tuy nhiên cần đo lại tần suất thật của nhóm mục tiêu và cộng thêm chi phí tích hợp API tồn chỗ/lịch bay thật trước khi triển khai chính thức.

## 4. *(Muốn sâu hơn, không bắt buộc)*

- Bảng độ nhạy: model rẻ hơn · cache · cắt ngữ cảnh · giới hạn bước — mỗi cần gạt đổi chi phí bao nhiêu
- Chi phí ngoài model: hosting, lưu trữ, giờ công người duyệt
- Quy mô nào thì bài toán còn đáng làm
