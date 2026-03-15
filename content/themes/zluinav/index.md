
+++
title = "UI Navigation"
description = "一个专为可访问性而非视觉设计的多语言主题。"
template = "theme.html"
date = 2025-09-10T09:22:29+06:30

[taxonomies]
theme-tags = ['blind', 'multilingual', 'accessible', 'responsive', 'search', 'documentation', 'blog', 'SEO']

[extra]
created = 2025-09-10T09:22:29+06:30
updated = 2025-09-10T09:22:29+06:30
repository = "https://github.com/harrymkt/zluinav"
homepage = "https://github.com/harrymkt/zluinav"
minimum_version = "0.19.2"
license = "MIT"
demo = "https://harrymkt.github.io/zluinav"

[extra.author]
name = "Harry Min Khant"
homepage = "https://harrymkt.github.io"
+++        

# UI Navigation

UI Navigation，或称为 zluinav，是一个专为可访问性而非视觉设计的 Zola 主题，并使用模板和宏使其尽可能简单。由于我是一个盲人开发者，我想尽可能开发可访问的内容，以便视障用户可以使用它们。

此主题也可用于 Hugo，名为 [Hguinav](https://github.com/harrymkt/hguinav)。

[Zola](https://www.getzola.org/) 是一个用 Rust 编写的快速站点生成器，由 tera 作为其模板引擎提供支持，并具有强大的主题创建功能。

[主题演示](https://harrymkt.github.io/zluinav)

## 许可证

此主题根据 [MIT 许可证](https://github.com/harrymkt/zluinav/blob/main/LICENSE.md) 分发。

## zluinav 主题的特性

- 可访问性；Zluinav 旨在尽可能易于访问，特别是对于盲人和视障人士。这是通过使用可访问性标签（如 ARIA）和其他可能的可访问性功能来实现的。
- SEO 友好。
- 配置；使用广泛的 [配置](https://harrymkt.github.io/zluinav/docs#extra-variables) 参数来控制你的站点，从主配置文件到 [Front Matter 配置](https://harrymkt.github.io/zluinav/docs/extra/frontmadder) 等等。
- 启用了分页的博客；可以通过将内容文件夹中的 blog 目录复制到新博客的新目录来创建多个博客。这意味着你可以在一个站点中拥有多个博客。实际上，Zola 没有内置的帖子，但使用版块是可能的。请注意，blog 以外的目录需要在其 `_index.md` 文件中手动将 `template` 设置为 `blogpage.html` 并将 `page_template` 设置为 `section_paginated.html`。
- 文档站点；通过使用专为文档设计的内置 1subsection 模板构建可访问的 [文档站点](https://harrymkt.github.io/zluinav/docs/documentation)。
- 多语言；用多种语言构建你的站点。
- [自定义菜单](https://harrymkt.github.io/zluinav/docs/extra/config#menus) 支持。
- 分类法支持。
- 内置 [搜索](https://harrymkt.github.io/zluinav/docs/search) 支持，有多种搜索格式可供选择。
- 通过基础模板和块可自定义 extrahead、header、navigation 和 footer。
- 复制代码块；添加代码块，然后可以使用按钮复制并在可用时显示代码语言，由 JavaScript 辅助。
- 变量；在页面内容中添加 [变量](https://harrymkt.github.io/zluinav/docs/writing)，以便在站点生成期间替换。
- 本地日期显示；无论日期设置在哪个时区，都在用户的本地时区显示日期。
- 使用广泛的宏和短代码来缩短内容长度。
- 能够为配置和每页 Front Matter 切换 JavaScript 的使用。
- 全面的文档；Zluinav 提供完整的综合文档，包括可能的模板、短代码、块、可配置参数等，一切随更新而变。

## 安装

使用 git clone:
```bash
cd themes
git clone https://github.com/harrymkt/zluinav.git
```
或者 [手动下载](https://github.com/harrymkt/zluinav/archive/refs/heads/main.zip) 并粘贴到 themes 目录中。

或者，添加到 Git 子模块（推荐）：
```bash
git submodule add --name zluinav https://github.com/harrymkt/zluinav.git themes/zluinav
git submodule update --remote
```

在你的 config.toml 文件中，添加以下内容
```toml
theme = "zluinav"
```

## 自定义

有关更多可自定义选项和配置，请参阅 [文档](https://harrymkt.github.io/zluinav/docs)

## 贡献

欢迎对此主题做出贡献，只要满足以下要求：
- HTML 使用 2 级空格缩进。CSS 和 JavaScript 使用 1 个制表符级别缩进。如果 Markdown 文件需要缩进，请使用 1 个制表符。
- 模板应对视障人士和/或盲人易于访问，并优先考虑可读性。别担心，我会在合并拉取请求之前处理可访问性问题。
- 此主题不需要照片。如果你愿意，你可以使用 CSS 进行视觉设计。
- 创建拉取请求时，建议你：
	- 使用除 main 以外的其他分支；这避免了在你的拉取请求被拒绝时更新的问题。

谢谢！
