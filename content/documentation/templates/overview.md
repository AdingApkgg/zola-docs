+++
title = "概览"
weight = 10
+++

Zola 使用 [Tera](https://keats.github.io/tera) 模板引擎，它与 Jinja2、Liquid 和 Twig 非常相似。

由于本文档仅讨论模板如何在 Zola 中工作，如果你想先了解更多相关信息，请阅读 [Tera 模板文档](https://keats.github.io/tera/docs/#templates)。

所有模板都位于 `templates` 目录中。如果你不确定模板中有哪些变量可用，可以在模板中放置 `{{ __tera_context }}` 以打印整个上下文。

除 feeds 和 sitemap 外，所有模板都有一些变量可用：

- `config`: 语言感知的 [配置](@/documentation/getting-started/configuration.md)
- `current_path`: 当前页面的路径（不带 `base_url` 的完整 URL），总是以 `/` 开头
- `current_url`: 当前页面的完整 URL
- `lang`: 当前页面的语言

配置变量可以像 `config.variable` 这样访问，例如在 HTML 中使用 `{{ config.base_url }}`。
404 模板无法获取 `current_path` 和 `current_url`（无法确定这些信息）。

除了上面提到的 `config` 属性外，它还获得了 `config.mode`，即它是在 `build`、`serve` 还是 `check` 模式下运行。

## 标准模板

默认情况下，Zola 将查找三个模板：`index.html`，应用于站点主页；`section.html`，应用于所有 sections（通过在 `content` 目录中创建目录生成的任何 HTML 页面）；以及 `page.html`，应用于所有 pages（通过在 `content` 目录中创建 `.md` 文件生成的任何 HTML 页面）。

主页始终是一个 section（无论它是否包含其他页面）。
因此，`index.html` 和 `section.html` 模板都可以访问 section 变量。`page.html` 模板可以访问 page 变量。
下一节将更详细地描述 page 和 section 变量。

## 内置模板

Zola 自带四个内置模板：`atom.xml` 和 `rss.xml`（在 [Feeds](@/documentation/templates/feeds/index.md) 中描述），`sitemap.xml`（在 [Sitemap](@/documentation/templates/sitemap.md) 中描述），以及 `robots.txt`（在 [Robots.txt](@/documentation/templates/robots.md) 中描述）。
此外，主题可以添加自己的模板，如果没有被覆盖，这些模板将被应用。你可以通过在正确路径中创建同名模板来覆盖内置或主题模板。例如，你可以通过创建 `templates/atom.xml` 文件来覆盖 Atom 模板。

## 自定义模板

除了标准的 `index.html`、`section.html` 和 `page.html` 模板外，你还可以通过在 `templates` 目录中创建 `.html` 文件来创建自定义模板。这些自定义模板默认不会被使用。相反，自定义模板 *仅* 在你通过将 `template` front-matter 变量设置为该模板的路径（或者如果你在另一个被应用的模板中 `include` 它）时才会被使用。例如，如果你为站点的“关于”页面创建了一个名为 `about.html` 的自定义模板，你可以通过在 `about.md` 页面中包含以下 front matter 来将其应用于 `about.md` 页面：

```md
+++
title = "关于我们"
template = "about.html"
+++
```

自定义模板不需要位于 `templates` 目录的根目录下。
例如，`product_pages/with_pictures.html` 是一个有效的模板。

## 内置过滤器

Zola 在 Tera 中已有的 [过滤器](https://keats.github.io/tera/docs/#filters) 之外添加了一些过滤器。

### markdown

使用 Markdown 将给定变量转换为 HTML。与 page/section Markdown 渲染相比，有一些区别：

- 此过滤器评估的 shortcodes 无法访问当前的渲染上下文：`config` 可用，但在 `markdown` 过滤器调用的 shortcode 中访问 `section` 或 `page`（以及其他变量）将阻止你的站点构建（请参阅 [此讨论](https://github.com/getzola/zola/pull/1358)）
- shortcodes 中的 `lang` 将始终等于站点的 `config.default_language`（否则为 `en`）；这应该不是问题，但在大多数情况下如果需要在过滤器中使用感知语言的 shortcodes，请参考文档的 [Shortcode context](@/documentation/content/shortcodes.md#shortcode-context) 部分。

默认情况下，过滤器会将所有文本包裹在一个段落中。要禁用此行为，你可以将 `true` 传递给 inline 参数：

```jinja
{{ some_text | markdown(inline=true) }}
```

你不需要对 `page.content` 或 `section.content` 使用此过滤器，内容已经渲染过了。

### base64_encode

将变量编码为 base64。

### base64_decode

从 base64 解码变量。

### regex_replace

通过正则表达式替换文本。

```jinja
{{ "World Hello" | regex_replace(pattern=`(?P<subject>\w+), (?P<greeting>\w+)`, rep=`$greeting $subject`) }}
<!-- Hello World -->
```

### num_format

将数字格式化为其字符串表示形式。

```jinja
{{ 1000000 | num_format }}
<!-- 1,000,000 -->
```

默认情况下，这将使用 config.toml 中 `config.default_language` 设置的语言环境来格式化数字。

要为特定语言环境格式化数字，你可以使用 `locale` 参数并传递所需语言环境的名称：

```jinja
{{ 1000000 | num_format(locale="en-IN") }}
<!-- 10,00,000 -->
```

## 内置函数

Zola 添加了一些 Tera 函数到 [Tera 内置函数](https://keats.github.io/tera/docs#built-in-functions) 中，以便更轻松地开发复杂的站点。

### 文件搜索逻辑

对于通过 `get_page` 和 `get_section` 以外的方式在磁盘上搜索文件的函数，适用以下逻辑。

1. 基本目录是 Zola 根目录，即 `config.toml` 所在的位置
2. 对于给定的路径：如果以 `@/` 开头，将其替换为 `content/` 并修剪任何前导 `/`
3. 按以下顺序在以下位置搜索，返回第一个存在文件的位置：
   1. `$base_directory` + `$path`
   2. `$base_directory` + `"static/"` + `$path`
   3. `$base_directory` + `"content/"` + `$path`
   4. `$base_directory` + `$output_path` + `$path`
   5. `$base_directory` + `"themes"` + `$theme` + `"static/"` + `$path`（仅当使用主题时）

实际上，这意味着 `@/some/image.jpg`、`/content/some/image.jpg` 和 `content/some/image.jpg` 将指向同一个东西。

如果路径在 Zola 目录之外，它将报错。

### `get_page`

获取 `.md` 文件的路径并返回关联的页面。基本路径是 `content` 目录。

```jinja
{% set page = get_page(path="blog/page2.md") %}
```

如果为页面选择特定语言，可以将带有语言代码的 `lang` 传递给函数：

```jinja
{% set page = get_page(path="blog/page2.md", lang="fr") %}

{# 如果 "fr" 是默认语言，这等效于 #}
{% set page = get_page(path="blog/page2.md") %}

{# 如果 "fr" 不是默认语言，这等效于 #}
{% set page = get_page(path="blog/page2.fr.md") %}
```

### `get_section`

获取 `_index.md` 文件的路径并返回关联的 section。基本路径是 `content` 目录。

```jinja
{% set section = get_section(path="blog/_index.md") %}
```

如果你只需要 section 的元数据，可以将 `metadata_only=true` 传递给函数：

```jinja
{% set section = get_section(path="blog/_index.md", metadata_only=true) %}
```

如果为 section 选择特定语言，可以将带有语言代码的 `lang` 传递给函数：

```jinja
{% set section = get_section(path="blog/_index.md", lang="fr") %}

{# 如果 "fr" 是默认语言，这等效于 #}
{% set section = get_section(path="blog/_index.md") %}

{# 如果 "fr" 不是默认语言，这等效于 #}
{% set section = get_section(path="blog/_index.fr.md") %}
```

### `get_taxonomy_url`

获取找到的 taxonomy 项目的永久链接。

```jinja
{% set url = get_taxonomy_url(kind="categories", name=page.taxonomies.category, lang=page.lang) %}
```

`name` 几乎总是来自变量，但如果你想手动执行此操作，该值应与 front matter 中的值相同，而不是 slugified 版本。

`lang`（可选）默认为 config.toml 中的 `config.default_language`

`required`（可选）如果定义了 taxonomy 但没有任何内容使用它，则抛出错误。默认为 true。

### `get_taxonomy`

获取特定类型的整个 taxonomy。

```jinja
{% set categories = get_taxonomy(kind="categories") %}
```

输出的类型是：

```ts
kind: TaxonomyConfig;
items: Array<TaxonomyTerm>;
lang: String;
permalink: String;
```

`lang`（可选）默认为 config.toml 中的 `config.default_language`

`required`（可选）如果定义了 taxonomy 但没有任何内容使用它，则抛出错误。默认为 true。

有关这些类型的完整文档，请参阅 [Taxonomies 文档](@/documentation/templates/taxonomies.md)。

### `get_taxonomy_term`

从特定类型的 taxonomy 中获取单个术语。

```jinja
{% set categories = get_taxonomy_term(kind="categories", term="term_name") %}
```

输出的类型是单个 `TaxonomyTerm` 项目。

`lang`（可选）默认为 config.toml 中的 `config.default_language`

`include_pages`（可选）默认为 true。如果为 false，`TaxonomyTerm` 中的 `pages` 项目将为空，无论该术语实际存在多少页面。在两种情况下，`page_count` 都将正确反映该术语的页面数。

`required`（可选）如果未找到 taxonomy 或术语。

有关这些类型的完整文档，请参阅 [Taxonomies 文档](@/documentation/templates/taxonomies.md)。

### `get_url`

获取给定路径的永久链接。
如果路径以 `@/` 开头，它将被视为指向 Markdown 文件的 [内部链接](@/documentation/content/linking.md#internal-links)，从根 `content` 目录开始并进行验证。

```jinja
{% set url = get_url(path="@/blog/_index.md") %}
```

它接受一个可选参数 `lang`，以便在多语言网站中计算 *感知语言的 URL*。假设 `config.base_url` 是 `"http://example.com"`，以下代码段将：

- 如果 `config.default_language` 是 `"en"`，则返回 `"http://example.com/blog/"`
- 如果 `config.default_language` **不是** `"en"` 且 `"en"` 出现在 `config.languages` 中，则返回 `"http://example.com/en/blog/"`
- 否则失败，错误消息为 `"'en' is not an authorized language (check config.languages)."`

```jinja
{% set url = get_url(path="@/blog/_index.md", lang="en") %}
```

这也可以用于获取静态文件的永久链接，例如如果你想链接到位于 `static/css/app.css` 的文件：

```jinja
{{/* get_url(path="css/app.css") */}}
```

默认情况下，链接不会有尾部斜杠。你可以通过将 `trailing_slash=true` 传递给 `get_url` 函数来强制添加一个。
例如：

```jinja
{{/* get_url(path="css/app.css", trailing_slash=true) */}}
```

对于非内部链接，你还可以通过将 `cachebust=true` 传递给 `get_url` 函数，在 URL 末尾添加格式为 `?h=<sha256>` 的缓存破坏。在这种情况下，路径需要解析为实际文件。
有关详细信息，请参阅 [文件搜索逻辑](@/documentation/templates/overview.md#file-searching-logic)。

### `get_hash`

返回文件或字符串字面量的哈希摘要（SHA-256、SHA-384 或 SHA-512）。

它可以接受以下参数：
- `path`: 强制，有关详细信息，请参阅 [文件搜索逻辑](@/documentation/templates/overview.md#file-searching-logic)
- **或** `literal`: 强制，要哈希的字符串值
- `sha_type`: 可选，`256`、`384` 或 `512` 之一，默认为 `384`
- `base64`: 可选，`true` 或 `false`，默认为 `true`。是否将哈希编码为 base64

必须给出 `path` 或 `literal`。

```jinja
{{/* get_hash(literal="Hello World", sha_type=256) */}}
{{/* get_hash(path="static/js/app.js", sha_type=256) */}}
```

当其 `base64` 参数设置为 `true` 时，该函数还可以输出 base64 编码的哈希值。这可用于实现 [子资源完整性](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity)。

```jinja
<script src="{{/* get_url(path="static/js/app.js") */}}"
  integrity="sha384-{{ get_hash(path="static/js/app.js", sha_type=384, base64=true) | safe }}"></script>
```

请注意，子资源完整性通常用于使用外部脚本时，`get_hash` 不支持此功能。

### `get_image_metadata`

获取图像的元数据。支持 JPEG、PNG、WebP、BMP、GIF 以及 SVG 等常见格式。

它可以接受以下参数：

- `path`: 强制，有关详细信息，请参阅 [文件搜索逻辑](@/documentation/templates/overview.md#file-searching-logic)
- `allow_missing`: 可选，`true` 或 `false`，默认为 `false`。丢失文件是否应引发错误。

该方法返回一个包含 `width`、`height`、`format` 和 `mime` 的映射。返回的 `format` 是文件格式最常见的文件扩展名，可能与用于图像的扩展名不匹配。

```jinja
  {% set meta = get_image_metadata(path="...") %}
  我们的图像 (.{{meta.format}}) 格式是 {{ meta.width }}x{{ meta.height }}
```

### `load_data`

从文件、URL 或字符串字面量加载数据。支持的文件类型包括 *toml*、*json*、*csv*、*bibtex*、*yaml*/*yml* 和 *xml*，仅支持 UTF-8 编码。

任何其他文件类型都将作为纯文本加载。

`path` 参数指定本地数据文件的路径，依据 [文件搜索逻辑](@/documentation/templates/overview.md#file-searching-logic)。

```jinja
{% set data = load_data(path="content/blog/story/data.toml") %}
```

或者，`url` 参数指定要加载的远程 URL 的位置。

```jinja
{% set data = load_data(url="https://en.wikipedia.org/wiki/Commune_of_Paris") %}
```

或者，`literal` 参数指定对象字面量。注意：如果未指定 `format` 参数，则假定为纯文本。

```jinja
{% set data = load_data(literal='{"name": "bob"}', format="json") %}
{{ data["name"] }}
```

*注意：当与 `literal` 参数结合使用时，`required` 参数无效。*

可选的 `required` 布尔参数可以设置为 false，以便丢失数据（HTTP 错误或本地文件未找到）不会产生错误，而是返回 null 值。但是，即使使用 `required=false`，本地文件的权限问题和无法解析为请求数据格式的无效数据仍将产生错误。

下面的代码段输出维基百科页面的 HTML，如果页面无法访问或未返回成功的 HTTP 代码，则输出 "No data found"：

```jinja
{% set data = load_data(url="https://en.wikipedia.org/wiki/Commune_of_Paris", required=false) %}
{% if data %}{{ data | safe }}{% else %}No data found{% endif %}
```

可选的 `format` 参数允许你指定并覆盖包含在指定文件或 URL 中的数据类型。
有效条目是 `toml`、`json`、`csv`、`bibtex`、`yaml`、`xml` 或 `plain`。如果未指定 `format` 参数，则使用路径扩展名。如果是字面量，如果未指定 `format`，则假定为 `plain`。


```jinja
{% set data = load_data(path="content/blog/story/data.txt", format="json") %}
```

当你的文件具有支持的扩展名但你想将其作为纯文本加载时，请使用 `plain` 格式。

对于 *toml*、*json*、*yaml* 和 *xml*，数据被加载到与原始数据文件匹配的结构中；
但是，对于 *csv*，没有这种结构的原生概念。相反，数据被分离为包含 *headers* 和 *records* 的数据结构。查看下面的示例以了解它是如何工作的。

在模板中：
```jinja
{% set data = load_data(path="content/blog/story/data.csv") %}
```

在 *content/blog/story/data.csv* 文件中：
```csv
Number, Title
1,Gutenberg
2,Printing
```

解析数据的等效 json 值将存储在模板中的 `data` 变量中：
```json
{
    "headers": ["Number", "Title"],
    "records": [
        ["1", "Gutenberg"],
        ["2", "Printing"]
    ],
}
```

`bibtex` 格式将数据加载到与 [nom-bibtex crate](https://crates.io/crates/nom-bibtex) 使用的格式匹配的结构中。以下是 bibtex 格式的数据示例：

```
@preamble{"A bibtex preamble" # " this is."}

@Comment{
    Here is a comment.
}

Another comment!

@string(name = "Vincent Prouillet")
@string(github = "https://github.com/getzola/zola")

@misc {my_citation_key,
    author= name,
    title = "Zola",
    note = "github: " # github
}                                                    }
```

以下是生成的 bibtex 数据结构的 json 等效格式：
```json
{
    "preambles": ["A bibtex preamble this is."],
    "comments": ["Here is a comment.", "Another comment!"],
    "variables": {
        "name": "Vincent Prouillet",
        "github": "https://github.com/getzola/zola"
    },
    "bibliographies": [
        {
            "entry_type": "misc",
            "citation_key": "my_citation_key",
            "tags": {
                "author": "Vincent Prouillet",
                "title": "Zola",
                "note": "github: https://github.com/getzola/zola"
            }
        }
    ]
}
```

最后，可以从模板访问 bibtex 数据，如下所示：
```jinja
{% set tags = data.bibliographies[0].tags %}
This was generated using {{ tags.title }}, authored by {{ tags.author }}.
```

#### 远程内容

你可以从远程 URL 加载数据，而不是使用文件。这可以通过指定 `load_data` 的 `url` 参数而不是 `path` 来完成。

```jinja
{% set response = load_data(url="https://api.github.com/repos/getzola/zola") %}
{{ response }}
```

默认情况下，响应主体将不进行解析直接返回。可以通过使用如下所示的 `format` 参数来更改此设置。


```jinja
{% set response = load_data(url="https://api.github.com/repos/getzola/zola", format="json") %}
{{ response }}
```

当未指定其他参数时，URL 将始终使用 HTTP GET 请求检索。
使用参数 `method`，自版本 0.14.0 起，你也可以选择使用 POST 请求检索 URL。

当使用 `method="POST"` 时，你还可以使用参数 `body` 和 `content_type`。
参数 body 是 POST 请求中发送的实际内容。
参数 `content_type` 应该是 body 的 mime 类型。

此示例将向 kroki 服务发出 POST 请求以生成 SVG。

```jinja
{% set postdata = load_data(url="https://kroki.io/blockdiag/svg", format="plain", method="POST" ,content_type="text/plain", body="blockdiag {
  'Doing POST' -> 'using load_data'
  'using load_data' -> 'can generate' -> 'block diagrams';
  'using load_data' -> is -> 'very easy!';

  'Doing POST' [color = 'greenyellow'];
  'block diagrams' [color = 'pink'];
  'very easy!' [color = 'orange'];
}")%}
{{postdata|safe}}
```

如果你需要对 HTTP 标头进行额外处理，可以使用 `headers` 参数。
当资源需要身份验证或需要通过特殊标头传递其他参数时，你可能需要此参数。
请注意，标头将附加到 Zola 本身设置的默认标头，而不是替换它们。

此示例将向 GitHub markdown 渲染服务发出 POST 请求。

```jinja
{% set postdata = load_data(url="https://api.github.com/markdown", format="plain", method="POST", content_type="application/json", headers=["accept=application/vnd.github.v3+json"], body='{"text":"headers support added in #1710, commit before it: b3918f124d13ec1bedad4860c15a060dd3751368","context":"getzola/zola","mode":"gfm"}')%}
{{postdata|safe}}
```

以下示例展示了如何向 GitHub 发送 GraphQL 查询（需要身份验证）。
如果你想在自己的机器上尝试此示例，你需要提供 GitHub PAT（个人访问令牌），
你可以在此链接获取访问令牌：https://github.com/settings/tokens，然后将 `GITHUB_TOKEN` 环境变量设置为你获得的访问令牌。

```jinja
{% set token = get_env(name="GITHUB_TOKEN") %}
{% set postdata = load_data(url="https://api.github.com/graphql", format="json", method="POST" ,content_type="application/json", headers=["accept=application/vnd.github.v4.idl", "authorization=Bearer " ~ token], body='{"query":"query { viewer { login }}"}')%}
{{postdata|safe}}
```

如果你需要指定多个具有相同名称的标头，可以像这样指定它们：

```
headers=["accept=application/json,text/html"]
```

这相当于两个 `Accept` 标头，分别为 `application/json` 和 `text/html`。

如果不起作用，你可以多次指定标头以达到类似的效果：

```
headers=["accept=application/json", "accept=text/html"]
```

#### 数据缓存

数据文件加载和远程请求在构建期间缓存在内存中，因此不会对同一端点发出多个请求。
URL 基于 URL 缓存，数据文件基于文件修改时间缓存。
缓存时也会考虑格式，因此如果以两种不同格式加载，请求将被发送两次。

### `trans`

获取给定 `key` 的翻译，针对 `default_language`、给定的 `lang`uage 或活动语言：

```jinja
{{/* trans(key="title") */}}
{{/* trans(key="title", lang="fr") */}}
{{/* trans(key="title", lang=lang) */}}
```

### `resize_image`

调整图像文件的大小。
有关完整文档，请参阅 [_内容 / 图像处理_](@/documentation/content/image-processing/index.md)。
