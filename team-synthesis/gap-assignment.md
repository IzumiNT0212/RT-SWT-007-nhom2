# Gap Assignment — Tổng hợp GAP của 5 thành viên

**Dự án:** LLM-Based Bug Report Reproducibility Quality Assessment  
**Mục tiêu:** Tổng hợp GAP cá nhân của 5 thành viên để chọn GAP nhóm, Research Question và hướng thực nghiệm cho RBL.  
**File nguồn:**  
- `gap-statement Ngo Tran Quan.md`
- `gap-statement Pham Minh Quan.md`
- `gap-statement Nguyen Ngoc Gia Thuan.md`
- `gap-statement Nguyen Minh Phuc.md`
- `gap-statement Dang Dang Khoa(1).md`

---

## 1. Nguyên tắc tổng hợp

Nhóm tổng hợp GAP theo các nguyên tắc sau:

1. **Evidence-based:** GAP được chọn phải xuất hiện trong evidence table hoặc được nhiều thành viên phát hiện từ các paper đã rà soát.
2. **No HARKing:** Không đổi GAP/RQ/metric/threshold sau khi đã có dữ liệu thực nghiệm, trừ khi có amendment rõ ràng.
3. **Reproducibility:** Mọi quyết định về dataset, prompt, model version, metric và threshold phải được ghi lại.
4. **Pilot bắt buộc:** Trước khi chạy full experiment, nhóm cần chạy pilot để kiểm tra dataset, prompt, API output và cách tính metric.
5. **Empty response = invalid:** Nếu LLM trả về rỗng/lỗi API, kết quả đó phải được ghi là invalid, không tự điền nhãn thay thế.

---

## 2. Tóm tắt GAP của từng thành viên

| Thành viên | Evidence table | GAP chính tìm được | Đóng góp cho GAP nhóm | Mức độ phù hợp với topic nhóm |
|---|---:|---|---|---|
| Ngô Trần Quân | N = 15 papers | Thiếu nghiên cứu đánh giá GPT-4o như automatic assessor cho chất lượng khả năng tái hiện lỗi của bug report so với developer/manual review. | Làm rõ 3 GAP: Technology, Metric, Dataset. Đề xuất Cohen's Kappa >= 0.70 và GitHub/Jira bug reports. | Cao |
| Phạm Minh Quân | N = 15 included studies | LLM đã được dùng cho bug reproduction, duplicate detection, prioritization, testing, nhưng chưa trực tiếp đánh giá reproducibility quality bằng GPT-4o so với developer review. | Củng cố Technology Gap, Metric Gap và Dataset/Evaluation Gap. | Cao |
| Nguyễn Ngọc Gia Thuận | N = 13 included studies | LLM chủ yếu được dùng cho downstream tasks như tái lập lỗi, phát hiện trùng lặp, phân loại, ưu tiên hóa, sinh test case; chưa đánh giá chất lượng của chính bug report. | Làm rõ Task Gap và nhu cầu human-review comparison design. | Cao |
| Nguyễn Minh Phúc | N = 8 papers | Thiếu bằng chứng về việc GPT-4o có thể đóng vai trò independent quality assessor cho bug report reproducibility quality. | Nhấn mạnh các tiêu chí bug report tốt như Steps to Reproduce, Expected Behavior và Observed/Actual Behavior. | Cao |
| Đặng Đăng Khoa | Không ghi N cụ thể | Thiếu nghiên cứu về semantic correctness, practical acceptance rate và reliability của LLM-as-a-Judge trong môi trường human-in-the-loop. | Bổ sung góc nhìn về độ tin cậy, bias, hallucination và nhu cầu kiểm soát bằng human-in-the-loop. | Trung bình - phù hợp làm supporting gap/threats hơn là GAP chính |

---

## 3. Nhận xét sau khi đối chiếu 5 GAP

Sau khi đối chiếu 5 file GAP, nhóm nhận thấy 4/5 thành viên đều hội tụ vào cùng một hướng chính:

> LLM đã được dùng nhiều trong các tác vụ liên quan đến bug report, nhưng còn thiếu bằng chứng thực nghiệm về việc dùng GPT-4o như một bộ đánh giá tự động để chấm chất lượng khả năng tái hiện lỗi của bug report và so sánh trực tiếp với đánh giá thủ công của developer/manual reviewer.

