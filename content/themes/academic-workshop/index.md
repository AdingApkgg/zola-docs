
+++
title = "Academic Workshop"
description = "一个用于列出科学研讨会或系列研讨会日程安排的 Zola 网站主题"
template = "theme.html"
date = 2025-10-21T20:16:41-04:00

[taxonomies]
theme-tags = []

[extra]
created = 2025-10-21T20:16:41-04:00
updated = 2025-10-21T20:16:41-04:00
repository = "https://github.com/aterenin/academic-workshop.git"
homepage = "https://github.com/aterenin/academic-workshop"
minimum_version = "0.18.0"
license = "MIT"
demo = "https://aterenin.github.io/academic-workshop"

[extra.author]
name = "Alexander Terein"
homepage = "https://avt.im"
+++        

# Academic Workshop: 一个 Zola 主题

[Academic Workshop](https://aterenin.github.io/academic-workshop) 是一个专为托管科学研讨会或科学系列研讨会网站而设计的 Zola 主题。
可以在 [aterenin.github.io/academic-workshop](https://aterenin.github.io/academic-workshop) 找到使用 Academic Workshop 构建的演示网站，分别用于系列研讨会和研讨会的示例仓库可以在 [github.com/gp-seminar-series/gp-seminar-series.github.io](https://github.com/gp-seminar-series/gp-seminar-series.github.io) 和 [https://github.com/gp-seminar-series/neurips-2024](https://github.com/gp-seminar-series/neurips-2024) 找到。

# 特性

[Academic Workshop](https://github.com/aterenin/academic-workshop) 旨在具有相当完整的功能。其功能包括：

* 一个自动页眉，列出标语、标题和副标题，带有可自定义的按钮，以及带有可自定义 CSS 的背景横幅图片。
* 用于各种类型列表的短代码，如演讲者列表和以前的研讨会列表，以及在首页突出显示即将举行的研讨会，以完全响应的方式实现，在桌面和移动设备上看起来都很专业。
* 智能图片调整大小，用于图片网格类型的列表，如演讲者列表。
* 支持从 CSV 文件创建已接受的研讨会论文表。
* 元数据，包括 Twitter Summary Card、OpenGraph 和 JSON-LD，实现类似于 [Jekyll SEO Tag](https://github.com/jekyll/jekyll-seo-tag)：这些确保页面对搜索引擎友好，并为社交媒体网站提供分享链接时显示的链接。

# 设计和可维护性

[Academic Workshop](https://github.com/aterenin/academic-workshop) 是 [设计为持久的](https://jeffhuang.com/designed_to_last/)。
这意味着它遵循一套最佳实践，试图确保用它正确构建的网站在无限的未来都能以最少的维护正确工作，即使互联网发生变化并且链接随着时间的推移而断裂。
因此，该主题没有任何类型的 JavaScript 或 CSS 依赖项。

# 文档

下面的示例记录了 TOML 文件中可用的主题选项，这些选项在每个文件中作为注释列出。

## Config.toml 

```toml
base_url = "https://example.com"
compile_sass = true # 应设置为 true
build_search_index = false # 主题不使用
generate_feed = false # 主题不使用
minify_html = true # 为了确保由于空白压缩而正确渲染，应设置为 true，除非有理由覆盖它

[markdown]
highlight_code = false # 除非页面有代码要高亮，否则应设置为 false

[extra]
footer_text = "This website is built using [Zola](https://www.getzola.org) and the [Academic Workshop](http://github.com/aterenin/academic-workshop/) theme, which is [designed to last](https://jeffhuang.com/designed_to_last/)." # 默认情况下，此页面添加一个带有链接到此仓库的小型且不显眼的页脚 - 如果你愿意，可以将其设置为 false 以移除页脚
title = {tagline = "Presenting the", title = "Academic Workshop Zola Theme", subtitles = ["For workshops, seminars, and academic events"]} # 这包含页眉的标语、标题和副标题列表，按顺序显示
banner = {extension = "svg", size = "fixed", fade = true} # 这启用了存储在 static/banner.svg 中的横幅图片，带有 CSS 类 bg-fixed：此 CSS 类旨在让用户通过覆盖 CSS 设置背景图片的高度和宽度 - 参见 _main.scss 获取其他类如 bg-contain 或 bg-cover - fade 选项启用了围绕文本的基于 CSS 的淡入淡出
buttons = [{name = "Example", url = "https://example.com/"}, {name="GitHub", url="http://github.com/aterenin/academic-workshop"}] # 创建按顺序显示的按钮列表，带有指向 URL 的链接
image = {resize = 400, ext = '.jpg'} # 这设置了图片调整大小的所需尺寸以及默认扩展名
list_page_limit = 10 # 这设置了列表中一页显示的默认项目数
header_pages = [{name = "Home", url = "/#home"},{name = "Design", url = "/#design"}] # 这设置了在移动设备上显示的导航菜单中显示的页面
button_shortcuts = [{variable = "video", name = "Video"}] # 此配置使得以不太冗长的方式向页面或版块添加按钮成为可能，例如通过编写 video = "/url/to/video" 而不是 buttons = [{name = "Video", url = "/url/to/video"}]
```

## 页面配置 

如果使用此主题作为研讨会列表，每个研讨会应作为页面添加在合适的版块内。此处给出了一个配置示例。 

```toml
+++
title = "Seminar Title"
[extra]
author = "Example Author" # 作者姓名
institution = "Example Institution" # 机构名称
author_url = "https://example.com" # 作者网页，主题将创建链接
time = "16:00 UTC" # 研讨会时间
buttons = [{name = "Example", url = "https://example.com/"}] # 在页面和列表中显示的按钮列表，按顺序显示
highlight = true # 研讨会是否使用 highlight 短代码显示在页面上，该短代码旨在在主题首页显示即将举行的研讨会的简短列表 - 默认为 false
image = "placeholder.svg" # 可选：允许覆盖默认图片 URL
+++

研讨会摘要在这里
```
