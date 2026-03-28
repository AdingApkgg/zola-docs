
+++
title = "tranquil"
description = "简洁清爽的 Zola 博客主题"
template = "theme.html"
date = 2025-08-20T16:30:36+02:00

[taxonomies]
theme-tags = []

[extra]
created = 2025-08-20T16:30:36+02:00
updated = 2025-08-20T16:30:36+02:00
repository = "https://github.com/TeaDrinkingProgrammer/tranquil.git"
homepage = "https://github.com/TeaDrinkingProgrammer/tranquil"
minimum_version = "0.9.0"
license = "MIT"
demo = "https://teadrinkingprogrammer.github.io/tranquil-demo/"

[extra.author]
name = "TeaDrinkingProgrammer"
homepage = "https://github.com/TeaDrinkingProgrammer"
+++        

![A screenshot (dark theme) of the example page of the demo website](https://github.com/TeaDrinkingProgrammer/tranquil/blob/main/screenshot.png?raw=true)
![A screenshot (light theme) of the example page of the demo website](https://github.com/TeaDrinkingProgrammer/tranquil/blob/main/screenshot-light.png?raw=true)
<br />
A blog 主题，适用于 [Zola](https://www.getzola.org)。风格简洁优雅，使用 Tailwind 构建。基于 [Isunjns Serene theme](https://github.com/isunjn/serene)。

## 演示

-  <https://teadrinkingprogrammer.github.io/tranquil-demo/>
-  我的个人博客：<https://teadrinkingprogrammer.github.io>

## 功能

- 简洁优雅的设计。
- 项目页面：可展示你参与过的项目列表并附带链接。
- 主题切换：无论浏览器偏好如何，都可在浅色与深色主题之间切换。
- 图片缩放（[Lightense](https://github.com/sparanoid/lightense-images)）：点击图片可放大查看。
- 过期提醒：当文章过旧时显示提示。
- 提示框（note、warning、alert 等）可直接在 Markdown 中使用。
- 评论系统支持 [Giscus](https://giscus.app)。
- 数学公式支持 [KaTeX](https://katex.org)。
- 图表与可视化支持 [Mermaid](https://github.com/mermaid-js/mermaid)。

## 致谢

没有 [Isunjns Serene theme](https://github.com/isunjn/serene)，这个主题就不会存在。它本身也非常优秀，推荐一并了解。

当我对布局拿不准时，我经常会参考 [FasterThanLimes blog](https://fasterthanli.me) 的做法。

当然，没有 [Zola](https://getzola.org) 这个网站无法生成；没有 [Tailwind](https://tailwindcss.com/) 它也不会有现在的样子。

## Tranquil 与 Serene

Tranquil 是 Serene 的一个分支。选择 fork 并不是因为 Serene 不好，而是我想实践一段时间 Tailwind，而重写一个博客主题正是很合适的方式。

Tranquil 与 Serene 的主要、几乎也是唯一差异，是样式层从零开始使用 Tailwind 构建。图标也做了调整，以更好地契合 Tailwind 风格。

## 用法

- 请查看 `main` 分支中的 [USAGE.md](./USAGE.md)。

## 贡献

- 在做任何非小改动前，建议先提交 issue，以便先讨论改动方案。

        
