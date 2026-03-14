+++
title = "Section"
weight = 20
+++

只要 `content` section 中的目录（或子目录）包含 `_index.md` 文件，就会创建一个 section。如果目录不包含 `_index.md` 文件，则不会创建 section，但该目录中的 Markdown 文件仍将创建页面（称为孤立页面）。

主页（即用户浏览你的 `base_url` 时显示的页面）是一个 section，无论你是否在 `content` 目录的根目录下添加 `_index.md` 文件，它都会被创建。如果你不在内容目录中创建 `_index.md` 文件，此主内容 section 将没有任何内容或元数据。如果你想添加内容或元数据，可以在 `content` 目录的根目录下添加一个 `_index.md` 文件，并像编辑任何其他 `_index.md` 文件一样编辑它；你的 `index.html` 模板随后将能够访问该内容和元数据。

Section 目录中的任何非 Markdown 文件都会添加到 section 的 `assets` 集合中，如 [内容概览](@/documentation/content/overview.md#asset-colocation) 中所述。这些文件随后可以使用相对链接在 Markdown 文件中使用。

## 草稿 (Drafting)

就像页面一样，section 可以通过在 front matter 中设置 `draft` 选项来设为草稿，该选项默认未设置（即 `false`）。当一个 section 被设为草稿时，它的后代（如页面、子 section 和资源）将**不会**被处理，除非传递了 `--drafts` 标志。请注意，如果页面的任何父 section 是草稿，无论它们自己的 `draft` 状态如何，这些页面都不会被处理。

## Front matter (前置数据)

目录中的 `_index.md` 文件定义了该 section 的内容和元数据。要设置元数据，请将 front matter 添加到文件中。

TOML front matter 是一组嵌入在文件开头的元数据，由三个加号 (`+++`) 包围。

在结束的 `+++` 之后，你可以添加内容，这些内容将被解析为 Markdown，并通过 `section.content` 变量提供给你的模板。

虽然没有 front matter 变量是强制性的，但开头和结尾的 `+++` 是必需的。

请注意，尽管鼓励使用 TOML，但也支持 YAML front matter 以便移植旧内容。在这种情况下，嵌入的元数据必须由三个减号 (`---`) 包围。

下面是一个包含所有可用变量的 `_index.md` 示例。下面提供的值是默认值。

```toml
title = ""

description = ""

# 草稿 section 只有在将 `--drafts` 标志传递给 `zola build`、`zola serve` 或 `zola check` 时才会加载。
draft = false

# 用于对页面进行排序，可按 "date", "update_date", "title", "title_bytes", "weight", "slug" 或 "none"。详见下文。
sort_by = "none"

# 父 section 用来排序其子 section。
# 值越小优先级越高。
weight = 0

# 用于渲染此 section 页面的模板。
template = "section.html"

# 给定的模板应用于 section 下的所有页面，递归地。
# 如果你有几个嵌套的 section，每个都设置了 page_template，页面将始终使用最接近自己的那个。
# 但是，页面自己的 `template` 变量总是具有优先权。
# 默认未设置。
page_template =

# 这设置了每个分页页面显示的页面数量。
# 如果未设置此项或值为 0，则不会进行分页。
paginate_by = 0

# 如果设置，这将是分页页面使用的路径。页码将追加在此路径之后。
# 默认为 page/1。
paginate_path = "page"

# 如果设置，分页将按相反顺序进行。
paginate_reversed = false

# 这决定了是否为每个标题插入链接，就像你在本网站上看到的那样（如果你将鼠标悬停在标题上）。
# 可以通过在 `templates` 目录中创建 `anchor-link.html` 文件来覆盖默认模板。
# 此值可以是 "left", "right", "heading" 或 "none"。
# "heading" 意味着整个标题成为锚点的文本。
insert_anchor_links = "none"

# 如果设置为 "true"，section 页面将包含在搜索索引中。这仅在 Zola 配置文件中 `build_search_index` 设置为 "true" 时使用。
in_search_index = true

# 如果设置为 "true"，则渲染 section 主页。
# 当 section 用于组织页面（不直接使用）时很有用。
render = true

# 这决定了当用户访问 section 时是否重定向。默认为未设置。
# 与 `render` 原因相同，但当你不想在访问根 section 页面时出现 404 时很有用。
# 示例：redirect_to = "documentation/content/overview"
redirect_to =

# 如果设置为 "true"，section 将把它的页面传递给父 section。默认为 `false`。
# 当 section 不应该拆分父 section 时很有用，例如 posts section 下的每年 section。
transparent = false

# 如果你正在移动内容但希望将以前的 URL 重定向到当前 URL，请使用别名。这接受路径数组，而不是 URL。
aliases = []

# 如果设置为 "true"，将在此 section 的根路径为此 section 生成 feed 文件。这独立于同名的全站变量。
# section feed 将仅包含来自该相应 feed 的文章，而不包含来自任何其他 section（包括该 section 下的子 section）的文章。
generate_feeds = false

# 你自己的数据。
[extra]
```

请记住，任何配置选项仅适用于直接页面，不适用于子 section 的页面。

## 分页

要为 section 的页面启用分页，请将 `paginate_by` 设置为正数。有关模板中可用变量的更多信息，请参阅 [分页模板文档](@/documentation/templates/pagination.md)。

你还可以通过设置 `paginate_path` 变量来更改分页路径（在 URL 中分页时显示的单词，如 `page/1`），默认为 `page`。

## 排序

Zola 模板遍历页面或 section 以显示给定目录中的所有页面/section 是非常常见的。考虑一个非常简单的示例：一个包含三个文件的 `blog` 目录：`blog/Post_1.md`、`blog/Post_2.md` 和 `blog/Post_3.md`。要遍历这些文章并创建指向文章的链接列表，一个简单的模板可能如下所示：

```jinja
{% for post in section.pages %}
  <h1><a href="{{ post.permalink }}">{{ post.title }}</a></h1>
{% endfor %}
```

这将按照相应 section 的 `_index.md` 页面中 `sort_by` 变量指定的顺序遍历文章。`sort_by` 变量可以赋予几个值：`date`, `update_date`, `title`, `title_bytes`, `weight`, `slug`, `permalink` 或 `none`。如果未设置 `sort_by`，页面将按 `none` 顺序排序，这不适用于排序内容。

任何缺少排序所需数据的页面都将被忽略且不会被渲染。例如，如果页面缺少日期变量并且其 section 设置 `sort_by = "date"`，则该页面将被忽略。如果发生这种情况，终端会警告你。

如果几个页面具有相同的日期/权重/顺序，它们的永久链接将用于根据字母顺序打破平局。

## 页面排序

`sort_by` front-matter 变量可以具有以下值：

### `date`
这将按 `date` 字段对所有页面进行排序，从最近的（在列表顶部）到最旧的（在列表底部）。每个页面都将获得 `page.lower` 和 `page.higher` 变量，分别包含日期较早和较晚的页面。

### `update_date`
与 `date` 相同，只是它会考虑页面的任何 `updated` 日期。

### `title`
这将按 `title` 字段以自然词法顺序对所有页面进行排序，由 [lexical-sort] crate 中的 `natural_lexical_cmp` 定义。每个页面都将获得 `page.lower` 和 `page.higher` 变量，分别包含具有上一个和下一个标题的页面。

例如，这里是自然词法排序："bachata, BART, bolero, μ-kernel, meter, Métro, Track-2, Track-3, Track-13, underground"。请注意特殊字符和数字是如何合理排序的。

[lexical-sort]: https://docs.rs/lexical-sort

### `title_bytes`
与 `title` 相同，只是它直接使用字节进行排序。
自然排序将非 ascii 字符视为其最接近的 ascii 字符。这可能会导致具有不同字符集的语言出现意外结果。例如，瑞典字母表的最后三个字符 åäö 会被自然排序视为 aao。在这种情况下，标准字节顺序排序可能更合适。

### `weight`
这将按 `weight` 字段对所有页面进行排序，从最轻的权重（在列表顶部）到最重的（在列表底部）。每个页面都获得 `page.lower` 和 `page.higher` 变量，分别包含具有更轻和更重权重的页面。

### `slug`
这将按 slug 以自然词法顺序对页面或 section 进行排序。

### `permalink`
与 `slug` 类似，这将按永久链接以自然词法顺序对页面或 section 进行排序。
如果你在页面上设置了 `path` 键，这很有用。

### 反向排序
在遍历页面时，你可能希望使用 Tera `reverse` 过滤器，它反转页面的顺序。例如，在使用 `reverse` 过滤器后，按权重排序的页面将从最轻（在顶部）排序到最重（在底部）；按日期排序的页面将从最旧（在顶部）排序到最新（在底部）。

`reverse` 对 `page.lower` / `page.higher` 没有影响。

如果 section 是分页的，应该在相关 section 的 front matter 中设置 `paginate_reversed=true`，而不是使用过滤器。

## 子 section 排序
排序 section 不太灵活：section 只能按 `weight` 排序，并且没有指向更重/更轻 section 的变量。

默认情况下，最轻（最低 `weight`）的子 section 将在列表顶部，最重（最高 `weight`）将在底部；`reverse` 过滤器反转此顺序。

**注意**：与页面不同，永久链接**不会**用于打破同样权重的 section 之间的平局。因此，如果你的 section 的 `weight` 变量未设置（或者如果设置的方式产生平局），那么你的 section 将按**随机**顺序排序。此外，该顺序是在构建时确定的，并且会在每次站点重建时更改。因此，如果有任何机会你会遍历你的 section，你应该总是为它们分配不同的权重。
