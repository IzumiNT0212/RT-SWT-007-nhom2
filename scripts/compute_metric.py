# -*- coding: utf-8 -*-
"""
RBL-4 Tuần 7 — Phân tích pilot.
Script này tính:
- Cohen’s Kappa giữa hai reviewer thủ công nếu có nhãn MR1/MR2
- Cohen’s Kappa giữa GPT-4o và nhãn chuẩn thủ công
- Confusion matrix
- Khoảng tin cậy bootstrap 95% với 1.000 lần resample
- Histogram bootstrap
- Báo cáo metric dạng Markdown
"""

import os
from pathlib import Path
import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import cohen_kappa_score, confusion_matrix

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

RANDOM_SEED = 3012026
N_BOOTSTRAP = 1000
TARGET_THRESHOLD = 0.70

# Ưu tiên cấu trúc thư mục project, nhưng vẫn cho phép chạy khi để file ngang thư mục.
gt_path = Path("data/pilot_ground_truth.csv")
if not gt_path.exists():
    gt_path = Path("pilot_ground_truth.csv")

llm_path = Path("results/pilot_llm_output.csv")
if not llm_path.exists():
    llm_path = Path("pilot_llm_output.csv")

figures_dir = Path("figures")
figures_dir.mkdir(exist_ok=True)
results_dir = Path("results")
results_dir.mkdir(exist_ok=True)

if not gt_path.exists():
    raise FileNotFoundError("Không tìm thấy data/pilot_ground_truth.csv hoặc pilot_ground_truth.csv")
if not llm_path.exists():
    raise FileNotFoundError("Không tìm thấy results/pilot_llm_output.csv hoặc pilot_llm_output.csv")

# 1. Đọc dữ liệu
df_gt = pd.read_csv(gt_path)
df_llm = pd.read_csv(llm_path)

required_gt = {"issue_id", "final_label"}
required_llm = {"issue_id", "label_gpt4o"}
missing_gt = required_gt - set(df_gt.columns)
missing_llm = required_llm - set(df_llm.columns)
if missing_gt:
    raise ValueError(f"Ground truth file missing columns: {sorted(missing_gt)}")
if missing_llm:
    raise ValueError(f"LLM output file missing columns: {sorted(missing_llm)}")

# 2. Gộp dữ liệu
df = pd.merge(df_gt, df_llm, on="issue_id", how="inner", suffixes=("_gt", "_llm"))
df = df.dropna(subset=["final_label", "label_gpt4o"]).copy()
df["final_label"] = df["final_label"].astype(int)
df["label_gpt4o"] = df["label_gpt4o"].astype(int)

# 3. Tính mức đồng thuận giữa hai reviewer thủ công nếu có dữ liệu
human_kappa = None
if {"label_mr1", "label_mr2"}.issubset(df_gt.columns):
    human_df = df_gt.dropna(subset=["label_mr1", "label_mr2"]).copy()
    human_df["label_mr1"] = human_df["label_mr1"].astype(int)
    human_df["label_mr2"] = human_df["label_mr2"].astype(int)
    if len(human_df) > 0:
        human_kappa = cohen_kappa_score(human_df["label_mr1"], human_df["label_mr2"])

# 4. Tính mức đồng thuận giữa GPT-4o và nhãn chuẩn thủ công cuối cùng
kappa = cohen_kappa_score(df["final_label"], df["label_gpt4o"])
cm = confusion_matrix(df["final_label"], df["label_gpt4o"], labels=[0, 1])

print(f"Số dòng được phân tích: {len(df)}")
if human_kappa is not None:
    print(f"Human-human Cohen’s Kappa: {human_kappa:.3f}")
print(f"Cohen’s Kappa giữa GPT-4o và nhãn thủ công: {kappa:.3f}")
print("Confusion matrix, dòng = nhãn thủ công [0,1], cột = nhãn GPT-4o [0,1]:")
print(cm)

# 5. Tính bootstrap 95% CI
rng = np.random.default_rng(RANDOM_SEED)
kappas = []
manual = df["final_label"].to_numpy()
gpt = df["label_gpt4o"].to_numpy()

for _ in range(N_BOOTSTRAP):
    idx = rng.integers(0, len(df), len(df))
    sample_manual = manual[idx]
    sample_gpt = gpt[idx]
    # Kappa có thể không xác định nếu bootstrap sample chỉ có một class ở một trong hai bên gán nhãn.
    if len(np.unique(sample_manual)) > 1 and len(np.unique(sample_gpt)) > 1:
        kappas.append(cohen_kappa_score(sample_manual, sample_gpt))

