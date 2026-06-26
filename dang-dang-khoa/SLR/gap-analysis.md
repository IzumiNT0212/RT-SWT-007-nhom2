# GAP Analysis – Automated Java Unit Test Generation using LLMs
Evidence table: N = 10 papers | Ngày: 2026-06-11

## Bảng GAP

| Cột | Phát hiện | Loại GAP | Phản chứng |
| :--- | :--- | :--- | :--- |
| **Metric** | Các nghiên cứu (Kang 2022, 2023; Plein 2023) chỉ đo Code Coverage/Compilation Rate; chưa đánh giá độ tương đồng ngữ nghĩa (Semantic Similarity). | **GAP-M** | :white_check_mark: Kiểm tra 10 paper: Không paper nào dùng Semantic Similarity. |
| **Dataset** | Các thực nghiệm trước đây dùng benchmark đóng (Defects4J); chưa thử nghiệm trên mã nguồn hệ thống quản lý nghiệp vụ thực tế. | **GAP-D** | :white_check_mark: Kiểm tra 10 paper: Không có dự án enterprise thực tế nào được sử dụng. |

## GAP Chính: GAP-M 
Các nghiên cứu hiện tại chưa đo lường khía cạnh **Semantic Similarity** giữa Unit Test Java do LLM tự động sinh ra và Unit Test do lập trình viên chuyên gia viết thủ công.

## GAP Secondary: GAP-D
Thiếu đánh giá thực nghiệm sinh Unit Test cho các hệ thống quản lý có cấu trúc nghiệp vụ thực tế.

## Chi tiết kiểm tra phản chứng
* **Kang_2022_FewShot_Testers & Kang_2023_Diverse_LLMs:** Chỉ đánh giá Line Coverage trên Defects4J. (:white_check_mark: Xác nhận GAP-M, GAP-D)
* **Plein_2023_Test_Cases:** Xoay quanh executable metrics. (:white_check_mark: Xác nhận GAP-M)
* **Zhang_2024_Critical_Review & Siddiq_2025_Reproducibility:** Xác nhận đo lường coverage đang là tiêu chuẩn thống trị. (:white_check_mark: Củng cố GAP)
* **Các paper còn lại:** Tập trung domain khác (Android Replay, Bug Gen). (:white_check_mark: Không vi phạm)

## Feasibility Check – GAP Chính (GAP-M)

| Tiêu chí | Mức | Ghi chú |
| :--- | :---: | :--- |
| **Dataset** | :white_check_mark: | Đã có mã nguồn Hospital Management System và Unit Test đối chứng. |
| **Tool/API** | :white_check_mark: | Dùng Gemini API và thư viện Sentence-Transformers. |
| **Compute** | :white_check_mark: | Google Colab bản free đủ chạy Python script. |
| **Ground truth**| :white_check_mark: | Bộ Test chuyên gia đã có sẵn. |
| **Skills** | :white_check_mark: | Nhóm có thể viết script tính similarity trong < 1 tuần. |
| **Thời gian** | :white_check_mark: | Có buffer > 1 tuần. |
| **Contribution**| :white_check_mark: | Cung cấp baseline đánh giá ngữ nghĩa đầu tiên. |

**Kết quả:** :white_check_mark: **An toàn** $\rightarrow$ Chọn GAP-M.