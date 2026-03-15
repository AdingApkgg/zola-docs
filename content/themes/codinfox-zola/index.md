
+++
title = "codinfox-zola"
description = "Zola 的 Codinfox 主题"
template = "theme.html"
date = 2023-05-11T01:34:05+02:00

[taxonomies]
theme-tags = []

[extra]
created = 2023-05-11T01:34:05+02:00
updated = 2023-05-11T01:34:05+02:00
repository = "https://github.com/svavs/codinfox-zola.git"
homepage = "https://github.com/svavs/codinfox-zola"
minimum_version = "0.11.0"
license = "MIT"
demo = "https://codinfox-zola.vercel.app/"

[extra.author]
name = "Silvano Sallese"
homepage = "https://svavs.github.io/"
+++        

# Codinfox-Zola

![Zola Deploy to Github Pages on push](https://github.com/svavs/codinfox-zola/workflows/Zola%20Deploy%20to%20Pages%20on%20push/badge.svg?branch=master)

这是一个 [Zola](https://www.getzola.com) 主题，灵感来自 [Codinfox-Lanyon](https://codinfox.github.com/)，一个基于 Lanyon 的 [Jekyll](http://jekyllrb.com) 主题。在此处查看实时演示 [here](https://codinfox-zola.vercel.app/)。

此主题将内容放在首位，将导航隐藏在抽屉中。

* 专为 [Zola](https://www.getzola.com) 构建
* 在 GitHub 上开发，并免费托管在 [GitHub Pages](https://pages.github.com) 和 [Vercel](https://vercel.com) 上
* 使用 [Spacemacs](https://www.spacemacs.org) 编写

此主题支持：

1. 主题颜色：你可以选择自己喜欢的主题颜色（在 `_config.scss` 中更改）
2. 可更改的侧边栏位置（通过更改 `_config.scss` 中的布尔值来反转它）
3. 集成 FontAwesome, MathJax, Disqus 和 Google Analytics
4. 支持多语言站点
5. 支持 Gravatar
6. 以及对原始 Lanyon 和 Codinfox-Lanyon 的许多改进

所有配置变量及其含义都在：

- `config.toml`（用于 zola 配置变量和此主题所需的一些额外变量），
- `author.toml`（用于显示关于站点作者的个人信息），
- `nav.toml`（用于站点侧边栏中可用的导航菜单结构）
- `_config.scss`（用于定义一些 css 自定义）

选项非常简单，并在注释中有描述。

在 [GitHub](https://github.com/svavs/codinfox-zola) 上了解更多信息并做出贡献。

有问题或建议？请随时在 [GitHub 上打开 issue](https://github.com/svavs/codinfox-zola/issues/new) 或在 [Twitter 上问我](https://twitter.com/svavs)。

### 开始之前

[获取一个 gravatar 帐户](https://gravatar.com) 并设置个人资料图片。

#### 将 gravatar 个人资料图片添加到 codinfox-zola 主题

1. 登录 gravatar.com
2. 点击 My Profile
3. 点击 RH 侧边栏中个人资料名称下方的 **view profile**
4. 点击 JSON
5. 复制第 4 行的 `hash` 值
6. 将 `hash` 值粘贴到 `author.toml` 第 10 行


### 安装和使用

要使用此主题，你可以遵循任何 Zola 主题所需的说明。

只需将此仓库克隆到你站点主文件夹的 `themes` 文件夹下即可。

然后，在 config.toml 中定义所需的额外变量（从主题的 config.toml 文件中获取），在站点的主文件夹中创建并定义 author.toml 和 nav.toml 配置文件（与 config.toml 同级），就是这样！

要定义你自己的主页图片，请将图像文件放入 `static/img/` 文件夹并在 config.extra.image 变量中设置路径。

现在可以像往常一样在 `content` 文件夹中创建内容。

如果你想使用此主题拥有博客，请在 `content` 文件夹内创建一个包含所有 Markdown 格式的博客文章的文件夹。Zola 会自动生成一个你可以作为博客管理的版块。在 [实时演示](https://codinfox-zola.vercel.app/blog/) 中查看示例。


 
## 许可证

根据 [MIT 许可证](LICENSE.md) 开源。


## 待办
 - 用于隐藏电子邮件地址链接的 recaptcha (https://developers.google.com/recaptcha/intro)
 - 主索引版块页面的顶部栏中隐藏的多语言链接
