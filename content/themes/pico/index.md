
+++
title = "pico"
description = "干净且极简主义的暗色主题"
template = "theme.html"
date = 2025-09-08T11:17:37+03:00

[taxonomies]
theme-tags = []

[extra]
created = 2025-09-08T11:17:37+03:00
updated = 2025-09-08T11:17:37+03:00
repository = "https://github.com/kuznetsov17/pico.git"
homepage = "https://github.com/kuznetsov17/pico"
minimum_version = "0.18.0"
license = "MIT"
demo = "https://kuznetsov17.github.io/pico/"

[extra.author]
name = "Vitaliy Kuznetsov"
homepage = "https://viku.me"
+++        

# 配置
# 通用

我不是最好的网站管理员，但应该有一定的响应能力。
我有意使用较大的字体来制作，可以在 main.css 中随意更改它

# 亮色模式
现在也支持亮色模式。

# 重要
请确保设置你的 base_url 带有尾部斜杠：
```toml
base_url = "https://kuznetsov17.github.io/pico/"
```
# 评论
主题支持使用 [Giscuss](https://giscuss.app) 进行评论。配置通过 config.toml 完成。在这里你可以看到用于此页面部署的示例部分：
```toml
[extra.giscus]
data_repo="kuznetsov17/pico"
data_repo_id="R_kgDOLIfXYA"
data_category="General"
data_category_id="DIC_kwDOLIfXYM4Ccn56"
data_mapping="title"
data_strict="0"
data_reactions_enabled="0"
data_emit_metadata="0"
data_input_position="top"
data_theme="//kuznetsov17.github.io/pico/css/gs_dark.css"
data_lang="en"
crossorigin="anonymous"
nonce=""
```

# 页面配置
通过在 **[extra]** 部分设置配置来自定义页面块：
```toml
show_copyright = true / false # 启用/禁用带有版权的页脚
show_comments = true / false # 启用/禁用评论
show_shares = true / false # 启用/禁用带有社交分享按钮的部分
show_toc = true / false # 启用/禁用目录
show_date = true / false # 在页面中显示发布日期
```

# 博客
我正在使用这个主题作为我的 [笔记](https://viku.me/notes/)，或者可能是博客。
版块模板支持分页、标签，按发布日期对页面进行排序。你可以在 [这里](content/notes/_index.md) 看到工作示例

# 搜索
主题支持使用 [elasticrunrjs](http://elasticlunr.com) 进行搜索。要启用搜索，你需要在 **config.toml** 中进行以下配置：

```toml
build_search_index = true

[search]
index_format = "elasticlunr_json"
```

# config.toml extras
```toml
author = "John Doe" # 作者。将被放入页面元数据中
description = "Some description, if you somehow didn't set it in page / section settings"
logo_src = "images/logo.svg" # logo src
avatar_src = "images/avatar.png" # avatar src
index_page="index" # 索引页面的名称。应该是 top_menu 之一以使其工作
top_menu = ["index","features","notes"] # 菜单项
copyright_string = "Сreated by John Doe in 2024 – %YEAR% for fun." # 页脚内容。%YEAR% 将被替换为当前年份
nonce = "${SOME_HASH_VALUE}" # 用于 JavaScript src nonce
```

# 时间轴
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

# Callouts
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
# Mermaid

阅读有关如何在他们的 [文档](https://mermaid.js.org/syntax/examples.html) 中使用 mermaid 的更多信息
```
{%/* mermaid() */%}
gitGraph
       commit
       commit
       branch develop
       checkout develop
       commit
       commit
       checkout main
       merge develop
       commit
       commit
{%/* end */%}
```
```
{%/* mermaid() */%}
graph LR
    A[Square Rect] -- Link text --> B((Circle))
    A --> C(Round Rect)
    B --> D{Rhombus}
    C --> D
{%/* end */%}
```
# 感谢
 - [Giscuss](https://giscuss.app) 优秀的评论系统
 - [bootstrap icons](https://icons.getbootstrap.com) 伟大的社交图标
 - [Urbanist Font](https://fonts.google.com/specimen/Urbanist)
 - [Mulush Font](https://fonts.google.com/specimen/Mulish)

# 截图
![截图](https://github.com/kuznetsov17/pico/blob/main/screenshot.png?raw=true)
