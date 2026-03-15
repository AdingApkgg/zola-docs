
+++
title = "polymathic"
description = "一个适合多才多艺者的作品集主题"
template = "theme.html"
date = 2024-10-15T17:51:38+03:00

[taxonomies]
theme-tags = []

[extra]
created = 2024-10-15T17:51:38+03:00
updated = 2024-10-15T17:51:38+03:00
repository = "https://github.com/anvlkv/polymathic.git"
homepage = "https://github.com/anvlkv/polymathic"
minimum_version = "0.17.2"
license = "MIT"
demo = "https://main--polymathic-demo.netlify.app/"

[extra.author]
name = "Aleksandr Novolokov"
homepage = "https://a.nvlkv.xyz"
+++        

# polymathic

<a href="https://www.producthunt.com/posts/polymathic?utm_source=badge-featured&utm_medium=badge&utm_souce=badge-polymathic" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=422530&theme=light" alt="polymathic - Zola&#0032;portfolio&#0032;theme&#0032;for&#0032;those&#0032;with&#0032;many&#0032;talents | Product Hunt" style="width: 250px; height: 54px;" width="250" height="54" /></a>

polymathic 是一个 [Zola](https://www.getzola.org/) 作品集（及更多）主题。

我是为自己的作品集制作的。主题名为 `polymathic`，灵感来自拥有广泛才华的个人。该主题专注于丰富且一致的导航体验，展示各种可供选择的主题，同时允许用户在做出选择后专注于你故事的一条线索。

文档和主题演示可在此处获得 [main--polymathic-demo.netlify.app](https://main--polymathic-demo.netlify.app/) 

__请务必查看 [演示仓库](https://github.com/anvlkv/polymathic-demo/)__ 并遵循 zola 文档中关于 [安装和使用主题](https://www.getzola.org/documentation/themes/installing-and-using-themes/#installing-a-theme) 的说明

此主题使用 [Bulma](https://bulma.io/) scss 框架，使主题样式高度可定制，并启用移动优先的主题设计。

此主题使用 [Animate.css](https://animate.style) 进行动画。

此主题向每个页面的 `head` 添加最小的 [Open Graph](https://ogp.me/) 标签。

你可以快速将主题部署到 [netlify](https://docs.netlify.com/site-deploys/create-deploys/)，主题附带配置文件。

## 特性

查看 [文档中演示的](https://main--polymathic-demo.netlify.app/features) 所有特性。

### 媒体支持

该主题对从 `mobile` 到 `fullhd` 的各种屏幕尺寸都很友好。主题附带了针对 `print` 媒体的最小样式。

#### 暗色模式

主题包括基于偏好的暗色模式作为单独的样式表。无切换开关。

#### 无障碍

此主题在使用自定义设置时会自动查找无障碍颜色，配置极少。

此主题支持无脚本环境。

此主题尊重用户对减少动画的偏好。

### 导航

此主题为你的网站构建导航。结果可以通过你的 `config.toml` 和版块的 front-matter 高度定制。

### 模板

主题附带了 `index.html`, `page.html`, `section.html`, `taxonomy_list.html`, `taxonomy_single.html`, `404.html` 的模板。你可以按原样在你的 Zola 项目中使用它们，也可以通过扩展它们来使用，模板分为 `block` 和 `partials/*.html`，以便于扩展主题。

### 品牌和风格

通过 `config.toml` 和 sass 变量，该主题高度可定制。你的自定义可以从仅主色开始，一直扩展到 bulma 变量。

### 短代码

主题附带了几个用于构建表单、画廊、导航卡和横幅的短代码。

## 安装

一旦你已经安装了 zola 并运行了 `zola init`，然后在你的项目目录中运行

    $ git init
    $ git submodule add https://github.com/anvlkv/polymathic themes/polymathic

你还需要安装 [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)，然后运行

    $ npm --prefix themes/polymathic install

对于使用 netlify 部署的用户，此处提供配置

    $ cp themes/polymathic/netlify.toml netlify.toml

在你的 `config.toml` 中将 zola 主题设置为 polymathic

    theme = "polymathic"


## 贡献

欢迎 issue 或贡献。另外，很好奇你用它做了什么。
