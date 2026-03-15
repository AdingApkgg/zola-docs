
+++
title = "Cela"
description = "一个极简主义的文档/博客主题。"
template = "theme.html"
date = 2025-12-06T11:43:01+08:00

[taxonomies]
theme-tags = ['blog', 'documentation', 'lightweight', 'minimal', 'responsive', 'search']

[extra]
created = 2025-12-06T11:43:01+08:00
updated = 2025-12-06T11:43:01+08:00
repository = "https://github.com/edwardzcn-decade/cela.git"
homepage = "https://github.com/edwardzcn-decade/cela"
minimum_version = "0.19.0"
license = "MIT"
demo = "https://edwardzcn-decade.github.io/cela/"

[extra.author]
name = "Edward Zhang"
homepage = "https://github.com/edwardzcn-decade"
+++        

# Cela

<p align="center">
  <a href="https://edwardzcn-decade.github.io/cela"><img src="https://img.shields.io/badge/Cela-f8f8f8?style=for-the-badge"></a>
  <a href="https://www.getzola.org"><img src="https://img.shields.io/badge/Zola-f8f8f8?style=for-the-badge&logo=zola&logoColor=black"></a>
</p>

*Cela* 是一个简单、轻量级的 Zola 主题，灵感来自 [Hugo PaperMod](https://github.com/adityatelange/hugo-PaperMod)。

样式表改编自 [Catppuccin](https://github.com/catppuccin/catppuccin)。
如果你喜欢它，请在 GitHub 上给它一个 🌟。谢谢！

![截图](screenshot.png)

---

## 主题特性

+ [x] Catppuccin 配色主题
+ [x] 亮色/暗色模式切换
+ [x] MathJax 支持
+ [x] 博客 RSS 订阅
+ [x] 全文搜索
+ [x] 机器人工具
+ [ ] 博客归档（按年份分组）
+ [ ] 国际化 (i18n)

### 标签、分类和分类法

Cela 提供了类似 Hexo/Hugo 的 `tags`（标签）和 `categories`（分类），与 Zola `taxonomies`（分类法）兼容。在 Front Matter 中：

```toml
[taxonomies]
tags = ["Rust", "Zola"]
categories = ["Programming"]
```

或者 YAML 风格：

```yaml
taxonomies:
  tags: ["Rust", "Zola"]
  categories: ["Programming"]
```

推荐使用 Zola `taxonomies`，因为它在构建内容结构方面更强大。更多信息请参阅 [Zola 分类法](https://www.getzola.org/documentation/content/taxonomies/)。

## 快速开始

如果你只需要安装主题，请跳到主题安装部分。

### Zola 安装

```bash
# macOS
brew install zola
# Alpine Linux
apk add zola
# Arch Linux
pacman -S zola
# Docker
docker pull ghcr.io/getzola/zola:v0.19.1
```

### 创建 Zola 站点

创建你的第一个 Zola 站点。

如果 `myblog` 已经存在但只包含隐藏文件（如 `.git`），Zola 也会填充该站点。

```bash
zola init myblog
# 或者
# 填充当前目录
zola init
```

你在初始化期间所做的任何选择稍后都可以在 `config.toml` 文件中更改。


### 主题安装

#### 通过 Git 子模块

```bash
git submodule add https://github.com/edwardzcn-decade/cela themes/cela
git submodule update --init --force --recursive
git submodule sync
```

然后在你的 `config.toml` 文件中设置 `theme`。

```toml
theme = "cela"
```

#### 通过下载发布版

1. 从 Cela 发布页面下载最新的发布归档文件。
2. 解压到 Zola 项目中的 themes/cela。
3. 在 config.toml 中设置 `theme`。
4. （可选）如果你是重新开始，请删除 content/ 下未使用的示例内容。

## 👐 贡献

> [!NOTE]
>
> 如果你觉得这个项目有帮助，并希望支持它的开发，请参阅我们的 [CONTRIBUTING](CONTRIBUTING.md) 和 [CODE_OF_CONDUCT](CODE_OF_CONDUCT.md) 指南。

## 许可证

MIT
