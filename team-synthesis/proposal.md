# Đề xuất nghiên cứu RBL-3

**Chủ đề:** Đánh giá mức độ đồng thuận giữa GPT-4o và đánh giá thủ công khi chấm chất lượng khả năng tái hiện lỗi của báo cáo lỗi  
**Môn học / Mã chủ đề:** SWT301 / SLR  
**Đầu ra:** `team-synthesis/proposal.md`  
**Trạng thái:** Bản đề xuất cuối dùng để bảo vệ RBL-3  

Đề xuất này được viết lại từ các sản phẩm tổng hợp của RBL-2, gồm: `gap-analysis.md`, `design-rationale.md` và `hypotheses-draft.md`. Nghiên cứu được thiết kế dưới dạng **thử nghiệm pilot để kiểm tra tính khả thi**, không phải là một đánh giá quy mô lớn trong môi trường công nghiệp.

---

## 1. Tên đề tài và thông tin nhóm

**Tên đề tài:** Đánh giá mức độ đồng thuận giữa GPT-4o và đánh giá thủ công khi chấm chất lượng khả năng tái hiện lỗi của báo cáo lỗi

Đề xuất này kiểm tra xem GPT-4o có thể tự động đánh giá chất lượng khả năng tái hiện lỗi của các báo cáo lỗi trên GitHub/Jira với mức đồng thuận cao so với nhãn chuẩn do con người đánh giá thủ công hay không.

---

## 2. Phát biểu vấn đề nghiên cứu

### 2.1 Bối cảnh và tầm quan trọng

Báo cáo lỗi là tài liệu giao tiếp quan trọng giữa người dùng, người kiểm thử và lập trình viên. Một báo cáo lỗi tốt giúp lập trình viên hiểu lỗi, tái hiện lỗi và sửa lỗi hiệu quả hơn. Các nghiên cứu trước về chất lượng báo cáo lỗi cho thấy lập trình viên thường cần những thông tin rõ ràng như **các bước tái hiện lỗi**, **kết quả mong đợi**, **kết quả thực tế**, **stack trace**, **test case** và **thông tin môi trường** [1].

Thông tin liên quan đến khả năng tái hiện lỗi đặc biệt quan trọng. Nếu báo cáo lỗi thiếu các bước tái hiện hoặc các bước này có chất lượng thấp, lập trình viên sẽ phải tốn nhiều công sức hơn trong quá trình phân loại lỗi và sửa lỗi [2]. Khi một báo cáo lỗi không cung cấp đủ thông tin để tái hiện, lập trình viên có thể phải hỏi lại người báo lỗi, tự điều tra các hành vi chưa rõ ràng, hoặc đóng issue với lý do không thể tái hiện lỗi.

### 2.2 Tình hình nghiên cứu hiện tại

Các nghiên cứu hiện có đã khai thác nhiều nhiệm vụ liên quan đến báo cáo lỗi, ví dụ như cải thiện chất lượng báo cáo lỗi, tái hiện lỗi, replay lỗi, phát hiện báo cáo lỗi trùng lặp, phân loại báo cáo lỗi, tóm tắt nội dung, sinh test case và phân tích các tài liệu kỹ thuật phần mềm bằng mô hình ngôn ngữ lớn.

Một số nghiên cứu dùng mô hình ngôn ngữ lớn cho thấy các mô hình này có thể xử lý báo cáo lỗi và hỗ trợ các nhiệm vụ như sinh test case, tái hiện lỗi Android, phát hiện báo cáo lỗi trùng lặp, hoặc cải thiện các phần quan trọng của báo cáo lỗi như các bước tái hiện lỗi, kết quả thực tế và kết quả mong đợi [4]-[8]. Một số nghiên cứu trong lĩnh vực kỹ thuật phần mềm cũng dùng người đánh giá hoặc gán nhãn thủ công để tạo dữ liệu chuẩn khi đánh giá các công cụ tự động [3].

Tuy nhiên, các nghiên cứu đã review **chưa trực tiếp đánh giá GPT-4o** như một công cụ tự động chấm chất lượng khả năng tái hiện lỗi của báo cáo lỗi, rồi so sánh với nhãn chuẩn từ đánh giá thủ công bằng **Cohen’s Kappa** như thước đo đồng thuận chính.

### 2.3 Khoảng trống nghiên cứu

Khoảng trống chính của đề tài là **GAP-M — khoảng trống về cách đánh giá / thước đo**. Cụ thể, chưa có paper nào trong nhóm tài liệu đã review trực tiếp kiểm tra việc GPT-4o đánh giá chất lượng khả năng tái hiện lỗi của báo cáo lỗi GitHub/Jira với mức đồng thuận đáng kể so với nhãn chuẩn từ đánh giá thủ công, đo bằng **Cohen’s Kappa ≥ 0.70**.

