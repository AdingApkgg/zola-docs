
+++
title = "Daisy"
description = "基于 TailwindCSS 和 DaisyUI 的美观且快速响应的主题。"
template = "theme.html"
date = 2025-10-04T19:56:32+02:00

[taxonomies]
theme-tags = ['multilingual', 'responsive', 'search']

[extra]
created = 2025-10-04T19:56:32+02:00
updated = 2025-10-04T19:56:32+02:00
repository = "https://codeberg.org/winterstein/zola-theme-daisy.git"
homepage = "https://codeberg.org/winterstein/zola-theme-daisy"
minimum_version = "0.19.0"
license = "MIT"
demo = "https://zola-daisy.winterstein.biz"

[extra.author]
name = "Adrian Winterstein"
homepage = "https://www.winterstein.biz"
+++        

# Daisy Theme

> 你可以在 [Codeberg](https://codeberg.org/winterstein/zola-theme-daisy) 和 [GitHub](https://github.com/awinterstein/zola-theme-daisy) 上找到此主题。

一个美观且快速的 [Zola](https://www.getzola.org/) 主题，基于 [TailwindCSS](https://tailwindcss.com) 和 [DaisyUI](https://daisyui.com) 构建，包含 37 种不同的配色方案。查看 *autumn* 配色示例：

![截图](https://codeberg.org/awinterstein/zola-theme-daisy/raw/branch/main/screenshot.png)

该主题是响应式的，在移动设备上效果很好：

<img src="https://codeberg.org/awinterstein/zola-theme-daisy/raw/branch/main/screenshot-mobile.png" alt="移动端截图" width="200"/>

## 特性

* 响应式设计（桌面和移动端效果俱佳）
* 自动选择暗色/亮色模式
* 包含 37 种配色方案
* 可自定义导航栏和页脚（带有社交链接）
* 可与任何 Zola 分类法（如标签、分类）一起使用
* 搜索功能
* 多语言支持
* 分页
* 可自定义 favicon
* 404 错误页面

### 样式

Daisy 主题支持 DaisyUI 的所有 [内置颜色主题](https://daisyui.com/docs/themes/#enable-a-built-in-theme) 以及我为自己的网站创建的亮色和暗色配色方案。颜色主题甚至可以在运行时切换。

![DaisyUI 颜色主题](https://codeberg.org/winterstein/zola-theme-daisy/raw/branch/main/daisyui-themes.png)

## 快速开始

该主题的安装与其他 Zola 主题相同。正如 [官方文档](https://www.getzola.org/documentation/themes/installing-and-using-themes/) 中所述。因此，首先需要将其添加为 git 子模块：

```bash
cd my-zola-website
git submodule add -b main \
    https://codeberg.org/winterstein/zola-theme-daisy.git \
    themes/daisy
```

请确保将其添加到 Zola 目录中的路径 `themes/daisy`。如果添加到其他目录，翻译和图标将无法工作。

作为第二步，可以在网站的 `config.toml` 文件中启用它：

```toml
theme = "daisy"
```

要开始使用此主题创建新的 Zola 网站，你也可以直接检出/分叉 [示例仓库](https://codeberg.org/winterstein/zola-theme-daisy-example) 并根据需要进行调整。该仓库已经包含基于 Zola 的网站的结构和配置。

## 配置

有关 `config.toml` 文件中主题的可能配置信息，请参阅以下部分。

### 配色方案

设置亮色和暗色配色方案：

```toml
daisyui_theme_light = "light"
daisyui_theme_dark = "dark"
```

有关所有可能的标识符，请参阅 [`theme.toml`](theme.toml) 中的 `themes` 列表。如果你不想基于访问者的浏览器设置自动切换暗色模式，你也可以只设置亮色或暗色配色方案。

如果你想允许访问者更改使用的配色方案，只需在 `config.toml` 的 `[extra]` 部分中设置以下变量：

```toml
[extra]
enable_theme_switching = true
```

然后在导航栏中会有一个下拉菜单，供访问者选择配色方案。

### 语言

要启用多语言支持，只需设置默认语言并为所有其他语言添加语言设置：

```toml
default_language = "en"

[languages.de]
# 其他语言的标题和描述
title = "Daisy Theme"
description = "Beispiel- und Demoseite des Daisy-Themas für Zola."

# 别忘了为其他语言也启用搜索或 feed 生成等功能
build_search_index = true
generate_feeds = true

# 默认语言的任何分类法也需要为其他语言定义
taxonomies = [
    { name = "tags", paginate_by = 2, feed = true },
    { name = "directors", paginate_by = 2, feed = true },
]
```

分类法在所有语言中应具有完全相同的（未翻译的）名称，以便语言切换能最好地工作。

你需要创建一个 i18n 文件，包含所有网站语言的主题变量翻译（如果主题中未包含）。目前包含 [英语](i18n/en.toml)、[德语](i18n/de.toml)、[匈牙利语](i18n/hu.toml)、[芬兰语](i18n/fi.toml)。你可以在网站根目录中创建一个 `i18n` 目录，其中的语言文件将被主题拾取。但是，如果你能在主题仓库上创建一个 [pull-request](https://codeberg.org/winterstein/zola-theme-daisy/pulls) 将你的翻译添加到主题中，那就太好了。

### 搜索

将搜索集成到你的网站非常简单，只需将以下内容添加到你的配置中：

```toml
# 为默认语言全局启用
build_search_index = true

[search]
# 主题仅支持此格式
index_format = "elasticlunr_json"

# 你需要在所有语言部分也启用搜索
[languages.de]
build_search_index = true
```

一旦启用 `build_search_index`，就会为在 `config.toml` 部分中启用此变量的所有语言创建搜索索引，并且网站导航栏中会显示搜索栏。

请注意，如果你使用除英语和德语以外的其他语言，则需要将兼容 [Elasticlunr.js](http://elasticlunr.com/) 的 [Lunr Languages](https://github.com/weixsong/lunr-languages) 文件添加到 `static` 目录。有关 [`min` 文件](https://github.com/weixsong/lunr-languages/tree/master/min)，请参阅相应的仓库。欢迎通过 [pull-request](https://codeberg.org/winterstein/zola-theme-daisy/pulls) 为主题添加对你的语言的支持。

### 导航栏

可以通过在 `[extra.navbar]` 部分定义以下列表来向页脚添加任意链接：

```toml
[extra.navbar]
links = [
    { url = "blog", i18n_key = "posts" },
    { url = "tags", i18n_key = "tags" },
    { url = "movies", i18n_key = "movies" },
]
```

`i18n_key` 的值必须在你的语言的 `i18n` 文件中（例如参见 [en.toml](i18n/en.toml)）。

### 页脚

页脚的所有三个部分都可以调整：链接、社交图标和版权声明。

#### 链接

可以通过在 `[extra.footer]` 部分定义以下列表来向页脚添加任意链接：

```toml
[extra.footer]
links = [
    { url = "about", i18n_key = "about" },
    { url = "sitemap.xml", i18n_key = "sitemap", no_translation = true },
]
```

`i18n_key` 的值必须在你的语言的 `i18n` 文件中（例如参见 [en.toml](i18n/en.toml)）。如果 `no_translation` 参数设置为 true，则 URL 不会包含当前语言代码。这对于外部链接或像 `sitemap.xml` 这样在网站内未翻译的内容是必需的。

#### 社交图标

可以通过设置以下任何变量来调整页脚中的社交图标：

```toml
[extra.social]
codeberg = ""
github = ""
gitlab = ""
stackoverflow = ""
mastodon = ""
linkedin = ""
instagram = ""
youtube = ""
signal = ""
telegram = ""
email = ""
phone = ""
```

对于每个非空变量，相应的图标将显示在页脚中。

#### 版权声明

可以通过在配置中添加以下变量来设置页脚中的版权声明：

```toml
[extra.footer]
notice = "This is my <b>copyright</b> notice."
```

此处可以使用 HTML。

## 自定义

可以通过继承模板并覆盖 `extra_headers` 或 `extra_javascript` 块，使用自定义 CSS 或 JavaScript 文件（或代码）扩展页面模板。`extra_headers` 的内容将添加到每个页面 `<head>` 部分的末尾，而 `extra_javascript` 的内容将添加到每个页面 `<body>` 部分的末尾。

```html
{%/* extends "daisy/templates/base.html" */%}

{%/* block extra_headers */%}
<!-- 例如添加自己的样式表 -->
<link rel="stylesheet" href="{{/* get_url(path='my_custom_style.css') */}}">
{%/* endblock */%}

{%/* block extra_javascript */%}
<script>
    /* 这里是一些自定义 JavaScript 代码 */
</script>
{%/* endblock */%}
```

但在大多数情况下，你可能不会扩展 `base` 模板，而是扩展更具体的模板，如 `page`、`section` 或 `index`。由于它们本身派生自 `base` 模板，因此你可以在这些情况下以相同的方式覆盖 `extra_headers` 和 `extra_javascript` 块。
