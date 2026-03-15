
+++
title = "Zulma"
description = "一个基于 bulma.css 的 Zola 主题"
template = "theme.html"
date = 2020-05-10T10:53:40Z

[taxonomies]
theme-tags = []

[extra]
created = 2020-05-10T10:53:40Z
updated = 2020-05-10T10:53:40Z
repository = "https://github.com/Worble/Zulma.git"
homepage = "https://github.com/Worble/Zulma"
minimum_version = "0.6.0"
license = "MIT"
demo = "https://festive-morse-47d46c.netlify.com/"

[extra.author]
name = "Worble"
homepage = ""
+++        

# Zulma

一个 Bulma 的 Zola 主题。点击 [这里](https://festive-morse-47d46c.netlify.com/) 查看在线预览。

![Zulma 截图](/screenshot.png)

## 目录

- Zulma
  - 内容
  - 安装
  - Javascript
    - 来源
    - 构建
  - 选项
    - 分页
    - 分类法
    - 菜单链接
    - 品牌
    - 搜索
    - 标题
    - 主题化
  - 原作
  - 已知 Bug

## 安装

首先将此主题下载到你的 `themes` 目录：

```bash
cd themes
git clone https://github.com/Worble/Zulma
```

然后在你的 `config.toml` 中启用它：

```toml
theme = "Zulma"
```

就是这样！不需要更多的配置，但它可能看起来有点基础。前往选项部分查看你可以设置什么以获得更多自定义性。

## JavaScript

### 来源

所有源 javascript 文件都在 `javascript/src` 中。以下是 javascript 文件及其用途和来源的列表。所有文件都以 `zulma_` 为前缀，以避免名称冲突。

- `zulma_search.js` - 当用户在导航栏上的搜索框中输入时使用（如果启用）。取自 [Zola 的站点](https://github.com/getzola/zola/blob/6100a43/docs/static/search.js)。
- `zulma_navbar.js` - 用于移动端导航栏切换。取自 Bulmaswatch 的 [bulma 模板](https://github.com/dansup/bulma-templates/blob/6263eb7/js/bulma.js)
- `zulma_switchcss.js` - 用于切换主题（如果启用）。

### 构建

JavaScript 文件由 babel 转译，由 webpack 压缩，生成 sourcemap，然后全部放置在 `static/js` 中。仓库已经包含转译和压缩后的文件及其对应的 sourcemap，因此你无需做任何事情即可使用这些文件。如果你更喜欢自己构建它，请随意检查 js 文件，然后运行构建过程（请确保你已安装 [node, npm](https://nodejs.org/en/) 和可选的 [yarn](https://yarnpkg.com/lang/en/)）：

```bash
cd javascript
yarn
yarn webpack
```

### Github 警告

你可能会收到关于 JavaScript 依赖项漏洞的警告。这不应该是一个问题，因为我们只有开发依赖项，而且它们都不会到达最终用户，但是如果你不想自己运行构建过程，并且想阻止 Github 骚扰你的安全警告，请随意在提交时删除顶级 `javascript` 文件夹。

## 选项

### 分页

Zulma 对你的项目不做任何假设。你可以自由地分页你的内容文件夹或你的分类法，它会相应地适应。例如，编辑或创建版块（`content/_index.md`）并设置分页：

```toml
paginate_by = 5
```

这是在内部处理的，不需要用户输入。

### 分类法

Zulma 内部已经设置了 3 个分类法：`tags`, `cateogories` 和 `authors`。像这样在你的 config.toml 中设置这三个中的任何一个：

```toml
taxonomies = [
    {name = "categories"},
    {name = "tags", paginate_by = 5, rss = true},
    {name = "authors", rss = true},
]
```

并在内容文件中设置它们中的任何一个：

```toml
[taxonomies]
categories = ["Hello world"]
tags = ["rust", "ssg", "other", "test"]
authors = ["Joe Bloggs"]
```

这将导致该元数据显示在文章上，要么在标题上显示名称，要么在底部显示标签和分类，并启用这些页面。

制作你自己的分类法也被设计得尽可能简单。首先，将其添加到你的 cargo.toml

```toml
taxonomies = [
    {name = "links"},
]
```

并在你的 templates 中制作相应的文件夹，在这种情况下：`templates\links`，以及必要的文件：`templates\links\list.html` 和 `templates\links\single.html`

然后对于每一个，只需继承该页面的分类法主页面。在渲染内容块之前，你可以选择设置一个名为 `title` 的变量以在该页面上显示 hero，否则它将使用该分类法的默认值。

在 `single.html` 中：

```jinja
{%/* extends "Zulma/templates/taxonomy_single.html" */%}
```

在 `list.html` 中：

```jinja
{%/* extends "Zulma/templates/taxonomy_list.html" */%}

{%/* block content */%}
{%/* set title = "These are all the Links"*/%}
{{/* super() */}}
{%/* endblock content */%}
```

### 菜单链接

在 extra 中，设置 `zulma_menu` 为一个项目列表将导致它们渲染到顶部菜单栏。它有两个参数，`url` 和 `name`。这些 _必须_ 设置。如果你在 url 中放入 \$BASE_URL，它会自动被替换为实际的站点 URL。这是允许用户导航到你的分类法的最简单方法：

```toml
[extra]
zulma_menu = [
    {url = "$BASE_URL/categories", name = "Categories"},
    {url = "$BASE_URL/tags", name = "Tags"},
    {url = "$BASE_URL/authors", name = "Authors"}
]
```

在移动设备上，使用 javascript 渲染下拉汉堡菜单。如果页面检测到客户端机器禁用了 javascript，它将优雅地降级为始终显示菜单（这不漂亮，但保持了站点的功能）。

### 品牌

在 extra 中，设置 `zulma_brand` 将导致在顶部菜单栏的左上角显示品牌图片。此链接将始终导回首页。它有两个参数，`image`（可选）和 `text`（必需）。`image` 将品牌设置为指定位置的图片，`text` 将为此图片提供 alt 文本。如果你在 url 中放入 \$BASE_URL，它会自动被替换为实际的站点 URL。如果未设置 `image`，品牌将仅为指定的文本。

```toml
[extra]
zulma_brand = {image = "$BASE_URL/images/bulma.png", text = "Home"}
```

### 搜索

Zulma 内置搜索功能。只要在 `config.toml` 中将 `build_search_index` 设置为 `true`，顶部导航栏上就会出现一个搜索输入框。这需要启用 javascript 才能通过功能；如果页面检测到客户端机器禁用了 javascript，它将隐藏自己。

搜索是无耻地从 [Zola 的站点](https://github.com/getzola/zola/blob/master/docs/static/search.js) 窃取的。谢谢，Vincent！

### 标题

在 extra 中，设置 `zulma_title` 将在索引页上设置一个 hero 横幅，并在其中显示该标题。

```toml
[extra]
zulma_title = "Blog"
```

如果你想搞点花样，你可以像这样使用 sass 在后面设置一张图片：

```scss
.index .hero-body {
  background-image: url(https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Plum_trees_Kitano_Tenmangu.jpg/1200px-Plum_trees_Kitano_Tenmangu.jpg);
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
  background-color: rgba(0, 0, 0, 0.6);
  background-blend-mode: overlay;
}
```

这将在 hero 后面设置图片，并将其变暗，以便主要文本仍然易于阅读。

### 主题化

在 extra 中，将 `zulma_theme` 设置为有效值会将当前的配色方案更改为该值。所有主题均取自 [Bulmaswatch](https://jenil.github.io/bulmaswatch/)。有效的主题值为：

- default
- darkly
- flatly
- pulse
- simplex
- lux
- slate
- solar
- superhero

所有有效主题也可以在 `theme.toml` 中的 `extra.zulma_themes` 变量下找到。选择无主题将设置 default 为主题。设置无效的主题值将导致站点渲染不正确。

```toml
[extra]
zulma_theme = "darkly"
```

此外，在 extra 中，你还可以设置 `zulma_allow_theme_selection` 布尔值。将其设置为 `true` 将允许页脚中的菜单允许用户选择他们自己的主题。此选项将把他们的主题选择存储在本地存储中，并将其应用到每个页面，假设 `zulma_allow_theme_selection` 仍然为真。这需要启用 javascript 才能通过功能；如果页面检测到客户端机器禁用了 javascript，它将隐藏自己。

每个主题都包含整个 Bulma，大约 180kb。如果你在空间严重受限的服务器上运行，那么我建议你删除你不使用的每个主题，无论是从源还是从 `/public`。显然，这样做会导致 `zulma_allow_theme_selection` 工作不正常，所以确保你要么在 `config.toml` 中覆盖 `extra.zulma_themes` 以仅显示你剩下的主题，要么根本不启用此选项。

```toml
[extra]
zulma_allow_theme_selection = true
```

## 原作

此模板基于 [Free Bulma Templates](https://bulmatemplates.github.io/bulma-templates/) 上的 [博客模板](https://bulmatemplates.github.io/bulma-templates/templates/blog.html)。所有主题均取自 [Bulmaswatch](https://jenil.github.io/bulmaswatch/)。背后的代码最初改编自 [after-dark](https://github.com/getzola/after-dark/blob/master/README.md) zola 模板。

## 已知 Bug

- 如果启用了用户主题切换并且用户选择了不同于默认的主题，页面渲染将会引入轻微的延迟，因为 css 会通过 javascript 被换出和换入。当使用暗色主题时这一点尤为明显，因为它会在回到黑色之前闪烁白色。这比未样式化内容或旧主题的替代闪烁要好，但仍然很烦人。我不知道有什么办法可以解决这个问题，但有了浏览器缓存，它应该足够快，不会造成严重问题。