Khoảng trống này được hỗ trợ bởi một khoảng trống phụ là **GAP-T — khoảng trống về công nghệ / nhiệm vụ**. Các mô hình ngôn ngữ lớn đã được dùng cho nhiều nhiệm vụ liên quan đến báo cáo lỗi như sinh nội dung, cải thiện báo cáo, replay/tái hiện lỗi, phát hiện trùng lặp, tóm tắt và sinh test case. Tuy nhiên, GPT-4o chưa được đánh giá trực tiếp như một công cụ tự động chấm chất lượng khả năng tái hiện lỗi, rồi so sánh với nhãn chuẩn từ đánh giá thủ công.

### 2.4 Động lực nghiên cứu

Nếu GPT-4o đạt mức đồng thuận ổn định với đánh giá thủ công, công cụ này có thể hỗ trợ lập trình viên và người phân loại lỗi bằng cách kiểm tra sơ bộ báo cáo lỗi, nhận diện những báo cáo còn thiếu thông tin để tái hiện, và giảm bớt công sức đánh giá thủ công. Nếu GPT-4o không đạt ngưỡng đồng thuận, kết quả vẫn có giá trị vì nó chỉ ra giới hạn của GPT-4o đối với nhiệm vụ cụ thể này trong kỹ thuật phần mềm.

---

## 3. Các nghiên cứu liên quan

### 3.1 Tổng quan các nhóm bằng chứng

| Nhóm bằng chứng | Paper chính | Đóng góp chính | Liên hệ với đề xuất này |
|---|---|---|---|
| Chất lượng và khả năng tái hiện của báo cáo lỗi | Zimmermann et al.; Chaparro et al. | Cho thấy lập trình viên cần các thông tin rõ ràng như các bước tái hiện lỗi, kết quả mong đợi, kết quả thực tế, stack trace, test case và môi trường/ngữ cảnh. | Hỗ trợ việc xây dựng rubric và giải thích vì sao chất lượng khả năng tái hiện lỗi là quan trọng. |
| Gán nhãn thủ công và người đánh giá | Islam / HumanAffect; các nghiên cứu dùng human annotation | Cho thấy người đánh giá và gán nhãn thủ công có thể được dùng để tạo dữ liệu chuẩn cho phân tích văn bản trong kỹ thuật phần mềm. | Hỗ trợ việc dùng đánh giá thủ công làm nhãn chuẩn để đánh giá GPT-4o. |
| Mô hình ngôn ngữ lớn / công cụ xử lý báo cáo lỗi | ReBL, AdbGPT, LIBRO, CUPID, Can LLMs Demystify Bug Reports?, các nghiên cứu LLM4SE liên quan | Cho thấy mô hình ngôn ngữ lớn hoặc công cụ tự động có thể tái hiện lỗi, replay lỗi, sinh test case, phân loại hoặc tìm báo cáo lỗi trùng lặp. | Hỗ trợ GAP-T vì các nhiệm vụ này có liên quan, nhưng không giống nhiệm vụ so sánh GPT-4o với đánh giá thủ công trong chấm chất lượng tái hiện lỗi. |
| Bằng chứng về thước đo đồng thuận | Cohen; Landis and Koch; HumanAffect; các nghiên cứu phân loại feedback bằng LLM | Hỗ trợ cách đo đồng thuận có tính đến yếu tố ngẫu nhiên và cách diễn giải mức đồng thuận đáng kể. | Hỗ trợ việc dùng Cohen’s Kappa ≥ 0.70 làm mục tiêu đánh giá trong thử nghiệm pilot. |

### 3.2 Chất lượng báo cáo lỗi và khả năng tái hiện lỗi

Zimmermann et al. nghiên cứu yếu tố làm nên một báo cáo lỗi tốt và chỉ ra rằng lập trình viên cần các thông tin cụ thể như các bước tái hiện lỗi, kết quả mong đợi, kết quả thực tế, stack trace, test case và môi trường/ngữ cảnh để hiểu và sửa lỗi hiệu quả [1]. Điều này trực tiếp hỗ trợ trọng tâm của đề tài: đánh giá các thông tin liên quan đến khả năng tái hiện lỗi.

Chaparro et al. đề xuất Euler để đánh giá chất lượng của các bước tái hiện lỗi trong báo cáo lỗi. Nghiên cứu này cho thấy chất lượng S2R là một vấn đề đã được quan tâm, và việc thiếu hoặc có S2R kém chất lượng có thể làm tăng công sức phân loại và xử lý lỗi thủ công [2]. Các nghiên cứu tập trung vào tái hiện lỗi Android như ReBL và AdbGPT cũng cho thấy tái hiện lỗi từ báo cáo lỗi là một nhiệm vụ thực tế nhưng khó [4], [5].

