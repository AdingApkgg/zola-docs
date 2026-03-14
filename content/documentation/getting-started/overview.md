+++
title = "概览"
weight = 5
+++

## Zola 一瞥

Zola 是一个静态站点生成器 (SSG)，类似于 [Hugo](https://gohugo.io/)、[Pelican](https://blog.getpelican.com/) 和 [Jekyll](https://jekyllrb.com/) (有关 SSG 的完整列表，请参阅 [Jamstack](https://jamstack.org/generators))。它使用 [Rust](https://www.rust-lang.org/) 编写，并使用 [Tera](https://keats.github.io/tera/) 模板引擎，该引擎类似于 [Jinja2](https://jinja.palletsprojects.com/en/2.10.x/)、[Django 模板](https://docs.djangoproject.com/en/2.2/topics/templates/)、[Liquid](https://shopify.github.io/liquid/) 和 [Twig](https://twig.symfony.com/)。

内容使用 [CommonMark](https://commonmark.org/) 编写，这是一种定义明确、高度兼容的 [Markdown](https://www.markdownguide.org/) 规范。Zola 使用 [pulldown-cmark](https://github.com/raphlinus/pulldown-cmark#pulldown-cmark) 解析 markdown 文件。该库的目标是 100% 符合 CommonMark 规范。它添加了一些额外功能，例如解析脚注、Github 风格的表格、Github 风格的任务列表和删除线。

SSG 使用动态模板将内容转换为静态 HTML 页面。因此，静态站点非常快，不需要数据库，这使得它们易于托管。关于静态站点和动态站点（如 WordPress、Drupal 和 Django）的比较，可以在[这里](https://dev.to/ashenmaster/static-vs-dynamic-sites-61f)找到。

要体验 Zola，请参阅下面的快速概览。

## Zola 第一步

与某些 SSG 不同，Zola 对站点的结构没有任何假设。在本概览中，我们将制作一个简单的博客站点。

### 初始化站点

> 本概览基于 Zola 0.19.1。

请参阅详细的[针对您平台的安装说明](@/documentation/getting-started/installation.md)。安装 Zola 后，让我们初始化我们的站点：

```
$ zola init myblog
```

你会遇到几个问题。

```
> What is the URL of your site? (https://example.com):
> Do you want to enable Sass compilation? [Y/n]:
> Do you want to enable syntax highlighting? [y/N]:
> Do you want to build a search index of the content? [y/N]:
```

对于我们的博客，让我们接受默认值（即，每个问题按 Enter 键）。我们现在有一个 `myblog` 目录，其结构如下：

```
├── config.toml
├── content
├── sass
├── static
├── templates
└── themes
```

作为参考，到本概览**结束**时，我们的 `myblog` 目录将具有以下结构：

```
├── config.toml
├── content/
│   └── blog/
│       ├── _index.md
│       ├── first.md
│       └── second.md
├── sass/
├── static/
├── templates/
│   ├── base.html
│   ├── blog-page.html
│   ├── blog.html
│   └── index.html
└── themes/
```

进入新创建的 `myblog` 目录。

### 模板

我们将首先创建一些模板来描述我们网站的结构。

#### 主页模板

让我们为主页制作一个模板。使用以下内容创建 `templates/base.html`。随着我们完成本概览，此步骤将更有意义。

```html
<!DOCTYPE html>
<html lang="zh-CN">

<head>
  <meta charset="utf-8">
  <title>MyBlog</title>
</head>

<body>
  <section class="section">
    <div class="container">
      {% block content %} {% endblock content %}
    </div>
  </section>
</body>

</html>
```  

现在，使用以下内容创建 `templates/index.html`。

```html
{% extends "base.html" %}

{% block content %}
<h1 class="title">
  This is my blog made with Zola.
</h1>
{% endblock content %}
```  

这告诉 Zola `index.html` 扩展了我们的 `base.html` 文件，并将名为 "content" 的块替换为 `{% block content %}` 和 `{% endblock content %}` 标签之间的文本。

#### 博客模板

要为列出所有博客文章的页面创建模板，请使用以下内容创建 `templates/blog.html`。

```html
{% extends "base.html" %}

{% block content %}
<h1 class="title">
  {{ section.title }}
</h1>
<ul>
  <!-- If you are using pagination, section.pages will be empty.
       You need to use the paginator object -->  
  {% for page in section.pages %}
  <li><a href="{{ page.permalink | safe }}">{{ page.title }}</a></li>
  {% endfor %}
</ul>
{% endblock content %}
```

正如 `index.html` 所做的那样，`blog.html` 扩展了 `base.html`，但在此模板中，我们希望列出博客文章。在这里，我们还可以看到诸如 `{{ section.[...] }}` 和 `{{ page.[...] }}` 之类的表达式，当 zola 将内容与此模板组合以渲染页面时，这些表达式将替换为我们的 [content](#content) 中的值。在标题下方的列表中，我们循环遍历 section 中的所有页面（`blog` 目录；当我们创建内容时将详细介绍），并分别使用 `{{ page.title }}` 和 `{{ page.permalink | safe }}` 输出每个页面标题和 URL。我们使用 `| safe` 过滤器，因为 permalink 不需要 HTML 转义（转义会导致 `/` 渲染为 `&#x2F;`）。

#### 博客文章模板

我们已经有了描述主页和列出所有博客文章页面的模板。现在让我们为单个博客文章创建一个模板。使用以下内容创建 `templates/blog-page.html`。

```html
{% extends "base.html" %}

{% block content %}
<h1 class="title">
  {{ page.title }}
</h1>
<p class="subtitle"><strong>{{ page.date }}</strong></p>
{{ page.content | safe }}
{% endblock content %}
```

> 注意 `{{ page.content }}` 的 `| safe` 过滤器。

### Zola 实时重载

现在我们已经概述了我们网站的结构，让我们在 `myblog` 目录下启动 Zola 开发服务器。

```
$ zola serve
Building site...
Checking all internal links with anchors.
> Successfully checked 0 internal link(s) with anchors.
-> Creating 0 pages (0 orphan) and 0 sections
Done in 13ms.

Web server is available at http://127.0.0.1:1111

Listening for changes in .../myblog/{config.toml,content,sass,static,templates}
Press Ctrl+C to stop
```

如果您将 Web 浏览器指向 <http://127.0.0.1:1111>，您将看到一条消息说："This is my blog made with Zola."

如果您转到 <http://127.0.0.1:1111/blog/>，您目前将获得 404，我们将在接下来修复它。

### 内容

我们现在将创建一些内容，Zola 将使用这些内容根据我们的模板生成站点页面。

#### Sections (栏目)

我们将从创建 `content/blog/_index.md` 开始。该文件告诉 Zola `blog` 是一个 [section](@/documentation/content/section.md)，这是 Zola 中对内容进行分类的方式。在 `_index.md` 文件中，我们将以 [TOML](https://github.com/toml-lang/toml) 格式设置以下变量：

```md
+++
title = "List of blog posts"
sort_by = "date"
template = "blog.html"
page_template = "blog-page.html"
+++
```

> 请注意，尽管没有变量是强制性的，但开头和结尾的 `+++` 是必需的。

* *sort_by = "date"* 告诉 Zola 使用日期对我们的 section 页面进行排序（有关页面的更多信息，请见下文）。
* *template = "blog.html"* 告诉 Zola 使用 `templates/blog.html` 作为列出此 section 中 Markdown 文件的模板。
* *page_template = "blog-page.html"* 告诉 Zola 使用 `templates/blog-page.html` 作为单个 Markdown 文件的模板。

有关 section 变量的完整列表，请参阅 [section](@/documentation/content/section.md) 文档。

这里的 `title` 变量的值可用于模板，例如 `blog.html` 中的 `{{ section.title }}`。

如果您现在转到 <http://127.0.0.1:1111/blog/>，您将看到一个空的帖子列表。

#### Markdown

我们现在将创建一些博客文章。使用以下内容创建 `content/blog/first.md`。

```md
+++
title = "My first post"
date = 2019-11-27
+++

This is my first blog post.
```

*title* 和 *date* 将分别在 `blog-page.html` 模板中作为 `{{ page.title }}` 和 `{{ page.date }}` 可用。结束 `+++` 下方的所有文本都将作为 `{{ page.content }}` 可用于模板。

如果您现在回到我们的博客列表页面 <http://127.0.0.1:1111/blog/>，您应该会看到我们孤独的帖子。让我们再加一个。使用以下内容创建 `content/blog/second.md`：

```md
+++
title = "My second post"
date = 2019-11-28
+++

This is my second blog post.
```

回到 <http://127.0.0.1:1111/blog/>，我们的第二篇文章显示在列表顶部，因为它比第一篇文章更新，并且我们在 `_index.md` 文件中设置了 *sort_by = "date"*。

作为最后一步，让我们修改 `templates/index.html`（我们的主页）以链接到我们的博客文章列表：

```html
{% extends "base.html" %}

{% block content %}
<h1 class="title">
  This is my blog made with Zola.
</h1>
<p><a href="{{/* get_url(path='@/blog/_index.md') */}}">Posts</a>.</p>
{% endblock content %}
```  

这就是 Zola 的快速概览。您现在可以深入研究其余的文档。
