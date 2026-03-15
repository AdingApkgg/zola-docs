
+++
title = "Bear"
description = "Bear 博客主题"
template = "theme.html"
date = 2026-02-24T15:58:49+01:00

[taxonomies]
theme-tags = []

[extra]
created = 2026-02-24T15:58:49+01:00
updated = 2026-02-24T15:58:49+01:00
repository = "https://codeberg.org/alanpearce/zola-bearblog.git"
homepage = "https://codeberg.org/alinnow/zola-bearblog"
minimum_version = "0.4.0"
license = "MIT"
demo = "https://zola-bearblog.alin.ovh/"

[extra.author]
name = "Alin"
homepage = "https://alin.ovh"
+++        

# Zola ʕ•ᴥ•ʔ Bear Blog

[![Netlify Deploy](http://img.shields.io/netlify/121b53ce-c913-4604-9179-eb3cca31cd2c?logo=netlify)](https://app.netlify.com/sites/zola-bearblog/deploys)
[![Forgejo Actions Status](https://codeberg.org/alanpearce/zola-bearblog/badges/workflows/zola.yaml/badge.svg)](https://codeberg.org/alanpearce/zola-bearblog/actions)
[![Gitlab Pipeline Status](https://gitlab.com/alanpearce/zola-bearblog/badges/main/pipeline.svg)](https://gitlab.com/alanpearce/zola-bearblog/-/commits/main)

🧸 一个基于 [Bear Blog](https://bearblog.dev) 的 [Zola](https://www.getzola.org/) 主题。

> 免费、简洁、超快的博客。

## 演示

此主题有多个演示站点，以提供如何设置部署的示例。

### 推荐

- [Netlify](https://zola-bearblog.netlify.app/)
- [Grebedoc](https://alanpearce.grebedoc.dev/zola-bearblog/)
- [Codeberg Pages](https://alanpearce.codeberg.page/zola-bearblog/)
- [Gitlab Pages](https://alanpearce.gitlab.io/zola-bearblog)

### 不推荐

这些提供商的构建环境尚未与 Zola 0.21.0 兼容。
- [Cloudflare Pages](https://zola-bearblog.pages.dev/)

## 截图

![截图][screenshot]

当用户的浏览器运行“暗色模式”时，将自动使用暗色配色方案。默认为亮色/白色配色方案。查看 [`style.html`](https://codeberg.org/alanpearce/zola-bearblog/src/branch/main/templates/style.html) 文件以了解实现。

## 安装

如果你机器上已经有一个 Zola 站点，你可以简单地通过以下方式添加此主题

```
git submodule add https://codeberg.org/alanpearce/zola-bearblog themes/zola-bearblog
```

然后，如下详述调整 `config.toml`。

有关更多信息，请阅读 Zola 的官方 [设置指南][zola-setup-guide]。

或者，你可以使用此按钮快速将主题站点的副本部署到 Netlify：

[![部署到 Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://gitlab.com/alanpearce/zola-bearblog)

（请注意，这种方法使得跟上主题更新变得更加困难，这对于较新版本的 Zola 可能是必要的。）

## 调整配置 / config.toml

请查看包含的 [config.toml](https://codeberg.org/alanpearce/zola-bearblog/src/branch/main/config.toml)

## 内容与结构

### 菜单

在 `extra` 中创建一个键为 `main_menu` 的数组。`url` 传递给 [`get_url`](https://www.getzola.org/documentation/templates/overview/#get-url)

```toml
[[extra.main_menu]]
name = "Home"
url = "@/_index.md"

[[extra.main_menu]]
name = "Bear"
url = "@/bear.md"

[[extra.main_menu]]
name = "Zola"
url = "@/zola.md"

[[extra.main_menu]]
name = "Blog"
url = "@/blog/_index.md"
```

### 添加 / 编辑内容

#### 首页

可以通过编辑你的 `content/_index.md` 文件来更改 `index` 页面的内容。


### 添加你的品牌 / 颜色 / css

在你的 `templates/` 目录中添加一个 `custom_head.html` 文件。在其中你可以添加一个 `<style>` 标签，*或者*你可以添加一个引用你自己的 `custom.css` 的 `<link>` 标签（如果你更喜欢有一个单独的 `.css` 文件）。查看 [`style.html`](https://codeberg.org/alanpearce/zola-bearblog/src/branch/main/templates/style.css.html) 文件以找出默认应用的 CSS 样式。

### 目录

目录默认不渲染。要渲染它们，请在 `config.toml` 中设置 `extra.table_of_contents.show = true`。

目录渲染在 `details` 元素内。
如果你希望该部分在页面加载时折叠，请设置 `extra.table_of_contents.visible_on_load = false`。
这默认为 `true`。

此外，`extra.table_of_contents.max_level` 可以限制显示的标题的最大级别。
要仅显示 `h1`，设置 `max_level = 1`，要显示 `h1` 和 `h2`，设置 `max_level = 2`，依此类推。
默认情况下，`max_level` 设置为 6，因此显示页面上的所有标题。

以下是如何在 `config.toml` 中配置目录的示例。

```toml
[extra.table_of_contents]
show = true
max_level = 2
visible_on_load = false
```

也可以逐页切换。在页面的 frontmatter 中添加 `extra.hide_table_of_contents = true` 以隐藏该特定页面的目录。

## 问题 / 反馈 / 贡献
请使用 [Codeberg issues](https://codeberg.org/alanpearce/zola-bearblog/issues) 和 [Pull Requests](https://codeberg.org/alanpearce/zola-bearblog/pulls)。

## 特别感谢 🎁

特别感谢 [Herman](https://herman.bearblog.dev)，感谢他创建了最初的 [ʕ•ᴥ•ʔ Bear Blog](https://bearblog.dev/)，以及 [Jan Raasch](https://www.janraasch.com) 创建了 Bear Blog 主题的 hugo 移植版。

## 许可证
[MIT License](http://en.wikipedia.org/wiki/MIT_License) © [Alan Pearce](https://www.alanpearce.eu/)

[zola-setup-guide]: https://www.getzola.org/documentation/getting-started/installation/
[screenshot]: https://codeberg.org/alanpearce/zola-bearblog/raw/branch/main/screenshot.png
