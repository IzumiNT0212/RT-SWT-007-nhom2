# IE Criteria – Bug Report Quality Assessment with LLM
**Thành viên:** Nguyễn Ngọc Gia Thuận
**RQ:** Việc ứng dụng các mô hình ngôn ngữ lớn (LLM) và các chiến lược Prompting/Agent chuyên dụng vào tác vụ đánh giá và cải thiện chất lượng của các Bug/Issue Report (Bug Report Quality Assessment) có giúp nâng cao độ chính xác, tính rõ ràng, khả năng tái hiện lỗi và giảm thiểu báo động giả khi tiến hành so sánh đối chiếu với các phương pháp kiểm tra truyền thống và kết quả thẩm định từ chuyên gia con người hay không?
**PICO:** P=[Bug/Issue Reports, GitHub Issues, Jira tickets] | I=[LLMs + Prompt Engineering + Multi-Agent Systems] | C=[Traditional ML, Rule-based systems, Human Experts] | O=[F1-score, Accuracy, ROUGE, BLEU, LLM-as-a-judge score]

---

## Inclusion Criteria (IC) – paper PHẢI có đủ tất cả

| Mã | Tiêu chí |
| :--- | :--- |
| **IC-L** | Viết bằng tiếng Anh |
| **IC-Y** | Xuất bản từ năm 2018 đến nay – Lý do: Đây là giai đoạn bùng nổ của kiến trúc Transformer và các mô hình ngôn ngữ lớn (LLM) trong Kỹ thuật phần mềm. |
| **IC-T** | Đăng trên conference hoặc journal – không phải blog, thesis, hay báo cáo kỹ thuật |
| **IC-P** | Về task: Thẩm định, chấm điểm, lọc nhiễu, phân loại hoặc tự động cải thiện chất lượng nội dung của các Bug/Issue Reports, GitHub Issues, Jira tickets |
| **IC-I** | Dùng kỹ thuật: Mô hình ngôn ngữ lớn (LLM) mã nguồn đóng/mở, Prompt Engineering, hoặc hệ thống Multi-Agent |
| **IC-E** | Có ít nhất 1 con số kết quả trong Table hoặc Figure của paper gốc |

## Exclusion Criteria (EC) – loại nếu BẤT KỲ điều kiện nào đúng

| Mã | Tiêu chí |
| :--- | :--- |
| **EC-D** | Trùng lặp với paper đã có trong danh sách |
| **EC-A** | Không truy cập được full-text |
| **EC-S** | Dưới 4 trang (extended abstract, poster, short paper) |
| **EC-N** | Không có thực nghiệm (position paper, vision paper, tutorial) |
| **EC-O** | Không về topic: Tập trung vào các tác vụ bảo trì chung như tự động sửa lỗi (Program Repair), sinh Unit Test, sinh code, hoặc tối ưu hóa giao diện (UI) mà không phân tích khía cạnh chất lượng của văn bản Bug Report. |