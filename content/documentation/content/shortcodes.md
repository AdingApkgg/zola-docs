+++
title = "Shortcodes"
weight = 40
+++

Zola 借鉴了 WordPress 的 [shortcodes](https://codex.wordpress.org/Shortcode_API)（短代码）概念。
在我们的例子中，shortcode 对应于 `templates/shortcodes` 目录中定义的模板，可以在 Markdown 文件中使用。

广义上讲，Zola 的 shortcodes 涵盖两个不同的用例：

* 注入更复杂的 HTML：Markdown 擅长写作，但当你需要添加内联 HTML 或样式时，它就不太好了。
* 简化基于数据的重复性任务：当你有想要在页面正文中显示的 [外部数据](@/documentation/templates/overview.md#load-data) 时。

后者也可以通过编写 HTML 来解决，但 Zola 允许使用以 `.md` 而不是 `.html` 结尾的基于 Markdown 的 shortcodes。如果你想在 [目录](@/documentation/content/table-of-contents.md) 中包含由 shortcode 生成的标题，这可能特别有用。

如果你想在模板中使用类似于 shortcodes 的东西，可以使用 [Tera macros](https://keats.github.io/tera/docs#macros)。它们是可以调用以返回一些文本的函数或组件。

## 编写 Shortcode

作为示例，让我们编写一个嵌入 YouTube 视频的 shortcode。
在 `templates/shortcodes` 目录中名为 `youtube.html` 的文件中，粘贴以下内容：

```jinja
<div {% if class %}class="{{class}}"{% endif %}>
    <iframe
        src="https://www.youtube.com/embed/{{id}}{% if autoplay %}?autoplay=1{% endif %}"
        webkitallowfullscreen
        mozallowfullscreen
        allowfullscreen>
    </iframe>
</div>
```

这个模板非常简单：一个指向 YouTube 嵌入 URL 的 iframe，包裹在一个 `<div>` 中。
就输入而言，此 shortcode 至少需要一个变量：`id`（[示例在此](#shortcodes-without-body)）。
因为其他变量在 `if` 语句中，所以它们是可选的。

就是这样。Zola 现在将识别此模板为名为 `youtube` 的 shortcode（文件名减去 `.html` 扩展名）。

Markdown 渲染器会将内联 HTML 节点（如 `<a>` 或 `<span>`）包装在一个段落中。
如果你想禁用此行为，请将你的 shortcode 包裹在 `<div>` 中。

反过来，基于 Markdown 的 shortcode 将被视为其返回的内容是页面正文的一部分。例如，如果我们在 `templates/shortcodes` 中创建 `books.md`：

```jinja
{% set data = load_data(path=path) -%}
{% for book in data.books %}
### {{ book.title }}

{{ book.description | safe }}
{% endfor %}
```

这将创建一个名为 `books` 的 shortcode，其参数 `path` 指向一个 `.toml` 文件，从中加载带有标题和描述的书籍列表。它们将与调用 `books` 的文档的其余部分一起流动。

Shortcodes 在解析页面的 Markdown 之前呈现，因此它们无法访问页面的目录。
因此，你也不能使用 [`get_page`](@/documentation/templates/overview.md#get-page) / [`get_section`](@/documentation/templates/overview.md#get-section) / [`get_taxonomy`](@/documentation/templates/overview.md#get-taxonomy) / [`get_taxonomy_term`](@/documentation/templates/overview.md#get-taxonomy-term) 全局函数。它在运行 `zola serve` 时可能会工作，因为它已被加载，但在 `zola build` 期间将失败。

## 使用 Shortcodes

有两种类型的 shortcodes：

- 不带主体的，例如上面的 YouTube 示例
- 带主体的，例如为引用添加样式的 shortcode

在这两种情况下，参数必须命名，并且它们都将传递给模板。
即使没有参数，括号也是强制性的。

请注意，虽然 shortcodes 看起来像普通的 Tera 表达式，但它们根本不是 Tera——它们几乎只是将参数传递给它们的模板。几个值得注意的限制是：

- 所有参数都是必需的
- Shortcode 不能引用 Tera 变量
- 连接和其他运算符不可用

如果 shortcode 无效，Markdown 解析器将不会解释它，而是直接渲染到最终 HTML 中。

最后，shortcode 名称（以及相应的 `.html` 文件）以及任何参数名称只能包含数字、字母和下划线，并且必须以字母或下划线开头。
用 Regex 术语来说，`^[A-Za-z_][0-9A-Za-z_]+$`。

参数值可以是以下五种类型之一：

- string: 由双引号、单引号或反引号包围
- bool: `true` 或 `false`
- float: 带小数点的数字 (例如 1.2)
- integer: 整数或其负对应物 (例如 3)
- array: 任何类型值的数组，数组除外

格式错误的值将被静默忽略。

两种类型的 shortcode 还将根据它们的使用位置获得 `page` 或 `section` 变量以及 `config` 变量。这些值将覆盖传递给 shortcode 的任何参数，因此不应将这些变量名用作 shortcode 中的参数名。

### 无主体 Shortcodes

只需像在变量块中调用 Tera 函数一样调用 shortcode。

```md
这是一个 YouTube 视频：

{{/* youtube(id="dQw4w9WgXcQ") */}}

{{/* youtube(id="dQw4w9WgXcQ", autoplay=true) */}}

一个内联 {{/* youtube(id="dQw4w9WgXcQ", autoplay=true, class="youtube") */}} shortcode
```

请注意，如果你想拥有一些看起来像 shortcode 的内容，但不希望 Zola 尝试渲染它，你需要通过使用 `{{/*` 和 `*/}}` 而不是 `{{` 和 `}}` 来转义它。

### 有主体 Shortcodes

让我们想象一下，我们有以下 `quote.html` shortcode 模板：

```jinja
<blockquote>
    {{ body }} <br>
    -- {{ author}}
</blockquote>
```

我们可以像这样在 Markdown 文件中使用它：

```md
正如某人所说：

{%/* quote(author="Vincent") */%}
A quote
{%/* end */%}
```

Shortcode 的主体将自动作为 `body` 变量传递给渲染上下文，并且需要在新行上。

### 无参数 Shortcodes

请注意，对于这两种情况，shortcodes 的括号都是必需的。
没有括号的 shortcode 将渲染为纯文本，并且不会发出警告。

例如，这是如何在 `aside.html` 中定义没有参数的带主体的 `aside` shortcode：
```jinja
<aside>
    {{ body }}
</aside>
```

我们可以像这样在 Markdown 文件中使用它：

```md
读者可以参考 aside 以获取更多信息。

{%/* aside() */%}
An aside
{%/* end */%}
```

### 类似 Shortcodes 的内容

如果你想拥有一些看起来像 shortcode 的内容，但不希望 Zola 尝试渲染它，你需要通过使用 `{%/*` 和 `*/%}` 而不是 `{%` 和 `%}` 来转义它。直到结束标记之前，你不需要转义其他任何内容。

## Shortcode 上下文

每个 shortcode 都可以访问一些变量，除了你显式传递为参数的变量之外。这些变量在以下小节中解释：

- 调用计数 (`nth`)
- 当前语言 (`lang`)，除非从 `markdown` 模板过滤器调用（在这种情况下，它将始终与配置中的 `default_language` 相同，或者在未设置时为 `en`）
- `colocated_path`

当这些变量之一与作为参数传递的变量冲突时，将使用参数值。

### `nth`: 调用计数

每个 shortcode 上下文都传入一个名为 `nth` 的变量，该变量跟踪特定 shortcode 在当前 Markdown 文件中被调用的次数。给定一个 shortcode `true_statement.html` 模板：

```jinja
<p id="number{{ nth }}">{{ value }} is equal to {{ nth }}.</p>
```

它可以像这样在我们的 Markdown 中使用：

```md
{{/* true_statement(value=1) */}}
{{/* true_statement(value=2) */}}
```

这在实现诸如旁注或尾注等功能的自定义标记时很有用。

### `lang`: 当前语言

**注意：** 从 `markdown` 模板过滤器中调用 shortcode 时，`lang` 变量将始终为 `en`。
如果你觉得你需要那个，请考虑改用模板宏。
如果你真的需要那个，你可以重写你的 Markdown 内容以将 `lang` 作为参数传递给 shortcode。

每个 shortcode 都可以访问上下文中的 `lang` 变量中的当前语言。
这对于根据每种语言在 shortcode 中呈现/过滤信息很有用。例如，要在名为 `bookcover.md` 的 shortcode 中显示当前页面的每种语言的书籍封面：

```jinja
![Book cover in {{ lang }}](cover.{{ lang }}.png)
```

### `page` 或 `section`

你可以访问普通模板中等效变量的略微精简版本。
以下属性将为空：

- translations
- backlinks
- pages

（注意：这是因为 markdown 的渲染是在填充 sections 之前完成的）

shortcodes 中 `page` 的一个有用属性是 `colocated_path`。
这用于当你想要将一些资源的名称传递给 shortcodes 而不重复完整的文件夹路径时。
当与 `load_data` 或 `resize_image` 结合使用时最有用。

```jinja
{% set resized = resize_image(format="jpg", path=page.colocated_path ~ img_name, width=width, op="fit_width") %}
<img alt="{{ alt }}" src="{{ resized.url | safe }}" />
```

## 示例

这里有一些 shortcodes 供灵感。

### YouTube

嵌入 YouTube 视频的响应式播放器。

参数有：

- `id`: 视频 id (强制)
- `playlist`: 播放列表 id (可选)
- `class`: 添加到围绕 iframe 的 `<div>` 的类
- `autoplay`: 当设置为 "true" 时，视频在加载时自动播放

代码：

```
<div {% if class %}class="{{class}}"{% endif %}>
    <iframe src="https://www.youtube-nocookie.com/embed/{{id}}{% if playlist %}?list={{playlist}}{% endif %}{% if autoplay %}?autoplay=1{% endif %}" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
</div>
```

使用示例：

```md
{{/* youtube(id="dCKeXuVHl1o") */}}

{{/* youtube(id="dCKeXuVHl1o", playlist="RDdQw4w9WgXcQ") */}}

{{/* youtube(id="dCKeXuVHl1o", autoplay=true) */}}

{{/* youtube(id="dCKeXuVHl1o", autoplay=true, class="youtube") */}}
```

### 图片库 (Image Gallery)

有关代码和示例，请参阅 [内容处理页面](@/documentation/content/image-processing/index.md#creating-picture-galleries)。
