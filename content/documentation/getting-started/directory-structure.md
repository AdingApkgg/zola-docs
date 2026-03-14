+++
title = "目录结构"
weight = 30
+++

运行 `zola init` 后，你应该在你的目录中看到以下结构：


```bash
.
├── config.toml
├── content
├── sass
├── static
├── templates
└── themes

5 directories, 1 file
```

如果你运行默认的 `zola build/serve` 命令，你也可能会看到一个 `public` 目录，其中包含站点的一些输出：`zola build` 生成的完整站点，而 `zola serve` 仅生成静态资源。此文件夹将由 `zola serve` 自动删除/创建。

以下是这些目录和 `config.toml` 的高级概览。

## `config.toml`

一个强制性的 TOML 格式的 Zola 配置文件。
此文件在 [配置文档](@/documentation/getting-started/configuration.md) 中有详细说明。

## `content`

包含所有标记内容（主要是 `.md` 文件）。
`content` 目录的每个子目录代表一个 [section](@/documentation/content/section.md)，其中包含 [pages](@/documentation/content/page.md)（你的 `.md` 文件）。

要了解更多信息，请阅读 [内容概览页面](@/documentation/content/overview.md)。

## `sass`

包含要编译的 [Sass](https://sass-lang.com) 文件。非 Sass 文件将被忽略。
复制编译后的文件时，将保留 `sass` 文件夹的目录结构；例如，`sass/something/site.scss` 处的文件将被编译为 `public/something/site.css`。

## `static`

包含任何类型的文件。`static` 目录中的所有文件/目录都将原样复制到输出目录。
如果你的静态文件很大，你可以通过在配置文件中设置 `hard_link_static = true` 来配置 Zola 对它们进行 [硬链接](https://zh.wikipedia.org/wiki/硬链接) 而不是复制它们。

## `templates`

包含将用于渲染站点的所有 [Tera](https://keats.github.io/tera) 模板。
查看 [模板文档](@/documentation/templates/_index.md) 以了解有关默认模板和可用变量的更多信息。

## `themes`

包含可用于你的站点的主题。如果你不打算使用主题，请将此目录留空。
如果你想了解有关主题的信息，请参阅 [主题文档](@/documentation/themes/_index.md)。
