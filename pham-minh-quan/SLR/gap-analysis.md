# GAP Analysis — LLM-Based Bug Report Reproducibility Quality Assessment

**Thành viên:** Phạm Minh Quân
**Evidence table:** N = 15 included studies
**Nguồn chính:** `SLR/evidence-table.md` và `SLR/gap-statement.md`

---

## 1. Mục tiêu của file này

File này dùng để giải thích rõ:

* GAP nào được phát hiện từ evidence table.
* GAP nào là GAP chính.
* GAP đó có bằng chứng từ paper nào.
* GAP đó có khả thi để chuyển thành thực nghiệm hay không.

Nói đơn giản: file này chứng minh rằng GAP của em không phải tự nghĩ ra, mà được rút ra từ 15 paper trong evidence table.

---

## 2. Tóm tắt bằng chứng từ evidence table

Trong 15 paper đã included, các nghiên cứu hiện tại chủ yếu tập trung vào:

* Tái hiện lỗi từ bug report.
* Tự động replay Android bug report.
* Sinh test case từ bug report.
* Phát hiện duplicate bug report.
* Phân loại bug report hoặc user feedback.
* Tổng quan về LLM trong Software Engineering.

Một số bằng chứng quan trọng:

| ID | File PDF cần bật                              | Paper                                                                                | Bằng chứng / số liệu quan trọng                                                                         | Dùng để chứng minh                                                                           |
| -: | --------------------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
|  1 | `Chen_2023_TestCasesFromBugReports.pdf`       | Automatic Generation of Test Cases based on Bug Reports                              | ChatGPT có thể sinh executable test cases cho bug reports liên quan tới tối đa 50% bugs trong Defects4J | LLM đã được dùng để sinh test case từ bug report, nhưng chưa chấm quality                    |
|  4 | `Li_2023_AndroidBugReplayLLM.pdf`             | Prompting Is All You Need: Automated Android Bug Replay with Large Language Models   | AdbGPT reproduced 81.3% bug reports, average 253.6 seconds                                              | LLM có thể replay bug report, nhưng task là reproduction, không phải quality assessment      |
| 30 | `LLMFeedback_2025_GameUserFeedback.pdf`       | The Use of Large Language Models to Automatically Categorise User Feedback for Games | Có dùng Cohen’s Kappa / inter-rater reliability trong ngữ cảnh categorization                           | Có metric agreement, nhưng không phải reproducibility quality                                |
| 41 | `FalsePositive_2024_DLCompilerBugReports.pdf` | False-Positive Bug Reports in Deep Learning Compilers                                | Few-shot prompting đạt promising accuracy và explanation quality                                        | LLM có thể hỗ trợ xử lý bug reports, nhưng domain hẹp                                        |
| 42 | `LIBRO_2023_GeneralBugReproduction.pdf`       | Large Language Models are Few-shot Testers                                           | Reproduced 251/750 bugs (33.5%) và 10/31 recent GitHub bug reports (32.2%)                              | LLM reproduction chưa ổn định, còn cần đánh giá reliability                                  |
| 44 | `ReBL_2024_AndroidBugReproduction.pdf`        | Feedback-Driven Automated Whole Bug Report Reproduction for Android Apps             | ReBL reproduced 90.63% Android bug reports, average 74.98 seconds                                       | LLM/GPT-4 rất mạnh trong reproduction, nhưng không đánh giá chất lượng report                |
| 45 | `Cupid_2024_DuplicateBugDetection.pdf`        | Cupid: Leveraging ChatGPT for More Accurate Duplicate Bug Report Detection           | Recall@10 = 0.602–0.654                                                                                 | LLM dùng cho duplicate detection, không phải quality assessment                              |
| 46 | `Demystify_2023_LLMBugReports.pdf`            | Can LLMs Demystify Bug Reports?                                                      | ChatGPT reproduced 50% reported bugs                                                                    | LLM hiểu và reproduce bug reports, nhưng không so sánh agreement với developer/manual review |

---

## 3. Bảng phân loại GAP

