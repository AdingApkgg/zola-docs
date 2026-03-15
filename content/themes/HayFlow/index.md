
+++
title = "HayFlow"
description = "HayFlow 是一个极简且完全模块化的 Zola 主题，适合任何希望拥有自己落地页的人。"
template = "theme.html"
date = 2023-03-15T12:00:30+01:00

[taxonomies]
theme-tags = []

[extra]
created = 2023-03-15T12:00:30+01:00
updated = 2023-03-15T12:00:30+01:00
repository = "https://gitlab.com/cyril-marpaud/hayflow.git"
homepage = "https://gitlab.com/cyril-marpaud/hayflow"
minimum_version = "0.4.0"
license = "CC-BY-SA 4.0"
demo = "https://cyril-marpaud.gitlab.io"

[extra.author]
name = "Cyril Marpaud"
homepage = "https://cyril-marpaud.gitlab.io"
+++        

# HayFlow - 模块化 Zola 主题

## 关于

<div align="center">
![预览截图](https://gitlab.com/cyril-marpaud/hayflow/-/raw/main/screenshot.png "预览截图")
</div>

[HayFlow](https://gitlab.com/cyril-marpaud/hayflow) 是一个模块化落地页，作为 [Zola](https://www.getzola.org)（一个用 [Rust](https://www.rust-lang.org) 编写的静态站点生成器）的主题制作。它具有带有粒子背景的暗色主题、用于导航的垂直箭头以及几种卡片类型，你可以自由包含这些卡片以最适合你的需求。几乎所有 UI 元素都经过微妙的动画处理，以传达专业的外观（虽然我不是设计师 🤷 仅仅是一个 [嵌入式系统工程师](https://www.linkedin.com/in/cyrilmarpaud)）。

它的设计目的是只需要编辑 [Markdown](https://www.markdownguide.org)（没有 HTML/CSS），但如果你需要，可以随意编辑。如果你实现了一个新的卡片类型，我很乐意审查 [Merge Request](https://gitlab.com/cyril-marpaud/hayflow/-/merge_requests)！

[[_TOC_]]

## 在线演示

查看 [我的个人网站](https://cyril-marpaud.gitlab.io) 以获取使用此主题在几分钟内可以完成的示例。其源代码也可以在我的 [Gitlab 网站仓库](https://gitlab.com/cyril-marpaud/cyril-marpaud.gitlab.io) 中作为示例获得。

## 构建于

- [Zola](https://www.getzola.org)
- [Particles.js](https://vincentgarreau.com/particles.js/)
- [Font Awesome](https://fontawesome.com)
- [Modern Normalize](https://github.com/sindresorhus/modern-normalize)
- 灵感来自 [particle-zola](https://github.com/svavs/particle-zola)，另一个主题。

## 快速开始

初始化一个 Zola 网站并安装 HayFlow：
```bash
zola init mywebsite
cd mywebsite
git clone git@gitlab.com:cyril-marpaud/hayflow.git themes/hayflow
```

在 `config.toml` 文件顶部添加 `theme = "hayflow"` 以告诉 Zola 使用 HayFlow（如 [文档](https://www.getzola.org/documentation/themes/installing-and-using-themes/) 中所述）。

最后，运行...

```bash
zola serve
```
...并前往 [http://localhost:1111](http://localhost:1111) 查看带有默认名称（John Doe）的落地页。

## 落地页自定义

自定义落地页归结为两件事：

- 将 `name` 和 `links` 变量添加到 `config.toml` 的 `[extra]` 部分（`links` 是可选的。如果你的名字是 John Doe，`name` 也是可选的）
- 将 `roles` 变量添加到 `content/_index.md` 的 `[extra]` 部分（也是可选的）

区别在于你可能需要将 `roles` 翻译成其他语言。为了实现这一点，它们必须放在 MarkDown 文件中。有关更多信息，请参阅多语言支持。

- `name` 不言自明。
- `roles` 是一个字符串数组。每个字符串显示在单独的行上。
- `links` 是 `{icon, url}` 对象的数组。你可以在这里使用 [Font Awesome](https://fontawesome.com/search?o=r&m=free) 中的任何 **免费** 图标，你只需要图标的代码。[信封图标](https://fontawesome.com/icons/envelope?s=solid&f=classic) 的代码是 `fa-solid fa-envelope`。[披萨切片图标](https://fontawesome.com/icons/pizza-slice?s=solid&f=classic) 的代码是 `fa-solid fa-pizza-slice`。

这是自定义后 `config.toml` 的 `[extra]` 部分可能的样子：

```TOML
[extra]
name = { first = "ninja", last = "turtle" }

links = [
   { icon = "fa-solid fa-envelope", url = "mailto:slice@pizza.it" },
   { icon = "fa-solid fa-pizza-slice", url = "https://en.wikipedia.org/wiki/Pizza" },
]
```

这是 `content/_index.md` 的自定义版本：

```TOML
+++
[extra]
roles = ["Green 🟢", "Turtle 🐢", "Pizza enthusiast 🍕"]
+++
```

## 添加版块

在 `content` 目录内，创建一个 `pizza` 文件夹并在其中放置此 `_index.md` 文件：

```TOML
+++
title = "Pizza"
+++

What a mouthful !
```

然后，将此 `sections` 变量（字符串数组）添加到 `config.toml` 的 `[extra]` 部分：

```TOML
[extra]
sections = ["pizza"]
```

一个新的指向该版块的内部链接将出现在落地页上。点击它看看会发生什么！这被称为“简单卡片”版块。

## 自定义版块

HayFlow 目前支持三种卡片类型：`simple`、`columns` 和 `list`。如果未指定，类型将默认为 `simple`。要更改它，请将 `card_type` 变量添加到 `_index.md` 的 `[extra]` 部分：

```TOML
+++
title = "Pizza"

[extra]
card_type = "simple"
+++

What a mouthful !
```

### 列卡片

添加一个新版块并将其卡片类型设置为 `columns`。然后，在 `_index.md` 文件旁边，创建另外三个文件：`one.md`、`two.md` 和 `three.md`。这些将是你新披萨的配料。它们的内容类似于 `_index.md`：

```TOML
+++
title = "Tomato"

[extra]
icons = ["fa-solid fa-tomato"]
+++

The basis of any self-respecting pizza. It is the edible berry of the plant Solanum lycopersicum.
```

`icons` 变量是可选的。

### 列表卡片

添加一个新版块并将其卡片类型设置为 `list`。然后，在 `_index.md` 文件旁边，创建另外三个文件：`one.md`、`two.md` 和 `three.md`。这些将是你最喜欢的披萨。它们的内容类似于 `_index.md`：

```TOML
+++
title = "Margherita"

[extra]
link = "https://en.wikipedia.org/wiki/Pizza_Margherita"
+++

Margherita pizza is a typical [Neapolitan pizza](https://en.wikipedia.org/wiki/Neapolitan_pizza), made with San Marzano tomatoes, mozzarella cheese, fresh basil, salt, and extra-virgin olive oil.
```

`link` 变量是可选的。

## 多语言支持

HayFlow 开箱即支持多语言网站。

### 声明更多语言

在 `config.toml` 中，添加你想要支持的语言，如下所示：

```TOML
default_language = "fr"
[translations]
flag = "🇫🇷"

[languages.en]
[languages.en.translations]
flag = "🇬🇧"

[languages.italian]
[languages.italian.translations]
flag = "🇮🇹"
```

这将使右上角的语言选择块可见。它由指向网站翻译版本的可点击链接组成。
`flag` 变量是可选的，你可以使用简单的文本而不是 emoji 旗帜。如果未指定，它将默认为你为该语言选择的国家代码（本例中为 `fr`、`en` 和 `italian`）。

### 翻译内容

现在需要将 `content` 文件夹中的每个 `.md` 文件翻译成之前在 `config.toml` 中声明的每种其他语言。

按照上面的示例（三种语言，法语、英语和意大利语）并给定此初始文件树：

```
content/
   _index.md
   pizzas/
      _index.md
      margherita.md
      capricciosa.md
```

为了完成翻译，最终的文件树应该如下所示：

```
content/
   _index.md
   _index.en.md
   _index.italian.md
   pizzas/
      _index.md
      _index.en.md
      _index.italian.md
      margherita.md
      margherita.en.md
      margherita.italian.md
      capricciosa.md
      capricciosa.en.md
      capricciosa.italian.md
```

### 列表卡片

此外，如果你的网站包含任何“列表卡片”版块，你可能希望在其 `[extra]` 部分指定一个 `discover` 变量，如下所示：

```TOML
+++
title = "List Card Section"

[extra]
card_type = "list"
discover = "Découvrir"
+++
```

## 我是谁

我叫 Cyril Marpaud，我是一名嵌入式系统自由工程师和 Rust 爱好者 🦀 我有近 10 年的经验，目前居住在里昂（法国）。

<div align="center">

[![LinkedIn][linkedin-shield]][linkedin-url]

[linkedin-url]: https://www.linkedin.com/in/cyrilmarpaud/
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=grey&logoColor=blue

</div>
