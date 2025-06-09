# QIACHIP 文档网站
0609
这是一个使用 MkDocs 构建的 QIACHIP 产品文档网站，旨在为 QIACHIP 的产品提供清晰、准确的用户指南和技术文档。

## 1. 项目概述

本项目基于 MkDocs 和 Material for MkDocs 主题，专注于提供高质量、易于访问的产品文档。所有文档内容均使用 Markdown 编写。

## 2. 技术栈与框架

- **主要框架:** MkDocs
- **主题:** Material for MkDocs
- **内容格式:** Markdown
- **版本管理:** `mike` 插件用于多版本文档管理
- **虚拟环境:** 使用 `venv` 管理 Python 依赖

## 3. 内容编写规范

- **语言:** 严格使用**英文**编写产品文档内容。文件名、目录名也应使用英文。
- **Markdown 风格:**
    - 遵循标准 Markdown 语法。
    - 充分利用 `attr_list`, `md_in_html`, `pymdownx.superfences`, `admonition` 等 Markdown 扩展。
    - 使用 `admonition` 突出显示重要信息（如注意、警告、提示）。
- **内容要求:**
    - 内容需清晰、简洁、准确。
    - 保持技术术语的一致性。
    - 为代码块指定语言类型。
- **图片:**
    - 图片应存放在对应产品文档的目录下。
    - 使用有意义的英文文件名（例如 `kr1201_wiring_diagram.jpg`）。
    - 优先使用 JPG, PNG, 或 SVG 格式。

## 4. 文件与目录结构

- `docs/` - 所有 Markdown 文档源文件
  - `docs/KR1201/` - KR1201 产品文档目录
  - `docs/KR1202-V05/` - KR1202-V05 产品文档目录
  - `docs/KR2202/` - KR2202 产品文档目录
- `mkdocs.yml` - MkDocs 主配置文件，用于定义网站结构和插件
- `.gitignore` - Git 忽略文件列表，包含 `temp/`, `.cursor/rules/`, `.trae/rules/`, `venv/` 等不需上传的文件和目录。
- `requirements.txt` - Python 依赖列表

## 5. 开发流程

### 5.1 环境设置

首次设置或在新环境进行开发时：

```bash
# 创建并激活虚拟环境
python -m venv venv
venv\Scripts\activate

# 安装所有必要的 Python 依赖
pip install -r requirements.txt
```

### 5.2 本地预览

在本地启动开发服务器以预览您的更改：

```bash
mkdocs serve
```

访问 `http://127.0.0.1:8000/` 即可在浏览器中查看文档网站。

### 5.3 依赖管理

如果需要添加新的 Python 库（例如 MkDocs 插件），请先激活虚拟环境，然后使用 `pip install <package_name>` 安装，并更新 `requirements.txt` 文件。

```bash
venv\Scripts\activate
pip install new-package-name
pip freeze > requirements.txt
```

## 6. 版本管理 (使用 `mike` 插件)

本项目使用 `mike` 插件进行版本管理，可以轻松部署和维护多个文档版本。

### 6.1 创建新版本

要发布新版本的文档，请使用以下命令：

```bash
# 激活虚拟环境
venv\Scripts\activate

# 部署新版本（例如 v1.0）并将其设为 latest
mike deploy --push --update-aliases 1.0 latest
```

这将创建一个名为 `1.0` 的新版本，并将 `latest` 别名指向该版本。

### 6.2 设置默认版本

如果需要更改默认版本，可以使用以下命令：

```bash
mike set-default --push latest
```

### 6.3 本地预览带版本选择器的文档

要在本地预览包含版本选择器的文档，请使用：

```bash
mike serve
```

### 6.4 版本管理最佳实践

- 使用语义化版本号（如 `1.0`, `1.1`, `2.0` 等）。
- 始终将最新稳定版本设置为 `latest` 别名。
- 在发布新版本前，确保所有文档内容已更新。
- 保留旧版本文档，以便用户可以查阅历史版本。