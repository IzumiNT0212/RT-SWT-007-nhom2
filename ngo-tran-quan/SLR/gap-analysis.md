# GAP Analysis — LLM for Bug Report Quality Assessment

**Evidence table:** `SLR/evidence-table.md`  
**Evidence table:** N = 15 papers  
**Date:** 2026-06-05  
**Topic:** LLM for Bug Report Quality Assessment  
**Refined RQ:** Can GPT-4o automatically assess the reproducibility quality of GitHub/Jira bug reports with substantial agreement compared to developer/manual review, measured by Cohen's Kappa >= 0.70?

---

## GAP Table

| Source column | Finding | GAP type | Refutation check |
|---|---|---|---|
| Tool/LLM | GPT-4o has not been directly validated as an automatic assessor of bug report reproducibility quality against developer/manual review. | GAP-T | ✅ Checked across 15 papers |
| Dataset | Prior studies use Bugzilla, Android, Mojira/Minecraft, crash reports, Signal GitHub reports, or duplicate-report datasets, but direct GitHub/Jira reproducibility-quality assessment with developer agreement is limited. | GAP-D | ✅ Checked across 15 papers |
| Metric | Prior work uses CTQRS, SBERT, ROUGE, F1, semantic similarity, reproduction success rate, accuracy, CodeBLEU, or hallucination rate, but not Cohen's Kappa >= 0.70 as the main LLM-vs-developer agreement metric. | GAP-M | ✅ Checked across 15 papers |
| Limitation / GAP | Many papers rely on domain-specific datasets, generation-focused evaluation, automatic metrics, or limited human/developer agreement. | GAP-S | ✅ Checked across 15 papers |

**Priority rule:** GAP-T > GAP-M > GAP-D > GAP-S  
**Selected emphasis:** GAP-M is selected as the primary gap because the missing validation metric directly determines whether the refined RQ can be answered. GAP-T is secondary because GPT-4o is the selected tool. GAP-D and GAP-S support the main gap.

---

## Primary GAP — GAP-M

**Claim:** Existing LLM-based bug report studies do not validate reproducibility-quality assessment using **Cohen's Kappa >= 0.70** as the main agreement threshold between LLM judgments and developer/manual review.

**Why this is the primary GAP:**  
The refined RQ is not only asking whether GPT-4o can assess bug report quality. It specifically asks whether GPT-4o can reach substantial agreement with developer/manual review. Therefore, the key missing element is an agreement-based validation metric.

---

## Secondary GAP — GAP-T

**Claim:** GPT-4o has been used in related LLM/software-engineering contexts, but it has not been directly validated as an automatic reproducibility-quality assessor for GitHub/Jira bug reports against developer/manual review.

**Why this is secondary:**  
The technology gap is important because the experiment focuses on GPT-4o. However, the main decision criterion of the experiment is still the agreement metric, so GAP-T supports GAP-M rather than replacing it.

---

## Supporting GAPs — GAP-D and GAP-S

### GAP-D — Dataset

Many reviewed studies use Bugzilla, Android, Mojira/Minecraft, crash reports, Signal GitHub reports, duplicate-report datasets, or summarization-specific datasets. Direct validation on GitHub/Jira bug reports for reproducibility-quality assessment remains limited.

### GAP-S — Shared limitation

Across the reviewed papers, common limitations include domain-specific datasets, generation-focused evaluation, reliance on automatic metrics, and limited direct comparison with developer/manual review.

---

## Detailed Check for Each Claim

| GAP claim | Already done in reviewed papers? | Decision | Notes |
|---|---|---|---|
| GAP-T: GPT-4o as a direct reproducibility-quality assessor | Partly related, but not directly done | Keep | ChatBR, AgentReport, ImproBR, BugScribe, ReBL, and crash-report studies focus on generation, improvement, reproduction, or support tasks, not direct GPT-4o quality-assessment agreement with developer review. |
| GAP-M: Cohen's Kappa >= 0.70 as the main LLM-vs-developer validation metric | Not directly done | Keep as primary | Some papers use Cohen's Kappa for annotation agreement or classification labels, but not as the main metric for GPT-4o vs developer/manual reproducibility-quality assessment. |
| GAP-D: GitHub/Jira bug reports as the target dataset | Partly addressed | Keep as supporting | Some studies use issue-tracking data or GitHub reports, but they usually target summarization, categorization, duplicate detection, or reproduction support rather than direct reproducibility-quality assessment. |
| GAP-S: repeated limitations around dataset specificity and automatic metrics | Present in reviewed papers | Keep as supporting | Repeated limitations strengthen the argument that a direct agreement-based evaluation is needed. |

