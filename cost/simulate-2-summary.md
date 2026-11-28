# Tóm tắt mô phỏng simulate-2@20261128-125133

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| khach_doi_nhanh | 28 | 1 | 1882 | 223 | 1.0 | 2.0 |
| khach_hoi_nhieu_luot | 15 | 3 | 5392 | 858 | 3.0 | 5.3 |
| khach_ca_kho | 7 | 4 | 7179 | 1062 | 4.0 | 6.9 |

Tỉ lệ đạt dùng để tính: 26/26 (100%) — lượt run-2@20261128-095947

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-2.csv (--rate-from).

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (500 người) | Chi phí / tháng — cơ sở (2.000 người) | Chi phí / tháng — cao (5.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-6-luna (vào 0.1 · ra 0.5 $/1M) | $0.00063 (≈ 16 ₫) | $0.00063 (≈ 16 ₫) | $0.00031 (≈ 8 ₫) | $0.4317 (≈ 11.234 ₫) | $1.73 (≈ 44.934 ₫) | $4.32 (≈ 112.336 ₫) | $0.00086 (≈ 22 ₫) |
| gpt-6.1-terra (vào 1.0 · ra 5.0 $/1M) | $0.0063 (≈ 165 ₫) | $0.0063 (≈ 165 ₫) | $0.0031 (≈ 82 ₫) | $4.32 (≈ 112.336 ₫) | $17.27 (≈ 449.345 ₫) | $43.17 (≈ 1.123.362 ₫) | $0.0086 (≈ 225 ₫) |
| gpt-6.2-sol (vào 2.0 · ra 10.0 $/1M) | $0.0127 (≈ 330 ₫) | $0.0127 (≈ 330 ₫) | $0.0063 (≈ 163 ₫) | $8.63 (≈ 224.672 ₫) | $34.54 (≈ 898.689 ₫) | $86.35 (≈ 2.246.723 ₫) | $0.0173 (≈ 449 ₫) |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (2.0) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: gpt-6-luna. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.
- Tỷ giá: 1 USD = 26.020 ₫ (https://www.vietcombank.com.vn (tỷ giá bán ra USD/VND cuối tháng 11/2026 · xem 28/11/2026)).
