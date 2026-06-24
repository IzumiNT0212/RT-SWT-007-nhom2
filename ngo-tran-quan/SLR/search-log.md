# Search Log — LLM for Bug Report Quality Assessment

**Student / Member:** Ngo Tran Quan  
**Topic:** LLM for Bug Report Quality Assessment  
**Date:** 2026-06-02  
**RQ after refinement:** Can GPT-4o automatically assess the reproducibility quality of GitHub/Jira bug reports with substantial agreement compared to developer manual review, measured by Cohen’s Kappa ≥ 0.70?

---

## 1. Search Databases Used

The search was conducted using academic databases and supporting tools listed below.

| Database / Source | Purpose |
|---|---|
| Semantic Scholar | Main academic search database for LLM + bug report papers |
| arXiv | Open-access preprints and downloadable PDFs |
| CORE | Additional open-access academic records |
| ResearchGate | Cross-checking metadata and locating full-text PDFs when available |
| Google Scholar + Unpaywall Extension | Cross-checking DOI/PDF availability and finding legal open-access versions |

---

## 2. Search Strings

Only two main query strings were used for the SLR search. String A was used for broad recall, while String B was used to cover the comparison/agreement part of PICO.

### String A — Broad Search: LLM + Bug Report Quality / Assessment

**Raw query:**

```text
("large language model" OR "LLM" OR "GPT" OR "ChatGPT")
AND ("bug report" OR "issue report")
AND ("quality" OR "assessment" OR "reproducibility" OR "steps to reproduce")
```

**PICO trace:**

| PICO Element | Keywords represented in String A |
|---|---|
| P | bug report, issue report |
| I | large language model, LLM, GPT, ChatGPT |
| O | quality, assessment, reproducibility, steps to reproduce |

**Note about C:** String A was intentionally broad, so it mainly covers P + I + O. The comparison element (C) was searched explicitly in String B.

**Databases searched:** Semantic Scholar, arXiv, CORE, Google Scholar  
**Filters:** English; Software Engineering / Computer Science; 2018 onward when filter was available; PDF preferred but not required at this stage.  
**Purpose:** Find papers directly related to LLM-based bug report quality assessment or reproducibility-related evaluation.

---

### String B — Comparison / Agreement Search: LLM + Bug Report + Manual Review

**Raw query:**

```text
("ChatGPT" OR "GPT-4" OR "GPT-4o" OR "large language model" OR "LLM")
AND ("bug report" OR "issue report")
AND ("developer review" OR "manual review" OR "human review" OR "expert review" OR "manual assessment" OR "Cohen's Kappa" OR agreement)
```

**PICO trace:**

| PICO Element | Keywords represented in String B |
|---|---|
| P | bug report, issue report |
| I | ChatGPT, GPT-4, GPT-4o, large language model, LLM |
| C | developer review, manual review, human review, expert review, manual assessment |
| O / Agreement metric | Cohen's Kappa, agreement |

**Databases searched:** Semantic Scholar, arXiv, ResearchGate, Google Scholar  
**Filters:** English; 2018 onward when available; PDF/open-access preferred.  
**Purpose:** Find papers that compare LLM outputs or assessments with human/developer/manual review or report agreement metrics. This string directly covers the C element of PICO.

---

### Overall PICO Coverage Across Search Strings

The search strategy does not require every individual string to contain all PICO elements. Instead, the two strings together cover the full PICO.

| PICO Element | Covered by |
|---|---|
| P — Population | String A and String B: bug report / issue report |
| I — Intervention | String A and String B: LLM / GPT / ChatGPT / GPT-4o |
| C — Comparison | String B: developer review / manual review / human review / expert review / manual assessment |
| O — Outcome | String A: quality, assessment, reproducibility, steps to reproduce; String B: Cohen's Kappa / agreement |

**Search strategy note:** String A was used to collect broad evidence about LLM-based bug report quality and reproducibility. String B was used to check whether prior work compared LLM judgments with developer/manual review or used agreement metrics such as Cohen's Kappa. This matches the refined PICO and RQ.

---

## 3. Search Result Summary Before Deduplication

The raw result counts in some databases were very large, especially in Semantic Scholar and Google Scholar. Therefore, only relevant records were captured/exported into the SLR record file for screening.

| Database / Source | Search approach used | Records captured for screening |
|---|---|---:|
| Semantic Scholar | String A + String B | 35 |
| arXiv | String A + String B | 20 |
| CORE | String A and related open-access checking | 9 |
| ResearchGate | String B + PDF/full-text checking | 12 |
| Google Scholar + Unpaywall | Cross-checking, citation lookup, and PDF availability checking | 20 |
| **Total before deduplication** |  | **96** |

**Note:** The 96 records are the records actually captured for screening, not the total raw search-result counts shown by databases.

---

## 4. Deduplication Method

**Tool used:** Zotero + manual checking in Google Sheets / CSV  
**Deduplication key:** Title, DOI, and very similar title strings  
**Deduplication result:**

| Stage | Number of records |
|---|---:|
| Records before deduplication | 96 |
| Duplicate records removed | 0 |
| Records after deduplication | 96 |

**Output file:** `SLR/01_all_records.csv`

---

## 5. PRISMA Screening Summary

| Screening Stage | Number of records |
|---|---:|
| Records after duplicate removal | 96 |
| Title + abstract screened | 96 |
| Excluded after V1 screening | 54 |
| Kept for full-text screening | 42 |
| Full-text assessed | 42 |
| Excluded after V2 screening | 27 |
| Final included papers | 15 |

