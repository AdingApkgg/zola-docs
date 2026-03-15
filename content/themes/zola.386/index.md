
+++
title = "zola.386"
description = "BOOTSTRA.386 主题的 Zola 移植版。"
template = "theme.html"
date = 2022-03-24T12:08:20-03:00

[taxonomies]
theme-tags = []

[extra]
created = 2022-03-24T12:08:20-03:00
updated = 2022-03-24T12:08:20-03:00
repository = "https://github.com/lopes/zola.386.git"
homepage = "https://github.com/lopes/zola.386"
minimum_version = "0.10.1"
license = "MIT"
demo = "https://zola386.netlify.com"

[extra.author]
name = "José Lopes"
homepage = "https://github.com/lopes"
+++        

# ZOLA.386

![ZOLA.386 截图](https://github.com/lopes/zola.386/blob/master/screenshot.png?raw=true)

## [在线演示](https://zola386.netlify.app/)

ZOLA.386 是 BOOTSTRA.386 主题的移植版，基于：

- [BOOTSTRA.386](https://kristopolous.github.io/BOOTSTRA.386/): 主要理念，设计。
- [HUGO.386](https://themes.gohugo.io/hugo.386/): 项目放置。
- [Dinkleberg](https://github.com/rust-br/dinkleberg): 内部结构和 SEO。
- [after-dark](https://github.com/getzola/after-dark): 导航栏和次要组件。

ZOLA.386 是一个引用 90 年代的主题，但具有快速响应的尖端功能。


## 安装

安装 ZOLA.386 最简单的方法是克隆此仓库并在其上构建你的站点：

```bash
$ git clone https://github.com/lopes/zola.386
```

当然，你也可以将其作为站点的另一个主题安装，但 ZOLA.386 必须作为模块添加：

```bash
$ cd themes
$ git submodule add https://github.com/lopes/zola.386 
```


## 配置

配置主要在 `config.toml` 中完成，这里我将描述主要主题。

### 全局

`config.toml` 以全局变量开始。所有这些项目都很重要，但至少创建两个分类法是基础：

```toml
taxonomies = [
  {name="categories", rss=true},
  {name="tags", rss=true},
]
```

请记住，所有描述（`config.description` 和 `page.description`）都显示在索引页上，一个在标题处，其他的通过正文显示。

### 额外配置

ZOLA.386 附带了许多额外变量，这简化了站点的创建和维护，因此安装主题后检查所有这些变量很重要。

`zola386_menu` 组成导航栏，通过设置 `path` 创建，该路径将附加到 `base_url`，`name` 将出现在导航栏上。

```toml
[extra]
zola386_menu = [
  {path="/", name="Home"},
  {path="categories", name="Categories"},
  {path="tags", name="Tags"},
  {path="about", name="About"},
]
```

### 社交

ZOLA.386 也准备处理 Google Analytics, Disqus, 和 Twitter --欢迎使用 [Open Graph Protocol](https://ogp.me/)。此主题准备使用 [Favicon Generator](https://www.favicon-generator.org/) 的输出，要这样做，你只需要下载该站点的输出并解压到 `static/images` 中。

如前所述，支持 Disqus，但除了在 `config.toml` 中设置用户名外，你还必须在启用 Disqus 的页面上放置 `comments = true` 额外选项 --这让你有自由在某些文章上启用或禁用评论。你可以在每个页面上使用额外选项 `image` 来代表该文章。

### 动画

所有 JavaScript 动画都可以在 `static/js/zola386.js` 中设置。基本上你可以禁用所有动画，使用一次或两次扫描，并更改扫描速度。个人而言，我更喜欢速度系数为 5 的单次扫描。

### 语言

在 `label_` 变量下，你可以设置名称以更好地本地化你的站点。注意你可以通过使用 `page.extra.lang` 更改单个页面的语言，这会导致 `<html lang="">` 仅在该页面上更改。一个为其所有者提供信息且 SEO 友好的主题。

### 搜索

搜索是根据 [官方文档](https://www.getzola.org/documentation/content/search/) 实现的。它使用 JavaScript 根据 `search_index.LANG.js`, `elasticlunr.min.js`, 和 `search.js` --前两个是在每次构建后生成的--搜索站点的索引版本。如果你在英语以外的其他默认语言中运行你的站点，你 **必须** 更改 `index.html` 中的 `search_index.LANG.js` 行，相应地设置 `LANG`。

### 其他文件

`content\_index.md` 文件必须正确配置以提供更好的体验。查看此文件以获取更多信息。

404 页面几乎是硬编码的，所以你必须直接编辑它。


## 许可证

此主题根据 MIT 许可证发布。有关更多信息，请阅读 [许可证](https://github.com/lopes/zola.386/blob/master/LICENSE)。


[![Netlify Status](https://api.netlify.com/api/v1/badges/5d6f1986-7bf3-40d3-b298-3339288585d4/deploy-status)](https://app.netlify.com/sites/zola386/deploys)