| Loại GAP                         | Cột nguồn trong evidence table | Câu hỏi kiểm tra                                   | Kết luận                                                                                                                                    |
| -------------------------------- | ------------------------------ | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| GAP-M — Metric / Evaluation Gap  | Metric                         | Khía cạnh nào chưa được đo đúng cách?              | Chưa có paper nào dùng Cohen’s Kappa ≥ 0.70 làm metric chính cho GPT-4o-vs-manual-review agreement trong reproducibility quality assessment |
| GAP-T — Technology / Task Gap    | Tool/LLM + Result              | Công nghệ hoặc tác vụ nào chưa được thử trực tiếp? | Chưa có paper nào trực tiếp dùng GPT-4o để đánh giá reproducibility quality của bug report                                                  |
| GAP-D — Dataset / Evaluation Gap | Dataset                        | Dataset/domain nào còn thiếu?                      | GitHub/Jira bug reports chưa được đánh giá cụ thể theo thiết kế GPT-4o-vs-manual-review agreement                                           |
| GAP-S — Shared Limitation        | Limitation                     | Hạn chế nào lặp lại trong nhiều paper?             | Nhiều paper bị giới hạn bởi domain, benchmark, task-specific setting, hoặc token/compute cost                                               |

---

## 4. GAP-M — Metric / Evaluation Gap

### Phát hiện

Các paper trong evidence table đã dùng nhiều metric khác nhau để đánh giá các task liên quan đến bug reports, ví dụ như:

* reproduction success rate,
* bug reproduction rate,
* Recall@10,
* precision,
* recall,
* F1-score,
* accuracy,
* executability.

Tuy nhiên, các metric này chủ yếu đo hiệu năng của từng task riêng lẻ, chẳng hạn như reproduce bug thành công hay detect duplicate bug report tốt hay không. Chúng chưa trực tiếp đo mức độ đồng thuận giữa LLM và manual reviewer khi cùng đánh giá chất lượng của một bug report.

Trong hướng nghiên cứu của em, mục tiêu không chỉ là xem GPT-4o trả lời đúng hay sai, mà là xem GPT-4o có đánh giá reproducibility quality giống với manual review hay không. Vì vậy, bài toán này cần một metric đo agreement giữa hai rater.

### Bằng chứng từ paper

| Paper                                        | Metric đã dùng                                                                                | Vì sao chưa đủ cho bài của em?                                                                         |
| -------------------------------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Paper 44 — ReBL                              | Reproduction success rate = 90.63%                                                            | Đo reproduce bug thành công, không đo agreement giữa LLM và human/manual reviewer                      |
| Paper 42 — LIBRO                             | 251/750 bugs reproduced = 33.5%; 10/31 recent GitHub bug reports = 32.2%                      | Đo số bug reproduce được, không đo chất lượng bug report                                               |
| Paper 45 — Cupid                             | Recall@10 = 0.602–0.654                                                                       | Metric cho duplicate bug report detection, không phải quality assessment                               |
| Paper 30 — Game feedback categorization      | Cohen’s Kappa / inter-rater reliability                                                       | Có dùng agreement metric, nhưng dùng cho categorization, không phải reproducibility quality assessment |
| Paper 31 — Learning Software Bug Reports SLR | Precision, recall, F1-score, accuracy là các metric phổ biến; statistical testing còn hạn chế | Cho thấy bug report research vẫn thiếu agreement-based validation                                      |

### Lý do chọn Cohen’s Kappa

Cohen’s Kappa phù hợp với bài của em vì nghiên cứu có hai bên đánh giá cùng một tập bug reports:

* Rater 1: GPT-4o assessment.
* Rater 2: manual review / human reviewer.

Cohen’s Kappa đo mức độ agreement giữa hai rater và có tính đến khả năng hai bên đồng ý do ngẫu nhiên. Vì vậy, nó phù hợp hơn accuracy trong trường hợp mục tiêu là đo agreement.

### Lý do chọn ngưỡng κ ≥ 0.70

