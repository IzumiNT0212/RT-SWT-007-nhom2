Paper (Tên + Năm + Venue) | URL | Tool/LLM | Dataset | Metric | Kết quả | Hạn chế tự nêu



\[ID 1] A Comparative Study of Contemporary Learning Paradigms in Bug Report Priority Detection (2024) - IEEE Access | https://ieeexplore.ieee.org/abstract/document/10654280/ | BERT, Contrastive BERT, OpenChat và RAG+OpenChat | Bộ dữ liệu Mozilla Core gồm 40.565 báo cáo lỗi | Precision, Recall, F1-Score | Contrastive BERT đạt hiệu năng tốt nhất, vượt BERT, OpenChat và RAG+OpenChat trong bài toán phân loại mức độ ưu tiên của báo cáo lỗi; F1-score cao nhất đạt 78,85% trên lớp ưu tiên P3 | Dữ liệu bị mất cân bằng nghiêm trọng, đặc biệt ở các lớp P4 và P5 có ít mẫu. Ngoài ra, báo cáo lỗi thường chứa nhiều mã nguồn (code snippets), nhật ký lỗi (error logs) và nội dung kỹ thuật phức tạp, làm tăng độ khó của bài toán phân loại mức độ ưu tiên.



\[ID 6] A Multi-Agent RAG Architecture with DPO Fine-Tuning for Automated Bug Report Generation (2025) - SSRN | https://papers.ssrn.com/sol3/papers.cfm?abstract\_id=5887029 | Qwen2.5-7B-Instruct kết hợp LoRA, DPO và kiến trúc Multi-Agent RAG | Bộ dữ liệu Bugzilla gồm 3.966 cặp dữ liệu summary – ground truth bug report | CTQRS, ROUGE-1 Recall, SBERT | Mô hình DPO đạt 81,1% CTQRS, 73,2% ROUGE-1 Recall và 85,0% SBERT. Khi kết hợp DPO với RAG (1-shot), CTQRS tăng lên 83,2% và ROUGE-1 Recall đạt 82,2%, vượt mô hình SFT baseline và GPT-4o trong một số tiêu chí đánh giá chất lượng báo cáo lỗi | Nghiên cứu chỉ được đánh giá trên dữ liệu Bugzilla; khả năng tổng quát hóa sang GitHub Issues, Jira và các hệ sinh thái quản lý lỗi khác vẫn chưa được kiểm chứng.



\[ID 14] Advancing Bug Report Management: Graph-Based Modeling, Large Language Models, and Quality Improvement (2025) - University of Calgary Thesis | https://ucalgary.scholaris.ca/items/817eadb0-c905-4fea-ba30-24afde9fe1da | GraphSAGE, GAT, Fine-tuned BERT; các mô hình LLM được fine-tune gồm Llama 3, Llama 3.2, Mistral 7B, Qwen2.5-7B và Phi-3.5 | Bộ dữ liệu Mozilla Bugzilla với khoảng 500.000 báo cáo lỗi; BugsRepo gồm 119.586 báo cáo lỗi, 19.351 thông tin cộng tác viên và 12.614 báo cáo lỗi có cấu trúc | Precision, Recall, F1-score, BLEU, ROUGE, METEOR, CTQRS, SBERT, Human Evaluation | Mô hình GraphSAGE kết hợp GAT cho kết quả dự đoán mức độ ưu tiên (priority) và mức độ nghiêm trọng (severity) của lỗi tốt hơn mô hình Fine-tuned BERT. Các mô hình LLM mã nguồn mở sau khi fine-tune đạt hiệu năng tương đương GPT-4o trong việc tạo báo cáo lỗi có cấu trúc; các báo cáo do AI tạo ra được đánh giá cao hơn một chút về độ rõ ràng và tính đầy đủ so với báo cáo do con người viết | Nghiên cứu chủ yếu được đánh giá trên dữ liệu Mozilla Bugzilla; khả năng tổng quát hóa sang các hệ thống quản lý lỗi khác và môi trường công nghiệp thực tế vẫn cần được kiểm chứng thêm.



\[ID 15] Advancing intrinsic and non-intrinsic bug classification with NLP, machine learning, and few-shot prompt engineering (2024) - UBC Thesis | https://open.library.ubc.ca/soa/cIRcle/collections/ubctheses/24/items/1.0444146 | TF-IDF, seBERT, SVM, Random Forest, KNN, Decision Tree, GPT-3.5-turbo (Few-Shot Prompt Engineering) | OpenStack dataset gồm 1.880 bug reports (1.120 intrinsic bugs và 760 non-intrinsic bugs) | Precision, Recall, F1-score, AUC-ROC | Phương pháp Few-Shot Prompt Engineering sử dụng GPT-3.5-turbo đạt F1-score 73% và AUC-ROC 62,58% trong bài toán phân loại intrinsic và non-intrinsic bugs, cho kết quả cạnh tranh với các mô hình ML truyền thống dù sử dụng ít dữ liệu huấn luyện hơn. | Kết quả phụ thuộc đáng kể vào cách thiết kế prompt; những thay đổi nhỏ trong prompt có thể dẫn đến đầu ra khác nhau. Ngoài ra, LLM có nguy cơ sinh ra thông tin không chính xác (hallucination), ảnh hưởng đến độ tin cậy của kết quả.



