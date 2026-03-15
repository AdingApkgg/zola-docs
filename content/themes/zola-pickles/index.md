
+++
title = "pickles"
description = "一个适用于 Zola 的现代、简单、干净的博客主题。"
template = "theme.html"
date = 2025-12-07T22:02:02-07:00

[taxonomies]
theme-tags = []

[extra]
created = 2025-12-07T22:02:02-07:00
updated = 2025-12-07T22:02:02-07:00
repository = "https://github.com/lukehsiao/zola-pickles.git"
homepage = "https://github.com/lukehsiao/zola-pickles"
minimum_version = "0.19.0"
license = "BlueOak-1.0.0"
demo = "https://zola-pickles.pages.dev/"

[extra.author]
name = "Luke Hsiao"
homepage = "https://luke.hsiao.dev"
+++        

<h1 align="center">
    🥒<br>
    zola-pickes
</h1>
<div align="center">
    <strong>Pickles 是一个适用于 <a href="https://www.getzola.org/">Zola</a> 的干净、响应式的博客主题，基于同名的 <a href="https://github.com/mismith0227/hugo_theme_pickles">Hugo 主题</a>。</strong>
</div>
<br>
<div align="center">
  <a href="https://zola-pickles.pages.dev/">
    <img src="https://img.shields.io/badge/demo-website-forestgreen" alt="演示网站"></a>
  <a href="https://github.com/lukehsiao/zola-pickles/blob/main/LICENSE.md">
    <img src="https://img.shields.io/badge/license-BlueOak--1.0.0-blue" alt="许可证">
  </a>
</div>
<br>

![pickles 截图](https://github.com/lukehsiao/zola-pickles/blob/main/screenshot.png?raw=true)

## 安装

首先将此主题下载到你的 `themes` 目录：

```bash
$ cd themes
$ git clone https://github.com/lukehsiao/zola-pickles.git
```
然后在你的 `config.toml` 中启用它：

```toml
theme = "zola-pickles"
```

此主题要求将文章放在 `content` 文件夹的根目录下，并启用分页，例如在 `content/_index.md` 中。

```
+++
paginate_by = 5
sort_by = "date"
insert_anchor_links = "right"
+++
```

## 参考指南

## 配置选项

```toml
[extra]
# 显示在主标题下方的一行
subtitle = "Example subtitle"

# 显示在页面页脚的文本
copyright = "Copyright authors year"

# 你的 Google Analytics ID
analytics = ""

# 见下文
katex_enable = false

# 见下文
instantpage_enable = false
```

`config.toml` 中包含一个完整的示例配置。

请注意 pickles 还期望在 Zola 配置中设置 `title` 和 `description`。

### KaTeX 数学公式支持

此主题包含使用 [KaTeX 公式](https://katex.org/) 的数学公式支持，可以通过在 `config.toml` 的 `extra` 部分设置 `katex_enable = true` 来启用。

启用此扩展后，可以在文档中使用 `katex` 短代码：
* `{%/* katex(block=true) */%}\KaTeX{%/* end */%}` 用于排版数学公式块，
  类似于 LaTeX 中的 `$$...$$`

### Figure 短代码

figure 短代码便于为图片添加标题。

```
{%/* figure(link="https://www.example.com/", src="https://www.example.com/img.jpeg", alt="sample alt text") */%}
Your caption here.
{%/* end */%}
```

### Table 短代码

table 短代码便于制作移动端友好的表格（居中且带有溢出滚动条）。

```
{%/* table() */%}
| Item         | Price | # In stock |
| :----------- | ----: | ---------: |
| Juicy Apples |  1.99 |        739 |
| Bananas      |  1.89 |          6 |
{%/* end */%}
```

### Fontawesome

此主题包含 fontawesome，因此可以直接使用 fontawesome 图标。

### Instant.page

此主题包含 instant.page 预取。可以通过在 `config.toml` 的 `extra` 部分设置 `instantpage_enable = true` 来启用。

## 显示文章摘要

默认情况下，如果没有提供使用 `<!-- more -->` 的适当 [页面摘要](https://www.getzola.org/documentation/content/page/#summary)，主题将使用文章的前 280 个字符作为摘要。
为了获得更合理的摘要，我们建议使用手动的 more 指示符。