Em chọn κ ≥ 0.70 vì đây là một ngưỡng nằm trong mức substantial agreement.

Theo cách diễn giải phổ biến của Landis and Koch, khoảng 0.61–0.80 được xem là substantial agreement. Do đó, κ ≥ 0.70 được dùng như một operational threshold: nếu GPT-4o đạt từ 0.70 trở lên, em xem đây là mức agreement đủ mạnh để chứng minh GPT-4o có tiềm năng hỗ trợ đánh giá reproducibility quality.

Ngoài ra, paper `LLMFeedback_2025_GameUserFeedback.pdf` có dùng Cohen’s Kappa để so sánh các GPT models với human reviewer trong task categorization. Kết quả GPT-human trong primary categorization chỉ khoảng 0.597, 0.628 và 0.635. Điều này cho thấy đạt agreement cao với human reviewer không dễ, nên việc đặt ngưỡng 0.70 là một mục tiêu rõ ràng và có tính thử thách.

### Kết luận GAP-M

GAP-M là GAP chính của em vì hiện tại chưa có nghiên cứu nào trực tiếp dùng Cohen’s Kappa ≥ 0.70 để đánh giá agreement giữa GPT-4o và manual review trong task bug report reproducibility quality assessment.

---

## 5. GAP-T — Technology / Task Gap

### Phát hiện

Các paper hiện tại đã dùng LLM cho nhiều task liên quan bug reports như:

* bug reproduction,
* Android bug replay,
* test generation,
* duplicate bug report detection,
* false-positive bug report mitigation,
* user feedback categorization.

Tuy nhiên, các task này chưa trực tiếp đánh giá GPT-4o như một công cụ chấm reproducibility quality của bug report.

### Bằng chứng từ paper

| Paper                                      | Đã làm gì?                                              | Vì sao chưa đủ cho GAP của em?                                                       |
| ------------------------------------------ | ------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| Paper 44 — ReBL                            | Dùng GPT-4 để reproduce Android bug reports, đạt 90.63% | Đây là bug reproduction, không phải chấm quality của bug report                      |
| Paper 46 — Can LLMs Demystify Bug Reports? | ChatGPT reproduced 50% reported bugs                    | Đo khả năng reproduce, không đo agreement với human/manual reviewer                  |
| Paper 45 — Cupid                           | Duplicate bug report detection, Recall@10 = 0.602–0.654 | Task là duplicate detection, không phải reproducibility quality                      |
| Paper 30 — LLM categorise user feedback    | Có Cohen’s Kappa trong categorization                   | Agreement dùng cho phân loại feedback, không phải bug report reproducibility quality |

### Kết luận GAP-T

GAP-T là GAP phụ của em. Nó cho thấy task GPT-4o-based reproducibility quality assessment vẫn chưa được nghiên cứu trực tiếp.

Tuy nhiên, vì phạm vi sinh viên khó đảm bảo có developer chuyên nghiệp làm ground truth, em không chọn GAP-T làm GAP chính. Thay vào đó, em chọn GAP-M làm GAP chính vì phần metric/evaluation có thể triển khai khả thi hơn bằng manual review theo rubric rõ ràng.

---

## 6. GAP-D — Dataset / Evaluation Gap

### Phát hiện

Các paper hiện tại chủ yếu dùng:

* Defects4J,
* Android bug reports,
* TVM/OpenVINO issues,
* game feedback datasets,
* duplicate bug report datasets,
* survey datasets.

Vẫn còn thiếu bằng chứng về GitHub/Jira bug reports được chấm reproducibility quality bằng GPT-4o và so sánh với manual review.

### Khó khăn

Nếu dùng nguyên dataset GitHub/Jira lớn hoặc đưa toàn bộ issue thread vào GPT-4o thì sẽ tốn rất nhiều token. Nhiều bug report có comment thread dài, stack trace dài, log dài hoặc discussion không liên quan. Vì vậy, dataset lớn không khả thi trong phạm vi sinh viên.

### Cách xử lý trong RBL-2

Trong RBL-2, em chỉ đề xuất pilot experiment nhỏ:

