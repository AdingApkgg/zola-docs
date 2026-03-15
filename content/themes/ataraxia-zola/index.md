
+++
title = "ataraxia"
description = "一个专注于易读性的个人主题。"
template = "theme.html"
date = 2023-04-22T22:26:07-05:00

[taxonomies]
theme-tags = []

[extra]
created = 2023-04-22T22:26:07-05:00
updated = 2023-04-22T22:26:07-05:00
repository = "https://github.com/gersonbdev/ataraxia-zola.git"
homepage = "https://github.com/gersonbenavides/ataraxia-zola"
minimum_version = "0.16.0"
license = "MPL-2.0"
demo = "https://www.gersonb.dev/"

[extra.author]
name = "Gerson Benavides"
homepage = "https://github.com/gersonbenavides/ataraxia-zola"
+++        

# Ataraxia

[![Ataraxia 预览](https://raw.githubusercontent.com/gersonbenavides/ataraxia-zola/main/mockup.png "Ataraxia mockup")](https://gersonbenavides.github.io/)

一个专注于可读性的 [Zola](https://www.getzola.org/) 个人主题，旨在简单、美观且现代。它被设计为支持多种语言并且高度可定制。

该主题的视觉灵感来自 [Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) 和 [Neumorphism](https://github.com/longpdo/neumorphism) 主题。

## 安装

在你的站点路径下打开命令终端并运行：

```bash
cd themes
```

```bash
git clone https://github.com/gersonbenavides/ataraxia-zola.git ataraxia
```

## 配置

将 `config_sample.toml` 文件复制到你的站点主路径，然后将其重命名为 `config.toml` 并使用你的站点数据进行编辑。

> 你可以查看 [Gerson 的网站](https://github.com/gersonbenavides/gersonbenavides.github.io) 仓库以获取主题设置指南。

为了让站点正常工作，你需要在 `content` 路径内创建一个具有以下结构的 `_index.md` 文件：

```toml
+++
title = "Home"
description = "Home site description."
sort_by = "date"
template = "index.html"
page_template = "page.html"
+++
```

如果需要，你可以在此文件中添加更多 markdown 内容。

如果你想启用站点的博客，请在 `content/blog` 路径内创建一个 _index.md 文件，然后将以下结构复制到文件中：

```toml
+++
title = "Blog"
description = "Blog site description."
sort_by = "date"
paginate_by = 5
template = "blog.html"
page_template = "blog_page.html"
+++
```

你可以通过运行以下命令来显示你的网站结果：

```bash
zola serve
```


## Hacking

默认情况下，该主题附带了所有已编译的 scss 样式，因此无需安装 Bootstrap，以避免在生产文件中使用 Node.js 等依赖项。

如果你想编辑主题的样式，你需要安装 [Node.js](https://nodejs.org/) 解释器和 [Sass 编译器](https://sass-lang.com/install)。之后，转到主题的主路径并执行：

```bash
npm install
```

```bash
sass --watch scss/custom.scss:static/assets/css/custom.css
```

> 请记住，此仓库的主分支仅包含主题的稳定版本，如果你想查看开发状态和不稳定版本，请切换到相应的分支。

## 致谢

此主题主要基于 [Zola](https://www.getzola.org/) 和 [Bootstrap](https://getbootstrap.com/) 构建，此外它还使用了 [Google Fonts](https://fonts.google.com/)。


## 赞助

[![Liberapay](https://img.shields.io/badge/Finance%20my%20work-F6C915?style=flat&logo=liberapay&logoColor=ffffff "Finance my work")](https://liberapay.com/gersonbenavides/donate)

[![PayPal](https://img.shields.io/badge/Make%20a%20donation-00457C?style=flat&logo=paypal "Make a donation")](https://paypal.me/gersonbdev?country.x=CO&locale.x=es_XC)


## 许可证

这项工作根据 [MPL-2.0](https://www.mozilla.org/en-US/MPL/2.0/) 许可证发布
