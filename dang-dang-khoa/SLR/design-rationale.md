# Experiment Design Rationale – Automated Java Unit Test Generation
Ngày: 2026-06-11 | GAP source: SLR/gap-analysis.md

## Bảng Quyết Định

| Quyết định | Giá trị | Nguồn gốc |
| :--- | :--- | :--- |
| LLM/Tool | Gemini 1.5 Pro (Zero-shot) | GAP-T: Thử nghiệm mô hình thế hệ mới |
| Dataset | 30 Java classes từ Hospital Management System | GAP-D: Tập dữ liệu hệ thống quản lý |
| Metric chính | Cosine Similarity (`sentence-transformers/all-MiniLM-L6-v2`) | GAP-M: Cột Metric |
| Metric phụ | Compilation Rate (%) | Kế thừa từ Kang_2022 |
| Baseline type | Absolute threshold | Claim type của RQ1 |
| Threshold RQ1 | 0.75 | Case 3: Chạy mini-pilot 5 samples |
| Pipeline base | Kang_2022 | Quy trình test generation |

## Lý giải threshold
**Threshold 0.75 – Case 3 – Mini-pilot.** Lý luận: Semantic Similarity là metric mới (chưa có trong 10 paper). Nhóm chạy mini-pilot trên 5 hàm Java nghiệp vụ. Kết quả Cosine Similarity thấp nhất là 0.75. Nhóm lấy giá trị sàn (floor) này làm ngưỡng đạt.