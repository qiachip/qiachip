# Notion Manual Template - Strict Blueprint Test

本文件只依据 `Refer/notion-manual-standard-blueprint.md` 生成，用于检验蓝图本身是否足以还原一篇 Notion 产品说明书。没有使用现有产品说明书、外部资料或标准页正文补齐缺口。

## 使用边界

- 只复制 `BEGIN NOTION BODY` 与 `END NOTION BODY` 之间的内容到 Notion 正文。
- 页面标题需单独填写到 Notion title property，不放进正文。
- 所有尖括号占位符都必须替换成经过核实的产品事实。
- 所有方括号标记都必须在正式发布前处理或删除。
- 本文件是内部验证材料，不同步到公开站点 `docs/`。

## 标记说明

- `<...>`：需要替换的产品事实或页面元数据。
- `[IMAGE BLOCK: ...]`：Notion 图片块及其 filename / alt 要求。
- `[REPEAT: ...]`：按产品实际数量复制整个相邻区块。
- `[OPTIONAL: ...]`：目标产品确有该内容时保留。
- `[CONDITIONAL: ...]`：根据核实后的产品事实决定是否保留。
- `[BLUEPRINT GAP: ...]`：蓝图不足以唯一确定该处的 Notion 结构或固定文本。

## Notion Page Title Property

```text
QIACHIP <Model> ( <Series> Series ) Instruction Manual <Voltage Range> <RF Frequency> RF <Product Type>
```

<!-- BEGIN NOTION BODY -->

[IMAGE BLOCK: Filename `QIACHIP_<Model>_Product_Diagram.webp`; Alt `QIACHIP <Model> Product Diagram.webp`; BLUEPRINT GAP: exact Notion image block serialization and alt storage are not specified]

> Version: <Version>
> Last Updated: <YYYY-MM-DD>
> Model: <Model> ( <Series> Series )

# Product Size

[IMAGE BLOCK: Filename `QIACHIP_<Model>_Size_Figure.webp`; Alt `QIACHIP <Model> Size Figure.webp`]

- Length (L) x Width (W) x Height (H): <Overall Size>

[CONDITIONAL: If the third dimension is PCB thickness rather than total assembled height, replace `Height (H)` with `Thickness (T)` and use a verified board-size value.]

[OPTIONAL: Add verified enclosure size, mounting-hole spacing, pin pitch, or other dimensional bullets required by the product.]

# Component Description

[IMAGE BLOCK: Filename `QIACHIP_<Model>_Component_Description_Figure.webp`; Alt `QIACHIP <Model> Component Description Figure.webp`]

<columns>

[BLUEPRINT GAP: exact child-column serialization is not specified]

[COLUMN 1]

- 1: <Component Name> (<Functional Meaning>)
- 2: <Component Name> (<Functional Meaning>)

[COLUMN 2]

- 3: <Component Name> (<Functional Meaning>)
- 4: <Component Name> (<Functional Meaning>)

</columns>

[REPEAT: Add or remove component entries and distribute them naturally between the two columns. Parenthetical text must describe real circuit meaning, not repeat the component name.]

# Wiring Diagram

[CONDITIONAL: Include only wiring notices that are factually applicable to this product.]

[CONDITIONAL: If factually applicable, include the following sentence exactly:]

Disconnect power before wiring.

[OPTIONAL: For a verified critical product-specific notice, use `<span color="red">**<Product-Specific Critical Wiring Notice>**</span>`.]

## Figure 1

[IMAGE BLOCK: Filename `QIACHIP_<Model>_Wiring_Diagram_1.webp`; Alt `QIACHIP <Model> Wiring Diagram 1.webp`]

Figure 1: Wiring diagram for <Product-Specific Object>

- Load: <Product-Specific Load>
- Input Power: <Input Power>

---

[REPEAT: Duplicate the complete Figure block for each additional wiring diagram. Keep the Figure heading, image, ordinary caption, Load, Input Power, and closing horizontal rule together. Increment every figure number and image suffix consistently.]

# Function description and setting method

**(1) <Mode 1 Name>; (2) <Mode 2 Name>; ...; (N) Reset function; <Optional Feature Names>**

[BLUEPRINT GAP: the pairing-retention sentence is listed as fixed text but contains slash-separated terminology and verb choices, so the blueprint does not define one exact sentence.]

- **Once the <receiver/receiving module> and <transmitter> are paired and a working mode is <set/selected>, the <receiver/receiving module> will <retain/keep> this mode even after <powered off and on again / power off and power on again>.**

[BLUEPRINT GAP: the brand-compatibility sentence is listed as fixed text but contains alternative receiver terminology, so the blueprint does not define one exact sentence.]

- **The following working modes require the use of QIACHIP brand remote controls (transmitters) and controllers (receiving modules/wireless remote control switches). Compatibility with other brands is not guaranteed.**

[OPTIONAL: Add each verified product-specific operating notice as a complete bold bullet: `- **<Product-Specific Operating Notice>**`.]

## (1) <Mode Name>

In this mode:

- <Mode Behavior 1>
- <Mode Behavior 2>

## <span color="red">How to set <mode> mode</span>

**Step 1**

<Verified Action>

**Step 2**

<Verified Action>

[REPEAT: Add `**Step N**` and its verified action as needed. Do not convert Step labels into headings.]

[REPEAT: Duplicate the complete mode block for each additional working mode. Increment the mode number and keep terminology consistent throughout the page.]

## (N) Reset function

In this mode:

- <Reset Behavior>

