# gap-statement-final.md — Phát biểu GAP cuối cùng của nhóm

**Nguồn tổng hợp:** 5 file `gap-statement.md` của các thành viên nhóm  
**Chủ đề nhóm:** LLM cho đánh giá chất lượng tái tạo Bug Report  
**Hướng tổng hợp:** Chọn GAP có bằng chứng mạnh nhất từ các thành viên

---

## 1. Bối cảnh chung

Bug Report là nguồn thông tin quan trọng trong quá trình bảo trì phần mềm vì nó giúp developer hiểu lỗi, tái hiện lỗi, phân tích nguyên nhân và sửa lỗi. Một Bug Report có chất lượng tốt thường cần mô tả rõ **Steps to Reproduce (S2R)**, **Expected Behavior (EB)**, **Observed/Actual Behavior (OB/AB)**, mức độ rõ ràng, đầy đủ và khả năng tái tạo của lỗi.

Các gap statement của nhóm cho thấy nhiều nghiên cứu trước đã dùng **LLM** như ChatGPT, GPT-4, GPT-4o, GPT-4o mini, Qwen, Mistral, Llama, ReBL, Cupid, LIBRO, ChatBR, AgentReport, ImproBR và BugScribe cho các tác vụ liên quan đến Bug Report. Những tác vụ này bao gồm tạo Bug Report, cải thiện Bug Report, tái hiện lỗi, replay lỗi Android, phát hiện duplicate Bug Report, phân loại issue, tóm tắt báo cáo lỗi, phát hiện hallucination và hỗ trợ software maintenance.

Cụ thể, **ChatBR**, **ImproBR**, **AgentReport**, **BugScribe** và **Can We Enhance Bug Report Quality Using LLMs?** là bằng chứng cho hướng **Bug Report generation/improvement**. **ReBL**, **LIBRO / Large Language Models are Few-shot Testers**, **AdbGPT** và **Can LLMs Demystify Bug Reports?** là bằng chứng cho hướng **bug reproduction / replay / reproduction-test generation**. **CUPID** là bằng chứng cho hướng **duplicate bug report detection**. **Nirujan et al.** là bằng chứng cho vấn đề **hallucination / reliability** trong bug report summaries. **Koyuncu** và các nghiên cứu **LLM-as-a-Judge / Human-in-the-loop evaluation** là bằng chứng rằng Cohen’s Kappa hoặc agreement có thể được dùng trong các task liên quan, nhưng chưa trực tiếp đúng với reproducibility-quality assessment.

Tuy nhiên, phần lớn nghiên cứu hiện tại vẫn tập trung vào **generation / improvement / reproduction / classification / duplicate detection**, thay vì kiểm chứng trực tiếp việc **LLM đánh giá chất lượng tái tạo của Bug Report** so với **developer/manual review** bằng một agreement metric rõ ràng.

---

## 2. Đối chiếu GAP của các thành viên

| Thành viên | GAP chính được nêu | Nhận xét khi merge |
|---|---|---|
| Nguyễn Minh Phúc | Thiếu kiểm chứng GPT-4o như automatic assessor cho reproducibility quality; thiếu Cohen’s Kappa ≥ 0.70; thiếu GitHub/Jira context | Khớp rất mạnh với hướng GAP-M/GAP-T/GAP-D của nhóm |
| Đặng Đăng Khoa | Thiếu nghiên cứu đánh giá LLM như công cụ tự thẩm định reproducibility quality; thiếu Cohen’s Kappa so với developer review; dataset GitHub/Jira còn hạn chế | Khớp mạnh với GAP-M và GAP-D |
| Ngô Trần Quân | Thiếu agreement-based validation bằng Cohen’s Kappa ≥ 0.70 giữa LLM assessment và developer/manual review | Khớp trực tiếp với hướng GAP chính của nhóm |
| Nguyễn Ngọc Gia Thuận | Nhấn mạnh thiếu kiểm chứng semantic correctness, practical acceptance rate, và Human-in-the-loop framework | Giữ làm supporting GAP-S vì liên quan đến độ tin cậy và human validation |
| Phạm Minh Quân | Thiếu direct reproducibility-quality assessment bằng GPT-4o, thiếu Cohen’s Kappa ≥ 0.70, thiếu GitHub/Jira dataset | Khớp mạnh với GAP-M/GAP-T/GAP-D |