### 3.3 Gán nhãn thủ công và người đánh giá

Luận án HumanAffect của Islam dùng các bình luận issue trên JIRA và gán nhãn thủ công bởi người đánh giá để xây dựng bộ dữ liệu chuẩn cho phân tích văn bản trong kỹ thuật phần mềm [3]. Nghiên cứu này cũng bàn về mức đồng thuận giữa các người đánh giá và cách diễn giải dựa trên đa số. Dù paper này không giải quyết cùng nhiệm vụ với đề xuất của nhóm, nó vẫn hỗ trợ về mặt phương pháp: đánh giá thủ công có thể được dùng làm dữ liệu chuẩn để đánh giá một công cụ tự động trong lĩnh vực kỹ thuật phần mềm.

Đề xuất này áp dụng logic phương pháp tương tự: người đánh giá thủ công sẽ gán nhãn chất lượng khả năng tái hiện lỗi của báo cáo lỗi theo một rubric cố định; GPT-4o sẽ gán nhãn trên cùng các báo cáo lỗi đó bằng prompt cố định; sau đó mức đồng thuận giữa hai bên sẽ được đo bằng Cohen’s Kappa.

### 3.4 Các nghiên cứu dùng mô hình ngôn ngữ lớn và công cụ tự động cho báo cáo lỗi

| Nghiên cứu / công cụ | Đóng góp chính | Vì sao khoảng trống vẫn còn |
|---|---|---|
| ReBL | Dùng GPT-4 và tự động hóa giao diện để tái hiện toàn bộ báo cáo lỗi Android theo hướng có phản hồi. | Đây là nhiệm vụ tái hiện/replay lỗi, không phải đánh giá chất lượng tái hiện lỗi so với nhãn chuẩn thủ công. |
| AdbGPT | Dùng prompt cho mô hình ngôn ngữ lớn để replay lỗi Android từ báo cáo lỗi. | Tập trung vào replay lỗi và trích xuất S2R, không phải đánh giá chất lượng bằng thước đo đồng thuận. |
| LIBRO | Dùng mô hình ngôn ngữ lớn để sinh test có khả năng tái hiện lỗi từ báo cáo lỗi. | Đây là sinh test/tái hiện lỗi, không phải chấm chất lượng báo cáo lỗi bằng Cohen’s Kappa. |
| CUPID | Dùng ChatGPT để cải thiện phát hiện báo cáo lỗi trùng lặp. | Đây là phát hiện trùng lặp, không phải đánh giá chất lượng khả năng tái hiện lỗi. |
| Can LLMs Demystify Bug Reports? | Khảo sát liệu ChatGPT có thể hiểu và tái hiện lỗi được báo cáo hay không. | Tập trung vào hiểu/tái hiện lỗi, không phải so sánh mức đồng thuận giữa GPT-4o và đánh giá thủ công. |
| Các survey về LLM4SE | Tổng hợp các ứng dụng rộng của mô hình ngôn ngữ lớn trong kỹ thuật phần mềm và chỉ ra các thách thức đánh giá. | Phạm vi rộng, không tập trung vào nhiệm vụ cụ thể của đề tài là đánh giá chất lượng tái hiện lỗi bằng mức đồng thuận. |

Nhìn chung, tài liệu hiện có cho thấy có nhiều hoạt động nghiên cứu liên quan đến mô hình ngôn ngữ lớn cho các nhiệm vụ như sinh báo cáo lỗi, cải thiện báo cáo lỗi, replay lỗi, tái hiện lỗi, phát hiện trùng lặp, tóm tắt và xử lý issue. Tuy nhiên, các nghiên cứu này chưa trả lời trực tiếp câu hỏi: GPT-4o có thể chấm chất lượng khả năng tái hiện lỗi với mức đồng thuận đáng kể so với đánh giá thủ công hay không. Vì vậy, GAP-M và GAP-T của đề tài vẫn hợp lệ.

### 3.5 Hỗ trợ về thước đo và mức đồng thuận

Cohen’s Kappa phù hợp với đề tài này vì đầu ra là nhãn phân loại: cả GPT-4o và người đánh giá thủ công đều gán nhãn cho cùng một tập báo cáo lỗi [11]. Ngưỡng **0.70** được dùng như mục tiêu thực tế cho thử nghiệm pilot vì nó nằm trong khoảng thường được xem là mức đồng thuận đáng kể, tức **0.61 đến 0.80**, theo Landis and Koch [12].

Vì đây là pilot study với bộ dữ liệu nhỏ, kết quả sẽ được diễn giải một cách thận trọng. Nhóm sẽ báo cáo Cohen’s Kappa kèm **khoảng tin cậy bootstrap 95%**, thay vì khẳng định mạnh rằng GPT-4o đã đạt năng lực ngang con người ở quy mô lớn.

