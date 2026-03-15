
+++
title = "zolastrap"
description = "一个 zola 的 bootstrap 主题"
template = "theme.html"
date = 2022-02-20T19:12:59-03:00

[taxonomies]
theme-tags = []

[extra]
created = 2022-02-20T19:12:59-03:00
updated = 2022-02-20T19:12:59-03:00
repository = "https://github.com/marcodpt/zolastrap.git"
homepage = "https://github.com/marcodpt/zolastrap"
minimum_version = "0.14.1"
license = "MIT"
demo = "https://marcodpt.github.io/zolastrap/"

[extra.author]
name = "Marco Tomic"
homepage = "https://marcodpt.github.io"
+++        

# zolastrap
一个 zola 的 bootstrap 主题

[在线演示](https://marcodpt.github.io/zolastrap/)

## `config.toml` [extra] 变量

### banner
 - 类型: 字符串
 - 默认值: ""

横幅图片的路径，使用空字符串表示无横幅

### date_format
 - 类型: 字符串
 - 默认值: "%d/%m/%Y"

日期格式表达式

### 主题
 - 类型: 字符串
 - 默认值: "default"

[Bootswatch](https://bootswatch.com) 主题之一

### bg
 - 类型: 字符串
 - 默认值: "dark"

[Bootstrap5](https://getbootstrap.com/docs/5.1/utilities/background/)
中用于 `navbar` 和 `footer` 的可用背景之一

### inverted
 - 类型: 布尔值
 - 默认值: false

反转 `navbar` 和 `footer` 的字体，以防默认选择不好

### themes
 - 类型: 字符串
 - 默认值: "Choose a Theme"

主题下拉菜单的导航栏标签。

此下拉菜单将允许用户更改
[Bootswatch](https://bootswatch.com) 主题。

如果你不想让用户选择主题，请使用空字符串。

### schemes
 - 类型: 字符串
 - 默认值: "Choose a Color Scheme"

配色方案下拉菜单的导航栏标签。

此下拉菜单将允许用户更改页脚和导航栏
[背景](https://getbootstrap.com/docs/5.1/utilities/background/)
颜色。

如果你不想让用户选择主题，请使用空字符串。

### 搜索
 - 类型: 字符串
 - 默认值: "Search"

导航栏搜索输入的占位符。

请记住，要启用和禁用搜索，你应该设置变量
[build_search_index](https://www.getzola.org/documentation/getting-started/configuration/)。

### tag
 - 类型: 字符串
 - 默认值: "Posts by Topic"

分类法 `tag` 单个标签。对翻译很有用。

### 标签
 - 类型: 字符串
 - 默认值: "Posts by Topics"

分类法 `tag` 列表标签。对翻译很有用。
你可以通过在 `_index.md` 中使用 `extra.tags` = true 在页面底部拥有一个漂亮的标签列表。

### links
 - 类型: 数组
 - 默认值: []

导航栏链接。使用空数组忽略此项。

项目 (对象):
 - title (String): 导航栏链接的标签
 - url (String): 关联链接的 href

### Email
 - 类型: 字符串
 - 默认值: ""

页脚电子邮件。使用空字符串忽略此项。

### icons
 - 类型: 数组
 - 默认值: []

页脚社交图标。使用空数组忽略此项。

项目 (对象):
 - title (string): 图标的可选标题字符串
 - icon (string): 其中之一
 - url (string): 图标的 href

### Utterances
 - 类型: 字符串
 - 默认值: "" 

[Utterances](https://github.com/utterance/utterances) 仓库 url。

使用空字符串忽略 utterances 小部件。

### utterances_label
 - 类型: 字符串
 - 默认值: "Comments" 

[Utterances](https://github.com/utterance/utterances) 小部件标签。

### utterances_theme
 - 类型: 字符串
 - 默认值: "github-light" 

[Utterances](https://github.com/utterance/utterances) 小部件主题。

### utterances_issue_term
 - 类型: 字符串
 - 默认值: "pathname" 

[Utterances](https://github.com/utterance/utterances) 小部件路径名。

## 贡献
非常感谢任何帮助！

 - [Tera 模板引擎](https://tera.netlify.app/docs)
 - [Zola SSG 模板](https://www.getzola.org/documentation/templates/overview/)
 - [Bootstrap5 文档](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
 - [Bootswatch](https://bootswatch.com)
