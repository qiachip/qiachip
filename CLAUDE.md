# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 常用命令 (Common Commands)

本项目依赖于 Python 虚拟环境，请确保在执行命令前激活环境：

- **激活虚拟环境 (Windows):** `venv\Scripts\activate`
- **安装/更新依赖:** `pip install -r requirements.txt`
- **本地启动预览服务器:** `mkdocs serve` （默认访问 http://127.0.0.1:8000/）
- **构建静态站点:** `mkdocs build`
- **版本管理与部署 (通过 mike 插件):**
  - 构建并推送特定版本: `mike deploy <version> <alias> --push` （例如：`mike deploy 1.0.0 latest --push`）
  - 本地预览指定版本: `mike serve`

## 项目架构与目录结构

本项目是一个使用 MkDocs 和 Material for MkDocs 主题构建的 QIACHIP 产品静态文档网站。

- **`mkdocs.yml`:** 站点的核心配置文件。包括导航菜单（`nav`）、主题设置、插件（如 `search`, `glightbox`, `mike`）和 Markdown 扩展的配置。当你添加新的产品文档时，必须在此文件中更新 `nav` 节点。
- **`docs/`:** 所有的 Markdown 源文件及其关联的媒体资源。
  - **文档组织约定:** 每个产品型号（如 `KR1201A`, `FLC05-E110V`）都有独立的目录。Markdown 文件和相关的图片（优先使用 `.webp`, `.jpg`, `.png`, `.svg` 格式）必须放在该产品对应的同一个目录下，以便于管理。
  - **样式覆盖:** 自定义 CSS 存放在 `docs/assets/css/extra.css` 中，默认模板的覆盖位于 `docs/overrides/`。
- **`site/`:** 由 MkDocs 构建生成的最终静态 HTML 文件输出目录。
- **`venv/`:** Python 虚拟环境目录（不应提交至 Git）。

## 编写与开发约定

1. **内容语言:** 内部的 `README` 说明可能包含中文，但产品文档源文件（在 `docs/` 内的 Markdown 文件）的**内容、文件名、目录名必须严格使用英文**。
2. **Markdown 规范:**
   - 充分利用配置好的 Markdown 扩展：如 `attr_list`, `md_in_html`, `pymdownx.superfences`, `admonition`, `pymdownx.details`。
   - 使用 `admonition` （警告框）来突出显示重要信息（如 `note`, `warning`, `tip`）。
3. **依赖更新:** 如果在开发过程中引入了新的 Python 库（如 MkDocs 插件），必须在虚拟环境下执行 `pip freeze > requirements.txt` 来更新依赖列表。
