
+++
title = "minimal-dark"
description = "简洁极简的深色主题"
template = "theme.html"
date = 2024-02-07T14:01:03+02:00

[taxonomies]
theme-tags = []

[extra]
created = 2024-02-07T14:01:03+02:00
updated = 2024-02-07T14:01:03+02:00
repository = "https://github.com/kuznetsov17/minimal-dark.git"
homepage = "https://github.com/kuznetsov17/minimal-dark"
minimum_version = "0.18.0"
license = "MIT"
demo = "https://kuznetsov17.github.io/minimal-dark/"

[extra.author]
name = "Vitaliy Kuznetsov"
homepage = "https://viku.me"
+++        

[![Deploy Zola with GitHub Pages](https://github.com/kuznetsov17/minimal-dark/actions/workflows/zola-build.yml/badge.svg)](https://github.com/kuznetsov17/minimal-dark/actions/workflows/zola-build.yml)


# 概览

我不是最专业的网站开发者，但这个主题应当具备基本的响应式支持。
我有意使用了更大的字体，你可以在 `main.scss` 里自由调整。


# 浅色模式
现在也支持浅色模式。 

# 重要提示
请确保 `base_url` 以斜杠结尾：
```toml
base_url = "https://kuznetsov17.github.io/minimal-dark/"
```
# 评论
主题支持使用 [Giscuss](https://giscuss.app) 作为评论系统。相关配置通过 `config.toml` 完成。下面是此站点部署所使用的示例配置：
```toml
[extra.giscus]
data_repo="kuznetsov17/minimal-dark"
data_repo_id="R_kgDOLIfXYA"
data_category="General"
data_category_id="DIC_kwDOLIfXYM4Ccn56"
data_mapping="title"
data_strict="0"
data_reactions_enabled="0"
data_emit_metadata="0"
data_input_position="top"
data_theme="//kuznetsov17.github.io/minimal-dark/css/gs_dark.css"
data_lang="en"
crossorigin="anonymous"
nonce=""
```

# 页面配置
可在 **[extra]** 区域设置以下配置来自定义页面区块：
```toml
copyright_string = "Сreated in %YEAR% for fun." # the string displayed in footer. %YEAR% is replaced by current year on build
show_copyright = true / false # enables / disables footer with copyright
show_comments = true / false # enables / disables comments
show_shares = true / false # enables / disables section with social share buttons
show_toc = true / false # enables / disable TOC
show_date = true / false # displays publication date in page
```

# 博客
我用这个主题来写自己的 [notes](https://viku.me/notes/)（也可以当作博客）。
分区模板支持分页、标签，并按发布时间排序。你可以在[这里](/notes/)查看实际效果。

# config.toml 附加配置
```toml
author = "John Doe" # author. Will be puth in page metadata
description = "Some description, if you somehow didn't set it in page / section settings"
logo_src = "images/logo.svg" # logo src
avatar_src = "images/avatar.png" # avatar src
index_page="index" # name of the index page. Should be one of top_menu to make things work
top_menu = ["index","features","notes"] # Menu items
copyright_string = "Сreated by John Doe in 2024 – %YEAR% for fun." # footer content. %YEAR% will be replaced with current year
nonce = "${SOME_HASH_VALUE}" # used for JavaScript src nonce
```

# 短代码

## 提示框（Callouts）
```
{%/* callout(type = 'warning') */%}
This is an example of **Warning** callout. [Some link](#)
{%/* end */%}
{%/* callout(type = 'alert') */%}
This is an example of **Alert** callout. [Some link](#)
{%/* end */%}
{%/* callout(type = 'info') */%}
This is an example of **Info** callout. [Some link](#)
{%/* end */%}
```
## 时间线（Timeline）
```
{%/* timeline() */%}
[{
    "title":"Lorem Ipsum Event",
    "body":"Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
    "date":"Jul-2023"
},
{
    "title":"Lorem Ipsum event 2",
    "body":"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.",
    "date":"Jun-2022"
}]
{%/* end */%}
```

# 致谢
 - 感谢 [Giscuss](https://giscuss.app) 提供优秀的评论系统
 - 感谢 [bootstrap icons](https://icons.getbootstrap.com) 提供出色的社交图标 

# 截图
![Screenshot](https://github.com/kuznetsov17/minimal-dark/blob/main/screenshot.png?raw=true)

        
