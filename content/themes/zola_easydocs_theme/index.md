
+++
title = "EasyDocs"
description = "为你的项目创建文档的简单方法"
template = "theme.html"
date = 2026-03-05T13:34:03+01:00

[taxonomies]
theme-tags = []

[extra]
created = 2026-03-05T13:34:03+01:00
updated = 2026-03-05T13:34:03+01:00
repository = "https://github.com/codeandmedia/zola_easydocs_theme.git"
homepage = "https://github.com/codeandmedia/zola_easydocs_theme"
minimum_version = "0.21.0"
license = "MIT"
demo = "https://easydocs.codeandmedia.com"

[extra.author]
name = "Roman Soldatenkov"
homepage = "https://codeandmedia.com"
+++        

## 为你的项目创建文档库的简单方法

演示: [https://easydocs.codeandmedia.com/](https://easydocs.codeandmedia.com/)

此 [Zola](https://getzola.org)（静态站点引擎）主题可帮助你轻松快速地构建和发布项目文档。Zola 只是一个二进制文件，在构建用 Markdown 编写的文档后输出 html 页面和其他静态资产。因此，你可以使用主题、你的 md 文件、Zola 并获得灵活简单的文档网站。

### 一步一步

正如你可能听说过的那样，Zola 非常灵活 :) 因此，下面的场景是完成任务的数百种可能方法之一，请随时寻找最适合你的方法。此外，Zola 提供了自己的机制来安装和使用主题，请参阅 [文档](https://www.getzola.org/documentation/themes/installing-and-using-themes/)。

1. Fork 仓库并将 content 文件夹内的演示内容替换为你的内容。但是请查看 _index.md 文件。它包含 `title`，当你想要在标题右侧有锚点时，请向每个 index 添加 `insert_anchor_links = "right"`。`theme.toml`、截图和自述文件也可以删除。
2. 在 `config.toml` 中更改 URL 和标题为你自己的。在 extra 部分，你可以指定 GitHub API 的路径，以便在导航栏上的 logo 下方显示版本、favicon 和 logo 本身。或者如果你不需要，只需删除这些行。此外，你可以配置或打开一些与 Zola 相关的其他设置。[规范在这里](https://www.getzola.org/documentation/getting-started/configuration/)。
3. 在 sass/_variables.scss 中，你可以根据需要更改字体、颜色或背景。
4. 差不多完成了。现在，你应该决定如何构建以及在哪里托管你的网站。你可以在本地构建并上传到某个地方。或者在 GitHub Actions 中构建并托管在 GitHub Pages / Netlify / CloudFlare Pages / AnyS3CloudStorage 上。[GitHub Pages 指南](https://www.getzola.org/documentation/deployment/github-pages/)。[我的示例](https://github.com/o365hq/o365hq.com/blob/main/.github/workflows/main.yml) GitHub 工作流，包含 2 步构建（第一步检查链接和拼写错误，第二步上传到 Azure）。用于制作 Docker 镜像的 [Dockerfile](https://github.com/codeandmedia/zola_docsascode_theme/blob/master/Dockerfile)。

## Zola v0.22 更新

看来对于 Zola 0.22，config.toml 已更新，某些字段失去了向后兼容性

之前: 

```
[markdown]
highlight_code = true
highlight_theme = "base16-ocean-light"

```

现在

```
[markdown]

[markdown.highlighting]
theme = "github-light"   
```

请查看你使用的版本并选择正确的配置。

## 提供的配置选项

这些选项可以在 [config.toml](config.toml) 的 `extra` 部分进行配置。
如果不存在任何选项，则其行为与入门 [config.toml](config.toml) 中显示的默认值相同。

- **easydocs_logo_always_clickable** 控制 logo 是否始终可点击。默认情况下，仅当你不在首页时 logo 才可点击。如果启用此选项，它将使 logo 在首页上也可点击。因此，在首页上，它基本上只会刷新页面，因为它会将你带到同一页面。
- **easydocs_uglyurls** 为不使用网络服务器的离线站点提供支持。如果设置为 true，导航中的链接将生成包含 `index.html` 的完整路径。此功能的灵感来自 [Abridge 主题](https://www.getzola.org/themes/abridge/)。请注意，要使其工作，还需要将 base URL 设置为存储站点的本地文件夹，例如 `base_url = file:///home/user/mysite/public/`。因此，这不是可移植的，仅适用于特定的本地文件夹，但不需要网络服务器即可导航站点。
- **easydocs_heading_threshold** 控制在左侧导航栏中显示标题之前页面所需的最小标题数。默认为 5。例如，可以通过将其设置为 1 来始终显示每个页面上的标题。

享受你的文档吧！

* _图标: [Office UI Fabric Icons](https://uifabricicons.azurewebsites.net/)_
* _复制代码按钮: [Aaron Luna](https://aaronluna.dev/blog/add-copy-button-to-code-blocks-hugo-chroma/)_
