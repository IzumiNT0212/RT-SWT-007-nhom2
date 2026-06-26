# GAP Analysis – Bug Report Quality Assessment with LLM

Evidence table: N = 13 papers | Ngày: 08/06/2026

## Bảng GAP

| Cột nguồn | Phát hiện | Loại GAP | Phản chứng                                                                                            
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Tool/LLM  | Các nghiên cứu hiện tại chủ yếu sử dụng LLM cho bug report generation, issue classification, duplicate bug detection, issue resolution và root cause analysis; rất ít nghiên cứu sử dụng LLM để đánh giá trực tiếp chất lượng và khả năng tái hiện lỗi (reproducibility) của bug reports. | GAP-T | Đã kiểm tra 13 papers, không tìm thấy nghiên cứu tập trung vào bug report reproducibility assessment.

| Dataset   | Phần lớn nghiên cứu được đánh giá trên Bugzilla, Mozilla hoặc SWE-bench; thiếu đánh giá trên GitHub Issues và Jira. | GAP-D | Một số paper sử dụng GitHub/SWE-bench nhưng chưa tập trung vào reproducibility assessment.

| Metric    | Các metric phổ biến gồm F1-score, Precision, Recall, ROUGE, SBERT, CTQRS, MAP và MRR; chưa có metric phổ biến để đánh giá trực tiếp khả năng tái hiện lỗi của bug report. | GAP-M | Không tìm thấy paper nào sử dụng Reproducibility Score hoặc Bug Report Reproducibility Metric.

| Hạn chế   | Nhiều nghiên cứu thừa nhận khả năng tổng quát hóa sang các hệ sinh thái khác (GitHub, Jira, industrial projects) còn hạn chế. | GAP-S | Xuất hiện trong ít nhất 6/13 papers.                                                                  |

## GAP Chính [GAP-T]

Mặc dù các nghiên cứu gần đây đã sử dụng Large Language Models (LLMs) cho sinh báo cáo lỗi, phân loại lỗi, phát hiện lỗi trùng lặp, phân tích nguyên nhân gốc và giải quyết issue, rất ít nghiên cứu sử dụng LLM để đánh giá trực tiếp chất lượng và khả năng tái hiện lỗi (reproducibility) của bug reports. Khoảng trống này làm hạn chế khả năng ứng dụng LLM như một công cụ hỗ trợ kiểm tra chất lượng báo cáo lỗi trước khi được chuyển tới nhóm phát triển.

## GAP Secondary [GAP-D]

Các nghiên cứu hiện tại chủ yếu được đánh giá trên Bugzilla hoặc Mozilla datasets và thiếu bằng chứng về khả năng tổng quát hóa sang GitHub Issues hoặc Jira, vốn là những nền tảng quản lý lỗi phổ biến trong thực tế.

## Chi tiết kiểm tra phản chứng cho GAP Primary

| Paper | Đã nghiên cứu Bug Report Reproducibility Assessment? | Ghi chú                         |
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| ID 1  | Không                                                | Priority Detection

| ID 6  | Không                                                | Bug Report Generation

| ID 14 | Không                                                | Bug Management & Generation

| ID 15 | Không                                                | Bug Classification

| ID 16 | Không                                                | Issue Classification
            
| ID 21 | Không                                                | Automated Bug Report Generation

| ID 27 | Không                                                | Duplicate Bug Detection

| ID 31 | Không                                                | Issue Resolution

| ID 36 | Không                                                | Conceptual Framework

| ID 45 | Không                                                | Survey & Vision Paper

| ID 49 | Không                                                | Guided Defect Report Form

| ID 51 | Không                                                | Bug Report Summarization

| ID 55 | Không                                                | Root Cause Analysis

Kết luận: Không tìm thấy nghiên cứu nào tập trung trực tiếp vào việc đánh giá khả năng tái hiện lỗi (reproducibility) của bug reports bằng LLM.

## Feasibility Check – GAP Chính

| Tiêu chí     | Mức  | Ghi chú
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Dataset      | ✅   | Có thể sử dụng Bugzilla hoặc GitHub Issues công khai

| Tool/API     | ✅   | Có thể sử dụng GPT-4o Mini hoặc các LLM mã nguồn mở

| Compute      | ✅   | Không yêu cầu fine-tuning quy mô lớn

| Ground Truth | ⚠️   | Cần xây dựng hoặc gán nhãn reproducibility

| Skills       | ✅   | Nhóm có nền tảng Software Engineering

| Thời gian    | ✅   | Phù hợp với phạm vi môn học

| Contribution | ✅   | Đóng góp mới so với evidence table hiện tại

**Kết quả:** ⚠️ = 1, ❌ = 0 → GAP khả thi và được chọn làm GAP chính.

## Quyết định cuối cùng

| 	Mục      | Nội dung |
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Primary GAP    | GAP-T (Technology Gap)                                                                                                                                                                                          

| Secondary GAP  | GAP-D (Dataset Gap)                                                                                                                                                                                             

| Lý do lựa chọn | GAP-T có mức ưu tiên cao nhất theo hướng dẫn (GAP-T > GAP-M > GAP-D > GAP-S), đồng thời có tính khả thi cao và phù hợp với mục tiêu nghiên cứu về chất lượng và khả năng tái hiện lỗi của bug reports bằng LLM.