**Output files:**

```text
SLR/02_after_screening_v1.csv
SLR/03_final_included.csv
SLR/prisma-flow.md
```

---

## 6. PDF Availability Log for Final Included Papers

According to the submission rule, only papers that pass V2 screening and appear in `03_final_included.csv` need to be stored in `SLR/papers/`. The following 15 papers have available PDFs and were included.

| # | Paper | PDF status | Saved PDF filename |
|---:|---|---|---|
| 1 | Automatic Generation of Bug Reports Using Large Language Models: An Evaluation in a Software Institute | Available | `Chaves_2025_AutomaticGenerationBugReports.pdf` |
| 2 | Exploring Fine-Grained Bug Report Categorization with Large Language Models and Prompt Engineering | Available | `Koyuncu_2026_FineGrainedBugReportCategorization.pdf` |
| 3 | ChatBR: Automated Assessment and Improvement of Bug Report Quality Using ChatGPT | Available | `Bo_2024_ChatBR.pdf` |
| 4 | Can We Enhance Bug Report Quality Using LLMs? | Available | `Acharya_2025_BugReportQualityLLMs.pdf` |
| 5 | Feedback-Driven Automated Whole Bug Report Reproduction for Android Apps | Available | `Wang_2024_ReBL.pdf` |
| 6 | AgentReport: A Multi-Agent LLM Approach for Automated and Reproducible Bug Report Generation | Available | `Choi_2025_AgentReport.pdf` |
| 7 | Crash Report Enhancement with Large Language Models: An Empirical Study | Available | `Fahim_2025_CrashReportEnhancement.pdf` |
| 8 | Empirical Analysis and Detection of Hallucinations in LLM-Generated Bug Report Summaries | Available | `Nirujan_2026_HallucinationsBugReportSummaries.pdf` |
| 9 | ImproBR: Bug Report Improver Using LLMs | Available | `Akyol_2026_ImproBR.pdf` |
| 10 | CTQRS-Based Reinforcement Learning Framework for Reliable Bug Report Generation Using Open-Source LLMs | Available | `Yang_2025_CTQRS_RL_BugReportGeneration.pdf` |
| 11 | Automated Generation of High-Quality Bug Reports for Android Applications | Available | `Saha_2026_BugScribe.pdf` |
| 12 | LLMs as Evaluators: A Novel Approach to Evaluate Bug Report Summarization | Available | `Kumar_2024_LLMsAsEvaluators.pdf` |
| 13 | CUPID: Leveraging ChatGPT for More Accurate Duplicate Bug Report Detection | Available | `Zhang_2024_CUPID.pdf` |
| 14 | Graph Neural Network vs. Large Language Model: A Comparative Analysis for Bug Report Priority and Severity Prediction | Available | `Acharya_2024_GNN_vs_LLM_BugReportPrediction.pdf` |
| 15 | Advancing Bug Report Management: Graph-Based Modeling, Large Language Models, and Quality Improvement | Available | `Acharya_2025_AdvancingBugReportManagement.pdf` |

---

## 7. Paywalled / Locked Papers Found During Search

Some relevant papers were found during database searching, but they were **not kept in the final included list** because the full-text PDF was not freely accessible. These papers were excluded during **V2 full-text screening** using **EC2: full-text/PDF not available**.

| Paper | Status | Action taken |
|---|---|---|
| Multi-dimensional Assessment of Crowdsourced Testing Reports via LLMs | Full-text PDF not freely accessible / access limited | Excluded in V2 using EC2 |
| KnowBug: Enhancing Large Language Models with Bug Report Knowledge for Deep Learning Framework Bug Prediction | ScienceDirect access/paywall; no open PDF found | Excluded in V2 using EC2 |

**Rule applied:** If a paper does not have an accessible PDF after checking Semantic Scholar, arXiv, CORE, ResearchGate, Google Scholar, and Unpaywall, it is recorded here and excluded from the final included list instead of leaving an empty PDF file in `SLR/papers/`.

**Note:** These two papers are **not included** in `03_final_included.csv`. They were replaced by accessible papers that passed V2 screening and have PDFs stored in `SLR/papers/`.

---

## 8. Cross-reference / Snowballing Notes

Snowballing was used only after the main database search. It was used to check references and discover closely related works from the included papers.

| Snowballing item | Note |
|---|---|
| Backward snowballing | Checked references from included papers such as ChatBR, ReBL, Can We Enhance Bug Report Quality Using LLMs?, and AgentReport |
| Forward/cross-reference checking | Used Google Scholar, Semantic Scholar, and ResearchGate to confirm newer related papers |
| PDF checking | Used arXiv, Semantic Scholar PDF buttons, publisher pages, ResearchGate, and Unpaywall |
| Final action | Only accessible full-text papers were kept in final included list |

---

## 9. Notes for Verification

- The final evidence table uses only papers with accessible PDFs.
- The final included list contains 15 papers, which matches the PRISMA flow.
- All quantitative values used in the evidence table were checked from the uploaded PDFs or paper abstracts/results sections.
- Papers without accessible full text were not kept in the final evidence table.
- The search strategy traces all PICO elements: P, I, and O are covered by String A, while C and agreement-related terms are covered by String B.
- The main GAP is that existing studies use LLMs for generation, improvement, reproduction, summarization, duplicate detection, categorization, and hallucination detection, but do not directly validate LLM-based reproducibility quality assessment against developer manual review using Cohen’s Kappa ≥ 0.70.