Các GAP lặp lại nhiều nhất gồm:

### 3.1. GAP-T — Task/Technology Gap

Các nghiên cứu hiện tại chủ yếu dùng LLM cho:

- bug report generation,
- bug report improvement,
- bug reproduction support,
- duplicate bug report detection,
- bug prioritization,
- issue understanding,
- test generation,
- software maintenance support.

Tuy nhiên, các nghiên cứu này chưa trực tiếp kiểm chứng việc:

> GPT-4o có thể đánh giá chất lượng khả năng tái hiện lỗi của bug report như một automatic assessor hay không.

Vì vậy, GAP-T là GAP quan trọng nhất và được nhóm chọn làm trọng tâm.

---

### 3.2. GAP-M — Metric/Measurement Gap

Các nghiên cứu được rà soát thường dùng các metric như:

- reproduction success rate,
- Recall@K,
- precision,
- recall,
- F1-score,
- accuracy,
- executability rate,
- CTQRS,
- SBERT similarity,
- ROUGE,
- METEOR,
- semantic similarity.

Tuy nhiên, các file GAP đều chỉ ra rằng chưa có nghiên cứu nào trong tập evidence sử dụng:

> Cohen's Kappa >= 0.70 làm tiêu chí chính để kiểm tra mức độ đồng thuận giữa GPT-4o assessment và developer/manual review trong đánh giá bug report reproducibility quality.

Do đó, GAP-M được giữ lại để định hướng metric chính cho nghiên cứu.

---

### 3.3. GAP-D — Dataset/Evaluation Gap

Các nghiên cứu hiện tại thường dùng dataset đặc thù hoặc benchmark như:

- Android bug reports,
- Defects4J,
- Mojira/Minecraft,
- Mozilla/Bugzilla,
- deep-learning compiler issues,
- game feedback datasets,
- duplicate-report datasets,
- crash reports.

Trong khi đó, GitHub/Jira bug reports có cấu trúc không đồng nhất, chất lượng mô tả khác nhau và gần với môi trường issue-tracking thực tế hơn. Nhóm nhận thấy còn thiếu bằng chứng về:

> GPT-4o đánh giá reproducibility quality của GitHub/Jira bug reports bằng thiết kế so sánh với human/developer review.

Do đó, GAP-D được giữ lại như một khoảng trống về dataset và thiết kế đánh giá.

---

### 3.4. Supporting Gap — Reliability of LLM-as-a-Judge

GAP của Đặng Đăng Khoa không trùng hoàn toàn với topic chính vì tập trung nhiều hơn vào việc standardize bug reports và đánh giá semantic correctness của LLM-generated bug reports. Tuy nhiên, phần này vẫn có giá trị hỗ trợ vì nhấn mạnh các rủi ro khi dùng LLM-as-a-Judge:

- position bias,
- hallucination,
- thiếu human-in-the-loop validation,
- thiếu framework kiểm soát độ tin cậy của LLM output.

Nhóm không chọn đây là GAP chính, nhưng sẽ dùng nó trong phần **Threats to Validity**, **Downscope Protocol** hoặc **Design Rationale**.

---

## 4. GAP nhóm chọn

Nhóm chọn GAP tổng hợp như sau:

> Mặc dù các nghiên cứu trước đây cho thấy LLM có thể hỗ trợ nhiều tác vụ liên quan đến bug report như tạo báo cáo lỗi, cải thiện mô tả lỗi, tái hiện lỗi, phát hiện trùng lặp, phân loại và ưu tiên hóa issue, vẫn còn thiếu bằng chứng thực nghiệm về việc GPT-4o có thể trực tiếp đánh giá chất lượng khả năng tái hiện lỗi của GitHub/Jira bug reports với mức độ đồng thuận đáng kể so với developer/manual review hay không. Đặc biệt, chưa có nghiên cứu nào trong tập evidence của nhóm kiểm chứng vấn đề này bằng Cohen's Kappa >= 0.70 như success threshold chính cho agreement giữa LLM assessment và human judgment.

---

## 5. Lý do chọn GAP này

Nhóm chọn GAP trên vì:

