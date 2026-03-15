
+++
title = "d3c3nt"
description = "一个简单、干净且灵活的个人站点主题。"
template = "theme.html"
date = 2022-06-13T18:37:21-07:00

[taxonomies]
theme-tags = []

[extra]
created = 2022-06-13T18:37:21-07:00
updated = 2022-06-13T18:37:21-07:00
repository = "git://git.figbert.com/d3c3nt.git"
homepage = "https://git.figbert.com/d3c3nt/"
minimum_version = "0.15.0"
license = "AGPLv3"
demo = "https://d3c3nt.figbert.com"

[extra.author]
name = "FIGBERT"
homepage = "https://figbert.com"
+++        

# d3c3nt

d3c3nt 是一个简单、干净且灵活的个人站点主题，由 [FIGBERT] 为 [Zola 静态站点引擎][Zola] 制作。此主题主要是为我的个人网站开发的，因此当我有需要制作新功能和样式时，就会添加它们。

总而言之，它相当……decent（不错）。

## 安装

要在你自己的站点中使用 d3c3nt，你必须将其添加到你的 `themes` 目录中。你可以通过多种方式做到这一点，但我建议将其添加为 git 子模块：

```
$ cd themes/
$ git submodule add git://git.figbert.com/d3c3nt.git
```

安装主题后，在你的 `config.toml` 中将顶级 `theme` 变量设置为 `"d3c3nt"`。

有关 Zola 主题的一般信息，请查看 Zola 的 [官方网站][zola-docs]。要了解有关 d3c3nt 的特性和配置的更多信息，请前往 [项目文档][docs]。

## whoami

要了解更多关于我的信息，请随意查看 [我的网站][FIGBERT] 并通过 [Atom 订阅][Atom] 订阅。你可以通过电子邮件联系我：
[figbert+d3c3nt@figbert.com][Email]。

[FIGBERT]: https://figbert.com/
[Zola]: https://getzola.org/
[zola-docs]: https://www.getzola.org/documentation/themes/overview/
[docs]: https://d3c3nt.figbert.com/config/
[Atom]: https://figbert.com/atom.xml
[Email]: mailto:figbert+d3c3nt@figbert.com