\[ID 16] Advancing LLM-Based Issue Report Classification with Explained Few-Shot Learning, Intent Extraction, Ensemble, and Summarization (2026) - ACM TOSEM | https://dl.acm.org/doi/10.1145/3815577 | GPT-4o, GPT-3.5-turbo, Qwen-2.5-32B | 1.4 million issue reports | Precision, Recall, F1-score (Micro/Macro), Consistency Metrics, Perplexity Analysis | Các phương pháp đề xuất vượt các baseline hiện tại với mức cải thiện khoảng 5–8% F1-score; GPT-4o đạt hiệu năng tốt nhất và phương pháp Ensemble giúp tăng độ ổn định phân loại. | Ensemble không phải lúc nào cũng sửa lỗi mà đôi khi còn củng cố các sai lệch hệ thống giữa các mô hình; đồng thời làm tăng chi phí suy luận và độ phức tạp triển khai.



\[ID 21] AgentReport: A Multi-Agent LLM Approach for Automated and Reproducible Bug Report Generation (2025) – Applied Sciences | https://www.mdpi.com/2076-3417/15/22/11931 | Qwen2.5-7B-Instruct + QLoRA-4bit | Dataset gồm 3.966 Bugzilla summary–report pairs được lọc từ khoảng 15.000 bug reports; 200 mẫu được kiểm tra thủ công | CTQRS, ROUGE-1 Recall, ROUGE-1 F1, SBERT | AgentReport đạt CTQRS 80,5%, ROUGE-1 Recall 84,6%, ROUGE-1 F1 56,8%, SBERT 86,4%; vượt Baseline về độ đầy đủ cấu trúc, độ phủ từ khóa và tính nhất quán ngữ nghĩa | Chỉ đánh giá trên dữ liệu Bugzilla; chưa kiểm chứng trên GitHub/Jira; Human Evaluation: N/A.



\[ID 27] Amalgamation of Classical and Large Language Models for Duplicate Bug Detection: A Comparative Study. (2025) - CMC | https://www.techscience.com/cmc/v83n1/60067 | TF-IDF, Word2Vec, GloVe, SBERT, OpenAI Embeddings, Voyage AI và các mô hình Amalgamated | Bộ dữ liệu Bugzilla gồm khoảng 914.000 báo cáo lỗi từ ba dự án mã nguồn mở Apache, Eclipse và KDE. | Recall Rate@k (RR@k), Mean Average Precision (MAP), Mean Reciprocal Rank (MRR) | Các mô hình kết hợp OpenAI + Voyage AI và SBERT + Voyage AI đạt hiệu năng tốt nhất, với Recall Rate dao động khoảng 68%–74%, đồng thời vượt các phương pháp riêng lẻ về MAP và MRR. | Hiệu năng suy luận của các phương pháp dựa trên LLM giảm khi quy mô dữ liệu tăng; cần các kỹ thuật tối ưu như quantization, pruning hoặc mô hình nhẹ hơn để cải thiện khả năng mở rộng.



\[ID 31] Magis: Llm-based multi-agent framework for github issue resolution (2024) - NeurIPS | https://proceedings.neurips.cc/paper\_files/paper/2024/hash/5d1f02132ef51602adf07000ca5b6138-Abstract-Conference.html | GPT-4 (base model), GPT-3.5, Claude-2, SWE-Llama 7B, SWE-Llama 13B | SWE-bench gồm 2.294 GitHub Issues thực tế từ 12 repository Python phổ biến; thí nghiệm sử dụng tập con 25% của SWE-bench. | Applied Ratio, Resolved Ratio | MAGIS đạt Resolved Ratio 13.94%, cao gấp khoảng 8 lần GPT-4 (1.74%) và hơn 2 lần Claude-2 (4.88%), thiết lập trạng thái SOTA trên SWE-bench tại thời điểm công bố. | Hiệu quả giảm đối với các issue yêu cầu sửa đổi nhiều file hoặc nhiều function; việc định vị chính xác file và dòng mã cần thay đổi trong repository lớn vẫn là thách thức do giới hạn ngữ cảnh của LLM.



