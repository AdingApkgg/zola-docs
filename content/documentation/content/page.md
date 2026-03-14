+++
title = "Page"
weight = 30
+++

页面是 `content` 目录中除名为 `_index.md` 的文件之外的任何以 `.md` 结尾的文件。**注意：**页面文件名不能包含 `_index.` [字样](https://github.com/getzola/zola/pull/1694)。

如果以 `.md` 结尾的文件名为 `index.md`，它将生成一个以其目录名称命名的页面（例如，`/content/about/index.md` 将在 `[base_url]/about` 创建一个页面）。（注意没有下划线；如果文件名为 `_index.md`，它将在 `[base_url]/about` 创建一个 **section**，如本文档前一部分所讨论的那样。相反，将文件命名为 `index.md` 将在 `[base_url]/about` 创建一个 **page**）。

如果文件被赋予 `index.md` 或 `_index.md` _以外_ 的任何名称，那么它将创建一个具有该名称的页面（不带 `.md`）。例如，在你的 content 目录根目录中命名一个文件 `about.md` 将在 `[base_url]/about` 创建一个页面。

此规则的另一个例外是，以日期时间（YYYY-mm-dd 或 [RFC3339 日期时间](https://www.ietf.org/rfc/rfc3339.txt)）开头的文件名将使用该日期作为页面日期，除非已在 front matter 中设置。日期时间文件名后面可以跟一个下划线 (`_`) 或破折号 (`-`) 和 slug。
页面名称将是日期时间或 `_`/`-` 之后的任何内容，因此文件 `2018-10-10.md` 将在 `[base_url]/2018-10-10` 可用，而 `2018-10-10-hello-world.md` 将在 `[base_url]/hello-world` 可用。请注意，完整的 RFC3339 日期时间包含冒号，这在 Windows 上的文件名中不是有效字符。
可以通过将 `slugify.paths_keep_dates` 设置为 `true`（默认为 `false`）来禁用此行为。请注意，当 `slugify.paths` 的默认值为 `"on"` 时，分隔日期的 `_` 将被 slugify 为 `-`。

如你所见，创建 `about.md` 文件等同于创建 `about/index.md` 文件。这两种方法之间的唯一区别是，创建 `about` 目录允许你使用资源共置，如 [概览](@/documentation/content/overview.md#asset-colocation) section 中所讨论的那样。

## 输出路径

对于你的 content 文件夹中的任何页面，其输出路径将由以下两者之一定义：

- 其 `slug` frontmatter 键
- 其文件名

无论哪种方式，这些建议的路径在使用前都会被清理。
如果在站点的配置中将 `slugify.paths` 设置为 `"on"` - 默认值 - 路径将被 [slugified](https://en.wikipedia.org/wiki/Clean_URL#Slug)。
如果设置为 `"safe"`，则仅执行清理，删除以下字符：`<`, `>`, `:`, `/`, `|`, `?`, `*`, `#`, `\\`, `(`, `)`, `[`, `]` 以及换行符和制表符。这确保了路径可以在所有操作系统上表示。
此外，尾随空格和点被删除，空格被替换为 `_`。

如果 `slugify.paths` 设置为 `"off"`，则不进行任何修改。

如果你想要包含非 ASCII 字符的 URL，`slugify.paths` 需要设置为 `"safe"` 或 `"off"`。

### 来自 frontmatter 的路径

页面的输出路径将首先从页面的 frontmatter 中的 `slug` 键读取。

**示例：**（文件 `content/zines/élevage-chèvre.md`）

```
+++
title = "L'élevage de chèvres, la carrière alternative de tous dévelopeurs'"
slug = "élevage-chèvre-carrière-alternative"
+++
This is my article.
```

此 frontmatter 将在 `slugify.paths` 设置为 `"safe"` 或 `"off"` 时将文章输出到 `[base_url]/zines/élevage-chèvre-carrière-alternative`，并在 `slugify.paths` 默认值 `"on"` 时输出到 `[base_url]/zines/elevage-chevre-carriere-alternative`。

### 来自文件名的路径

当文章的输出路径未在 frontmatter 中指定时，它将从 content 文件夹中的文件路径中提取。考虑一个文件 `content/foo/bar/thing.md`。输出路径的构造如下：

- 如果文件名是 `index.md`，其父文件夹名称 (`bar`) 用作输出路径
- 否则，输出路径从 `thing`（不带 `.md` 扩展名的文件名）中提取

如果找到的路径以日期时间字符串（`YYYY-mm-dd` 或 [RFC3339 日期时间](https://www.ietf.org/rfc/rfc3339.txt)）开头，后跟可选空格，然后是下划线 (`_`) 或破折号 (`-`)，则此日期将从输出路径中删除，并将用作页面日期（除非已在 front-matter 中设置）。请注意，完整的 RFC3339 日期时间包含冒号，这在 Windows 上的文件名中不是有效字符。

从文件路径提取的输出路径随后根据 `slugify.paths` 配置进行 slugify 或不进行 slugify，如前所述。

**示例：**
文件 `content/blog/2018-10-10-hello-world.md` 将生成页面 `[base_url]/blog/hello-world`。带有可选空格的文件 `content/blog/2021-01-23 -hello new world.md` 将生成页面 `[base_url]/blog/hello-new-world`。

## Front matter (前置数据)

TOML front matter 是一组嵌入在文件开头的元数据，由三个加号 (`+++`) 包围。

虽然没有 front matter 变量是强制性的，但开头和结尾的 `+++` 是必需的。

请注意，尽管鼓励使用 TOML，但也支持 YAML front matter 以便移植旧内容。在这种情况下，嵌入的元数据必须由三个减号 (`---`) 包围。

下面是一个包含所有可用变量的示例页面。下面提供的值是默认值。

```toml
title = ""
description = ""

# 文章的日期。
# 允许两种格式：YYYY-MM-DD (2012-10-02) 和 RFC3339 (2002-10-02T15:00:00Z)。
# 不要将日期用引号括起来；下面的行仅表示没有默认日期。
# 如果 section 变量 `sort_by` 设置为 `date`，那么任何缺少 `date` 的页面将不会被渲染。
# 设置此项将覆盖文件名中设置的日期。
date =

# 文章的最后更新日期，如果与日期不同。
# 格式与 `date` 相同。
updated =

# 文档 Section 页面上定义的权重。
# 如果 section 变量 `sort_by` 设置为 `weight`，那么任何缺少 `weight` 的页面将不会被渲染。
weight = 0

# 草稿页面只有在将 `--drafts` 标志传递给 `zola build`、`zola serve` 或 `zola check` 时才会加载。
draft = false

# 当设置为 "false" 时，Zola 不会为此页面创建一个包含 index.html 的单独文件夹。
render = false

# 如果设置，将使用此 slug 代替文件名来制作 URL。
# section 路径仍将被使用。
slug = ""

# 内容将出现的路径。
# 如果设置，它不能为空字符串，并且将覆盖 `slug` 和文件名。
# section 的路径将不会被使用。
# 它不应以 `/` 开头，如果开头有 `/` 将被删除。
path = ""

# 如果你正在移动内容但希望将以前的 URL 重定向到当前 URL，请使用别名。这接受路径数组，而不是 URL。
aliases = []

# 页面作者列表。如果启用了站点 feed，第一个作者（如果有）将在默认 feed 模板中用作页面的作者。
authors = []

# 如果设置为 "true"，页面将包含在搜索索引中。这仅在 Zola 配置中 `build_search_index` 设置为 "true"
# 并且父 section 在其 front matter 中没有将 `in_search_index` 设置为 "false" 时使用。
in_search_index = true

# 用于渲染此页面的模板。
template = "page.html"

# 此页面的分类法。键必须与 `config.toml` 中配置的分类法名称相同，值是字符串对象数组。例如，
# tags = ["rust", "web"].
[taxonomies]

# 你自己的数据。
[extra]
```

## 摘要

你可以要求 Zola 创建摘要，例如，如果你只想在列表中显示页面内容的第一段。

为此，请在内容中你希望摘要结束的位置添加 `<!-- more -->`。到该点为止的内容将通过 `page.summary` 在 [模板](@/documentation/templates/pages-sections.md#page-variables) 中单独可用。

在此位置会创建一个带有 `continue-reading` id 的 span 元素，因此如果需要，你可以直接链接到它。例如：
`<a href="{{ page.permalink }}#continue-reading">继续阅读</a>`。

`<!-- more -->` 标记也可以存在于行中间，它将确保这不会发出未闭合的 HTML 标签。
你可以使用 `summary-cutoff.html` 根据截止前的摘要显示摘要之后的文本（但在这些闭合标签之前）。

默认情况下，无论摘要的内容如何，它都会显示省略号 (…)，但如果你想仅在摘要不以任何标点符号结尾时显示省略号，你可以使用不同的模板：

```jinja
{% if summary is matching("\PP$") %}&hellip;{% endif %}
```
