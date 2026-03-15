
+++
title = "zerm"
description = "一个基于 Radek Kozieł Hugo 主题的极简暗色主题"
template = "theme.html"
date = 2022-06-13T20:01:34-07:00

[taxonomies]
theme-tags = []

[extra]
created = 2022-06-13T20:01:34-07:00
updated = 2022-06-13T20:01:34-07:00
repository = "https://github.com/ejmg/zerm.git"
homepage = "https://github.com/ejmg/zerm"
minimum_version = "0.8.0"
license = "MIT"
demo = "https://zerm.ejmg.now.sh/"

[extra.author]
name = "elias julian marko garcia"
homepage = "https://github.com/ejmg"
+++        

# zerm

一个适用于 [Zola](https://getzola.org) 的极简暗色主题。

![截图](../master/zerm-preview.png?raw=true)

[**在线预览！**](https://zerm.ejmg.now.sh/)

该主题很大程度上移植自 Radek Kozieł 为 Hugo 制作的 [Terminal Theme](https://github.com/panr/hugo-theme-terminal)。在移植过程完成了 4/5 时，我发现了 Paweł Romanowski 为 Zola 制作的独立分支 [Terminimal](https://github.com/pawroman/zola-theme-terminimal)，它帮助我更快地完成了从 PostCSS 到 Sass 的样式转换。衷心感谢你们两位！

## 差异

本主题在很大程度上忠实于 Radek 的原作，但也有一些细微的差别。这些差异几乎都是风格上的，旨在进一步强调极简主义。其中一些如下：
- 标签（tags）现在包含在文章的元数据中。
- 没有文章图片预览。
- 分类（categories）包含在分类法（taxonomy）中。
- 项目符号的边距稍大，嵌套使用不同的符号。
- 不支持社交媒体或评论。

其中一些功能可能会在以后添加，随时[欢迎提交 PR](https://github.com/ejmg/zerm/pulls)。

## 配置

请遵循 Zola 文档了解[如何使用主题](https://www.getzola.org/documentation/themes/installing-and-using-themes/#installing-a-theme)。

在 `config.toml` 中，你会发现目前支持的所有自定义值都有文档说明其用法。如果有任何困惑或功能不符合预期，[请提交 issue](https://github.com/ejmg/zerm/issues)！

## 数学公式

你可以使用 KaTeX 进行数学排版。
只有在页面 Front Matter 的 `extra` 部分通过单行配置（`math=true`）选择启用时，资源才会加载。

```md
# index.md
+++
title="页面标题"
...

[extra]
math=true
+++

内容
```

未选择启用的页面不会受到任何影响，因此你不必担心性能下降。

## 许可证

MIT。详情请参阅 `LICENSE.md`。