---

## 3. Quy tắc xử lý conflict khi gộp GAP

### Conflict 1 — Cùng GAP nhưng diễn đạt khác nhau

Một số thành viên viết GAP theo hướng **Technology Gap**: “chưa kiểm chứng GPT-4o như assessor”. Một số khác viết theo hướng **Metric Gap**: “chưa dùng Cohen’s Kappa ≥ 0.70”. Khi merge, nhóm không chọn theo số đông mà đối chiếu lại với evidence table.

**Quyết định:** Giữ cả hai, nhưng chọn **GAP-M** làm GAP chính vì refined RQ yêu cầu chứng minh mức độ đồng thuận giữa GPT-4o và developer/manual review. Nếu thiếu metric agreement thì RQ không thể được kiểm chứng.

### Conflict 2 — Khác loại GAP: GAP-T, GAP-M, GAP-D, GAP-S

Các thành viên nêu nhiều loại GAP khác nhau. Theo quy tắc xử lý conflict, cần đếm bằng chứng trong evidence table và ưu tiên GAP có chứng cứ mạnh nhất, không bỏ phiếu theo cảm tính.

**Quyết định nhóm:**

1. **Primary GAP:** GAP-M — thiếu agreement-based validation bằng Cohen’s Kappa ≥ 0.70.
2. **Secondary GAP:** GAP-T — GPT-4o chưa được kiểm chứng trực tiếp như automatic assessor cho reproducibility quality.
3. **Supporting GAP:** GAP-D — thiếu dataset/evaluation trên GitHub/Jira Bug Reports.
4. **Supporting GAP:** GAP-S — hạn chế chung về domain-specific datasets, automatic metrics, hallucination, bias và thiếu human validation.

### Conflict 3 — Một số GAP quá rộng hoặc lệch trọng tâm

Một số gap statement đề cập đến APR, code repair, Human-in-the-loop patch evaluation hoặc LLM-as-a-Judge nói chung. Những hướng này có liên quan nhưng không trực tiếp trả lời RQ của nhóm.

**Quyết định:** Không chọn làm GAP chính. Các ý này được giữ dưới dạng **supporting evidence** cho vấn đề độ tin cậy, human validation và hạn chế của LLM-as-a-Judge.

### Conflict 4 — Khác RQ focus

Một số thành viên thiên về “Bug Report generation”, một số thiên về “Bug reproduction”, một số thiên về “LLM-as-evaluator”.

**Quyết định:** Quay về GAP mạnh nhất từ evidence table: nhiều paper đã làm generation/improvement/reproduction, nhưng chưa có paper nào kiểm chứng trực tiếp GPT-4o đánh giá reproducibility quality so với developer/manual review bằng Cohen’s Kappa ≥ 0.70. Vì vậy RQ nhóm tập trung vào **LLM-as-assessor for Bug Report reproducibility quality**.

---

## 4. GAP-T — Technology Gap

### Mô tả

Các nghiên cứu trước đã sử dụng LLM trong nhiều tác vụ liên quan đến Bug Report, ví dụ tạo Bug Report tự động, cải thiện cấu trúc và nội dung Bug Report, sinh hoặc cải thiện Steps to Reproduce, replay/reproduce lỗi Android, phát hiện duplicate Bug Report, phân loại issue, tóm tắt Bug Report và hỗ trợ sửa lỗi hoặc giải quyết GitHub issue.

### Bằng chứng cụ thể từ paper

