+++
title = "内部链接和深度链接"
weight = 50
+++

## 标题 ID 和锚点插入

在渲染 Markdown 内容时，将自动为每个标题分配一个唯一 ID。
如果 `slugify.anchors` 设置为 `"on"`（默认值），则此 ID 是通过将标题文本转换为 [slug](https://zh.wikipedia.org/wiki/Slug_(%E7%BD%91%E7%BB%9C%E5%87%BA%E7%89%88)) 来创建的。
如果 `slugify.paths` 设置为 `"safe"`，空格将被替换为 `-`，并删除以下字符：`#`, `%`, `<`, `>`, `[`, `]`, `(`, `)`, \`, `^`, `{`, `|`, `}`。
如果 `slugify.paths` 设置为 `"off"`，则不进行任何修改，你可能会留下名义上非法的 ID。
如果该文章的 slug 已经存在，则在末尾附加一个数字。
例如：

```md
# Something exciting! <- something-exciting
## Example code <- example-code

# Something else <- something-else
## Example code <- example-code-1
```

你还可以在标题行上手动指定带有 `{#…}` 后缀的 ID 以及 CSS 类：

```md
# Something manual! {#manual .header .bold}
```

这对于使深度链接健壮很有用，无论是主动地（以便以后更改标题文本而不破坏指向它的链接）还是追溯地（在更改文本时保留旧标题文本的 slug）。它对于迁移具有不同标题 ID 方案的现有站点也很有用，以便你可以保持深度链接正常工作。

## 锚点插入

Zola 可以自动在标题旁边插入锚点链接，如果你将鼠标悬停在标题上或覆盖整个标题文本，你可以在本文档中看到这一点。

此选项在全局 [`config.toml`](@/documentation/getting-started/configuration.md) 的 `[markdown]` section 中设置，并可以通过 [section front matter 页面](@/documentation/content/section.md#front-matter) 上的 `insert_anchor_links` 变量在 section 级别覆盖。

默认模板非常基础，需要在你的项目中进行 CSS 调整才能看起来体面。
如果你想更改锚点模板，可以通过在 `templates` 目录中创建 `anchor-link.html` 文件来轻松覆盖它。在 [这里](https://github.com/getzola/zola/blob/master/components/templates/src/builtins/anchor-link.html) 你可以找到默认模板。

锚点链接模板具有以下变量：

- `id`: 应用 `slugify.anchors` 定义的规则后的标题 ID
- `lang`: 当前语言，除非从 `markdown` 模板过滤器调用，在这种情况下它将始终为 `en`
- `level`: 标题级别（1 到 6 之间）

如果你使用 `insert_anchor_links = "heading"`，模板仍将被使用，但只有开头的 `<a>` 标签将从中提取，其他所有内容将不被使用。

## 内部链接

链接到其他页面及其标题非常常见，以至于 Zola 向 Markdown 链接添加了一种特殊语法来处理它们：以 `@/` 开头链接，并指向你要链接到的 `.md` 文件。文件的路径从 `content` 目录开始。

例如，链接到位于 `content/pages/about.md` 的文件将是 `[my link](@/pages/about.md)`。
你仍然可以直接链接到锚点；`[my link](@/pages/about.md#example)` 将按预期工作。

默认情况下，损坏的内部链接被视为错误。要将它们视为警告，请访问 `config.toml` 的 `[link_checker]` section 并设置 `internal_level = "warn"`。注意：将损坏的链接视为警告允许在损坏的链接完好无损的情况下构建站点，因此诸如 `[my link](@/pages/whoops.md)` 之类的链接将被渲染为 HTML `<a href="@/pages/whoops.md">`。
