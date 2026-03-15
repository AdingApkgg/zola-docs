
+++
title = "abridge"
description = "一个快速、轻量级的 Zola 主题，使用语义化 html、轻量级 abridge.css，且无强制 JS。"
template = "theme.html"
date = 2026-01-21T18:04:10+08:00

[taxonomies]
theme-tags = []

[extra]
created = 2026-01-21T18:04:10+08:00
updated = 2026-01-21T18:04:10+08:00
repository = "https://github.com/Jieiku/abridge.git"
homepage = "https://github.com/jieiku/abridge"
minimum_version = "0.19.1"
license = "MIT"
demo = "https://abridge.pages.dev/"

[extra.author]
name = "Jake G (jieiku)"
homepage = "https://github.com/jieiku/"
+++        

<div align="center">
<img src="https://raw.githubusercontent.com/Jieiku/abridge/master/abridge.svg"/>

# Abridge Zola 主题

一个快速、轻量且现代的 [Zola](https://getzola.org) 主题，利用 [abridge.css](https://github.com/Jieiku/abridge.css)（一个类轻量的语义化 HTML CSS 框架）。完美的 [Lighthouse](https://pagespeed.web.dev/report?url=abridge.pages.dev)、[YellowLabTools](https://yellowlab.tools/) 和 [Observatory](https://developer.mozilla.org/en-US/observatory/analyze?host=abridge.netlify.app) 评分。这里是 [Zola 主题基准测试](https://github.com/Jieiku/zola-themes-benchmarks/blob/main/README.md) 页面。

![Lighthouse 评分](https://raw.githubusercontent.com/Jieiku/abridge/master/content/overview-abridge/lighthouse.png)

本项目的维护由所有 <a href="https://github.com/Jieiku/abridge/graphs/contributors">贡献者</a> 和 <a href="https://github.com/sponsors/Jieiku">赞助者</a> 共同实现。如果你想赞助这个项目并让你的头像或公司 logo 出现在下方，请 <a href="https://github.com/sponsors/Jieiku">点击这里</a>。💖

<!-- sponsors --><a href="https://github.com/yugfletcher"><img src="https:&#x2F;&#x2F;github.com&#x2F;yugfletcher.png" width="60px" alt="User avatar: " /></a><a href="https://github.com/samueloph"><img src="https:&#x2F;&#x2F;github.com&#x2F;samueloph.png" width="60px" alt="User avatar: Samuel Henrique" /></a><a href="https://github.com/bensuperpc"><img src="https:&#x2F;&#x2F;github.com&#x2F;bensuperpc.png" width="60px" alt="User avatar: Bensuperpc" /></a><!-- sponsors -->

---

**[查看 Abridge 演示](https://abridge.pages.dev/overview-abridge/)**

**[查看 Abridge.css 演示](https://abridge-css.pages.dev/overview-abridge/)** [[abridge.css 框架](https://github.com/Jieiku/abridge.css/tree/master/dist)]

Abridge.css 演示只是将 Abridge 主题作为子模块使用：[config.toml](https://github.com/Jieiku/abridge.css/blob/master/config.toml), [sass/abridge.scss](https://github.com/Jieiku/abridge.css/blob/master/sass/abridge.scss)
</div>

## 特性

- 完美的 [Lighthouse](https://pagespeed.web.dev/report?url=abridge.pages.dev)、[YellowLabTools](https://yellowlab.tools/) 和 [Observatory](https://developer.mozilla.org/en-US/observatory/analyze?host=abridge.netlify.app) 评分。
- [PWA 支持](https://abridge.pages.dev/overview-abridge/#pwa-progressive-web-app)（渐进式 Web 应用程序）。
- 所有 JavaScript 均可 [完全禁用](https://abridge.pages.dev/overview-abridge/#javascript-files)。
- 暗色、亮色、自动和切换主题。（颜色可自定义，css 变量）
- 代码 [语法高亮](https://abridge.pages.dev/overview-code-blocks/)。（颜色可自定义，css 变量）
- 带有 [行高亮](https://abridge.pages.dev/overview-code-blocks/#toml) 的编号代码块。
- 通过使用 PWA **或** 在 `config.toml` 中设置 `search_library = "offline"` 实现完全离线站点。
- 多语言支持。
- 搜索支持。([elasticlunr](https://abridge.pages.dev/), [pagefind](https://abridge-pagefind.pages.dev/), [tinysearch](https://abridge-tinysearch.pages.dev/))
- 搜索建议导航键，`/` 聚焦，`arrow` 移动，`enter` 选择，`escape` 关闭。
- 搜索结果页面，输入搜索查询然后按 `Enter 键` 或 `点击` 搜索按钮图标。
- [SEO](https://abridge.pages.dev/overview-abridge/#seo-and-header-tags) 支持。（搜索引擎优化）
- [分页](https://abridge.pages.dev/overview-abridge/#pagination) 首页带有编号分页器。
- 文章底部的基于标题的上一篇和下一篇文章链接。
- 页面索引中的目录（可选，可点击链接）
- 最近文章块。（可选）
- 返回顶部按钮。（仅使用 css）
- 代码块复制按钮。
- 页脚中的电子邮件链接混淆。（反垃圾邮件）
- [KaTeX](https://katex.org/) 支持。
- [归档页面](https://abridge.pages.dev/archive/)。
- [标签](https://abridge.pages.dev/tags/)。
- 分类。（类似于标签，默认禁用/注释掉）
- 页脚中的社交图标链接。
- 响应式设计。（移动优先）
- 视频短代码：[Youtube](https://abridge.pages.dev/video-streaming-sites/overview-embed-youtube/)、[Vimeo](https://abridge.pages.dev/video-streaming-sites/overview-embed-vimeo/)、[Streamable](https://abridge.pages.dev/video-streaming-sites/overview-embed-streamable/)。
- 媒体短代码：[video](https://abridge.pages.dev/overview-rich-content/#video)、[img](https://abridge.pages.dev/overview-images/#img-shortcode)、[imgswap](https://abridge.pages.dev/overview-images/#imgswap-shortcode)、[image](https://abridge.pages.dev/overview-rich-content/#image)、[gif](https://abridge.pages.dev/overview-rich-content/#gif)、[audio](https://abridge.pages.dev/overview-rich-content/#audio)。
- 其他短代码：[showdata](https://abridge.pages.dev/overview-showdata/)、[katex](https://abridge.pages.dev/overview-math/#usage-1)。

**[完整文档可在这里获得](https://abridge.pages.dev/overview-abridge/)**

## 快速开始

此主题需要 [Zola](https://www.getzola.org/documentation/getting-started/installation/) 0.19.1 或更高版本

```bash
git clone https://github.com/jieiku/abridge.git
cd abridge
zola serve
# 在浏览器中打开 http://127.0.0.1:1111/
```

## 安装

快速开始展示了如何直接运行主题。接下来我们将使用 abridge 作为新站点的主题。

### 1: 创建一个新的 zola 站点

```bash
yes "" | zola init mysite
cd mysite
```

### 2: 安装 Abridge

将主题添加为 git 子模块：

```bash
git init  # 如果你的项目已经是 git 仓库，请忽略此命令
git submodule add https://github.com/jieiku/abridge.git themes/abridge
git submodule update --init --recursive
git submodule update --remote --merge
```

或者将主题克隆到你的 themes 目录：

```bash
git clone https://github.com/jieiku/abridge.git themes/abridge
```

### 3: 配置

从主题目录复制一些文件到你的项目根目录：

```bash
rsync themes/abridge/.gitignore .gitignore
rsync themes/abridge/config.toml config.toml
rsync themes/abridge/content/_index.md content/
rsync -r themes/abridge/COPY-TO-ROOT-SASS/* sass/
rsync themes/abridge/netlify.toml netlify.toml
rsync themes/abridge/package_abridge.js package_abridge.js
rsync themes/abridge/package.json package.json
```

- `config.toml` 包含所有配置值的基本配置。
- `content/_index.md` 设置分页所需。
- `COPY-TO-ROOT-SASS/abridge.scss` 覆盖以自定义 Abridge 变量。
- `netlify.toml` 设置以使用 netlfiy 部署你的仓库。
- `package_abridge.js` node 脚本用于：更新 PWA 中的缓存文件列表，压缩 js，打包 js
- `package.json` 以便于使用 package_abridge.js

取消注释项目根目录 config.toml 中的主题行：

```bash
sed -i 's/^#theme = "abridge"/theme = "abridge"/' config.toml
```

### 4: 添加新内容

从主题目录复制内容到你的项目或制作新帖子：

```bash
rsync -r themes/abridge/content .
```

### 5: 运行项目

只需在项目的根路径运行 `zola serve`：

```bash
zola serve
```

Zola 将启动开发 Web 服务器，默认访问地址为 `http://127.0.0.1:1111`。

保存的更改将在浏览器中实时重新加载。（按 `ctrl+f5`，或在开发时在 `config.toml` 中设置 `pwa=false`）

## 自定义

有关进一步的自定义，请务必 [查看文档](https://abridge.pages.dev/overview-abridge/)。

## 赞助

你喜欢这个主题吗？它对你有用吗？请给个 github star，如果你愿意捐赠，你可以通过 [github sponsors](https://github.com/sponsors/Jieiku/) 向我捐款。

## 贡献和理念

我们需要你的帮助！特别是修复问题或改进现有功能。

Abridge 的目标是轻量、快速，并且即使禁用了 javascript 或阻止了 javascript 也能正常工作。

唯一可能被认为是必要且依赖于 javascript 的功能是搜索。

## 许可证

**Abridge** 根据 [MIT 许可证](https://github.com/jieiku/abridge/blob/master/LICENSE) 分发。
