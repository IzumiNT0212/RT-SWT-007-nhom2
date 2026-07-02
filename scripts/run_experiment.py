# -*- coding: utf-8 -*-
"""
RBL-4 Tuần 7 — Batch-run GPT-4o trên pilot qua endpoint tương thích Azure AI / Azure OpenAI.

QUAN TRỌNG:
- Không hardcode API key trong file này.
- Thiết lập thông tin xác thực bằng biến môi trường trước khi chạy.
- Model/deployment phải là GPT-4o hoặc tên deployment GPT-4o của nhóm trên Azure.

Windows CMD example:
    set AZURE_AI_API_KEY=your_key_here
    set AZURE_AI_BASE_URL=https://models.inference.ai.azure.com
    set AZURE_AI_MODEL=gpt-4o
    python run_experiment.py

PowerShell example:
    $env:AZURE_AI_API_KEY="your_key_here"
    $env:AZURE_AI_BASE_URL="https://models.inference.ai.azure.com"
    $env:AZURE_AI_MODEL="gpt-4o"
    python run_experiment.py
"""

import os
import json
import time
import re
from pathlib import Path

import pandas as pd
from openai import OpenAI

# -----------------------------
# Cấu hình
# -----------------------------
BASE_URL = os.getenv("AZURE_AI_BASE_URL") or os.getenv("AZURE_OPENAI_BASE_URL") or "https://models.inference.ai.azure.com"
API_KEY = os.getenv("AZURE_AI_API_KEY") or os.getenv("AZURE_OPENAI_API_KEY")
MODEL_NAME = os.getenv("AZURE_AI_MODEL") or os.getenv("AZURE_OPENAI_DEPLOYMENT") or "gpt-4o"
TEMPERATURE = 0
PROMPT_VERSION = "v1"

if not API_KEY:
    raise RuntimeError(
        "Missing API key. Set AZURE_AI_API_KEY or AZURE_OPENAI_API_KEY as an environment variable. "
        "Do not put the key directly in this Python file."
    )

client = OpenAI(base_url=BASE_URL, api_key=API_KEY)

# Ưu tiên cấu trúc thư mục project, nhưng vẫn cho phép chạy khi để file ngang thư mục.
input_path = Path("data/pilot_sample.csv")
if not input_path.exists():
    input_path = Path("pilot_sample.csv")

results_dir = Path("results")
results_dir.mkdir(exist_ok=True)
output_path = results_dir / "pilot_llm_output.csv"
log_path = results_dir / "pilot_api_log.txt"

if not input_path.exists():
    raise FileNotFoundError("Không tìm thấy data/pilot_sample.csv hoặc pilot_sample.csv")

# -----------------------------
# Prompt cố định theo proposal
# -----------------------------
PROMPT_TEMPLATE = """You are assessing the reproducibility quality of a software bug report.

Use the following rubric:
- Steps to reproduce
- Actual behavior
- Expected behavior
- Environment/context
- Supporting evidence
- Clarity/completeness

Assign exactly one binary label:
1 = enough information to reproduce the bug
0 = not enough information to reproduce the bug

Only assign label 1 if the report clearly describes the actual behavior and has at least two supporting elements for reproducibility, such as steps to reproduce, expected behavior, environment/context, logs, screenshots, stack traces, or error messages.

Return only valid JSON in the following format:
{{
  "label": 0 or 1,
  "justification": "brief justification"
}}

Bug report:
Title: {title}
Description: {description}
Comments/context: {comments_context}
"""

# -----------------------------
# Hàm hỗ trợ
# -----------------------------
def clean_json_content(content: str) -> str:
    content = (content or "").strip()
    content = re.sub(r"^```json", "", content, flags=re.IGNORECASE).strip()
    content = re.sub(r"^```", "", content).strip()
    content = re.sub(r"```$", "", content).strip()
    return content