1. **Có sự đồng thuận cao giữa các thành viên:** 4/5 file GAP đều trực tiếp nói về LLM-based bug report reproducibility quality assessment.
2. **Có thể đo được:** GAP có thể kiểm chứng bằng Cohen's Kappa, agreement rate và phân tích disagreement cases.
3. **Phù hợp với RBL:** Nghiên cứu có thể triển khai theo pilot experiment trước, sau đó mới scale lên full experiment.
4. **Không claim quá rộng:** Nhóm chỉ kiểm tra mức độ đồng thuận giữa GPT-4o và manual review, không khẳng định GPT-4o thay thế hoàn toàn developer.
5. **Có hướng thực nghiệm rõ ràng:** Có thể dùng bug reports từ GitHub/Jira, manual labels làm ground truth/comparison baseline, sau đó cho GPT-4o đánh giá theo cùng rubric.

---

## 6. Research Question sau khi tổng hợp

**RQ chính:**

> GPT-4o có thể tự động đánh giá chất lượng khả năng tái hiện lỗi của bug reports từ GitHub/Jira với mức độ đồng thuận đáng kể so với developer/manual review, đo bằng Cohen's Kappa >= 0.70, hay không?

---

## 7. Metric và threshold được chốt

| Thành phần | Quyết định của nhóm |
|---|---|
| Metric chính | Cohen's Kappa |
| Success threshold | Cohen's Kappa >= 0.70 |
| Baseline so sánh | Developer/manual review |
| Dataset mục tiêu | GitHub/Jira bug reports |
| Đơn vị đánh giá | Bug report |
| Output chính | Reproducibility quality label |
| Bổ sung | Agreement rate, confusion matrix, disagreement analysis, invalid/empty response count |
| Pilot | Bắt buộc chạy trước full experiment |

---

## 8. Các GAP không chọn làm trọng tâm chính

| GAP không chọn làm trọng tâm | Lý do không chọn làm GAP chính | Cách sử dụng trong nghiên cứu |
|---|---|---|
| LLM-generated bug report semantic correctness | Lệch nhẹ khỏi topic vì nhóm không sinh bug report mới, mà đánh giá bug report có sẵn. | Có thể đưa vào Related Work hoặc Future Work. |
| Practical acceptance rate trong industrial projects | Quá rộng và cần industrial validation, vượt phạm vi pilot của nhóm. | Đưa vào Threats to Validity. |
| Bias/hallucination của LLM-as-a-Judge | Quan trọng nhưng là rủi ro phương pháp hơn là GAP chính. | Dùng để thiết kế prompt, log raw output và quy định empty response = invalid. |
| Human-in-the-loop framework tổng quát | Rộng hơn scope SWT301/RBL hiện tại. | Dùng làm design rationale cho manual review comparison. |

---

## 9. Liên kết với thực nghiệm RBL-4

Để giải quyết GAP đã chọn, nhóm sẽ thực hiện pilot experiment theo hướng:

1. Chọn một tập bug reports từ GitHub/Jira.
2. Chuẩn bị manual/developer labels làm baseline so sánh.
3. Thiết kế prompt cố định cho GPT-4o.
4. Lưu model version, temperature, prompt nguyên văn, input và raw output.
5. Cho GPT-4o đánh giá reproducibility quality.
6. Tính Cohen's Kappa giữa GPT-4o labels và manual labels.
7. Phân tích các disagreement cases.
8. Ghi invalid/empty response riêng, không tự điền kết quả.
9. Nếu pilot ổn, tiếp tục full experiment; nếu pilot fail, kích hoạt downscope protocol.

---

## 10. Decision Log

| Decision | Nội dung |
|---|---|
| GAP chính | Thiếu agreement-based validation cho GPT-4o trong bug report reproducibility quality assessment |
| GAP phụ | Reliability of LLM-as-a-Judge, hallucination, human-in-the-loop validation |
| RQ chính | GPT-4o có đạt Cohen's Kappa >= 0.70 so với developer/manual review không? |
| Metric chính | Cohen's Kappa |
| Threshold | >= 0.70 |
| Dataset | GitHub/Jira bug reports |
| Scope | Pilot feasibility experiment, không claim industrial-scale validation |
| Người quyết định | Nhóm + PL, dựa trên GAP của 5 thành viên |




