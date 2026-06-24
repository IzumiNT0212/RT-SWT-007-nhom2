# PRISMA Flow for SLR Screening

## Topic
LLM for Bug Report Quality Assessment

## Search and Deduplication
- Records from database searching: **N = 96**
- Records after duplicate removal: **N = 96**

## Round 1: Title and Abstract Screening
- Records screened by title and abstract: **N = 96**
- Records excluded in Round 1: **N = 54**
- Records kept for full-text screening: **N = 42**
  - INCLUDE: **N = 24**
  - UNSURE: **N = 18**

## Round 2: Full-text Screening
- Full-text assessed: **N = 42**
- Full-text excluded: **N = 27**

### Main exclusion reasons in Round 2
- Focuses on classification/detection/triage but not quality or reproducibility assessment: **N = 14**
- Focuses on testing/test generation but not bug report quality: **N = 3**
- LLM-based bug report quality assessment is not central or unclear: **N = 5**
- Only partially related after full-text screening: **N = 5**

## Final Included Papers
- Included in evidence table: **N = 15**

## Text Flowchart

```text
Records from database searching
(N = 96)
        |
        v
After duplicate removal
(N = 96)
        |
        v
Round 1: Title + Abstract screened
(N = 96)  ---->  Excluded (N = 54)
        |
        v
Round 2: Full-text assessed
(N = 42)  ---->  Excluded (N = 27)
        |
        v
Included in Evidence Table
(N = 15)
```
