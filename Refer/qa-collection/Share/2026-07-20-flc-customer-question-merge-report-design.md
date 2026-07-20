# FLC Customer Question Merge Report Design

## Goal

Create a simple internal report that groups the classified FLC customer questions into broad FAQ questions. The report is an intermediate question bank for later answer research, not a public FAQ and not a final technical answer set.

## Source

- Workbook: `Refer/QA飞书收集/电商产品QA采集表_FLC产品QA翻译与分类_2026-07-20.xlsx`
- Use the existing `分类` column and the approved multi-label index.
- Ignore the trailing blank worksheet row.
- Keep every source ID and product model traceable.

## Merge level

Merge by the affected core function, not by the detailed symptom.

Example: LOW too fast, MED and HI having the same speed, one speed failing, and speed-button order being wrong all belong to one broad `风速` question: the three speed levels do not match expectations.

Do not merge different core functions. `风速`, `灯`, `遥控器`, and `蜂鸣器` remain separate even when one source row appears under more than one topic.

## Report scope

Cover the approved classified topics:

- `风速`
- `遥控器`
- `灯`
- `蜂鸣器`
- `大小问题`
- `不适配`
- `噪音`
- `停电后恢复`
- `三年后有问题`
- `改进建议`
- `线太短`
- `法语说明书`

List the eight not-yet-classified IDs in an appendix, but do not force them into the approved categories: `10`, `39`, `94`, `116`, `119`, `121`, `136`, and `142`.

## Section format

Each topic section contains:

1. `来源索引`: all source IDs in the topic.
2. `涉及型号`: source product models, without assuming undocumented models are equivalent.
3. `合并逻辑`: the shared customer intent and the detailed symptoms intentionally deferred.
4. `合并后的问题`: one broad Chinese customer question.
5. `后续分析重点`: short symptom dimensions to investigate when answers are written.

For a topic with only one source ID, state that it is a standalone topic rather than claiming multiple questions were merged.

## Product and fact boundaries

- Current public manuals exist only for `FLC05-E110V` and `FLC05-E220V`.
- Do not treat `FLC-110V`, `FLC-220V`, or `FLC06-E110V` as identical to documented FLC05 models.
- The report may merge customer intent across models, but must retain model labels and mark technical applicability for later confirmation.
- Do not invent causes, settings, compatibility, wiring, or safety conclusions.
- Burned or melted product incidents remain separate safety evidence and are not converted into a normal public FAQ without review.

## Output

- Create: `Refer/qa-collection/Share/FLC_Customer_Question_Merge_Report_2026-07-20.md`
- Internal report language: Chinese.
- Do not modify the source workbook, the translated CSV, or files under `docs/`.

## Validation

- All approved topic indexes are present.
- Every classified source ID appears in at least one topic section.
- Multi-label IDs may appear in more than one section.
- The eight pending IDs appear only in the pending-classification appendix unless already approved under a topic.
- Every topic contains an index, merge logic, merged question, and later-analysis focus.
- No answer text or unsupported product fact is added.
