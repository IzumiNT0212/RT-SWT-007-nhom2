# Gap Statement — LLM for Bug Report Quality Assessment

Evidence table: N = 15 papers

## Topic
LLM for Bug Report Quality Assessment

## RQ Context
For bug reports from GitHub/Jira, can an LLM automatically assess bug report quality based on reproducibility criteria compared with developer manual review, achieving Cohen's Kappa >= 0.70?

## Detected Research Gaps

### GAP-T (Technology): LLM-based reproducibility quality assessment

**Description:**  
Several reviewed papers applied LLMs to bug report generation, improvement, reproduction, summarization, duplicate detection, categorization, hallucination detection, and crash-report enhancement. However, no reviewed paper directly evaluates GPT-4o as an automatic assessor of bug report reproducibility quality against developer/manual review.

**Evidence:**  
Evidence table — Tool/LLM column: ChatGPT, GPT-4, GPT-4o, GPT-4o mini, Qwen 2.5, Mistral, Llama 3.2, LLaMA-3, Gemini, BERT, T5, ReBL, ChatBR, AgentReport, ImproBR, BugScribe, Cupid, and other LLM-based approaches were used. These tools mainly focus on generation, improvement, classification, reproduction, summarization, duplicate detection, or hallucination detection rather than direct quality assessment compared with developer review.

### GAP-M (Metric): Agreement-based validation using Cohen's Kappa

**Description:**  
Most reviewed papers use automatic metrics such as CTQRS, SBERT, ROUGE, semantic similarity, executable S2R rate, reproduction success rate, Top-1 localization, CodeBLEU, hallucination rate, precision, recall, and F1-score. Some papers use agreement or Cohen's Kappa in related contexts, such as annotation agreement or categorization agreement. However, no reviewed paper uses Cohen's Kappa >= 0.70 as the main validation metric for agreement between LLM-based bug report quality assessment and developer/manual review.

**Evidence:**  
Evidence table — Metric column: no included paper directly reports Cohen's Kappa >= 0.70 for LLM-vs-developer agreement in bug report reproducibility quality assessment.

### GAP-D (Dataset): GitHub/Jira bug reports and reproducibility quality

**Description:**  
The reviewed papers often use domain-specific datasets such as Android apps, Mojira/Minecraft, Mozilla Bugzilla, crash reports, Signal GitHub reports, or curated duplicate-report datasets. There is still limited evidence on whether GPT-4o can assess the reproducibility quality of GitHub/Jira bug reports in a way that agrees with developer/manual reviewers.

**Evidence:**  
Evidence table — Dataset column: datasets are mostly Android, Mojira/Minecraft, Mozilla/Bugzilla, crash reports, Signal GitHub reports, or specific duplicate-report datasets. None directly evaluates GitHub/Jira reproducibility quality assessment with developer agreement as the main target.

## Overall GAP Statement

Although prior studies show that LLMs can support bug report generation, improvement, reproduction, summarization, classification, categorization, duplicate detection, hallucination detection, and crash-report enhancement, there is still insufficient evidence that an LLM can directly assess the reproducibility quality of GitHub/Jira bug reports with substantial agreement compared to developer manual review.

The main research gap is the lack of agreement-based validation for LLM-based bug report reproducibility quality assessment, especially using Cohen's Kappa >= 0.70 as the success threshold.

## Contribution

This study addresses the gap by evaluating whether GPT-4o can automatically assess the reproducibility quality of GitHub/Jira bug reports and achieve substantial agreement with developer manual review, measured by Cohen's Kappa >= 0.70.

## Refined RQ

Can GPT-4o automatically assess the reproducibility quality of bug reports from GitHub/Jira with substantial agreement compared to developer manual review, measured by Cohen's Kappa >= 0.70?
