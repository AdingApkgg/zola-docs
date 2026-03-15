
+++
title = "Ergo"
description = "一个专注于写作的简单博客主题，灵感来自 svbtle"
template = "theme.html"
date = 2025-07-30T22:58:44+02:00

[taxonomies]
theme-tags = []

[extra]
created = 2025-07-30T22:58:44+02:00
updated = 2025-07-30T22:58:44+02:00
repository = "https://github.com/insipx/Ergo.git"
homepage = "https://github.com/insipx/Ergo"
minimum_version = "0.4.1"
license = "MIT"
demo = "https://ergo.liquidthink.net"

[extra.author]
name = "Andrew Plaza"
homepage = "https://liquidthink.net"
+++        

[ergo 现场演示](http://ergo.liquidthink.net)



![Ergo 截图](https://i.imgur.com/l182IYg.jpg)

一个轻量、简单且美观的 Zola 主题，专注于写作。灵感来自 sbvtle 和 Pixyll。

像这两个网页设计一样，Ergo 是一个强调内容的主题，但仍然试图保持时尚。坦率地说，设计最像 sbvtle (http://sbvtle.com)，但没有巧妙的 svbtle 引擎、Javascript、社区或 kudos 按钮（不过 kudos 在添加列表中！但我得用 JS...）
如果你发现你喜欢所有这些东西，请查看 [svbtle](http://svbtle.com)；此主题旨在作为一种更轻量（免费）的替代方案，随着我以及它的用户（如果有的话）的发展，ergo 的设计很可能在未来会有更多分歧。
这并不意味着是 svbtle 的克隆。


这里有一个延时摄影：
[![Ergo 创作延时摄影](https://img.youtube.com/vi/ogEjvM-v_-s/0.jpg)](https://www.youtube.com/watch?v=ogEjvM-v_-s)


## 安装

获取 [Zola](https://www.getzola.org/) 和/或按照他们的指南 [安装主题](https://www.getzola.org/documentation/themes/installing-and-using-themes/)。
确保将 `theme = "ergo"` 添加到你的 `config.toml`

Ergo 依赖于在 `content/_index.md` 中设置 `paginate_by` 变量。

#### 检查 zola 版本（仅 0.11.0+）
只是为了再次检查以确保你有正确的版本。不支持在 0.11.0 以下的版本中使用此主题。

### 如何服务
进入你的站点目录，并输入 `zola serve`。你应该会在 `localhost:1111` 看到你的新站点。

### 部署到 Github Pages 或 Netlify
[Zola](https://www.getzola.org) 已经有很好的文档用于部署到 [Netlify](https://www.getzola.org/documentation/deployment/netlify/) 或 [GitHub Pages](https://www.getzola.org/documentation/deployment/github-pages/)。我就不用重复的解释让你感到厌烦了。

### 自定义主题
站点上使用的所有颜色都来自 `sass/colors.scss`。总共只有大约 5-6 种颜色。
随你喜欢更改它们！随意进入主题并编辑颜色。但是，强烈建议不要编辑除 `sass/colors.scss` 以外的任何内容。继续自行承担风险！

#### 主题选项
```toml
# 指定要在主题中的徽标中使用的个人资料图片。它可以是 svg, png, jpg 等，只要确保复制你想要的徽标并将其放在 img/${YOUR_PROFILE}.* 中
# 并相应地更新你的 config.toml
profile = 'profile.svg'

# 描述。这对于 SEO/站点元数据目的是必需的
description = "Simple blog theme focused on writing, inspired by svbtle"

# 主题使用的颜色主题（主题将使用 ${color_theme}.css 文件，由具有相同名称的 SASS 或 SCSS 文件生成）。默认为 ["default"]。用户可以选择其中之一，默认主题是列表中的第一个。
color_themes = ["my-awesome-theme", "default"]

[[extra.socials]] # website
icon = "globe"
icon_class = "fas"
display = "code.liquidthink.net"
uri = "https://code.liquidthink.net"

[[extra.socials]] # github
icon = "github"
display = "Insipx"
uri = "https://github.com/Insipx"

[[extra.socials]] # twitter
icon = "twitter"
display = "@liquid_think"
uri = "https://twitter.com/liquid_think"

[[extra.socials]] # email
icon = "envelope"
icon_class = "fas"
display = "say hello"
uri = "mailto:${MY_EMAIL}@cool_domain.com?subject=hi"

[[extra.socials]]
icon = "instagram"
display = "${your_insta}"
uri = "https://instagram.com/${your_insta}"

[[extra.socials]]
icon = "keybase"
display = "${your_keybase}"
uri = "https://keybase.io/${your_keybase}"

[[extra.socials]]
icon = "linkedin"
display = "${your_linkedin}"
uri = "https://www.linkedin.com/in/${your_linkedin}"

[[extra.socials]]
icon = "reddit"
display = "${your_reddit}"
uri = "https://www.reddit.com/u/${your_reddit}"

[[extra.socials]]
icon = "youtube"
display = "${your_youtube_channel_id}"
uri = "https://youtube.com/channel/${your_youtube_channel_id}"

# 是否使用国旗或语言代码
country_flags = true
```

## 特性
  - [x] 分页
  - [ ] 动态配色方案
  - [ ] 在 `config.toml` 中编辑颜色
  - [x] 无 JS
  - [ ] 分析
  - [x] 评论？
  - [ ] 点赞按钮 http://kudosplease.com/
  - [ ] 分类？
  - [ ] 相关文章？（没有数据库，有意义的相关文章或无意义的相关文章值得吗？）
  - [ ] 用户请求：打开一个 Issue，或者如果你愿意，提交一个 Pull Request
