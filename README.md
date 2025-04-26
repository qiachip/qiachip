# QIACHIP Docs 文档网站

这是QIACHIP产品的官方文档网站，使用MkDocs和Material for MkDocs主题构建。

## 项目概述

本项目是一个使用 MkDocs 构建的产品文档网站，旨在为 QIACHIP 的产品提供清晰、准确的用户指南和技术文档。

## 版本管理

本项目使用 `mike` 插件进行版本管理，可以轻松部署和维护多个文档版本。

### 版本管理使用方法

#### 1. 创建新版本

要发布新版本的文档，请使用以下命令：

```bash
# 激活虚拟环境
venv\Scripts\activate

# 部署新版本（例如v1.0）并将其设为latest
mike deploy --push --update-aliases 1.0 latest
```

这将创建一个名为`1.0`的新版本，并将`latest`别名指向该版本。

#### 2. 设置默认版本

如果需要更改默认版本，可以使用以下命令：

```bash
mike set-default --push latest
```

#### 3. 本地预览

要在本地预览文档（包括版本选择器），请使用：

```bash
mike serve
```

### 版本管理最佳实践

- 使用语义化版本号（如`1.0`、`1.1`、`2.0`等）
- 始终将最新稳定版本设置为`latest`别名
- 在发布新版本前，确保所有文档内容已更新
- 保留旧版本文档，以便用户可以查阅历史版本

## 本地开发

### 环境设置

```bash
# 创建并激活虚拟环境
python -m venv venv
venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt
```

### 本地预览

```bash
mkdocs serve
```

访问 http://127.0.0.1:8000/ 查看文档网站。

## 项目结构

- `docs/` - 所有文档源文件
  - `KR1201/` - KR1201产品文档
  - `KR1202-V05/` - KR1202-V05产品文档
  - `KR2202/` - KR2202产品文档
- `mkdocs.yml` - MkDocs配置文件