\[ID 36] Next-Generation bug reporting: enhancing development with AI automation (2025) - Preprints | https://www.preprints.org/manuscript/202410.2106 | LLMs, Machine Learning, NLP (không nêu model cụ thể) | N/A | N/A | N/A | Phụ thuộc mạnh vào chất lượng dữ liệu lịch sử và gặp thách thức khi tích hợp với nhiều testing framework và bug tracking system khác nhau.



\[ID 45] Past, Present, and Future of Bug Tracking in the Generative AI Era (2026) – ACM TOSEM | https://dl.acm.org/doi/10.1145/3806655 | LLMs, AI Agents, GPT, Gemini, Llama (khảo sát và đề xuất framework) | Survey \& Vision Paper (không thực hiện thực nghiệm mới) | N/A | Đề xuất AI-Powered Bug Tracking Framework tích hợp LLM Agents để hỗ trợ bug reporting, reproduction, classification, assignment, localization, repair và verification trong toàn bộ vòng đời bug tracking. | Chưa có đánh giá thực nghiệm quy mô lớn; tồn tại các thách thức về độ tin cậy của LLM, hallucination, quyền riêng tư, accountability và tích hợp với quy trình hiện có.



\[ID 49] Preliminary Evaluation of a Guided Usability Defect Report Form (2018) – IEEE ASWEC | https://nzjohng.github.io/publications/papers/aswec2018\_2.pdf | Guided Usability Defect Report Form | 10 báo cáo lỗi khả dụng của Firefox for iOS được đánh giá bởi 3 chuyên gia phần mềm | Điểm chất lượng (0–11), Informative, Accuracy, Claim \& Rationale, Impact, Fleiss Kappa | Biểu mẫu báo cáo có hướng dẫn giúp nâng cao chất lượng báo cáo lỗi thông qua việc cải thiện độ rõ ràng, tính đầy đủ và khả năng mô tả các bước tái hiện lỗi. | Quy mô thực nghiệm nhỏ, chỉ đánh giá trên một dự án phần mềm và chưa có sự tham gia của người dùng cuối.



\[ID 51] Progressive Code Integration for Abstractive Bug Report Summarization (2025) – arXiv | https://arxiv.org/abs/2512.00325 | Kỹ thuật Progressive Code Integration, Prompt Engineering và LoRA Fine-Tuning trên các mô hình CodeLlama, LLaMA-3.1, Mistral, Phi-3, Gemma, Qwen3, DeepSeek Coder và GPT-3.5 Turbo | Các bộ dữ liệu Defects4J, SDS, ADS và Fang et al.'s Corpus chứa báo cáo lỗi kèm các đoạn mã nguồn liên quan | BERTScore (Precision, Recall, F1), ROUGE-1, ROUGE-2, ROUGE-L | Kỹ thuật tích hợp mã nguồn theo từng bước (Progressive Code Integration) giúp cải thiện đáng kể chất lượng tóm tắt báo cáo lỗi và vượt các phương pháp tóm tắt trích xuất (extractive baselines) từ 7,5% đến 58,2%; cấu hình GPT-3.5 Turbo kết hợp mã nguồn và few-shot prompting đạt BERTScore F1 = 0,9003. | Số lượng bộ dữ liệu đa phương thức (bug report kết hợp mã nguồn) còn hạn chế; quá trình chia nhỏ và tóm tắt mã nguồn có thể làm mất thông tin quan trọng; chưa có đánh giá trực tiếp từ chuyên gia hoặc người dùng thực tế.



\[ID 55] RCEGen: A Generative Approach for Automated Root Cause Analysis Using Large Language Models (LLMs) (2025) – Software | https://www.mdpi.com/2674-113X/4/4/29 | Qwen2.5-Coder-32B-Instruct, DeepSeek-Coder-33B-Instruct, Codestral-22B, CodeLlama-34B-Instruct và OpenCoder-8B-Instruct (được đánh giá bởi GPT-4o và DeepSeek-V3) | 298 báo cáo lỗi được chọn lọc từ bộ dữ liệu của Hirsch và cộng sự sau khi loại bỏ các báo cáo quá dài | Correctness, Clarity, Depth of Reasoning, Overall Score, CodeBERTScore, ROUGE-L | Qwen2.5-Coder-32B-Instruct đạt hiệu năng tốt nhất với Correctness khoảng 0,89 và Overall Score khoảng 0,79. Các giải thích nguyên nhân gốc do mô hình sinh ra có độ tương đồng ngữ nghĩa rất cao với phân tích của lập trình viên, đạt CodeBERTScore khoảng 0,989. | Hiệu quả suy giảm khi báo cáo lỗi thiếu các bước tái hiện (reproduction steps), stack trace, log hệ thống hoặc mô tả rõ ràng về hành vi mong đợi và hành vi thực tế; khả năng suy luận nguyên nhân gốc vẫn còn hạn chế dù độ chính xác tổng thể cao.