**Result:** The main GAP is valid because no reviewed paper fully covers the combination of **GPT-4o + GitHub/Jira bug reports + reproducibility-quality assessment + developer/manual review + Cohen's Kappa >= 0.70**.


## Primary GAP Verification Matrix

| Criteria | Tool/LLM | Dataset | Metric | Human review | Final choice |
|---|---|---|---|---|---|
| GPT-4o as assessor | Directly relevant | Partly related | Partly related | Partly related | Keep as secondary GAP-T |
| GitHub/Jira reproducibility quality | Partly related | Directly relevant | Partly related | Partly related | Keep as supporting GAP-D |
| Cohen's Kappa >= 0.70 agreement | Partly related | Partly related | Directly relevant | Directly relevant | Keep as primary GAP-M |
| General automatic-metric limitation | Not sufficient alone | Partly related | Directly relevant | Not sufficient alone | Supporting only |

---

## Feasibility Check — Primary GAP

| Criterion | Check | Status |
|---|---|---|
| Dataset | GitHub issues are publicly available. Jira data can be collected from open-source projects if available; otherwise GitHub can be used as the main source. | ✅ SAFE |
| Tool/API | GPT-4o can be accessed through ChatGPT/API. If cost is an issue, the sample size can be reduced or GPT-4o mini can be used for pilot testing only. | ⚠️ NEEDS HANDLING |
| Compute | No model training is required; only prompting and agreement calculation are needed. | ✅ SAFE |
| Ground truth | Manual review can be performed by trained team members using a fixed rubric. If no professional developer is available, this must be reported as a threat to validity. | ⚠️ NEEDS HANDLING |
| Skills | The group needs issue sampling, rubric design, GPT-4o prompting, manual labeling, and Cohen's Kappa calculation. This is feasible using Google Sheets or Python. | ✅ SAFE |
| Time | The experiment is feasible if the sample size is controlled, for example 30-50 bug reports. | ✅ SAFE |
| Contribution | A negative result is still useful because Kappa < 0.70 would show that GPT-4o is not reliable enough as a standalone assessor. | ✅ SAFE |

**Feasibility result:** 0 BLOCKER, 2 NEEDS HANDLING, 5 SAFE  
**Decision:** The GAP is feasible if the mitigation plan is clearly written.

---

## Mitigation Plan

- Use a manageable sample size, such as 30-50 GitHub/Jira bug reports.
- Use a clear reproducibility-quality rubric based on Steps to Reproduce, Expected Behavior, and Actual/Observed Behavior.
- Use trained manual reviewers if professional developers are not available.
- Report the lack of professional developer review as a threat to validity if needed.
- Use GPT-4o for the main run and GPT-4o mini only for pilot testing if cost becomes a problem.

---

## Final GAP Statement

Although prior studies show that LLMs can support bug report generation, improvement, reproduction, summarization, categorization, duplicate detection, hallucination detection, and crash-report enhancement, the reviewed evidence does not show whether **GPT-4o** can directly assess the **reproducibility quality** of **GitHub/Jira bug reports** with substantial agreement compared to developer/manual review.

The primary research gap is the lack of agreement-based validation for LLM-based bug report reproducibility-quality assessment, especially using **Cohen's Kappa >= 0.70** as the success threshold.

---

## Design Implication

The experiment should evaluate GPT-4o as a reproducibility-quality assessor on GitHub/Jira bug reports, compare GPT-4o labels with developer/manual review labels, and calculate Cohen's Kappa. The experiment is feasible if the sample size is controlled and the manual-review rubric is clearly defined.
