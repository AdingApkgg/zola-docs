
+++
title = "hallo"
description = "一个介绍你自己的单页主题。"
template = "theme.html"
date = 2025-09-22T20:09:00+02:00

[taxonomies]
theme-tags = []

[extra]
created = 2025-09-22T20:09:00+02:00
updated = 2025-09-22T20:09:00+02:00
repository = "https://github.com/flyingP0tat0/zola-hallo.git"
homepage = "https://github.com/janbaudisch/zola-hallo"
minimum_version = "0.4.0"
license = "MIT"
demo = "https://zola-hallo.janbaudisch.dev"

[extra.author]
name = "Jan Baudisch"
homepage = "https://janbaudisch.dev"
+++        

# Hallo

> 一个介绍你自己的单页主题。
>
> [hallo-hugo][hallo-hugo] 的 [Zola][zola] 移植版。

![截图](screenshot.png)

## 原作

这是 Hugo 主题 [hallo-hugo][hallo-hugo] ([许可证][upstream-license]) 的移植版。

## 安装

安装此主题最简单的方法是克隆它...

```
git clone https://github.com/janbaudisch/zola-hallo.git themes/hallo
```

... 或者将其用作子模块。

```
git submodule add https://github.com/janbaudisch/zola-hallo.git themes/hallo
```

无论哪种方式，你都必须在 `config.toml` 中启用该主题。

```toml
theme = "hallo"
```

### 介绍

介绍文本取自 `content/_index.md`。

#### 模板

或者，可以通过以下配置选项从 `templates/partials/introduction.html` 包含它：

```toml
[extra]
hallo_use_introduction_template = true
```

## 选项

有关示例配置，请参阅 [`config.toml`][config]。

### 作者

给定的名称将用于 'I am ...' 文本。

默认值：`Hallo`

```toml
[extra.author]
name = "Hallo"
```

### 问候语

该字符串将用作问候语。

默认值：`Hello!`

```toml
[extra]
greeting = "Hello!"
```

### `iam`

此变量定义 `I am` 文本，你可能想将其换成另一种语言。

默认值：`I am`

```toml
[extra]
iam = "I am"
```

### 链接

链接显示在介绍下方。它们使用 [Font Awesome][fontawesome] 样式化，你可以选择图标集（默认为 [brands][fontawesome-brands]）。

```toml
[extra]
links = [
    { title = "E-Mail", url = "mailto:mail@example.org", iconset = "fas", icon = "envelope" },
    { title = "GitHub", url = "https://github.com", icon = "github" },
    { title = "Twitter", url = "https://twitter.com", icon = "twitter" }
]
```

### 主题

更改使用的颜色。

```toml
[extra.theme]
background = "#6FCDBD"
foreground = "#FFF" # 文本和肖像边框
hover = "#333" # 链接悬停
```

[zola]: https://www.getzola.org
[hallo-hugo]: https://github.com/EmielH/hallo-hugo
[fontawesome]: https://fontawesome.com
[fontawesome-brands]: https://fontawesome.com/icons?d=gallery&s=brands&m=free
[upstream-license]: https://github.com/janbaudisch/zola-hallo/blob/master/upstream/LICENSE
[config]: https://github.com/janbaudisch/zola-hallo/blob/master/config.toml
