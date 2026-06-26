# Search Log — Bug Report Quality Assessment with LLM

**Thành viên:** Nguyễn Ngọc Gia Thuận
**Ngày thực hiện:** 2026-05-31

---

## Chuỗi tìm kiếm (Query Strings)

### String A

**Query nguyên văn:**
"bug report" AND ("large language model" OR "LLM") AND ("reproducibility quality" OR "assess quality" OR "quality evaluation")

**Database:** Google Scholar
**Bộ lọc:** English, Software Engineering related papers
**Ngày search:** 2026-05-31
**Số kết quả:** 125 papers

---

### String B

**Query nguyên văn:**
("bug report" OR "GitHub issue") AND ("reproducibility" OR "steps to reproduce") AND ("developer review" OR "human evaluation" OR "manual assessment")

**Database:** Google Scholar
**Bộ lọc:** English, Software Engineering related papers
**Ngày search:** 2026-05-31
**Số kết quả:** 211 papers

---



## Tổng hợp trước dedup

| Database             | String   |  Kết quả |
| -------------------- | -------- | -------: |
| Google Scholar       | String A |      125 |
| Google Scholar       | String B |      211 |
| **Tổng trước dedup** |          | **336**  |
| **Sau dedup          |          | **56**   |
---

## Sau relevance filtering và dedup

| Mục                                                                 | Số lượng |
| ------------------------------------------------------------------- | -------: |
| Tổng kết quả ban đầu                                                |      336 |
| Records giữ lại sau manual relevance filtering và duplicate removal |       56 |
| Số bị loại do không liên quan / trùng lặp / không phù hợp           |      280 |

Các records được giữ lại được lưu trong file `01_all_records.csv`.

---

## Screening V1 — Title and Abstract Screening

| Mục                                   | Số lượng |
| ------------------------------------- | -------: |
| Records screened                      |       56 |
| Records excluded                      |       19 |
| Records passed to full-text screening |       37 |

Quyết định screening vòng 1 được lưu trong file `02_after_screening_v1.csv` với các cột `v1_decision` và `v1_reason`.

---

## Screening V2 — Full-text Screening

| Mục                       | Số lượng |
| ------------------------- | -------: |
| Full-text papers assessed |       37 |
| Full-text papers excluded |       24 |
| Final included studies    |       13 |

Quyết định screening vòng 2 được lưu trong file `03_final_included.csv` với các cột `v2_decision` và `v2_reason`.

---

## Phần S — Cross-reference Search / Snowballing

**Phương pháp:** Không thực hiện snowballing trong phần cá nhân này.

**Lý do:** Phần tìm kiếm cá nhân chỉ sử dụng database Google Scholar và 2 search strings. Snowballing có thể được thực hiện ở bước tổng hợp nhóm nếu cần mở rộng thêm tài liệu.

---

## Ghi chú

* Dedup và relevance filtering được thực hiện bằng Zotero / Tay / Excel.
* Các số liệu trong file này khớp với PRISMA flow:
  
  * 336 raw results
  * 56 records sau filtering và dedup
  * 19 records excluded ở V1
  * 37 full-text assessed
  * 24 full-text excluded
  * 13 final included studies
  
* Evidence table được xây dựng từ 13 studies cuối cùng.