## <span color="red">How to reset</span>

**Step 1**

<Verified Reset Action>

[REPEAT: Add further reset steps only when required by the product.]

[OPTIONAL: For a non-mode feature, use a product-appropriate subheading with `<span color="red">How to set <feature></span>` and the same bold Step structure.]

# Electrical characteristics

<table header-row="true">

[BLUEPRINT GAP: exact row and cell serialization is not specified]

[HEADER ROW: Parameter | Value]

[CONDITIONAL ROW: Input voltage | <Input Voltage>]

[CONDITIONAL ROW: RF frequency | <RF Frequency>]

[CONDITIONAL ROW: Quiescent Current | <Quiescent Current in mA>]

[REPEAT ROW: <Product-Specific Parameter> | <Verified Value>]

[CONDITIONAL ROW: Working temperature | <Working Temperature>]

[ROW: Size | <Overall Size>]

</table>

[FORMAT: Write voltage ranges as `DC <Minimum>V-<Maximum>V` without meaningless `.0`. A value in mA must use a current parameter name, not `Power Consumption`.]

[BLUEPRINT GAP: when both safety blocks exist, their relative order is not explicitly defined. This test template places `Warning` before `NOTE` only for inspection.]

# Warning

[CONDITIONAL: Keep this section for verified safety warnings. Remove it only when the product has no safety-warning facts and an independent NOTE section remains.]

- <Verified Safety Warning>

# NOTE

[CONDITIONAL: Keep this section for verified usage precautions. Remove it only when the product has no usage-note facts and an independent Warning section remains.]

- <Verified Usage Note>

[REQUIRED: The final document must retain at least one independent `Warning` or `NOTE` section. Do not move safety content into unrelated sections.]

[OPTIONAL: Remove the complete FAQ section when the target product has no FAQ content.]

# Frequently Asked Questions (Q&A)

## Question 1: <Question Text>

**Answer:**

<Verified Answer Body>

[REPEAT: Duplicate the complete Question/Answer pair for each additional FAQ and increment the question number.]

[OPTIONAL: Remove the complete add-on section when the product has no product-specific supplemental block. Product-specific add-ons must remain at the very end.]

# <Product-Specific Add-on Title>

[BLUEPRINT GAP: the blueprint does not define a generic internal structure for product-specific add-on blocks.]

<Product-Specific Add-on Content>

<!-- END NOTION BODY -->

## Blueprint Coverage And Gaps

| Blueprint rule | Template evidence | Status |
|---|---|---|
| Top-level block order | Body follows Product Diagram, metadata, size, components, wiring, functions, characteristics, safety, optional FAQ, and optional add-on | Covered |
| Page title is stored outside the body | Separate `Notion Page Title Property` pattern | Covered |
| Series-name parentheses retain inner spaces | `( <Series> Series )` is used in title and metadata | Covered |
| Product Diagram is the first body block | First body item is the Product Diagram image marker | Covered structurally |
| Image filename and alt naming patterns | Every image marker records both required values | Covered structurally |
| Exact Notion image block and alt storage | No exact block serialization is given by the blueprint | Gap |
| Metadata blockquote contains three fixed labels | `Version`, `Last Updated`, and `Model` appear in order | Covered |
| Product Size structure and height/thickness distinction | Size image, shared `<Overall Size>`, and conditional thickness rule | Covered |
| Component Description uses two columns | `<columns>` shell and two logical column groups | Covered structurally |
| Exact child-column serialization | Blueprint names `<columns>` but does not define its children | Gap |
| Wiring figure adjacency | Heading, image, ordinary caption, Load, Input Power, and rule stay together | Covered |
| Wiring notice follows product facts | Notice is conditional | Covered |
| `Disconnect power before wiring.` is fixed text | The fixed-text list conflicts with the rule not to force this sentence | Conflict |
| Function section fixed heading and mode structure | Exact heading, overview, mode, red setting heading, and bold Steps | Covered |
| Pairing-retention sentence is fixed | Slash-separated terminology and verbs prevent one exact rendering | Ambiguous |
| Brand-compatibility sentence is fixed | Alternative receiver terminology prevents one exact rendering | Ambiguous |
| Electrical table uses `Parameter` / `Value` | `<table>` shell and logical row contents are present | Covered structurally |
| Exact table row and cell serialization | Blueprint does not define Notion row/cell syntax | Gap |
| At least one independent safety block | Both test blocks are shown with a retain-at-least-one rule | Covered |
| Relative order when both `Warning` and `NOTE` exist | Blueprint defines their position after the table but not their mutual order | Gap |
| FAQ is optional and paired | One complete Question/Answer pair with repeat/remove rules | Covered |
| Product-specific add-on remains last | Add-on placeholder is the final body section | Covered structurally |
| Generic add-on internal structure | No reusable block structure is defined | Gap |
| Notion headings differ from MkDocs headings | Body uses `#` chapters and `##` subheadings | Covered |
| Titles are not bold; Steps and Answer remain bold body text | Heading and body-emphasis patterns are shown separately | Covered |

## Test Conclusion

The blueprint is sufficient to generate the document skeleton, fixed section order, heading hierarchy, repeated block shapes, naming rules, and most fixed labels.

It is not yet sufficient to generate one unambiguous, directly importable Notion Markdown document without consulting another source. The unresolved areas are the exact serialization of image, column, and table blocks; the mutual ordering of `Warning` and `NOTE`; the generic shape of product-specific add-ons; and several entries described as fixed text that still contain alternatives or conflict with conditional product-fact rules.
