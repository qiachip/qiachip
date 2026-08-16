# Notion Manual Blueprint Test Template 实现计划

> **面向 AI 代理的工作者：** 必需子技能：使用 superpowers:executing-plans 逐任务实现此计划。步骤使用复选框（`- [ ]`）语法跟踪进度。

**目标：** 仅依据 `Refer/notion-manual-standard-blueprint.md` 生成一份通用 Notion 产品说明书模板，并明确暴露蓝图不足以唯一确定的结构。

**架构：** 单个内部 Markdown 文件分为审阅说明、可复制 Notion 正文、蓝图覆盖与缺口报告三部分。正文使用英文和语义占位符；验证使用只读 PowerShell 断言检查顺序、层级、固定文本、占位符和缺口标记。

**技术栈：** Markdown、Notion Markdown 块标记、PowerShell、Git

---

## 文件结构

- 创建：`Refer/notion-manual-template-blueprint-test.md`，承载审阅说明、完整模板正文和蓝图覆盖/缺口报告。
- 保留：`Refer/notion-manual-template-blueprint-test-design.md`，作为已批准规格，不在实现阶段改写。

### 任务 1：生成严格蓝图模板

**文件：**
- 创建：`Refer/notion-manual-template-blueprint-test.md`
- 参考：`Refer/notion-manual-standard-blueprint.md`
- 参考：`Refer/notion-manual-template-blueprint-test-design.md`

- [x] **步骤 1：确认输入文件与目标边界**

运行：

```powershell
$required = @(
  'Refer\notion-manual-standard-blueprint.md',
  'Refer\notion-manual-template-blueprint-test-design.md'
)
foreach ($path in $required) {
  if (-not (Test-Path $path)) { throw "Missing required input: $path" }
}
if (Test-Path 'docs\notion-manual-template-blueprint-test.md') {
  throw 'Internal template must not exist under docs.'
}
'Template inputs and public-site boundary confirmed.'
```

预期：输出 `Template inputs and public-site boundary confirmed.`。

- [x] **步骤 2：创建内部审阅头和占位符说明**

在目标文件顶部写明：

- 本文件只依据标准蓝图生成，不使用现有产品说明书补缺。
- 只复制 `BEGIN NOTION BODY` 与 `END NOTION BODY` 之间的内容。
- `<...>`、`[IMAGE BLOCK: ...]`、`[REPEAT: ...]`、`[OPTIONAL: ...]`、`[CONDITIONAL: ...]`、`[BLUEPRINT GAP: ...]` 六类标记的含义。
- Notion 页面 title property 使用固定句式：

```text
QIACHIP <Model> ( <Series> Series ) Instruction Manual <Voltage Range> <RF Frequency> RF <Product Type>
```

- [x] **步骤 3：写入完整 Notion 正文骨架**

正文必须按以下顺序写入，章节级使用 `#`，子节使用 `##`，标题不加粗：

```text
[IMAGE BLOCK: Product Diagram]
Version / Last Updated / Model blockquote
# Product Size
# Component Description
# Wiring Diagram
## Figure 1
# Function description and setting method
## (1) <Mode Name>
## <span color="red">How to set <mode> mode</span>
## (N) Reset function
## <span color="red">How to reset</span>
# Electrical characteristics
# Warning
# NOTE
# Frequently Asked Questions (Q&A)
## Question 1: <Question Text>
# <Product-Specific Add-on Title>
```

正文必须同时满足：

- Product、Size、Component、Wiring 图片分别写出所需 filename 和 alt 占位符。
- 尺寸正文与参数表都使用同一个 `<Overall Size>` 占位符；尺寸图另列为三向核对证据。
- Component Description 显示 `<columns>` 外壳，并在内部放置 `[BLUEPRINT GAP: exact child-column serialization is not specified]`。
- Wiring Diagram 的提示句使用条件标记；不得把 `Disconnect power before wiring.` 作为所有产品必写事实。
- Figure 块严格保持“子标题、图片、普通图注、Load、Input Power、分隔线”连续顺序。
- 模式总览、配对保持句和品牌兼容句保留蓝图中的可选词分支，并明确标为蓝图无法逐字唯一确定。
- 模式块以 `In this mode:` 开始，步骤使用 `**Step 1**`，不用 Step 标题层级。
- 参数表写出 `<table header-row="true">` 外壳、固定 `Parameter` / `Value` 表头和 `[BLUEPRINT GAP: exact row and cell serialization is not specified]`。
- `Warning` 与 `NOTE` 都展示，并注明实际产品至少保留一类、内容必须按事实归类。
- FAQ 和产品专属附加块标为可选，产品专属附加块保持最后。

- [x] **步骤 4：写入蓝图覆盖与缺口报告**

正文结束后增加一张 `Blueprint rule | Template evidence | Status` 表。至少逐项记录：

