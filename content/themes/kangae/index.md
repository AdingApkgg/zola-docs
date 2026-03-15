
+++
title = "kangae"
description = "一个用于 zola 的轻量级微博主题"
template = "theme.html"
date = 2023-06-20T18:32:08-07:00

[taxonomies]
theme-tags = []

[extra]
created = 2023-06-20T18:32:08-07:00
updated = 2023-06-20T18:32:08-07:00
repository = "https://github.com/ayushnix/kangae.git"
homepage = "https://github.com/ayushnix/kangae"
minimum_version = "0.15.0"
license = "NCSA"
demo = "https://kangae.ayushnix.com/"

[extra.author]
name = "Ayush Agarwal"
homepage = "https://microblog.ayushnix.com"
+++        

# kangae (考え, idea or thought)

[kangae][1] 是一个用于 [zola][2] 的轻量级微博主题。

<details>
  <summary>kangae 桌面端和移动端截图</summary>

  ![kangae 桌面端亮色模式截图](static/images/kangae-desktop-light.webp)
  ![kangae 桌面端暗色模式截图](static/images/kangae-desktop-dark.webp)
  ![kangae 移动端亮色模式截图](static/images/kangae-mobile-light.webp)
  ![kangae 移动端暗色模式截图](static/images/kangae-mobile-dark.webp)
</details>

我从零开始创建了 kangae，它不基于任何其他主题。然而，我是在看到 [Wolfgang Müller 的微博][3] 后受到启发创建 kangae 的。谢谢 Wolf！

kangae 根据 [NCSA 许可证][5] 授权，这与 BSD-3-Clause 许可证非常相似。
与 BSD-3-Clause 不同，NCSA 还涵盖项目的文档。

# 展示

以下是使用 kangae 主题的网站列表

- [ayushnix microblog][4]

如果你想在本节中提及你的网站，请提出拉取请求。

# 安装

在使用此主题之前，请 [安装 zola][6]。安装 zola 后，

```
$ zola init microblog
> What is the URL of your site? (https://example.com):
> Do you want to enable Sass compilation? [Y/n]:
> Do you want to enable syntax highlighting? [y/N]:
> Do you want to build a search index of the content? [y/N]:
$ cd microblog/
```

kangae 不使用 Sass 或语法高亮，所以如果你不想使用自定义 Sass 代码或启用语法高亮，请在第 2 和第 3 个问题回答 'no'。kangae 也不使用任何 JavaScript 库来搜索内容。如果你不打算安装 JavaScript 库以在你的微博上启用搜索，请在最后一个问题也回答 'no'。

如果你打算在 GitHub 等 forge 上发布你的微博，请使用以下命令初始化一个空的 git 仓库

```
$ git init
$ git commit --allow-empty -m 'initial empty root commit'
```

如果你不想进行空提交，请添加并提交 README 或 LICENSE 文件。

此时，你可以使用以下方法之一安装 kangae

## 使用 `git subtree`

```
$ git subtree add -P themes/kangae/ --squash https://github.com/ayushnix/kangae.git master
```

## 使用 `git submodule`

```
$ git submodule add https://github.com/ayushnix/kangae.git themes/kangae
```

## 在 themes 目录下载 kangae

如果你想保持简单并在以后弄清楚版本控制，你可以

```
$ git clone https://github.com/ayushnix/kangae.git themes/kangae
```

# 配置

安装后开始使用 kangae，

```
$ cp themes/kangae/config.toml ./
$ sed -i 's;# theme =\(.*\);theme =\1;' config.toml
```

kangae 的 [`config.toml`][7] 文件已使用 TOML 注释仔细记录。如果你有任何关于配置 kangae 的问题，而 `config.toml` 文件本身没有回答，请 [提出 issue][8]。

## 短代码

kangae 提供了几个短代码，可用于以可访问的方式添加内容

### kaomoji `(・_・)ノ`

如果你想在你的帖子中使用颜文字，你可以使用以下方式以可访问的方式插入它们

```
I don't know. {{/* kaomoji(label="shrug kaomoji", text="╮( ˘_˘ )╭") */}} I've never thought about it.
```