### 3.6 Bảng ánh xạ khoảng trống

| Loại khoảng trống | Tóm tắt bằng chứng | Trạng thái |
|---|---|---|
| GAP-M: Khoảng trống về cách đánh giá / thước đo | Chưa có paper đã review nào trực tiếp dùng Cohen’s Kappa ≥ 0.70 làm tiêu chí chính để so sánh đánh giá chất lượng tái hiện lỗi của GPT-4o với nhãn chuẩn thủ công. | Khoảng trống chính đã xác nhận |
| GAP-T: Khoảng trống về công nghệ / nhiệm vụ | LLM/công cụ đã được dùng cho sinh nội dung, cải thiện, tái hiện, replay, phát hiện trùng lặp, tóm tắt và xử lý issue, nhưng chưa làm đúng nhiệm vụ đánh giá này. | Khoảng trống phụ đã xác nhận |
| Hỗ trợ phương pháp | Gán nhãn thủ công và người đánh giá đã được dùng trong các nghiên cứu kỹ thuật phần mềm để tạo dữ liệu chuẩn cho việc đánh giá công cụ tự động. | Được hỗ trợ |

---

## 4. Câu hỏi nghiên cứu

### 4.1 Câu hỏi nghiên cứu chính

**RQ1:** GPT-4o có thể đánh giá chất lượng khả năng tái hiện lỗi của các báo cáo lỗi trên GitHub/Jira với mức đồng thuận đáng kể so với nhãn chuẩn từ đánh giá thủ công, đo bằng Cohen’s Kappa ≥ 0.70, hay không?

### 4.2 Loại claim

Đây là **claim về mức đồng thuận với con người**. Nghiên cứu không khẳng định GPT-4o thay thế lập trình viên. Nghiên cứu chỉ kiểm tra xem trong một thử nghiệm pilot có kiểm soát, GPT-4o có đạt mức đồng thuận đáng kể với đánh giá thủ công hay không.

### 4.3 Giả thuyết nghiên cứu

- **H0:** Mức đồng thuận giữa GPT-4o và nhãn chuẩn từ đánh giá thủ công thấp hơn mức đồng thuận đáng kể: **κ < 0.70**.
- **H1:** Mức đồng thuận giữa GPT-4o và nhãn chuẩn từ đánh giá thủ công đạt mức đồng thuận đáng kể: **κ ≥ 0.70**.

### 4.4 Thước đo và ngưỡng đánh giá

| Mục | Giá trị |
|---|---|
| Thước đo chính | Cohen’s Kappa |
| Ngưỡng đánh giá | κ ≥ 0.70 |
| Cách diễn giải | Vì bộ dữ liệu nhỏ, ngưỡng này chỉ được xem là bằng chứng ở mức pilot, không phải xác nhận chắc chắn ở quy mô lớn. |

---

## 5. Quy trình thử nghiệm

### 5.1 Tổng quan pipeline

1. Thu thập báo cáo lỗi trên GitHub/Jira từ các dự án mã nguồn mở.
2. Làm sạch và chuẩn bị nội dung báo cáo lỗi, đồng thời giữ lại các trường quan trọng cho việc tái hiện lỗi.
3. Xây dựng rubric để đánh giá chất lượng khả năng tái hiện lỗi.
4. Yêu cầu người đánh giá thủ công gán nhãn độc lập cho từng báo cáo lỗi.
5. Đo mức đồng thuận giữa các người đánh giá thủ công trước khi chốt nhãn chuẩn.
6. Giải quyết các trường hợp bất đồng bằng biểu quyết đa số hoặc thảo luận, rồi tạo nhãn chuẩn thủ công cuối cùng.
7. Chạy GPT-4o trên cùng tập báo cáo lỗi bằng prompt cố định.
8. So sánh nhãn của GPT-4o với nhãn chuẩn thủ công bằng Cohen’s Kappa.
9. Báo cáo Cohen’s Kappa, khoảng tin cậy bootstrap 95%, các lỗi đánh giá và các hạn chế của nghiên cứu.

### 5.2 Bộ dữ liệu

- **Nguồn:** Báo cáo lỗi GitHub/Jira từ các dự án mã nguồn mở.
- **Quy mô dữ liệu:** bộ dữ liệu pilot khoảng **10-30 báo cáo lỗi**. Nếu thời gian và nguồn lực cho phép, nhóm có thể mở rộng thêm.
- **Cách chọn mẫu:** chọn các báo cáo lỗi có đủ thông tin văn bản để đánh giá, ví dụ như tiêu đề, mô tả, bình luận, metadata của issue hoặc ngữ cảnh liên quan đến việc tái hiện lỗi.

