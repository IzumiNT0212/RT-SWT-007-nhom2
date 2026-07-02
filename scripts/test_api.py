# -*- coding: utf-8 -*-
"""
RBL-4 Tuần 7 — Gate E3: test 1 API call với Azure AI GPT-4o.

Cách chạy từ thư mục gốc project:
    Windows CMD:
        set AZURE_AI_API_KEY=your_key_here
        set AZURE_AI_BASE_URL=https://models.inference.ai.azure.com
        set AZURE_AI_MODEL=gpt-4o
        python scripts/test_api.py

    PowerShell:
        $env:AZURE_AI_API_KEY="your_key_here"
        $env:AZURE_AI_BASE_URL="https://models.inference.ai.azure.com"
        $env:AZURE_AI_MODEL="gpt-4o"
        python scripts/test_api.py

Không hardcode API key trong file này.
"""

import os
import json
import time
from pathlib import Path
from openai import OpenAI

BASE_URL = os.getenv("AZURE_AI_BASE_URL") or os.getenv("AZURE_OPENAI_BASE_URL") or "https://models.inference.ai.azure.com"
API_KEY = os.getenv("AZURE_AI_API_KEY") or os.getenv("AZURE_OPENAI_API_KEY")
MODEL_NAME = os.getenv("AZURE_AI_MODEL") or os.getenv("AZURE_OPENAI_DEPLOYMENT") or "gpt-4o"

if not API_KEY:
    raise RuntimeError("Thiếu API key. Hãy set AZURE_AI_API_KEY hoặc AZURE_OPENAI_API_KEY bằng biến môi trường.")

client = OpenAI(base_url=BASE_URL, api_key=API_KEY)

prompt = """Return only valid JSON: {\"label\": 1, \"justification\": \"API test successful\"}"""

response = client.chat.completions.create(
    model=MODEL_NAME,
    messages=[
        {"role": "system", "content": "You are a helpful software engineering assistant."},
        {"role": "user", "content": prompt},
    ],
    temperature=0,
    response_format={"type": "json_object"},
)

content = response.choices[0].message.content or ""
parsed = json.loads(content)

results_dir = Path("results")
results_dir.mkdir(exist_ok=True)
log_path = results_dir / "pilot_api_log.txt"
usage = getattr(response, "usage", None)
prompt_tokens = getattr(usage, "prompt_tokens", "NA") if usage else "NA"
completion_tokens = getattr(usage, "completion_tokens", "NA") if usage else "NA"
returned_model = getattr(response, "model", MODEL_NAME)

timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
with open(log_path, "a", encoding="utf-8") as f:
    f.write(f"[{timestamp}] API TEST | Provider: Azure AI | Model: {returned_model} | Prompt Tokens: {prompt_tokens} | Completion Tokens: {completion_tokens} | Status: OK\n")

print("API test thành công.")
print(parsed)
print(f"Đã ghi log vào: {log_path}")
