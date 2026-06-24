# notes.md — RBL-4 Tuần 7 Pilot

## 1. Proposal approval

- Proposal đã được GV chốt: [x] Có / [ ] Chưa
- Ngày chốt proposal: 2026-06-xx
- Người xác nhận: GV môn SWT301 / RBL
- Ghi chú nếu có: GAP/RQ/metric/threshold đã được chốt trước khi chạy thử nghiệm. Sau khi xem dữ liệu/kết quả, nhóm không tự ý đổi RQ, metric hoặc threshold.

## 2. Random sampling

- Dataset nguồn: `data/raw/issues_raw.csv`
- Tổng số bug reports trong raw dataset: **N = 50**
- Pilot sample size: **n = 10**
- Tỷ lệ pilot: **20%**
- Random seed cố định: **3012026**
- Ngày tạo mẫu pilot: **2026-06-23**
- Cách chọn:
  - [x] Random bằng script Python từ `data/raw/issues_raw.csv`
  - [x] Không chọn theo cảm tính
  - [x] Không loại case khó nếu vẫn đúng tiêu chí bug report
  - [x] Sample được sort lại theo `issue_id` sau khi chọn để dễ đọc file

### Pilot sample được chọn

  - 1. GH010 — flutter/flutter — CONTEXT_LOST_WEBGL in Chrome in Linux
  - 2. GH011 — flutter/flutter — DVTDeviceOperation: Encountered a build number issue
  - 3. GH019 — vercel/next.js — bug: Client-side navigation freezes
  - 4. GH025 — vercel/next.js — ReactRemoveProperties does not work as it was
  - 5. GH030 — microsoft/vscode — Broken rendering when editor.scrollBeyondLastLine set to false
  - 6. GH032 — microsoft/vscode — v1.91 does not launch on Catalina or Big Sur due to fatal error
  - 7. GH033 — microsoft/vscode — VS Code update access denied error
  - 8. GH042 — angular/angular — Dynamically creating a component through ComponentFactory issue
  - 9. GH043 — angular/angular — Child component with FormGroup/FormControl issue
  - 10. GH049 — nodejs/node — Node does not completely uninstall itself on Windows

## 3. Dataset filtering rule

Loại khỏi pilot/full experiment nếu:

- Không phải bug report.
- Là feature request/enhancement thuần túy.
- Là question/support/documentation issue.
- Là duplicate issue.
- Không có textual description.
- Không có đủ dữ liệu để đánh giá khả năng tái hiện lỗi ở mức tối thiểu.

Lưu ý: File hiện tại là raw/candidate dataset. Trước khi gán nhãn thủ công, nhóm nên mở URL của từng issue trong `data/pilot_sample.csv` để copy issue body gốc nếu cần thêm chi tiết.

## 4. Manual ground truth plan

- File gán nhãn: `data/pilot_ground_truth.csv`
- Manual Reviewer 1: **Ngô Trần Quân**
- Manual Reviewer 2: **Phạm Minh Quân**
- Hai reviewer gán nhãn độc lập trước khi thảo luận.
- Nhãn dùng trong pilot:
  - `1` = bug report có đủ thông tin để thử tái hiện lỗi.
  - `0` = thông tin thiếu/mơ hồ khiến reviewer khó thử tái hiện lỗi.
- Sau khi hai reviewer gán nhãn, nhóm tính IAA bằng **Cohen's Kappa**.
- Nếu Kappa giữa hai reviewer thấp hơn 0.7, nhóm cần đọc lại rubric, thảo luận case bất đồng và ghi vào `disagreement_note`.

## 5. API / GPT-4o run log

- Model chính: **GPT-4o**
- Cách chạy: ChatGPT web thủ công nếu không có API credit.
- Temperature: `0` hoặc lowest stable setting nếu có thể kiểm soát.
- Prompt version: **v1.0**
- Prompt freeze date: 2026-06-xx
- Có thay đổi prompt sau khi xem kết quả không? [x] Không / [ ] Có amendment
- File lưu output: `results/pilot_llm_output.csv`
- Khi chạy GPT-4o, phải lưu:
  - ngày chạy;
  - model;
  - prompt version;
  - input issue;
  - raw output;
  - nhãn GPT-4o;
  - lý do ngắn của GPT-4o.

## 6. Budget note

Nhóm không có API credit, nên pilot có thể chạy thủ công trên giao diện ChatGPT/GPT-4o. Cách này vẫn phù hợp với pilot feasibility experiment nếu nhóm lưu lại prompt, ngày chạy, model, input và raw output đầy đủ.

## 7. Pilot decision checklist

| Check | Kết quả | Ghi chú |
|---|---|---|
| Dataset format đúng | Pass | `issues_raw.csv` có 50 dòng dữ liệu, đúng header |
| Pilot sample được chọn đúng | Pass | 10/50 reports = 20%, random seed = 3012026 |
| Manual annotation hoàn tất | Pending | Hai Quân sẽ gán nhãn trong `pilot_ground_truth.csv` |
| Human-human Kappa tính được | Pending | Tính sau khi có nhãn của 2 reviewer |
| GPT-4o output đúng format | Pending | Lưu vào `results/pilot_llm_output.csv` |
| GPT-vs-manual Kappa tính được | Pending | Tính sau khi có `final_manual_label` và `gpt4o_label` |
| Bootstrap CI tính được | Pending | 1,000 resamples nếu đủ dữ liệu |
| Có blocker kỹ thuật | Chưa thấy | Không dùng API, chạy thủ công bằng ChatGPT web |