if kappas:
    lower, upper = np.percentile(kappas, [2.5, 97.5])
    print(f"Bootstrap 95% CI: [{lower:.3f}, {upper:.3f}]")
else:
    lower = upper = np.nan
    print("Không tính được Bootstrap 95% CI vì tất cả bootstrap sample hợp lệ chỉ có một class.")

# 6. Lưu histogram
hist_path = figures_dir / "bootstrap_histogram.png"
plt.figure(figsize=(8, 5))
if kappas:
    plt.hist(kappas, bins=20, edgecolor="black", alpha=0.7)
plt.axvline(x=TARGET_THRESHOLD, color="red", linestyle="--", linewidth=2, label="Ngưỡng mục tiêu (0.70)")
plt.axvline(x=kappa, color="green", linestyle="-", linewidth=2, label=f"Kappa đạt được ({kappa:.2f})")
plt.title("Phân phối bootstrap của Cohen’s Kappa")
plt.xlabel("Cohen’s Kappa")
plt.ylabel("Tần suất")
plt.legend()
plt.tight_layout()
plt.savefig(hist_path, dpi=150)
print(f"Đã lưu biểu đồ tại: {hist_path}")

# 7. Disagreement table
df["agreement"] = (df["final_label"] == df["label_gpt4o"]).astype(int)
disagree_cols = [c for c in ["issue_id", "url", "title", "final_label", "label_gpt4o", "reason_mr1", "reason_mr2", "justification"] if c in df.columns]
disagreements = df[df["agreement"] == 0][disagree_cols]
disagree_path = results_dir / "pilot_disagreements.csv"
disagreements.to_csv(disagree_path, index=False, encoding="utf-8")

# 8. Markdown report
report_path = results_dir / "pilot_metric_report.md"
manual_counts = df["final_label"].value_counts().sort_index().to_dict()
gpt_counts = df["label_gpt4o"].value_counts().sort_index().to_dict()

human_kappa_text = f"{human_kappa:.3f}" if human_kappa is not None else "N/A"

report = f"""# Báo cáo metric pilot RBL-4 Tuần 7

## File đầu vào

- Nhãn chuẩn thủ công: `{gt_path.as_posix()}`
- Output GPT-4o: `{llm_path.as_posix()}`

## Cấu hình

- Metric: Cohen’s Kappa
- Ngưỡng mục tiêu: {TARGET_THRESHOLD:.2f}
- Số lần bootstrap resample: {N_BOOTSTRAP}
- Random seed: {RANDOM_SEED}

## Kết quả

- Số dòng được phân tích: {len(df)}
- Human-human Cohen’s Kappa: {human_kappa_text}
- Cohen’s Kappa giữa GPT-4o và nhãn thủ công: {kappa:.3f}
- Bootstrap 95% CI: [{lower:.3f}, {upper:.3f}]

## Phân phối nhãn

- Nhãn thủ công cuối cùng: {manual_counts}
- Nhãn GPT-4o: {gpt_counts}

## Confusion matrix

Dòng = nhãn thủ công cuối cùng `[0, 1]`; cột = nhãn GPT-4o `[0, 1]`.

```text
{cm}
```

## Diễn giải cho pilot Tuần 7

Pipeline pilot đã tạo được nhãn thủ công, nhãn GPT-4o, Cohen’s Kappa, khoảng tin cậy bootstrap và histogram. Kappa quan sát được chỉ được diễn giải như bằng chứng ở mức pilot. Nhóm không thay đổi RQ, metric hoặc threshold đã được duyệt sau khi xem kết quả.

Nếu Kappa thấp, hành động phù hợp trước full experiment Tuần 8 là kiểm tra các case bất đồng, chất lượng input và độ rõ của rubric, sau đó ghi lại trong `notes.md`. Không thay đổi ngưỡng thành công chỉ để làm kết quả đẹp hơn.

## File đầu ra

- Histogram: `{hist_path.as_posix()}`
- Các case bất đồng: `{disagree_path.as_posix()}`
"""
report_path.write_text(report, encoding="utf-8")
print(f"Đã lưu báo cáo tại: {report_path}")