- **ChatBR** và **Can We Enhance Bug Report Quality Using LLMs?** cho thấy LLM có thể hỗ trợ đánh giá/cải thiện các thành phần chất lượng như OB, EB và S2R, nhưng hướng chính vẫn là detection/improvement hơn là agreement-based assessment với developer review.
- **ImproBR**, **AgentReport**, **BugScribe** và các nghiên cứu về automatic bug report generation cho thấy LLM có thể tạo hoặc cải thiện Bug Report có cấu trúc tốt hơn.
- **ReBL**, **AdbGPT**, **LIBRO / Large Language Models are Few-shot Testers** và **Can LLMs Demystify Bug Reports?** cung cấp evidence cho khả năng reproduction/replay hoặc sinh test case dựa trên Bug Report.
- **CUPID** cho thấy ChatGPT/LLM có thể hỗ trợ duplicate bug report detection thông qua trích xuất thông tin và retrieval.
- Các nghiên cứu về **AutoCodeRover**, **Magis** hoặc GitHub issue resolution cho thấy LLM có thể hỗ trợ software maintenance, nhưng trọng tâm là issue fixing/resolution chứ không phải quality assessment.

### Kết luận GAP-T

**GAP-T hợp lệ**, vì GPT-4o và các LLM hiện đại đã được dùng nhiều trong bug report generation, improvement, reproduction và issue resolution, nhưng chưa có bằng chứng đủ mạnh cho thấy **GPT-4o** đã được kiểm chứng trực tiếp như một **automatic assessor** độc lập để đánh giá **reproducibility quality** của Bug Report so với developer/manual review. Tuy nhiên, GAP-T không phải GAP chính; nó hỗ trợ cho GAP-M vì GPT-4o là công nghệ được chọn trong RQ cuối cùng.

---

## 5. GAP-M — Metric Gap

### Mô tả

Các nghiên cứu được rà soát sử dụng nhiều metric khác nhau như CTQRS, SBERT similarity, ROUGE, METEOR, S2R F1, reproduction success rate, executable test generation, Recall@K, F1-score, precision, recall, accuracy, CodeBLEU, human evaluation, semantic similarity và Cohen’s Kappa trong một số ngữ cảnh phân loại hoặc annotation.

### Bằng chứng cụ thể từ paper

- **ChatBR**, **ImproBR**, **AgentReport** và **Can We Enhance Bug Report Quality Using LLMs?** dùng các metric như CTQRS, semantic similarity, S2R F1, ROUGE, SBERT hoặc high-quality completion rate để đánh giá chất lượng generation/improvement.
- **ReBL**, **AdbGPT**, **LIBRO** và **Can LLMs Demystify Bug Reports?** dùng reproduction success rate, replay success rate, executable test generation hoặc test usefulness để đánh giá khả năng tái hiện lỗi.
- **CUPID** dùng Recall Rate@K cho duplicate bug report detection, không dùng agreement với developer/manual review cho quality assessment.
- **Nirujan et al.** có sử dụng Cohen’s Kappa trong quá trình annotation/hallucination analysis, nhưng paper này tập trung vào hallucination trong bug report summaries, không phải đánh giá reproducibility quality của Bug Reports.
- **Koyuncu** và các nghiên cứu liên quan đến **LLM-as-a-Judge / Human-in-the-loop evaluation** có dùng Cohen’s Kappa hoặc agreement trong các task phân loại/đánh giá liên quan, nhưng không trực tiếp kiểm chứng GPT-4o đánh giá reproducibility quality của GitHub/Jira Bug Reports.

### Vì sao GAP-M được chọn làm GAP chính?

Refined RQ của nhóm không chỉ hỏi GPT-4o có thể hỗ trợ Bug Report hay không. RQ hỏi cụ thể:

> GPT-4o có thể đánh giá reproducibility quality của GitHub/Jira Bug Reports với mức độ đồng thuận đáng kể so với developer/manual review, đo bằng Cohen’s Kappa ≥ 0.70, hay không?