| Trường dữ liệu | Mô tả |
|---|---|
| issue_id | Mã định danh hoặc đường dẫn của báo cáo lỗi. |
| project | Tên dự án trên GitHub/Jira. |
| title | Tiêu đề báo cáo lỗi. |
| description | Nội dung chính do người dùng/người kiểm thử gửi. |
| comments | Các bình luận liên quan nếu có thông tin giúp tái hiện lỗi. |
| metadata/context | Phiên bản, hệ điều hành, trình duyệt, thiết bị, cấu hình, log, stack trace hoặc ảnh chụp màn hình nếu có. |
| label_manual | Nhãn chuẩn cuối cùng từ đánh giá thủ công. |
| label_gpt4o | Nhãn do GPT-4o dự đoán. |
| notes | Ghi chú của người đánh giá hoặc lý do bất đồng nếu có. |

### 5.3 Rubric đánh giá thủ công

| Tiêu chí | Đủ thông tin | Thiếu thông tin |
|---|---|---|
| Các bước tái hiện lỗi | Có các bước/hành động rõ ràng để người đánh giá có thể thử tái hiện lỗi. | Không có bước tái hiện, hoặc các bước quá mơ hồ để làm theo. |
| Hành vi thực tế | Mô tả rõ lỗi hoặc hành vi sai đã xảy ra. | Không giải thích rõ chuyện gì đã xảy ra. |
| Hành vi mong đợi | Mô tả rõ hệ thống lẽ ra phải hoạt động như thế nào. | Thiếu hoặc không rõ kết quả mong đợi. |
| Môi trường / ngữ cảnh | Có thông tin hữu ích như phiên bản, hệ điều hành, trình duyệt, thiết bị, cấu hình, ngữ cảnh dự án hoặc dependency. | Không có môi trường/ngữ cảnh, hoặc quá chung chung nên không giúp tái hiện lỗi. |
| Bằng chứng hỗ trợ | Có log, ảnh chụp màn hình, stack trace, thông báo lỗi hoặc bằng chứng khác khi cần. | Không có bằng chứng hỗ trợ dù báo cáo lỗi khó hiểu hoặc khó tái hiện. |
| Độ rõ ràng / đầy đủ | Báo cáo dễ hiểu và có đủ chi tiết để thử tái hiện lỗi. | Báo cáo mơ hồ, thiếu thông tin hoặc khó diễn giải. |

### 5.4 Quy tắc gán nhãn

| Nhãn | Ý nghĩa |
|---|---|
| 1 | Đủ thông tin để tái hiện lỗi |
| 0 | Không đủ thông tin để tái hiện lỗi |

Một báo cáo lỗi được gán **nhãn 1** nếu nó mô tả rõ hành vi thực tế đã xảy ra và có ít nhất hai yếu tố hỗ trợ việc tái hiện lỗi, ví dụ như các bước tái hiện, hành vi mong đợi, môi trường/ngữ cảnh, log, ảnh chụp màn hình, stack trace hoặc thông báo lỗi.

Một báo cáo lỗi được gán **nhãn 0** nếu thông tin bị thiếu, chưa đầy đủ, mơ hồ hoặc quá chung chung khiến người đánh giá khó thực hiện một lần thử tái hiện lỗi hợp lý.

### 5.5 Nhãn chuẩn thủ công và mức đồng thuận giữa người đánh giá

Trong pilot, nhóm sử dụng **ít nhất hai người đánh giá thủ công chính là Ngô Trần Quân và Phạm Minh Quân**. Hai người này sẽ gán nhãn độc lập cho cùng một bộ 10–30 báo cáo lỗi dựa trên rubric đã chốt. Việc để hai người đánh giá độc lập giúp nhóm kiểm tra xem nhãn chuẩn thủ công có đủ ổn định trước khi đem so sánh với GPT-4o hay không.

Trước khi tạo nhãn chuẩn cuối cùng, nhóm sẽ đo mức đồng thuận giữa hai người đánh giá bằng **Cohen’s Kappa**. Nếu mức đồng thuận giữa người với người thấp, nhóm sẽ thảo luận các trường hợp chưa rõ, làm rõ lại rubric và chỉnh cách gán nhãn trước khi chốt bộ dữ liệu.

Sau khi hai người đánh giá hoàn tất, các trường hợp bất đồng sẽ được giải quyết bằng thảo luận theo rubric để tạo **nhãn chuẩn thủ công cuối cùng**. Nếu nhóm không mời được lập trình viên chuyên nghiệp, nhóm sẽ dùng người đánh giá đã được hướng dẫn theo rubric và ghi rõ đây là một hạn chế của nghiên cứu.

### 5.6 Cấu hình GPT-4o và kiểm soát prompt

