+++
title = "配置"
weight = 40
+++

默认配置足以让 Zola 在本地运行，但也仅此而已。
它遵循“按需付费”的理念，几乎所有内容默认都是关闭的。

要更改配置，请编辑 `config.toml` 文件。
如果你不熟悉 TOML，请查看 [TOML 规范](https://github.com/toml-lang/toml)。

⚠️ 如果你在 `config.toml` 中添加键，必须注意它属于哪个 TOML 部分。TOML 部分以标题开头，例如 `[search]`，并在下一个部分或文件末尾结束。

以下是当前的 `config.toml` 部分：
1. main (未命名)
2. markdown
3. link_checker
4. slugify
5. search
6. translations
7. languages
8. extra

**只有 `base_url` 变量是强制性的**。其他一切都是可选的。下面列出了 Zola 使用的所有配置变量及其默认值：

```toml
# 站点的基本 URL；唯一必需的配置变量。
base_url = "https://mywebsite.com"

# 站点标题和描述；默认情况下用于 feed。
title = ""
description = ""

# 默认语言；用于 feed。
default_language = "zh"

# 要使用的站点主题。
theme = ""

# 用于覆盖默认输出目录 `public`，将其设置为其他值（例如："docs"）
output_dir = "public"

# 是否在（重新）构建站点时保留输出目录根级别的点文件。
# 启用此功能还可以防止在重建时删除输出文件夹本身。
preserve_dotfiles_in_output = false

# 当设置为 "true" 时，站点根目录中 `sass` 目录下的 Sass 文件将被编译。
# 主题目录中的 Sass 文件总是会被编译。
compile_sass = false

# 当设置为 "true" 时，生成的 HTML 文件将被压缩。
minify_html = false

# 指定在处理内容目录时要忽略的资源文件的 glob 模式列表。
# 默认为空，这意味着所有资源文件都将复制到 `public` 目录。
# 示例：
#     ignored_content = ["*.{graphml,xlsx}", "temp.*", "**/build_folder"]
ignored_content = []

# 与 ignored_content 类似，指定在处理 static 目录时要忽略的资源文件的 glob 模式列表。
# 默认为空，这意味着所有资源文件都将复制到 `public` 目录。
ignored_static = []

# 当设置为 "true" 时，会自动生成 feed。
generate_feeds = false

# 当设置为 "all" 时，分页页面不包含在 sitemap 中，默认为 "none"
exclude_paginated_pages_in_sitemap = "none"

# 用于 feed 的文件名。也用作模板文件名。
# 默认为 ["atom.xml"]，它有一个内置模板，可以渲染 Atom 1.0 feed。
# 还有一个内置模板 "rss.xml"，可以渲染 RSS 2.0 feed。
feed_filenames = ["atom.xml"]

# 包含在 feed 中的文章数量。如果没有设置此限制（默认值），则包含所有项目。
# feed_limit = 20

# 当设置为 "true" 时，`static` 目录中的文件将被硬链接。对于大型静态文件很有用。
# 请注意，要使其工作，`static` 和输出目录都需要在同一个文件系统上。
# 请注意，无论此设置如何，主题的 `static` 文件总是被复制。
hard_link_static = false

# 页面的默认作者
author =

# 为站点渲染的分类法及其默认语言的配置
# 示例：
#     taxonomies = [
#       {name = "tags", feed = true}, # 每个标签都有自己的 feed
#       {name = "tags"}, # 你可以在多种语言中使用相同名称的分类法
#       {name = "categories", paginate_by = 5},  # 一个术语每页 5 个项目
#       {name = "authors"}, # 基本定义：没有 feed 或分页
#     ]
#
taxonomies = []

# 所有分类法的可选基本路径。如果设置，所有分类法路径将相对于此路径。
# 例如，如果 taxonomy_root 是 "blog" 并且 taxonomy 是 "tags"，路径将是 /blog/tags/
# taxonomy_root = "blog"

# 当设置为 "true" 时，将从 `default_language` 的页面和 section 内容构建搜索索引。
build_search_index = false

# 当设置为 "false" 时，不生成 Sitemap.xml
generate_sitemap = true

# 当设置为 "false" 时，不生成 robots.txt
generate_robots_txt = true

# Markdown 渲染的配置
[markdown]
# 当设置为 "true" 时，emoji 别名将转换为渲染后的 Markdown 文件中对应的 Unicode emoji。（例如：:smile: => 😄）
render_emoji = false

# 添加到外部链接的 CSS 类（例如 "external-link"）
external_links_class =

# 外部链接是否在新标签页中打开
# 如果为 true，出于安全原因，总是会自动添加 `rel="noopener"`
external_links_target_blank = false

# 是否为所有外部链接设置 rel="nofollow"
external_links_no_follow = false

# 是否为所有外部链接设置 rel="noreferrer"
external_links_no_referrer = false

# 是否为所有外部链接设置 rel="external"
external_links_external = true

# 是否启用智能标点符号（将引号、破折号、点更改为其排版形式）
# 例如，`...` 变为 `…`，`"quote"` 变为 `“curly”` 等
smart_punctuation = false

# 是否启用定义列表的解析
definition_list = false

# 是否为所有图像设置 decoding="async" 和 loading="lazy"
# 当开启时，alt 文本必须是纯文本。
# 例如，`![xx](...)` 可以，但 `![*x*x](...)` 不行
lazy_async_image = false

# 脚注是渲染为 GitHub 风格（在底部，带有反向引用）还是普通风格（在定义的地方）
bottom_footnotes = false

# 当设置为 "true" 时，在 Markdown 解析器中启用对 GitHub 风格警告（也称为 callouts 或 admonitions）的支持。
# 例如，以下 Markdown 语法：
#
#     > [!NOTE]
#     > alert note
#
# 将导致生成以下 HTML：
#
#     <blockquote class="markdown-alert-note">
#     <p>alert note</p>
#     </blockquote>
#
# 其中 CSS 类名后缀可能是 `note`, `tip`, `important`, `warning` 或 `caution`，具体取决于警告类型。
# 视觉外观取决于主题级支持；有关更多信息，请参阅主题文档。
github_alerts = false

# 这决定了是否为每个标题插入链接，就像你在本网站上看到的那样（如果你将鼠标悬停在标题上）。
# 可以通过在 `templates` 目录中创建 `anchor-link.html` 文件来覆盖默认模板。
# 此值可以是 "left", "right", "heading" 或 "none"。
# "heading" 意味着整个标题成为锚点的文本。
# 有关更多信息，请参阅文档中的“内部链接和深度链接”。
insert_anchor_links = "none"

# 语法高亮配置（可选）
[markdown.highlighting]
# 当设置为 "true" 时，缺少高亮语言将被视为错误。默认为 false，但建议设置为 true。
error_on_missing_language = false

# 是使用内联十六进制颜色 (`inline`) 还是 CSS 类 (`class`)
style = "inline"

# 选择主题总是必需的：你可以选择单个 (1) 或双重主题 (2)。
# 不再可能像 0.22 之前那样仅输出 CSS 类。
# 1. 如果你使用单个主题，请将其名称放在此处。有关可能的选择，请参阅语法高亮页面。
theme = ""

# 2. 如果你需要浅色/深色主题，请改用下面的 2 个字段。有关可能的选择，请参阅语法高亮页面。
light_theme = ""
dark_theme = ""

# 额外的 JSON TextMate 语法文件列表
extra_grammars = []

# 额外的 JSON TextMate 主题文件列表
# 从 https://textmate-grammars-themes.netlify.app/ 获取主题
extra_themes = []

# 链接检查器的配置。
[link_checker]
# 跳过以此前缀开头的外部 URL 的链接检查
skip_prefixes = [
    "http://[2001:db8::]/",
]

# 跳过以此前缀开头的外部 URL 的锚点检查
skip_anchor_prefixes = [
    "https://caniuse.com/",
]

# 将内部链接问题视为 "error" 或 "warn"，默认为 "error"
internal_level = "error"

# 将外部链接问题视为 "error" 或 "warn"，默认为 "error"
external_level = "error"

# 各种 slugification 策略，详见下文
# 默认为所有内容都变成 slug
[slugify]
paths = "on"
taxonomies = "on"
anchors = "on"
# 是否删除页面路径 slug 的日期前缀。
# 例如，content/posts/2016-10-08_a-post-with-dates.md => posts/a-post-with-dates
# 当为 true 时，content/posts/2016-10-08_a-post-with-dates.md => posts/2016-10-08-a-post-with-dates
paths_keep_dates = false

[search]
# 是否在索引中包含页面/section 的标题
include_title = true
# 是否在索引中包含页面/section 的描述
include_description = false
# 是否在搜索索引中包含页面的 RFC3339 日期时间
include_date = false
# 是否在索引中包含页面/section 的路径（永久链接总是包含在内）
include_path = false
# 是否在索引中包含页面/section 的渲染内容
include_content = true
# 在哪个代码点截断内容。如果你有很多页面并且索引在站点上加载会变得太大，这很有用。
# 默认为未设置。
# truncate_content_length = 100

# 是生成 javascript 文件还是 JSON 文件作为搜索索引
# 接受的值：
# - "elasticlunr_javascript", "elasticlunr_json"
# - "fuse_javascript", "fuse_json"
index_format = "elasticlunr_javascript"

# 默认语言的可选翻译对象
# 示例：
#     default_language = "fr"
#
#     [translations]
#     title = "Un titre"
#
[translations]

# 其他语言定义
# 你可以定义特定于语言的配置值和翻译：
# title, description, generate_feeds, feed_filenames, taxonomies, build_search_index
# 以及它自己的搜索配置和翻译（详见上文）
[languages]
# 例如
# [languages.fr]
# title = "Mon blog"
# generate_feeds = true
# taxonomies = [
#    {name = "auteurs"},
#    {name = "tags"},
# ]
# build_search_index = false

# 你可以在这里放置任何类型的数据。这些数据
# 将在所有模板中可用
# 示例：
#     [extra]
#     author = "Famous author"
#
# author 值将在模板中使用 {{ config.extra.author }} 可用
#
[extra]
```

## Slugification 策略

默认情况下，Zola 会将每个路径、分类法和锚点转换为 slug，这是一种没有特殊字符的 ASCII 表示形式。
但是，如果你希望 URL 中包含 UTF-8 字符，你可以为每种类型的项目更改该策略。有 3 种策略：

- `on`：默认策略，所有内容都转换为 slug
- `safe`：Windows (`<>:"/\|?*`) 或 Unix (`/`) 上文件中不能存在的字符被删除，其他所有内容保留
- `off`：不更改任何内容，你的站点可能无法在某些操作系统上构建和/或破坏各种 URL 解析器

由于锚点没有文件名问题，`safe` 和 `off` 策略在锚点的情况下是相同的：唯一的更改是将空格替换为 `_`，因为空格在锚点中无效。

请注意，如果你使用默认策略以外的策略，你将不得不手动转义空格和 Markdown 标记以便能够链接到你的页面。例如，指向名为 `some space.md` 的文件的内部链接需要在你的 Markdown 文件中写成 `some%20space.md`。
