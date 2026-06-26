Gap Statement – LLM-Based Bug Report Reproducibility Quality Assessment
Evidence table size: N = 13 included studies.

## Evidence observed 
- Các nghiên cứu được rà soát cho thấy LLM ngày càng được sử dụng rộng rãi cho các tác vụ kỹ nghệ phần mềm liên quan đến báo cáo lỗi. Bằng chứng bao gồm:
- Tái tạo và chạy lại báo cáo lỗi (Bug report reproduction and replay) sử dụng ChatGPT/GPT-4, chẳng hạn như tự động sinh các ca kiểm thử khả thi hoặc tái lập các báo cáo lỗi trên ứng dụng Android.
- Phát hiện báo cáo lỗi trùng lặp (Duplicate bug report detection) sử dụng ChatGPT kết hợp với các kỹ thuật thu thập thông tin (Information Retrieval).
- Phân loại và thiết lập thứ tự ưu tiên cho báo cáo lỗi hoặc phản hồi của người dùng (Bug report or user feedback classification and prioritization) sử dụng LLM và các mô hình học máy khác.
- Các bài tổng quan diện rộng (Broad surveys) chỉ ra rằng LLM rất hữu ích trong kỹ nghệ phần mềm nhưng vẫn phải đối mặt với các thách thức về độ tin cậy, hiện tượng "ảo giác" (hallucination) và phương pháp đánh giá.

## Identified gaps 
### GAP-T – Task gap 
Hầu hết các nghiên cứu hiện tại đều sử dụng báo cáo lỗi làm dữ liệu đầu vào cho các tác vụ xuôi dòng (downstream tasks) như tái lập lỗi, phát hiện trùng lặp, sắp xếp độ ưu tiên và sinh ca kiểm thử. Tuy nhiên, các nghiên cứu được rà soát không trực tiếp đánh giá liệu một mô hình LLM có thể tự thẩm định chất lượng của chính bản báo cáo lỗi đó hay không, đặc biệt là đánh giá chất lượng khả năng tái lập (reproducibility quality) của nó.

### GAP-M – Metric gap 
Các nghiên cứu hiện nay chủ yếu báo cáo các chỉ số định lượng như tỷ lệ tái hiện lỗi thành công (reproduction success rate), Recall@K, F1-score, precision, recall, accuracy, hoặc tính khả thi khi thực thi (executability). Rất ít nghiên cứu sử dụng các chỉ số đo lường độ đồng thuận giữa các người đánh giá (inter-rater agreement metrics). Chưa có bài báo nào được rà soát trực tiếp kiểm thử năng lực đánh giá chất lượng khả năng tái lập của LLM đối với báo cáo lỗi so với kết quả rà soát thủ công của các lập trình viên bằng chỉ số Cohen’s Kappa.

### GAP-D – Dataset / evaluation gap 
Nhiều nghiên cứu chỉ tập trung vào các bộ dữ liệu chuẩn (benchmarks) hoặc các domain đặc thù như Defects4J, ứng dụng Android, trình biên dịch học sâu (deep-learning compilers), phản hồi trò chơi (game feedback), hoặc các tập dữ liệu báo cáo lỗi trùng lặp. Các bằng chứng thực nghiệm về việc đánh giá chất lượng khả năng tái lập trên các báo cáo lỗi từ GitHub/Jira dựa trên thiết kế đối sánh với rà soát của con người (human-review comparison design) hiện còn rất hạn chế.

## Final gap statement 
Mặc dù các nghiên cứu trước đây đã chứng minh rằng LLM có thể tái lập lỗi, phát hiện báo cáo lỗi trùng lặp, phân loại phản hồi của người dùng và hỗ trợ các tác vụ kỹ nghệ phần mềm khác, nhưng vẫn còn rất ít bằng chứng thực nghiệm về việc liệu LLM có thể đánh giá một cách đáng tin cậy chất lượng khả năng tái lập của báo cáo lỗi hay không. Đặc biệt, chưa có nghiên cứu được rà soát nào trực tiếp đối sánh kết quả đánh giá chất lượng khả năng tái lập bằng LLM với kết quả rà soát thủ công của các lập trình viên chuyên nghiệp thông qua chỉ số Cohen’s Kappa. Do đó, nghiên cứu này tập trung giải quyết khoảng trống trên bằng cách đánh giá liệu một mô hình LLM có thể đạt được độ đồng thuận cao (substantial agreement) với những nhận định chuyên môn của lập trình viên khi thẩm định chất lượng khả năng tái lập của báo cáo lỗi hay không.