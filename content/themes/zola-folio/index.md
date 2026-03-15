
+++
title = "zola-folio"
description = "Jekyll *folio 主题的 Zola 移植版"
template = "theme.html"
date = 2024-12-31T14:02:39-06:00

[taxonomies]
theme-tags = []

[extra]
created = 2024-12-31T14:02:39-06:00
updated = 2024-12-31T14:02:39-06:00
repository = "https://github.com/evjrob/zola-folio"
homepage = "https://github.com/evjrob/zola-folio"
minimum_version = "0.19.2"
license = "MIT"
demo = "https://zola-folio.pages.dev/"

[extra.author]
name = "Everett Robinson"
homepage = "http://everettsprojects.com"
+++        

# *folio

[![zola-folio](static/img/zola-folio.png)](https://zola-folio.pages.dev/)

*folio 是一个 [Zola](https://www.getzola.org) 主题，移植自 [Lia Boegev 的原始 Jekyll 主题](https://github.com/bogoli/-folio/tree/master)。

**[在线演示](https://zola-folio.pages.dev/)**

## 特性

- [x] 菜单栏
- [x] 社交链接
- [x] 标签
- [x] MathJax
- [x] 搜索
- [x] 可自定义颜色
- [x] SEO 标签
- [ ] 多语言支持

## 安装

在你的 zola 站点的 git 仓库中：

### 将主题添加为 git 子模块：

```bash
git submodule add https://github.com/evjrob/zola-folio themes/zola-folio
git submodule update --init --recursive
git submodule update --remote --merge
```

### 或者直接克隆主题到你的 themes 目录：

```bash
git clone https://github.com/evjrob/zola-folio themes/zola-folio
```

然后在你的 config.toml 文件中设置 `theme = "zola-folio"`。你现在可以通过在终端运行 `zola serve` 并导航到命令显示的 localhost URL 来本地测试主题。

## 配置

### 菜单栏

顶部菜单栏中的项目可以通过 config.toml 中的 `extra.menu_items` 设置进行控制：

```toml
menu_items = [
    {name = "about", url = "/pages/about"},
    {name = "projects", url = "/pages/projects"},
    {name = "photography", url = "/pages/photography"},
]
```

### 关于页面的社交联系方式

如果你有一个关于页面，你可以使用页面 Front Matter 中的 `extra.socials` 设置添加社交联系链接：

```toml
+++
title = "about"
template = "about.html"
[extra]
socials = [
	{name = "email", uri = "mailto:you@example.com"},
	{name = "github", uri = "https://github.com"},
	{name = "instagram", uri = "https://www.instagram.com/"},
	{name = "bluesky", uri = "https://bsky.app/"}
]
+++
```

### MathJax 支持

可以通过在 config.toml 中设置 `extra.math` 来启用 MathJax：

```toml
[extra]
math = true
```
[示例](https://zola-folio.pages.dev/math/).

### 搜索

使用 elasticlunr.js 进行搜索：

```toml
default_language = "en"
build_search_index = true

[search]
include_title = true
include_description = true
include_path = true
include_content = true
index_format = "elasticlunr_json"
```

### 可自定义颜色

只需在 config.toml 中设置 `extra.theme_color`：

```toml
[extra]
theme_color = "red"|"blue"|"green"|"purple"
```
如果现有的颜色不合你意，你可以通过添加一个 **sass/color/custom.scss** 文件来创建你自己的颜色，内容如下：

```scss
:root {
    --theme-color: #ffffff;
    --theme-color-light: #ffffff;
}
```
然后设置 `theme_color = "custom"`。

### SEO 标签

典型的 `<meta>` 标签（包括 Open Graph 和 Twitter）会自动使用每篇文章 Front Matter 中的信息进行设置。为了确保为 Open Graph 和 Twitter 卡片设置图片，请确保 Front Matter 包含 `extra.feature_image` 值：

```toml
[extra]
feature_image = "my_image.ext"
```
