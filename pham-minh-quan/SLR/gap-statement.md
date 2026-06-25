# Gap Statement — LLM-Based Bug Report Reproducibility Quality Assessment

**Evidence table size:** N = 15 included studies.

## Topic

LLM-Based Bug Report Reproducibility Quality Assessment

## Research Context

The reviewed studies demonstrate that Large Language Models (LLMs) are increasingly used in software engineering tasks involving bug reports. Existing research covers bug reproduction, duplicate bug report detection, bug prioritization, user-feedback categorization, test generation, software maintenance, and other related activities.

However, the evidence extracted from the reviewed papers reveals several unresolved research gaps.

---

## Identified Research Gaps

### GAP-T — Technology Gap

**Description**

Several reviewed studies applied LLMs to bug reproduction, duplicate detection, bug prioritization, software testing, user-feedback categorization, and software engineering automation. However, none of the reviewed studies directly evaluates GPT-4o as an automated assessor of bug report reproducibility quality compared with developer manual review.

**Evidence**

Evidence Table — Tool/LLM Column

The reviewed studies employ ChatGPT, GPT-4, GPT-4o, ReBL, Cupid, LIBRO, BERT-based models, and other LLM-based approaches. These models are mainly used for reproduction, classification, prioritization, duplicate detection, or software engineering support tasks rather than direct reproducibility-quality assessment.

---

### GAP-M — Metric Gap

**Description**

Most reviewed studies evaluate performance using task-specific metrics such as reproduction success rate, Recall@K, precision, recall, F1-score, accuracy, executability rate, ranking metrics, or classification metrics.

Although some studies mention agreement measures in related contexts, none of the reviewed papers evaluates LLM-based bug report reproducibility quality assessment using Cohen’s Kappa as the primary agreement metric between LLM judgments and developer manual review.

**Evidence**

Evidence Table — Metric Column

The extracted metrics include reproduction rate, Recall@10, precision, recall, F1-score, accuracy, and executability measures. No reviewed paper directly reports Cohen’s Kappa ≥ 0.70 for agreement between GPT-4o assessment and developer manual review of bug report reproducibility quality.

---

### GAP-D — Dataset and Evaluation Gap

**Description**

The reviewed studies commonly use specialized datasets such as Android bug reports, Defects4J, duplicate-report datasets, deep-learning compiler issues, game feedback datasets, and other benchmark repositories.

There is limited evidence regarding GitHub and Jira bug reports evaluated specifically for reproducibility quality using an agreement-based evaluation framework.

**Evidence**

Evidence Table — Dataset Column

Most reviewed datasets originate from Android applications, Defects4J, TVM/OpenVINO issues, game-feedback datasets, or duplicate-report benchmarks. None of the reviewed studies directly evaluates GitHub/Jira bug report reproducibility quality using developer agreement as the primary evaluation target.

---

## Overall Gap Statement

Although prior studies demonstrate that LLMs can reproduce bugs, detect duplicate reports, classify user feedback, prioritize bug reports, and support various software engineering activities, there is still insufficient evidence that GPT-4o can directly assess bug report reproducibility quality with substantial agreement compared to developer manual review.

More specifically, no reviewed study directly evaluates GPT-4o-based reproducibility-quality assessment using Cohen’s Kappa ≥ 0.70 as the primary success criterion.

---

## Contribution

This study addresses the identified gaps by evaluating whether GPT-4o can automatically assess the reproducibility quality of GitHub/Jira bug reports and achieve substantial agreement with developer manual review, measured using Cohen’s Kappa.

---

## Refined Research Question

Can GPT-4o automatically assess the reproducibility quality of bug reports from GitHub and Jira with substantial agreement compared to developer manual review, achieving Cohen’s Kappa ≥ 0.70?