def write_log_header_if_needed(log_file_obj):
    if log_path.exists() and log_path.stat().st_size > 0:
        return
    header = (
        "# Log API pilot\n"
        "Provider: Azure AI / endpoint tương thích Azure OpenAI\n"
        f"Base URL: {BASE_URL}\n"
        f"Model / deployment: {MODEL_NAME}\n"
        f"Temperature: {TEMPERATURE}\n"
        f"Phiên bản prompt: {PROMPT_VERSION}\n"
        f"File input: {input_path.as_posix()}\n"
        f"File output: {output_path.as_posix()}\n"
        "Ghi chú: API key được đọc từ biến môi trường và không được lưu trong repository này.\n\n"
        "## Bản ghi từng lần chạy\n"
    )
    log_file_obj.write(header)
    log_file_obj.flush()

# -----------------------------
# Chạy chính
# -----------------------------
df = pd.read_csv(input_path)
required_columns = {"issue_id", "title", "description"}
missing = required_columns - set(df.columns)
if missing:
    raise ValueError(f"pilot_sample.csv thiếu các cột bắt buộc: {sorted(missing)}")

output_results = []
print("Bắt đầu chạy Azure AI GPT-4o để đánh giá các bug report trong pilot...")

with open(log_path, "a", encoding="utf-8") as log_file:
    write_log_header_if_needed(log_file)

    for _, row in df.iterrows():
        issue_id = row["issue_id"]
        title = str(row.get("title", ""))
        description = str(row.get("description", ""))
        comments = str(row.get("comments", ""))
        metadata_context = str(row.get("metadata_context", ""))
        comments_context = f"Comments: {comments} | Context: {metadata_context}"

        prompt = PROMPT_TEMPLATE.format(
            title=title,
            description=description,
            comments_context=comments_context,
        )

        content = ""
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": "You are a helpful software engineering assistant."},
                    {"role": "user", "content": prompt},
                ],
                temperature=TEMPERATURE,
                response_format={"type": "json_object"},
            )

            content = response.choices[0].message.content or ""
            result_json = json.loads(clean_json_content(content))
            label_gpt4o = result_json.get("label")
            justification = result_json.get("justification", "")

            # Validate label
            if label_gpt4o not in [0, 1, "0", "1"]:
                raise ValueError(f"Invalid label from model: {label_gpt4o}")
            label_gpt4o = int(label_gpt4o)

            usage = getattr(response, "usage", None)
            prompt_tokens = getattr(usage, "prompt_tokens", "NA") if usage else "NA"
            completion_tokens = getattr(usage, "completion_tokens", "NA") if usage else "NA"
            returned_model = getattr(response, "model", MODEL_NAME)

            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(
                f"[{timestamp}] ID: {issue_id} | Provider: Azure AI | Model: {returned_model} | "
                f"Prompt Tokens: {prompt_tokens} | Completion Tokens: {completion_tokens} | Status: OK\n"
            )
            log_file.flush()

            print(f"Xử lý thành công {issue_id} -> Nhãn GPT-4o: {label_gpt4o}")

        except Exception as e:
            label_gpt4o = None
            justification = f"Error: {e}"
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(f"[{timestamp}] ID: {issue_id} | Provider: Azure AI | Model: {MODEL_NAME} | Status: ERROR | Error: {e}\n")
            log_file.flush()
            print(f"Lỗi tại ID {issue_id}: {e}")

        output_results.append({
            "issue_id": issue_id,
            "label_gpt4o": label_gpt4o,
            "justification": justification,
            "raw_llm_response": content,
            "model_provider": "Azure AI / Azure OpenAI compatible endpoint",
            "model_or_deployment": MODEL_NAME,
            "temperature": TEMPERATURE,
            "prompt_version": PROMPT_VERSION,
        })

        time.sleep(2)

output_df = pd.DataFrame(output_results)
final_df = pd.merge(df, output_df, on="issue_id", how="left")
final_df.to_csv(output_path, index=False, encoding="utf-8")
print(f"Completed. Results saved to: {output_path}")
print(f"Log saved to: {log_path}")
