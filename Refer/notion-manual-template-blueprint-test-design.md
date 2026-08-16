# Notion Manual Blueprint Test Template Design

**Status:** Draft for user review
**Scope:** Internal `Refer/` material only
**Source of truth:** `Refer/notion-manual-standard-blueprint.md`

## Purpose

Create one generic, copyable Notion manual template that is generated strictly from the standard blueprint. The artifact is a test of whether the blueprint contains enough information to produce a correctly structured page; it is not a product manual and must not introduce facts from any existing product page.

## Boundary

- The template is stored under `Refer/` and is never added to `docs/` navigation.
- The Notion body uses English because product-manual body content follows the project language rule.
- All model-specific facts remain semantic placeholders, such as `<Model>`, `<Input Voltage>`, and `<Product-Specific Load>`.
- Existing product Markdown, external sources, and the source standard page are not used to fill missing values or syntax.
- No Notion API write, deployment, push, or generated-site change is included.

## Artifact

Create `Refer/notion-manual-template-blueprint-test.md` with two layers:

1. A short internal review header explaining the source, placeholder convention, and copy boundary.
2. A complete Notion body template followed by a blueprint coverage and gap report.

The body must be visually separable from the review material so a reviewer can copy only the body into a Notion page.

## Body structure

The body follows the blueprint's top-level order:

1. Bare Product Diagram image block.
2. Three-line `Version` / `Last Updated` / `Model` blockquote.
3. `Product Size` with a size image and dimension bullets.
4. `Component Description` with a component image and a two-column component list.
5. `Wiring Diagram` with a conditional product-specific notice and one repeatable figure block.
6. `Function description and setting method` with a mode overview, required caution bullets, one repeatable mode block, and a reset/feature-setting variant marker.
7. `Electrical characteristics` with a two-column `Parameter` / `Value` table.
8. `Warning` and `NOTE` safety blocks, each represented so the reviewer can test the one-or-both rule.
9. Optional `Frequently Asked Questions (Q&A)` with one question/answer pair and a repeat marker.
10. Optional product-specific add-on block at the end.

Notion heading levels are used in the body: `#` for chapter headings and `##` for subheadings. No heading is bold. `**Step N**` and `**Answer:**` remain body emphasis as required by the blueprint.

## Placeholder convention

- `<...>` means a value that must be replaced with verified product information.
- `[IMAGE BLOCK: ...]` means a Notion image block; it records the required filename and alt text without inventing a file.
- `[REPEAT: ...]` marks a block that may occur more than once and states what must remain adjacent.
- `[OPTIONAL: ...]` marks content that is included only when the target product has that content.
- `[CONDITIONAL: ...]` marks a rule whose presence depends on product facts.
- `[BLUEPRINT GAP: ...]` is used only where the blueprint does not specify enough Notion syntax or ordering to generate an unambiguous block. The marker must not be silently resolved from another document.

## Strictness rules

- Preserve fixed headings and fixed labels exactly, including case.
- Use the blueprint's explicit Notion forms where provided: blockquote, `<columns>`, `<table header-row="true">`, red `<span color="red">`, and horizontal rules.
- Where the blueprint gives alternatives, show the alternative as a conditional marker rather than selecting a product fact.
- Keep the wiring caption, `Load`, and `Input Power` together inside each figure block.
- Keep the dimension value in the size bullet and the `Size` table row as the same placeholder token; keep the image block as a separate required evidence placeholder so the size check remains three-way (image, body text, table).
- Include at least one independent `Warning` or `NOTE` block in the body, while showing both blocks in the test template so the coexistence rule can be reviewed.
- Keep FAQ and product-specific add-ons optional and in their specified positions.

## Gap report

After the body, record a compact table with columns `Blueprint rule`, `Template evidence`, and `Status`. The report must call out unresolved ambiguity instead of masking it. At minimum, inspect:

- exact Notion serialization for `<columns>` and its child columns;
- exact Notion serialization for `<table header-row="true">` rows and cells;
- how a Notion image block stores filename and alt text;
- the ordering of `Warning` versus `NOTE` when both exist;
- the generic structure of a product-specific add-on block;
- the slash-separated alternatives in the supposedly fixed pairing sentence and brand-compatibility sentence;
- the conflict between the conditional wiring notice rule and the fixed-text list entry for `Disconnect power before wiring.`.

## Validation

Before delivery, inspect the generated file for:

- top-level order matching the blueprint;
- correct `#`/`##` heading levels and no bold headings;
- all fixed labels and sentence prefixes present with required case;
- image filename and alt placeholders following the blueprint naming pattern;
- one complete repeatable example for wiring, mode, and FAQ blocks;
- table and column markers present without fabricated product values;
- matching size placeholder tokens in the size bullet and table;
- optional/conditional markers at every non-universal block;
- no real product model, dimension, voltage, frequency, load, pin, or behavior copied into the template;
- every unresolved rule listed in the gap report.

## Out of scope

- Filling the template for a real model.
- Correcting the blueprint itself in this task.
- Importing or patching a Notion page.
- Adding a public MkDocs page, navigation entry, image asset, or build output.

## Acceptance criteria

The user can read the body as a complete Notion manual skeleton, copy it without consulting another product page, and see exactly which details are required, repeatable, optional, or still underspecified by the blueprint.