| Mục cấu hình | Quyết định |
|---|---|
| Mô hình | GPT-4o. Nhóm sẽ ghi lại đúng phiên bản/ngày chạy trước khi thử nghiệm. |
| Temperature | 0 hoặc mức thấp nhất có thể để kết quả ổn định hơn. |
| Cách dùng prompt | Phân loại zero-shot dựa trên rubric. Ví dụ few-shot chỉ được dùng nếu cố định trước khi chạy và không thay đổi sau khi xem kết quả. |
| Định dạng đầu ra | JSON hoặc dạng phân loại cố định, chỉ gồm nhãn dự đoán và một lý do ngắn. |
| Kiểm soát khả năng lặp lại | Nhóm sẽ lưu nguyên văn prompt template trong thư mục experiment. Prompt gồm rubric, nội dung báo cáo lỗi và định dạng đầu ra yêu cầu. Prompt không được đổi sau khi đã xem kết quả. |

### 5.7 Kế hoạch phân tích thống kê

Phân tích chính sẽ báo cáo Cohen’s Kappa giữa nhãn của GPT-4o và nhãn chuẩn thủ công cuối cùng.

Nhóm cũng sẽ báo cáo **khoảng tin cậy bootstrap 95%** cho Cohen’s Kappa. Cụ thể, nhóm sẽ lấy mẫu lại bộ báo cáo lỗi đã gán nhãn **1.000 lần**, tính Cohen’s Kappa cho mỗi lần lấy mẫu lại, rồi báo cáo hai mốc **2,5% và 97,5%** làm khoảng tin cậy.

Vì đây là pilot study, khoảng tin cậy sẽ được dùng để diễn giải mức độ không chắc chắn và độ ổn định của kết quả đồng thuận. Kết quả pilot được xem là có hỗ trợ nếu Cohen’s Kappa quan sát được **≥ 0.70**. Khoảng tin cậy được báo cáo nhằm tránh việc kết luận quá mạnh từ một bộ dữ liệu nhỏ.

---

## 6. Kế hoạch đánh giá

| Mục tiêu | Thước đo | Ngưỡng / mục tiêu | Cách diễn giải |
|---|---|---|---|
| RQ1 | Cohen’s Kappa giữa GPT-4o và nhãn chuẩn thủ công | κ ≥ 0.70 | GPT-4o đạt mức đồng thuận đáng kể ở mức pilot với đánh giá thủ công. |
| Đồng thuận giữa người đánh giá | Cohen’s Kappa giữa các người đánh giá thủ công | Nên đạt mức từ vừa phải đến đáng kể trước khi chốt nhãn cuối | Nhãn chuẩn thủ công đủ đáng tin để dùng làm cơ sở so sánh. |
| Độ không chắc chắn | Khoảng tin cậy bootstrap 95% | Không dùng như điều kiện đạt/rớt cứng trong pilot | Cho thấy kết quả đồng thuận của pilot ổn định đến đâu. |

Các trường hợp diễn giải kết quả:

1. **Kết quả pilot tích cực:** κ ≥ 0.70. GPT-4o có thể hữu ích như một công cụ hỗ trợ đánh giá chất lượng khả năng tái hiện lỗi trong bối cảnh thử nghiệm có kiểm soát.
2. **Kết quả pilot chưa chắc chắn:** κ gần hoặc trên 0.70 nhưng khoảng tin cậy rộng. Khi đó cần thêm dữ liệu, rubric rõ hơn hoặc prompt tốt hơn.
3. **Kết quả pilot âm:** κ < 0.70. GPT-4o chưa đủ đáng tin cho nhiệm vụ này trong thiết lập hiện tại.

Sau khi đã xem kết quả, nhóm không thay đổi thước đo, ngưỡng đánh giá hoặc câu hỏi nghiên cứu.

---

## 7. Các nguy cơ ảnh hưởng đến độ tin cậy

| Loại nguy cơ | Nguy cơ cụ thể | Cách giảm thiểu |
|---|---|---|
| Độ tin cậy nội tại | Người đánh giá thủ công có thể bị thiên kiến khi gán nhãn. | Dùng rubric rõ ràng, gán nhãn độc lập và kiểm tra mức đồng thuận giữa người đánh giá. |
| Độ tin cậy nội tại | Đầu ra của GPT-4o có thể thay đổi giữa các lần chạy hoặc do cập nhật mô hình. | Dùng prompt cố định, ghi lại phiên bản/ngày chạy của mô hình và đặt temperature thấp. |
| Khả năng khái quát | Bộ dữ liệu pilot có thể không đại diện cho mọi loại báo cáo lỗi GitHub/Jira. | Nếu khả thi, chọn báo cáo lỗi từ nhiều dự án và ghi rõ phạm vi dataset. |
| Độ phù hợp của khái niệm đo | Nhãn nhị phân có thể đơn giản hóa quá mức chất lượng khả năng tái hiện lỗi. | Định nghĩa rubric rõ ràng và lưu ghi chú cho các trường hợp ranh giới. |
| Độ tin cậy của kết luận | Cỡ mẫu nhỏ có thể làm Cohen’s Kappa không ổn định. | Báo cáo khoảng tin cậy bootstrap 95% và tránh kết luận quá mạnh. |
| Độ tin cậy của người đánh giá | Người đánh giá có thể không phải lập trình viên chuyên nghiệp. | Ghi rõ nền tảng của người đánh giá và xem đây là hạn chế của nghiên cứu. |
| Độ tin cậy của prompt | GPT-4o có thể nhạy với cách viết prompt. | Chốt prompt trước khi thử nghiệm và không thay đổi sau khi xem kết quả. |

