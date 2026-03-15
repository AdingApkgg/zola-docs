
+++
title = "tale-zola"
description = "Tala-Zola 是一个极简的 Zola 主题，帮助你构建一个漂亮且利于 SEO 的博客。"
template = "theme.html"
date = 2021-12-05T00:18:16+08:00

[taxonomies]
theme-tags = []

[extra]
created = 2021-12-05T00:18:16+08:00
updated = 2021-12-05T00:18:16+08:00
repository = "https://github.com/aaranxu/tale-zola.git"
homepage = "https://github.com/aaranxu/tale-zola"
minimum_version = "0.13.0"
license = "MIT"
demo = "https://tale-zola.netlify.app/"

[extra.author]
name = "Aaran Xu"
homepage = "https://github.com/aaranxu"
+++        

# Tale-Zola Theme

Tala-Zola 是一个极简的 [Zola](https://www.getzola.org) 主题，帮助你构建一个轻量级且利于 SEO 的博客，你可以在不修改模板代码的情况下自定义博客的任何信息。Tala-Zola 是 Jekyll 主题 [Tale](https://github.com/chesterhow/tale) 的移植版。

## 演示

[在线预览](https://tale-zola.netlify.app/).

## 要求

在使用此主题之前，你需要安装 [Zola](https://www.getzola.org/documentation/getting-started/installation/) ≥ 0.13.0。

## 快速开始

```bash
git clone git@github.com:aaranxu/tale-zola.git
cd tale-zola
zola serve
# 在浏览器中打开 http://127.0.0.1:1111/
```

## 安装

刚才我们展示了如何直接运行主题。现在我们开始逐步在现有站点中安装主题。

### 第一步：创建一个新的 Zola 站点

```bash
zola init blog
```

### 第二步：安装 Tale-Zola

下载此主题到你的 themes 目录：

```bash
cd blog/themes
git clone git@github.com:aaranxu/tale-zola.git
```

或者作为子模块安装：

```bash
cd blog
git init  # 如果你的项目已经是 git 仓库，请忽略此命令
git submodule add git@github.com:aaranxu/tale-zola.git themes/tale-zola
```

### 第三步：配置

在站点目录下的 `config.toml` 中启用主题：

```toml
theme = "tale-zola"
```

或者将 `config.toml.example` 从主题目录复制到你的项目根目录：

```bash
cp themes/tale-zola/config.toml.example config.toml
```

### 第四步：添加新内容

在你的 `content` 目录下添加一个 `_index.md` 文件，内容如下：

```text
+++
sort_by = "date"
paginate_by = 5
+++
```

添加一个文件名为 `first-post.md`（或其他文件名）的博客文章文件，并输入一些内容。

```text
+++
title = "First Post"
date = 2021-05-01T18:18:18+00:00

[taxonomies]
tags = ["Post"]

[extra]
author = "Your Name"
+++

This is my first post.
```

或者你可以直接将主题目录中的 content 复制到你的项目中：

```bash
cp -r themes/tale-zola/content .
```

### 第五步：运行项目

只需在项目根路径下运行 `zola serve`：

```bash
zola serve
```

Tale-Zola 将启动 Zola 开发 Web 服务器，默认访问地址为 `http://127.0.0.1:1111`。保存的更改将在浏览器中实时重新加载。

## 自定义

你可以自定义配置、模板和内容。查看此仓库中的 `config.toml`、`theme.toml` 和模板文件以获取灵感。

在大多数情况下，你只需要修改 `config.toml` 文件中的内容即可自定义你的博客，包括使用你的语言的不同表达方式。

### 必要配置

为你的博客添加一些信息。

```toml
title = "You Blog Title"
description = "The description of your blog."
```

设置站点的标签。

```toml
taxonomies = [
  {name = "tags"},
]
```

为你的博客添加菜单和页脚信息。

```
# 菜单项
[[extra.menu]]
name = "Posts"
url = "/"

[[extra.menu]]
name = "Tags"
url = "tags"

[[extra.menu]]
name = "About"
url = "about"

[extra.footer]
start_year = "2020"  # 站点开始年份
end_year = "2021"    # 站点结束年份
info = "The information on the footer."
```

#### 选项配置

全局添加你的名字作为博客的作者名。

```toml
[extra]
author = "Your Name"
```

使用 Google Analytics。添加你自己的 Google Analytics ID。

```toml
[extra]
google_analytics = "UA—XXXXXXXX-X"
```

是否全局使用 Disqus 并设置为你的 disqus id 名称。
你也可以通过 `extra.disqus` 选项在每篇文章页面上启用 disqus。

```toml
[extra]
disqus = false
disqus_id = ""
```

代码语法高亮。另请参阅 [语法高亮](https://www.getzola.org/documentation/getting-started/configuration/#syntax-highlighting)。

```toml
[markdown]
highlight_code = true
highlight_theme = "base16-ocean-light"
```

使用 KaTeX 支持数学符号

```toml
[extra]
katex = true
```

> 注意：你也可以在页面或版块的 markdown 文件中添加 `katex` 选项。

设置站点中的日期格式

```toml
[extra]
timeformat = "%B %e, %Y" # 例如 June 14, 2021，这是默认格式
```

SEO 设置，如 Open Graph + Twitter Cards

```toml
[extra.seo]
# 如果页面没有自己的图片，将使用此图片作为后备
image = "tale.png"
image_height = 50
image_width = 50
og_locale = "en_US"

  [extra.seo.twitter]
  site = "twitter_accout"
  creator = "twitter_accout"

  [extra.seo.facebook]
  admins = "facebook_accout"
  publisher = "facebook_accout"
```

更改你的语言中的词汇。

```toml
[extra.expressions]
home = "首页"              # 主页名称
pinned = "置顶"          # 文章列表头部
written_by = "作者"  # 例如：作者 Aaran Xu
on = "于"                  # 例如：于 2021年5月3日
top = "顶部"                # 文章中返回顶部
tags = "标签"              # 标签页中

# disqus 评论块
disqus_discussion = "讨论与反馈"

# 404 页面内容
p404 = "404: 页面未找到"
p404_info = "哎呀！我们似乎找不到你要找的页面。"
p404_back_home_start = "让我们"
p404_back_home_with_link = "回到首页"
p404_back_home_end = "。"
```

### 自定义 CSS 样式

只需将你自己的样式添加到 `sass/_custom.scss` 文件中。

## 报告问题

我们使用 GitHub Issues 作为 **Tale-Zola** 的官方 bug 追踪器。请搜索 [现有 issues](https://github.com/aaranxu/tale-zola/issues)。可能已经有人报告了同样的问题。

如果你的问题或想法尚未解决，[打开一个新 issue](https://github.com/aaranxu/tale-zola/issues/new)。

## 贡献

我们需要你的帮助！请查看 [CONTRIBUTING.md](./CONTRIBUTING.md) 以了解我们需要什么样的贡献。

## 许可证

Tale-Zola 根据 [MIT 许可证](LICENSE) 分发。