* Chọn khoảng 10–20 GitHub/Jira bug reports.
* Không đưa toàn bộ issue thread vào GPT-4o.
* Chỉ giữ các trường quan trọng: title, description, steps to reproduce, expected behavior, actual behavior, environment.
* Loại bỏ comment dài, log quá dài, attachment, nội dung trùng lặp hoặc không liên quan.
* Ghi rõ đây là pilot study để kiểm tra feasibility trước khi mở rộng dataset.

### Kết luận GAP-D

GAP-D là gap hỗ trợ. Nó cho thấy còn thiếu đánh giá trên GitHub/Jira bug reports, nhưng trong phạm vi RBL-2, em chỉ xử lý bằng pilot sample nhỏ để giảm token cost và giữ experiment khả thi.

---

## 7. Feasibility Check — GAP chính

**GAP chính được chọn:** GAP-M — Metric / Evaluation Gap

| Tiêu chí     | Đánh giá     | Ghi chú                                                                                             |
| ------------ | ------------ | --------------------------------------------------------------------------------------------------- |
| Dataset      | ⚠️ Cần xử lý | Chỉ dùng pilot sample nhỏ 10–20 GitHub/Jira bug reports; mỗi report được rút gọn để giảm token cost |
| Tool/API     | ✅ An toàn    | GPT-4o có thể dùng qua ChatGPT/API                                                                  |
| Compute      | ✅ An toàn    | Không cần GPU riêng                                                                                 |
| Ground truth | ⚠️ Cần xử lý | Dùng manual review theo rubric rõ ràng; không khẳng định có developer chuyên nghiệp                 |
| Skills       | ✅ An toàn    | Có thể thiết kế prompt, rubric, label, và tính Cohen’s Kappa                                        |
| Time         | ⚠️ Cần xử lý | Giới hạn pilot sample và không dùng full issue thread                                               |
| Token cost   | ⚠️ Cần xử lý | Chỉ dùng title, description, S2R, expected/actual behavior, environment                             |
| Contribution | ✅ An toàn    | Có giá trị vì chưa có paper nào làm trực tiếp agreement-based validation cho task này               |

**Kết quả feasibility:** 0 blocker, 4 warnings. GAP này khả thi nếu giới hạn scope dataset, rút gọn input và dùng manual review/rubric rõ ràng.

---

## 8. GAP chính và GAP phụ

### GAP chính

**GAP-M — Metric / Evaluation Gap**

Chưa có nghiên cứu nào trong 15 included studies trực tiếp dùng Cohen’s Kappa ≥ 0.70 để đánh giá agreement giữa GPT-4o và manual review trong task bug report reproducibility quality assessment.

### GAP phụ 1

**GAP-T — Technology / Task Gap**

Các nghiên cứu hiện tại đã dùng LLM cho bug reproduction, bug replay, test generation, duplicate detection, và categorization, nhưng chưa dùng GPT-4o để chấm reproducibility quality của bug report.

### GAP phụ 2

**GAP-D — Dataset / Evaluation Gap**

Còn thiếu nghiên cứu trên GitHub/Jira bug reports theo hướng GPT-4o assessment vs manual review. Tuy nhiên, trong phạm vi sinh viên, dataset cần được giới hạn thành pilot sample nhỏ để tránh token cost quá cao.

---

## 9. Final GAP Statement

Although previous studies show that LLMs can reproduce bugs, replay Android bug reports, detect duplicate reports, classify user feedback, and support software engineering analysis, there is still insufficient evidence on agreement-based validation for GPT-4o when assessing bug report reproducibility quality.

More specifically, no reviewed study directly evaluates whether GPT-4o can assess the reproducibility quality of GitHub/Jira bug reports with Cohen’s Kappa ≥ 0.70 compared to manual review.

Therefore, this study addresses the metric/evaluation gap by proposing a pilot experiment where GPT-4o and manual reviewers assess the same small curated sample of GitHub/Jira bug reports, and their agreement is measured using Cohen’s Kappa.

---

 