Do đó, thành phần quan trọng nhất để trả lời RQ là **agreement metric**. Nếu thiếu Cohen’s Kappa hoặc thiếu ngưỡng kiểm chứng agreement thì nghiên cứu không thể kết luận GPT-4o có đạt mức tương đương developer/manual review hay không.

### Kết luận GAP-M

**GAP-M là GAP chính của nhóm.** Các paper hiện có cho thấy nhiều metric đã được dùng trong generation, improvement, reproduction, duplicate detection, hallucination detection và classification. Tuy nhiên, chưa có nghiên cứu nào trong evidence table trực tiếp dùng **Cohen’s Kappa ≥ 0.70** làm **main success criterion** để đo mức độ đồng thuận giữa **GPT-4o-based Bug Report reproducibility-quality assessment** và **developer/manual review**.

---

## 6. GAP-D — Dataset / Evaluation Gap

### Mô tả

Các nghiên cứu trước thường dùng dataset hoặc bối cảnh cụ thể như Bugzilla/Mozilla, Android Bug Reports, Mojira/Minecraft, Defects4J, duplicate Bug Report datasets, game feedback, crash reports, TVM/OpenVINO compiler issues, SWE-bench hoặc GitHub issue resolution benchmarks.

### Bằng chứng cụ thể từ paper

- **ImproBR** sử dụng Mojira/Minecraft bug reports, nên domain khá cụ thể và không trực tiếp đại diện cho GitHub/Jira Bug Reports nói chung.
- **ReBL**, **AdbGPT**, **BugScribe** và **BugRepro** chủ yếu tập trung vào Android bug reports hoặc Android app replay/reproduction.
- **LIBRO**, **Can LLMs Demystify Bug Reports?** và các paper test generation thường dùng Defects4J hoặc GitHub bug reports trong bối cảnh sinh test/reproduction, không phải evaluation dataset cho LLM-as-assessor.
- **Acharya & Ginde**, **AgentReport**, **Can We Enhance Bug Report Quality Using LLMs?** và các paper liên quan đến Bugzilla/Mozilla cung cấp evidence quan trọng cho bug report quality/improvement, nhưng chưa trực tiếp cover GitHub/Jira reproducibility-quality assessment với developer review.
- **CUPID** và các duplicate detection datasets tập trung vào duplicate bug report detection, không phải reproducibility quality.

### Kết luận GAP-D

**GAP-D được giữ làm supporting GAP**, vì GitHub/Jira là population trong RQ và là bối cảnh gần với issue tracking thực tế. Các dataset hiện có hữu ích nhưng còn phân tán theo domain, task và platform, nên chưa trực tiếp kiểm chứng được việc GPT-4o đánh giá reproducibility quality trên GitHub/Jira Bug Reports theo cùng một protocol với developer/manual review.

---

## 7. GAP-S — Shared Limitation / Human Validation Gap

### Mô tả

Một số gap statement trong nhóm nhấn mạnh các hạn chế chung: LLM có thể hallucinate, LLM-as-a-Judge có thể có bias, nhiều nghiên cứu vẫn cần Human-in-the-loop, một số kết quả chỉ dựa trên automatic metrics, một số nghiên cứu có dataset nhỏ hoặc domain-specific, và một số paper là feasibility study hoặc supporting/background evidence.

### Bằng chứng cụ thể từ paper

