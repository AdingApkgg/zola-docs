
+++
title = "Kita"
description = "Kita 是一个干净、优雅且简单的 Zola 博客主题。"
template = "theme.html"
date = 2025-10-02T20:07:02+08:00

[taxonomies]
theme-tags = []

[extra]
created = 2025-10-02T20:07:02+08:00
updated = 2025-10-02T20:07:02+08:00
repository = "https://github.com/st1020/kita.git"
homepage = "https://github.com/st1020/kita"
minimum_version = "0.17.0"
license = "MIT"
demo = "https://kita-zola.pages.dev"

[extra.author]
name = "st1020"
homepage = "https://st1020.com"
+++        

# Kita

Kita 是一个干净、优雅且简单的 Zola 博客主题。

此主题基于 Hugo 主题 [hugo-paper](https://github.com/nanxiaobei/hugo-paper)，并添加了一些功能。

[演示](https://kita-zola.pages.dev)

![截图](https://raw.githubusercontent.com/st1020/kita/main/screenshot.png)

## 特性

- 易于使用和修改
- 无预设限制（此主题不限制你的内容目录结构、分类法名称等。它适用于所有 zola 站点。）
- 注入支持
- 暗色模式
- 响应式设计
- 社交图标
- 分类法支持
- 项目页面
- 归档页面
- 目录和浮动侧边目录
- Admonition 短代码
- SEO 友好
- 使用 [Giscus](https://giscus.app/) 评论
- 使用 [KaTeX](https://katex.org/) 进行数学符号表示
- 使用 [Mermaid](https://mermaid.js.org/) 绘制图表

## 安装

安装此主题最简单的方法是将此仓库克隆到 themes 目录：

```sh
git clone https://github.com/st1020/kita.git themes/kita
```

或者作为子模块使用：

```sh
git submodule add https://github.com/st1020/kita.git themes/kita
```

然后在 `config.toml` 中将 `kita` 设置为你的主题。

```toml
theme = "kita"
```

## 配置

请参阅 [config.toml](https://github.com/st1020/kita/blob/main/config.toml) 中的 `extra` 部分作为示例。

## 注入支持

你可以轻松使用注入在你的站点添加新功能，而无需修改主题本身。

要使用注入，你需要将一些 HTML 文件添加到 `templates/injects` 目录。

可用的注入点有：`head`, `header_nav`, `body_start`, `body_end`, `page_start`, `page_end`, `footer`, `page_info`。

例如，要加载自定义脚本，你可以添加一个 `templates/injects/head.html` 文件：

```html
<script src="js-file-path-or-cdn-url.js"></script>
```

## 许可证

[MIT License](https://github.com/st1020/kita/blob/main/LICENSE)

Copyright (c) 2023-present, st1020
