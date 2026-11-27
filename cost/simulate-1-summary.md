# Tóm tắt mô phỏng simulate-1@20261128-014342

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| khach_doi_nhanh | 28 | 1 | 1882 | 208 | 1.0 | 2.0 |
| khach_hoi_nhieu_luot | 15 | 3 | 5392 | 859 | 3.0 | 5.3 |
| khach_ca_kho | 7 | 4 | 7179 | 1063 | 4.0 | 6.9 |

Tỉ lệ đạt dùng để tính: 25/26 (96%) — lượt run-1@20261127-224214

- Tự chọn: lượt run-N mới nhất đã chấm xong, chạy bằng đúng model đang đo (run-1.csv). Muốn dùng lượt khác (vd lượt 2): thêm `--rate-from eval/run-2.csv`.

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (500 người) | Chi phí / tháng — cơ sở (2.000 người) | Chi phí / tháng — cao (5.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-6-luna (vào 0.1 · ra 0.5 $/1M) | $0.00063 (≈ 16 ₫) | $0.00065 (≈ 17 ₫) | $0.00032 (≈ 8 ₫) | $0.4300 (≈ 11.189 ₫) | $1.72 (≈ 44.754 ₫) | $4.30 (≈ 111.886 ₫) | $0.00086 (≈ 22 ₫) |
| gpt-6.1-terra (vào 1.0 · ra 5.0 $/1M) | $0.0063 (≈ 164 ₫) | $0.0065 (≈ 170 ₫) | $0.0032 (≈ 84 ₫) | $4.30 (≈ 111.886 ₫) | $17.20 (≈ 447.544 ₫) | $43.00 (≈ 1.118.861 ₫) | $0.0086 (≈ 224 ₫) |
| gpt-6.2-sol (vào 2.0 · ra 10.0 $/1M) | $0.0126 (≈ 327 ₫) | $0.0131 (≈ 341 ₫) | $0.0065 (≈ 169 ₫) | $8.60 (≈ 223.772 ₫) | $34.40 (≈ 895.089 ₫) | $86.00 (≈ 2.237.722 ₫) | $0.0172 (≈ 448 ₫) |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (2.0) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: gpt-6-luna. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.
- Tỷ giá: 1 USD = 26.020 ₫ (https://www.vietcombank.com.vn (tỷ giá bán ra USD/VND cuối tháng 11/2026 · xem 28/11/2026)).
