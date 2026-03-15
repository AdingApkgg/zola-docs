
+++
title = "sam"
description = "一个简单极简的主题，专注于排版和内容。"
template = "theme.html"
date = 2025-09-24T11:42:47+02:00

[taxonomies]
theme-tags = []

[extra]
created = 2025-09-24T11:42:47+02:00
updated = 2025-09-24T11:42:47+02:00
repository = "https://github.com/janbaudisch/zola-sam.git"
homepage = "https://github.com/janbaudisch/zola-sam"
minimum_version = "0.4.0"
license = "AGPL-3.0"
demo = "https://zola-sam.janbaudisch.dev"

[extra.author]
name = "Jan Baudisch"
homepage = "https://janbaudisch.dev"
+++        

[![Build Status][build-img]][build-url]
[![演示][demo-img]][demo-url]

# Sam

> 一个简单极简的主题，专注于排版和内容。
>
> [hugo-theme-sam][hugo-sam] 的 [Zola][Zola] 移植版。

![截图](screenshot.png)

## 原作

这是 Hugo 主题 [hugo-theme-sam][hugo-sam] ([许可证][upstream-license]) 的移植版。

参见 [`upstream`][upstream] 了解源代码来源。

## 安装

安装此主题最简单的方法是克隆它...

```
git clone https://github.com/janbaudisch/zola-sam.git themes/sam
```

... 或者将其用作子模块。

```
git submodule add https://github.com/janbaudisch/zola-sam.git themes/sam
```

无论哪种方式，你都必须在 `config.toml` 中启用该主题。

```toml
theme = "sam"
```

## 分类法

Sam 支持 `tags` 和 `authors` 分类法。

要使用它们，请在 `config.toml` 中声明它们：

```toml
taxonomies = [
    { name = "tags", rss = true },
    { name = "authors", rss = true }
]
```

在你的页面 Front Matter 中设置它们：

```toml
[taxonomies]
tags = ["some", "tag"]
authors = ["Alice", "Sam"]
```

有关更多详细信息，请参阅 [Zola 文档][taxonomies-docs]。

## 选项

有关示例配置，请参阅 [`config.toml`][config]。

### 菜单

首页上的菜单创建如下：如果设置了 `sam_menu` 变量，则使用它。

```toml
[extra]
sam_menu = [
    { text = "posts", link = "/posts" },
    { text = "about", link = "/about" },
    { text = "github", link = "https://github.com" }
]
```

如果未设置，则会链接 `content` 下的所有版块。

#### 底部菜单

此变量决定菜单（如上所述）是否也会显示在页面底部。

默认值：`false`

```toml
[extra]
sam_bottom_menu = true
```

### `home`

设置菜单和 404 页面中指向首页的所有链接的名称。

默认值：`home`

```toml
[extra]
home = "home"
```

### 日期格式

指定如何显示日期。格式在 [这里][date-format-docs] 描述。

默认值：`%a %b %e, %Y`

```toml
[extra]
date_format = "%a %b %e, %Y"
```

### 字数统计和阅读时间

你可以为整个网站的文章启用或禁用字数统计和阅读时间：

默认值：`true` (两者)

```toml
[extra]
show_word_count = true
show_reading_time = true
```

如果启用，你可以通过 Front Matter 在每个页面上选择退出：

默认值：`false` (两者)

```
+++
[extra]
hide_word_count = true
hide_reading_time = true
+++
```

### 禁用页面页眉

如果你想禁用页面的完整页眉（例如明确不是文章的页面），你可以通过 Front Matter 这样做：

默认值：`false`

```
+++
[extra]
no_header = true
+++
```

### 页脚

要在页面末尾放置一些文本，请设置以下内容：

```toml
[extra.sam_footer]
text = "Some footer text."
```

[build-img]: https://builds.sr.ht/~janbaudisch/zola-sam.svg
[build-url]: https://builds.sr.ht/~janbaudisch/zola-sam
[demo-img]: https://img.shields.io/badge/demo-live-green.svg
[demo-url]: https://zola-sam.janbaudisch.dev
[Zola]: https://getzola.org
[hugo-sam]: https://github.com/victoriadotdev/hugo-theme-sam
[upstream]: https://github.com/janbaudisch/zola-sam/blob/master/upstream
[upstream-license]: https://github.com/janbaudisch/zola-sam/blob/master/upstream/LICENSE
[taxonomies-docs]: https://www.getzola.org/documentation/content/taxonomies
[config]: https://github.com/janbaudisch/zola-sam/blob/master/config.toml
[date-format-docs]: https://docs.rs/chrono/latest/chrono/format/strftime/index.html