- **Nirujan et al.** cho thấy hallucination có thể xuất hiện trong bug report summaries, bao gồm missing information hoặc fabricated content. Đây là bằng chứng quan trọng cho thấy LLM output cần được kiểm chứng về độ tin cậy.
- Các nghiên cứu về **LLM-as-a-Judge** và **Human-in-the-loop patch evaluation** cho thấy agreement với con người có thể đạt mức đáng kể trong một số task nếu có rubric rõ, nhưng đây là task liên quan như patch evaluation hoặc categorization, chưa phải reproducibility-quality assessment.
- **Koyuncu** cho thấy Cohen’s Kappa/agreement có thể dùng để kiểm tra mức đồng thuận trong fine-grained bug report categorization, nhưng task này khác với việc đánh giá khả năng tái tạo lỗi.
- Các paper như **Siddiq et al.** về reproducibility crisis trong LLM-for-SE research cho thấy vấn đề thiếu mô tả môi trường, prompt và artifact có thể ảnh hưởng đến tính tái lập của nghiên cứu.
- Một số paper như **AutoCodeRover**, **Magis**, **RCEGen** hoặc APR/code repair studies có giá trị background, nhưng không trực tiếp kiểm chứng LLM-as-assessor cho Bug Report reproducibility quality.

### Kết luận GAP-S

**GAP-S được giữ làm supporting GAP**, dùng để giải thích vì sao nghiên cứu cần manual review, rubric rõ ràng và agreement metric. Các evidence này không tạo ra GAP chính, nhưng củng cố lập luận rằng automatic LLM assessment cần được đối chiếu với con người thay vì chỉ dựa trên automatic metrics.

---

## 8. GAP cuối cùng của nhóm

Mặc dù các nghiên cứu trước đã chứng minh rằng LLM có thể hỗ trợ nhiều tác vụ liên quan đến Bug Report như generation, improvement, reproduction, replay, duplicate detection, categorization, summarization, issue resolution và software maintenance, vẫn còn thiếu bằng chứng thực nghiệm cho thấy **GPT-4o** có thể trực tiếp đánh giá **reproducibility quality** của **GitHub/Jira Bug Reports** với mức độ đồng thuận đáng kể so với **developer/manual review**.

GAP chính của nhóm là: chưa có nghiên cứu nào trong tập evidence kiểm chứng trực tiếp **LLM-based Bug Report reproducibility-quality assessment** bằng **Cohen’s Kappa ≥ 0.70** như tiêu chí thành công chính cho agreement giữa **GPT-4o assessment** và **developer/manual review**.

---

## 9. Đóng góp dự kiến của nghiên cứu nhóm

Nghiên cứu của nhóm sẽ giải quyết GAP trên bằng cách:

1. Sử dụng **GPT-4o** làm automatic assessor cho **Bug Report reproducibility quality**.
2. Đánh giá trên **GitHub/Jira Bug Reports**.
3. Xây dựng rubric đánh giá dựa trên **S2R**, **Expected Behavior** và **Observed/Actual Behavior**.
4. So sánh trực tiếp kết quả đánh giá của GPT-4o với **developer/manual review**.
5. Đo mức độ agreement bằng **Cohen’s Kappa**.
6. Dùng ngưỡng **Cohen’s Kappa ≥ 0.70** như success threshold cho substantial agreement.

---

## 10. RQ cuối cùng của nhóm

**RQ:** GPT-4o có thể tự động đánh giá **reproducibility quality** của **GitHub/Jira Bug Reports** với mức độ đồng thuận đáng kể so với **developer/manual review**, đo bằng **Cohen’s Kappa ≥ 0.70**, hay không?

---

## 11. Ghi chú về quyết định merge

- Không chọn GAP bằng cách bỏ phiếu số đông.
- Không chọn GAP chỉ vì thành viên nào viết dài hơn hoặc thuyết phục hơn.
- GAP được chọn dựa trên evidence table merged và mức độ trực tiếp với RQ.
- Các GAP liên quan đến APR, code repair, patch evaluation hoặc survey chỉ được giữ làm supporting/background evidence nếu không trực tiếp liên quan đến Bug Report reproducibility-quality assessment.
- Nếu sau này nhóm làm `gap-analysis.md`, cần kiểm chứng lại từng claim trong file này bằng từng paper trong `evidence-table-merged.md`.