提供 `label` 的值是可选的，但强烈建议。应该提到一个简短的文本，解释颜文字想要传达的意思。`text` 的值应该是实际的表情符号本身。

此短代码也可用于任何其他可以放入内联段落的 ASCII 表情符号。
这包括西方表情符号如 `;)` 和组合表情符号如 `<(^_^<)`。

### 引用

你可以在微博帖子中添加引用，使用

```
{%/* quote(author="Nara Shikamaru") */%}
You would think just this once, when it was life or death, I could pull through.
{%/* end */%}
```

这是相对于在 markdown 中简单使用 `>` 编写引用的最基本改进形式。

如果你想提及引用来源的名称，例如书名或电影名，你可以使用

```
{%/* quote(citation="Mass Effect 3", author="Javik") */%}
Stand in the ashes of a trillion dead souls, and ask the ghosts if honor matters. The silence is your answer.
{%/* end */%}
```

也可以为此短代码提供 `citeurl` 作为参数，以提供借用来源的实际 URL。

```
{%/* quote(author="Edward Snowden", citeurl="https://old.reddit.com/r/IAmA/comments/36ru89/just_days_left_to_kill_mass_surveillance_under/crglgh2/") */%}
Arguing that you don't care about the right to privacy because you have nothing to hide is no different than saying you don't care about free speech because you have nothing to say.
{%/* end */%}
```

可以在 [这篇博文][14] 中找到这些短代码外观的实时预览。

## 可选特性

kangae 包含一些默认未启用的可选特性

- [使用 ↗ unicode 符号样式化外部链接][11]

# 捐赠

如果你发现 kangae 对创建你自己的微博网站有帮助，请考虑通过给我买杯咖啡来支持我 :coffee:

<a href='https://www.buymeacoffee.com/ayushnix' target='_blank' rel="noopener"><img src='https://cdn.buymeacoffee.com/buttons/default-blue.png' alt='buy ayushnix a coffee at buymeacoffee.com' border='0' height='36'></a>
<a href='https://ko-fi.com/O5O64SQ4C' target='_blank' rel="noopener"><img src='https://cdn.ko-fi.com/cdn/kofi1.png?v=2' alt='buy ayusnix a coffee at ko-fi.com' border='0' height='36'></a>

如果你在印度，你也可以使用 UPI 进行捐赠。我的 UPI 地址是 `ayushnix@ybl`。

# 备注

虽然我不是 Web 开发人员，但我有兴趣学习 HTML 和 CSS 以创建轻量级文本网站。你可能有兴趣阅读 [关于我如何学习 HTML 和 CSS 的日志][12]。
然而，该页面只是我思想的无组织转储，并不是一篇润色过的博文。
[Seirdy 关于创建文本网站的博文][13] 可能是一个更好的参考。

# 待办 (也许?)

- (响应式) 图片短代码
- 部署前在 HTML 和 CSS 上运行 prettier
- twitter 和 mastodon 短代码
- 添加可选支持以在不使用 JS 的情况下在 mastodon 上交叉发布和评论
- 添加对 [giscus][9] 和 [加载 mastodon 评论][10] 的可选支持
- 为 asciinema 添加短代码
- 为 blockquote 和 citation 添加短代码
- 分页
- 亮色和暗色模式切换
- 内容选项卡
- 微数据和 microformats2

[1]: https://kangae.ayushnix.com/
[2]: https://www.getzola.org/
[3]: https://zunzuncito.oriole.systems/
[4]: https://microblog.ayushnix.com
[5]: LICENSE
[6]: https://www.getzola.org/documentation/getting-started/installation/
[7]: config.toml
[8]: https://github.com/ayushnix/kangae/issues/new
[9]: https://giscus.app/
[10]: https://carlschwan.eu/2020/12/29/adding-comments-to-your-static-blog-with-mastodon/
[11]: https://github.com/ayushnix/kangae/blob/master/static/css/style-external-links.css
[12]: https://wiki.ayushnix.com/frontend/creating-a-website/
[13]: https://seirdy.one/2020/11/23/website-best-practices.html
[14]: https://kangae.ayushnix.com/being-shikamaru-102/
