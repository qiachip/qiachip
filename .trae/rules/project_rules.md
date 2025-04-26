# QIACHIP Docs 项目规则

## 1. 项目概述

本项目是一个使用 MkDocs 构建的产品文档网站，旨在为 QIACHIP 的产品提供清晰、准确的用户指南和技术文档。

## 2. 技术栈与框架

- **主要框架:** MkDocs
- **主题:** Material for MkDocs
- **内容格式:** Markdown
- **虚拟环境:** 项目使用 `venv` 虚拟环境管理 Python 依赖。所有 `pip` 安装或 `mkdocs` 相关命令都应在激活虚拟环境后执行。

## 3. 内容编写规范

- **语言:** 主要使用**英文**编写产品文档内容。文件名、目录名也使用英文。
- **Markdown 风格:**
    - 使用标准 Markdown 语法。
    - 充分利用已启用的 Markdown 扩展：`attr_list`, `md_in_html`, `pymdownx.superfences`, `admonition`。
    - 使用 `admonition` 突出显示注意、警告、提示等信息。
- **内容要求:**
    - 保持内容清晰、简洁、准确。
    - 技术术语使用一致。
    - 为代码块指定语言类型。
- **图片:**
    - 图片应存放在对应产品文档的目录下。
    - 使用有意义的英文文件名（例如 `kr1201_wiring_diagram.jpg`）。
    - 优先使用 JPG, PNG, 或 SVG 格式。

## 4. 文件与目录结构

- **文档源文件:** 所有 Markdown 文档 (.md 文件) 必须存放在 `docs/` 目录下。
- **产品文档:** 每个产品的文档应放在 `docs/` 下对应的子目录中（例如 `docs/KR1201/`）。
- **导航配置:** 新增页面后，需要在 `mkdocs.yml` 文件中的 `nav` 部分更新导航结构。
- **配置文件:** 主要配置文件为根目录下的 `mkdocs.yml`。

## 5. 开发流程

- **依赖管理:** 如果需要添加新的 Python 库（例如 MkDocs 插件），请先激活虚拟环境 (`venv\Scripts\activate`)，然后使用 `pip install <package_name>` 安装，并考虑更新 `requirements.txt` 文件（如果尚不存在，请创建）。
- **本地预览:** 使用 `mkdocs serve` 命令在本地启动开发服务器预览更改。
- **代码风格 (Python):** 如果编写 Python 脚本（例如自定义插件），请遵循 PEP 8 风格指南。

## 6. 通用开发原则 (遵循用户通用规范)

- **代码简洁可读:** 保持 Markdown 和配置文件 (`mkdocs.yml`) 的整洁。
- **模块化:** 遵循 `docs/` 目录下的结构组织文档。
- **DRY 原则:** 避免在不同文档中重复大段相同内容，考虑使用 Markdown 包含或链接。
- **可维护性:** 保持 `mkdocs.yml` 配置清晰，添加必要的注释说明。