---

## 8. Kế hoạch thời gian và tài nguyên

### 8.1 Phân công vai trò

Phần phân công được sắp xếp lại để khớp với nội dung thuyết trình của từng thành viên. Sau khi bảo vệ proposal, nếu giảng viên hỏi từng người thì mỗi thành viên sẽ trả lời đúng phần mình đã trình bày và đúng phần mình phụ trách trong thực nghiệm.

| Vai trò | Thành viên | Trách nhiệm cụ thể |
|---|---|---|
| **PL + MR1 — Project Lead / Manual Reviewer 1** | **Ngô Trần Quân** | Phụ trách mở đầu đề tài, vấn đề nghiên cứu và động lực nghiên cứu; điều phối tiến độ chung của nhóm; kiểm tra sự thống nhất giữa GAP, RQ, metric, threshold, proposal và slide; tham gia **test/gán nhãn thủ công** với vai trò manual reviewer 1 trên bộ 10–30 GitHub/Jira Bug Reports. |
| **EG + MR2 — Evidence & Gap Lead / Manual Reviewer 2** | **Phạm Minh Quân** | Phụ trách phần GAP-M, GAP-T và related work/evidence map; nắm các paper chính như Zimmermann 2010, Chaparro 2019, HumanAffect 2020, ReBL, AdbGPT, LIBRO, CUPID, Cohen 1960 và Landis & Koch 1977; tham gia **test/gán nhãn thủ công** với vai trò manual reviewer 2 trên cùng bộ dữ liệu để tính human-human agreement với Ngô Trần Quân. |
| **RQ + EP — Research Question & Experiment Protocol Lead** | **Nguyễn Ngọc Gia Thuận** | Phụ trách RQ, H0/H1, metric, threshold và experiment pipeline; đảm bảo RQ, metric và threshold không bị thay đổi sau khi proposal được duyệt; mô tả quy trình từ thu thập dữ liệu, làm sạch dữ liệu, thiết kế rubric, manual labeling, human-human agreement, chạy GPT-4o đến phân tích Cohen’s Kappa. |
| **DG + LR — Data, Rubric & LLM Runner** | **Đặng Đăng Khoa** | Phụ trách dataset, rubric, manual ground truth và cấu hình GPT-4o; thu thập 10–30 GitHub/Jira Bug Reports cho pilot; lọc bỏ issue trùng lặp, feature request hoặc issue không phải bug; chuẩn hóa các trường dữ liệu như title, description, comments và metadata/context; chuẩn bị prompt cố định, chạy GPT-4o và lưu model/date, temperature, prompt version, raw output và label dự đoán. |
| **MS + RW — Metrics, Threats & Report Writer** | **Nguyễn Minh Phúc** | Phụ trách evaluation plan, threats to validity, timeline và contribution; tính hoặc hỗ trợ tính Cohen’s Kappa giữa GPT-4o và nhãn chuẩn thủ công, Cohen’s Kappa giữa hai manual reviewers, confusion matrix và khoảng tin cậy bootstrap 95% với 1.000 lần resample; chỉnh sửa proposal, references, slide và đảm bảo nhóm không overclaim quá phạm vi pilot study. |

### 8.2 Timeline

| Tuần | Hoạt động | Đầu ra |
|---|---|---|
| Tuần 5-6 | Viết proposal và chuẩn bị tài nguyên. | Bản nháp proposal.md, bản nháp prompt template, bản nháp rubric. |
| Tuần 6 | Nộp và bảo vệ proposal. | `presentation/slides_proposal_defense.pptx`. |
| Tuần 7 | Gán nhãn bộ dữ liệu pilot và chạy GPT-4o. | `pilot_ground_truth.csv`, `pilot_llm_output.csv`. |
| Tuần 8 | Chỉnh quy trình và mở rộng dataset nếu khả thi. | Dataset cập nhật và prompt cuối cùng. |
| Tuần 9-10 | Phân tích kết quả và chuẩn bị báo cáo cuối. | Phân tích cuối, kết quả Kappa, khoảng tin cậy và bài trình bày cuối. |