1. 顶层区块顺序：`Covered`。
2. Notion 标题层级：`Covered`。
3. 图片 filename / alt 命名：规则已覆盖，但 Notion 图片块如何存储 alt 为 `Gap`。
4. `<columns>` 子列序列化：`Gap`。
5. `<table>` 行列序列化：`Gap`。
6. Wiring notice 条件规则与固定文字清单冲突：`Conflict`。
7. 配对保持句含 slash 选项：`Ambiguous`。
8. 品牌兼容句含术语选项：`Ambiguous`。
9. `Warning` 与 `NOTE` 同时存在时的相对顺序：`Gap`。
10. 产品专属附加块通用结构：`Gap`。

报告结论必须区分“足以生成骨架”和“足以生成可直接导入 Notion 的唯一序列化文档”，不能把两者混为一谈。

### 任务 2：执行确定性验证

**文件：**
- 验证：`Refer/notion-manual-template-blueprint-test.md`

- [x] **步骤 1：运行结构与内容断言**

运行：

```powershell
$path = 'Refer\notion-manual-template-blueprint-test.md'
$text = Get-Content -Raw -Encoding UTF8 $path

$required = @(
  'BEGIN NOTION BODY',
  'END NOTION BODY',
  '# Product Size',
  '# Component Description',
  '# Wiring Diagram',
  '## Figure 1',
  'Figure 1: Wiring diagram for <Product-Specific Object>',
  '- Load: <Product-Specific Load>',
  '- Input Power: <Input Power>',
  '# Function description and setting method',
  'In this mode:',
  '**Step 1**',
  '# Electrical characteristics',
  '# Warning',
  '# NOTE',
  '# Frequently Asked Questions (Q&A)',
  '**Answer:**',
  '<Overall Size>',
  '[BLUEPRINT GAP: exact child-column serialization is not specified]',
  '[BLUEPRINT GAP: exact row and cell serialization is not specified]',
  'Blueprint rule | Template evidence | Status'
)
foreach ($item in $required) {
  if (-not $text.Contains($item)) { throw "Missing required template evidence: $item" }
}

$bodyStart = [regex]::Match(
  $text,
  '(?s)<!-- BEGIN NOTION BODY -->\s*(?<first>[^\r\n]+)'
)
if (-not $bodyStart.Success -or -not $bodyStart.Groups['first'].Value.StartsWith('[IMAGE BLOCK:')) {
  throw 'Product Diagram is not the first Notion body block.'
}

if ($text -match '(?m)^#{1,6}\s+\*\*') {
  throw 'Bold heading found.'
}

$headings = @(
  '# Product Size',
  '# Component Description',
  '# Wiring Diagram',
  '# Function description and setting method',
  '# Electrical characteristics',
  '# Warning',
  '# NOTE',
  '# Frequently Asked Questions (Q&A)',
  '# <Product-Specific Add-on Title>'
)
$last = -1
foreach ($heading in $headings) {
  $index = $text.IndexOf($heading)
  if ($index -lt 0) { throw "Missing heading: $heading" }
  if ($index -le $last) { throw "Heading order error: $heading" }
  $last = $index
}

if ([regex]::Matches($text, [regex]::Escape('<Overall Size>')).Count -lt 2) {
  throw 'Size placeholder is not shared by body and table.'
}

if ($text -match 'KR1202|RX480E|68x48x16|DC 5V-60V|DC motors') {
  throw 'Real source or target product facts leaked into the generic template.'
}

'Notion template deterministic checks passed.'
```

预期：输出 `Notion template deterministic checks passed.`。

- [x] **步骤 2：检查文件范围与格式**

运行：

```powershell
$path = 'Refer\notion-manual-template-blueprint-test.md'
$lines = Get-Content -Encoding UTF8 $path
for ($i = 0; $i -lt $lines.Count; $i++) {
  if ($lines[$i] -match '[ \t]+$') {
    throw "Trailing whitespace at line $($i + 1)."
  }
}
git status --short -- 'Refer/notion-manual-template-blueprint-test.md'
```

预期：没有尾随空格错误；状态只显示新的 `Refer/notion-manual-template-blueprint-test.md`。现有工作区的其他改动不属于本任务，不据此判断本模板失败。

### 任务 3：审阅并提交模板

**文件：**
- 创建：`Refer/notion-manual-template-blueprint-test.md`

- [x] **步骤 1：审阅差异**

运行：

```powershell
Get-Content -Raw -Encoding UTF8 'Refer\notion-manual-template-blueprint-test.md'
```

预期：文件只包含严格蓝图模板、覆盖表和缺口报告，不包含产品事实、站点配置或公开文档内容。

- [ ] **步骤 2：提交单一产物**

运行：

```powershell
git add -- 'Refer/notion-manual-template-blueprint-test.md'
git diff --cached --name-only
git diff --cached --check
git commit -m "docs: add Notion blueprint test template (task 3/3)"
```

预期：暂存清单只有 `Refer/notion-manual-template-blueprint-test.md`，提交成功且不推送。
