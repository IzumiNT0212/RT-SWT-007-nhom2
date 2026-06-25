# Search Log — LLM Bug Report Reproducibility Quality

**Thành viên:** Phạm Minh Quân  
**Date:** 2026-05-31  
**Topic:** Evaluating the Reliability of Large Language Models in Assessing Bug Report Reproducibility Quality  
**Database chính:** CORE

---

## Chuỗi tìm kiếm (Query Strings)

### String A

**Query nguyên văn:**  
bug report GPT-4o reproducibility

**Database:** CORE  
**Bộ lọc:** English, software-engineering relevance, bug/defect/issue-report relevance  
**Ngày search:** 2026-05-31  
**Số kết quả:** 55 papers

---

### String B

**Query nguyên văn:**  
bug report ChatGPT quality assessment

**Database:** CORE  
**Bộ lọc:** English, software-engineering relevance, bug/defect/issue-report relevance  
**Ngày search:** 2026-05-31  
**Số kết quả:** 1137 papers

---

### String C

**Query nguyên văn:**  
defect report GPT-4o automated evaluation

**Database:** CORE  
**Bộ lọc:** English, software-engineering relevance, bug/defect/issue-report relevance  
**Ngày search:** 2026-05-31  
**Số kết quả:** 78 papers

---

### String D

**Query nguyên văn:**  
bug report quality assessment inter-rater agreement

**Database:** CORE  
**Bộ lọc:** English, software-engineering relevance, bug/defect/issue-report relevance  
**Ngày search:** 2026-05-31  
**Số kết quả:** 709 papers

---

## Tổng hợp trước dedup

| Database | String | Kết quả |
|---|---|---:|
| CORE | String A | 55 |
| CORE | String B | 1137 |
| CORE | String C | 78 |
| CORE | String D | 709 |
| **Tổng trước dedup** |  | **1979** |

---

## Pre-filtering audit trail

Phần pre-filtering được thực hiện trước khi đưa records vào `01_all_records.csv` để tránh giữ các kết quả quá rộng từ CORE. Các tiêu chí kiểm tra thủ công gồm:

- Giữ paper tiếng Anh.
- Giữ paper thuộc software engineering hoặc software maintenance/testing context.
- Ưu tiên paper có liên quan đến bug reports, defect reports, issue reports, bug reproduction, bug triage, duplicate bug reports, bug-report classification, hoặc bug-report quality.
- Ưu tiên paper có liên quan đến LLMs, ChatGPT, GPT, GPT-4/GPT-4o, hoặc AI/NLP-based evaluation.
- Loại các kết quả rõ ràng ngoài phạm vi như education-only, healthcare, ontology-only, smart contract-only, generic productivity, hoặc cybersecurity/vulnerability repair không có bug-report analysis.
- Loại record trùng lặp theo title hoặc nội dung paper.

| Stage | Count |
|---|---:|
| Raw CORE search results | 1979 |
| Removed during manual relevance filtering / duplicate removal | 1932 |
| Records retained in `01_all_records.csv` | 47 |

---

## Screening V1 — Title and Abstract Screening

| Mục | Số lượng |
|---|---:|
| Records screened in `02_after_screening_v1.csv` | 47 |
| Records excluded after title/abstract screening | 29 |
| Records passed to full-text screening | 18 |

Quyết định screening vòng 1 được lưu trong file `02_after_screening_v1.csv` với các cột `v1_decision` và `v1_reason`.

---

## Screening V2 — Full-text Screening

| Mục | Số lượng |
|---|---:|
| Full-text papers assessed in `03_final_included.csv` | 18 |
| Full-text papers excluded | 3 |
| Final included studies | 15 |

Quyết định screening vòng 2 được lưu trong file `03_final_included.csv` với các cột `v2_decision` và `v2_reason`.

---

## Phần S — Cross-reference Search / Snowballing

**Phương pháp:** Không thực hiện snowballing trong phần cá nhân này.

**Lý do:** Phần tìm kiếm cá nhân chỉ sử dụng CORE và 4 search strings chính. Snowballing có thể được thực hiện ở bước tổng hợp nhóm nếu nhóm cần mở rộng thêm tài liệu.

---

## Notes for Verification

- Dedup và relevance filtering được thực hiện thủ công bằng Excel.
- Cột `search_string` trong các file CSV dùng để truy vết paper về String A/B/C/D.
- Các số liệu trong file này khớp với PRISMA và CSV:
  - 1979 raw results
  - 47 records sau pre-filtering và dedup
  - 29 records excluded ở V1
  - 18 full-text assessed
  - 3 full-text excluded
  - 15 final included studies
- Evidence table được xây dựng từ 15 studies cuối cùng.