### 8.3 Tài nguyên và phương án dự phòng

Các tài nguyên cần có gồm báo cáo lỗi GitHub/Jira, người đánh giá thủ công, quyền truy cập GPT-4o, công cụ bảng tính và công cụ phân tích thống kê như Python hoặc Excel.

Nếu dataset quá lớn, nhóm sẽ giảm số lượng mẫu và báo cáo rõ ràng. Nếu quyền truy cập GPT-4o/API bị giới hạn, nhóm sẽ chạy thử nghiệm trên bộ pilot nhỏ hơn. Nếu người đánh giá thủ công bất đồng nhiều, nhóm sẽ làm rõ rubric trước khi chốt nhãn. Nếu không mời được lập trình viên chuyên nghiệp, nhóm sẽ dùng người đánh giá đã được hướng dẫn và báo cáo đây là một hạn chế.

---

## 9. Tài liệu tham khảo

[1] T. Zimmermann, R. Premraj, N. Bettenburg, S. Just, A. Schroeter, and C. Weiss. 2010. *What Makes a Good Bug Report?* IEEE Transactions on Software Engineering, 36(5), 618-643.

[2] O. Chaparro, C. Bernal-Cardenas, J. Lu, K. Moran, A. Marcus, M. Di Penta, D. Poshyvanyk, and V. Ng. 2019. *Assessing the Quality of the Steps to Reproduce in Bug Reports.* ESEC/FSE 2019.

[3] M. R. Islam. 2020. *Analysis of Human Affect and Bug Patterns to Improve Software Quality and Security.* PhD Dissertation, University of New Orleans.

[4] D. Wang, Y. Zhao, S. Feng, Z. Zhang, W. G. J. Halfond, C. Chen, X. Sun, J. Shi, and T. Yu. 2024. *Feedback-Driven Automated Whole Bug Report Reproduction for Android Apps.* ISSTA 2024.

[5] S. Feng and C. Chen. 2024. *Prompting Is All You Need: Automated Android Bug Replay with Large Language Models.* ICSE 2024.

[6] S. Kang, J. Yoon, and S. Yoo. 2023. *Large Language Models are Few-shot Testers: Exploring LLM-Based General Bug Reproduction.*

[7] L. Plein and T. F. Bissyandé. 2023. *Can LLMs Demystify Bug Reports?*

[8] T. Zhang, I. C. Irsan, F. Thung, and D. Lo. 2024. *Cupid: Leveraging ChatGPT for More Accurate Duplicate Bug Report Detection.*

[9] X. Hou, Y. Zhao, Y. Liu, Z. Yang, K. Wang, L. Li, X. Luo, D. Lo, J. Grundy, and H. Wang. 2024. *Large Language Models for Software Engineering: A Systematic Literature Review.*

[10] A. Fan, B. Gokkaya, M. Harman, M. Lyubarskiy, S. Sengupta, S. Yoo, and J. M. Zhang. 2023. *Large Language Models for Software Engineering: Survey and Open Problems.*

[11] J. Cohen. 1960. *A Coefficient of Agreement for Nominal Scales.* Educational and Psychological Measurement, 20(1), 37-46.

[12] J. R. Landis and G. G. Koch. 1977. *The Measurement of Observer Agreement for Categorical Data.* Biometrics, 33(1), 159-174.

---

## Phụ lục A. Prompt template

Prompt dưới đây sẽ được chốt trước khi chạy thử nghiệm và được lưu trong thư mục experiment.

```text
Bạn đang đánh giá chất lượng khả năng tái hiện lỗi của một báo cáo lỗi phần mềm.

Hãy dùng rubric sau:
- Các bước tái hiện lỗi
- Hành vi thực tế
- Hành vi mong đợi
- Môi trường/ngữ cảnh
- Bằng chứng hỗ trợ
- Độ rõ ràng/đầy đủ

Hãy gán đúng một nhãn nhị phân:
1 = đủ thông tin để tái hiện lỗi
0 = không đủ thông tin để tái hiện lỗi

Chỉ gán nhãn 1 nếu báo cáo mô tả rõ hành vi thực tế và có ít nhất hai yếu tố hỗ trợ khả năng tái hiện lỗi, ví dụ như các bước tái hiện, hành vi mong đợi, môi trường/ngữ cảnh, log, ảnh chụp màn hình, stack trace hoặc thông báo lỗi.

Chỉ trả về JSON hợp lệ theo định dạng sau:
{
  "label": 0 hoặc 1,
  "justification": "lý do ngắn gọn"
}

Báo cáo lỗi:
Tiêu đề: [TITLE]
Mô tả: [DESCRIPTION]
Bình luận/ngữ cảnh: [COMMENTS_OR_CONTEXT]
```
