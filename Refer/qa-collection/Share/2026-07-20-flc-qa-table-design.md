# FLC QA Translation Table Design

## Goal

Create a separate CSV containing every source row whose trimmed `产品型号` starts with `FLC`.

## Input and output

- Source: `Refer/QA飞书收集/电商产品QA采集表_Q&A收集表格 _2026-07-20 114155.csv`
- Output: a new UTF-8 CSV in the same directory; do not overwrite the source.
- Preserve the original 10 columns and source-row order.
- Append three columns: `问题的英文翻译`, `问题的中文翻译`, and `推荐问题分类`.

## Translation rules

- Translate the `问题` field faithfully rather than rewriting it as a polished public FAQ.
- Preserve product models, voltages, button names, terminal labels, measurements, URLs, timelines, symptoms, and customer scenarios.
- Keep complaints and safety incidents as translations; do not invent technical causes or answers.
- Write clear English that a non-native reader can understand quickly.
- Use the original English text as the English translation when it is already clear; correct obvious spelling or grammar only when meaning is unchanged.
- Translate multilingual or Chinese source questions into both English and Chinese.

## Recommended categories

Use exactly one of these three values:

- `产品适配`: parameters, dimensions, supported functions, compatibility, or purchase-fit questions.
- `安装设置`: installation, wiring, remote operation, pairing, or feature configuration.
- `故障排除`: failures, abnormal speed, noise, light problems, overheating, burning, or other operating faults.

Classify by the customer's main intent. For a row containing more than one issue, use the issue that most strongly determines the needed action. Do not mechanically copy the original category.

## Validation

- Output contains exactly 50 data rows.
- Every output model starts with `FLC` after trimming.
- The original 10 fields match the source rows exactly.
- All three appended fields are non-empty.
- `推荐问题分类` contains only the three approved values.
- Output can be imported as UTF-8 CSV without malformed rows.
