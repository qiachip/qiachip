# FLC QA Translation Table 实现计划

> **面向 AI 代理的工作者：** 必需子技能：使用 superpowers:subagent-driven-development（推荐）或 superpowers:executing-plans 逐任务实现此计划。步骤使用复选框（`- [ ]`）语法来跟踪进度。

**目标：** 从 2026-07-20 QA 采集表提取 50 条 FLC 产品记录，补齐英中问题翻译和三分类推荐，生成独立 CSV。

**架构：** 原 CSV 是唯一输入，目标 CSV 是唯一数据产物。逐行保留原 10 个字段和顺序，在末尾追加三个审核字段；最后用 PowerShell 重新导入目标文件并验证行数、型号、字段完整性和分类值域。

**技术栈：** UTF-8 CSV、PowerShell `Import-Csv`、人工语义翻译与意图分类。

---

### 任务 1：锁定输入集合和输出约束

**文件：**
- 读取：`Refer/QA飞书收集/电商产品QA采集表_Q&A收集表格 _2026-07-20 114155.csv`
- 参考：`Refer/qa-collection/Share/2026-07-20-flc-qa-table-design.md`

- [ ] **步骤 1：验证输入 FLC 行数**

运行：

```powershell
$source = 'Refer/QA飞书收集/电商产品QA采集表_Q&A收集表格 _2026-07-20 114155.csv'
$rows = @(Import-Csv -LiteralPath $source -Encoding UTF8 | Where-Object { $_.'产品型号'.Trim() -match '^FLC' })
$rows.Count
```

预期：输出 `50`。

- [ ] **步骤 2：记录源行身份和顺序**

运行：

```powershell
$rows | Select-Object ID, 产品型号 | Format-Table -AutoSize
```

预期：第一条 ID 为 `6`，最后一条 ID 为 `154`，共 50 条，顺序与源文件一致。

### 任务 2：翻译问题并推荐三分类

**文件：**
- 创建：`Refer/QA飞书收集/电商产品QA采集表_FLC产品QA翻译与分类_2026-07-20.csv`

- [ ] **步骤 1：为每条记录编写英文翻译**

按设计规格逐行处理 `问题`：保留型号、数值、单位、端子、按钮、URL、症状和时间线。原文已是清楚英文时保留语义，仅修正不影响原意的明显拼写或语法；其他语言忠实译成清晰英文，不改写为标准 FAQ，也不补充原因或答案。

- [ ] **步骤 2：为每条记录编写中文翻译**

逐行翻译相同 `问题`，保留客户的多问题结构、抱怨、安全事故、退货意图和诊断线索。不得把主观投诉改写成已证实的产品事实。

- [ ] **步骤 3：为每条记录选择唯一推荐分类**

只使用以下值：

```text
产品适配
安装设置
故障排除
```

判断顺序：已安装后出现失效或异常归 `故障排除`；主要询问安装、接线或遥控功能操作归 `安装设置`；主要判断尺寸、参数、功能支持或兼容性归 `产品适配`。一条包含多个问题时，选择最影响后续处理动作的核心意图。

- [ ] **步骤 4：生成目标 CSV**

目标表头必须严格为：

```text
ID,登记人,填写日期,产品型号,问题分类,问题,答案,来源备注,图片,视频,问题的英文翻译,问题的中文翻译,推荐问题分类
```

使用 CSV 标准双引号转义包含逗号、换行或双引号的字段。保持 50 条原记录的前 10 个字段和排列顺序不变。

### 任务 3：验证目标 CSV

**文件：**
- 验证：`Refer/QA飞书收集/电商产品QA采集表_FLC产品QA翻译与分类_2026-07-20.csv`

- [ ] **步骤 1：运行结构和值域验证**

运行：

```powershell
$source = 'Refer/QA飞书收集/电商产品QA采集表_Q&A收集表格 _2026-07-20 114155.csv'
$target = 'Refer/QA飞书收集/电商产品QA采集表_FLC产品QA翻译与分类_2026-07-20.csv'
$sourceRows = @(Import-Csv -LiteralPath $source -Encoding UTF8 | Where-Object { $_.'产品型号'.Trim() -match '^FLC' })
$targetRows = @(Import-Csv -LiteralPath $target -Encoding UTF8)
$allowed = @('产品适配', '安装设置', '故障排除')
$originalColumns = @('ID','登记人','填写日期','产品型号','问题分类','问题','答案','来源备注','图片','视频')
$errors = [System.Collections.Generic.List[string]]::new()
if ($targetRows.Count -ne 50) { $errors.Add("row count: $($targetRows.Count)") }
for ($i = 0; $i -lt $targetRows.Count; $i++) {
    if ($targetRows[$i].'产品型号'.Trim() -notmatch '^FLC') { $errors.Add("non-FLC row: $i") }
    foreach ($column in $originalColumns) {
        if ($targetRows[$i].$column -cne $sourceRows[$i].$column) { $errors.Add("source mismatch: row $i, $column") }
    }
    if ([string]::IsNullOrWhiteSpace($targetRows[$i].'问题的英文翻译')) { $errors.Add("missing English: row $i") }
    if ([string]::IsNullOrWhiteSpace($targetRows[$i].'问题的中文翻译')) { $errors.Add("missing Chinese: row $i") }
    if ($targetRows[$i].'推荐问题分类' -notin $allowed) { $errors.Add("invalid category: row $i") }
}
if ($errors.Count -eq 0) { 'PASS: 50 FLC rows validated' } else { $errors; exit 1 }
```

预期：输出 `PASS: 50 FLC rows validated`，退出码为 `0`。

- [ ] **步骤 2：人工抽查多语言和复杂记录**

抽查 ID `21`（中文参数）、`39`（德文烧毁事故）、`56`（英文多问题）、`84`（法文长评论）、`142`（阿拉伯文兼容性）。确认英中译文保留型号、数值、单位、症状与风险语气，分类符合三分类口径。

- [ ] **步骤 3：检查工作区范围**

运行：

```powershell
git status --short -- 'Refer/QA飞书收集' 'Refer/qa-collection/Share/2026-07-20-flc-qa-table-plan.md'
```

预期：本任务只新增目标 CSV 和本计划文件，不修改源 CSV。
