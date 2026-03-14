+++
title = "概览"
weight = 10
+++

Zola 使用目录结构来确定站点结构。
`content` 目录中的每个子目录代表一个 [section](@/documentation/content/section.md)，其中包含 [pages](@/documentation/content/page.md)（你的 `.md` 文件）。

```bash
.
└── content
    ├── content
    │   └── something.md // -> https://mywebsite.com/content/something/
    ├── blog
    │   ├── cli-usage.md // -> https://mywebsite.com/blog/cli-usage/
    │   ├── configuration.md // -> https://mywebsite.com/blog/configuration/
    │   ├── directory-structure.md // -> https://mywebsite.com/blog/directory-structure/
    │   ├── _index.md // -> https://mywebsite.com/blog/
    │   └── installation.md // -> https://mywebsite.com/blog/installation/
    └── landing
        └── _index.md // -> https://mywebsite.com/landing/
```

每个页面路径（`base_url` 之后的部分，例如 `blog/cli-usage/`）可以通过更改 [页面 front-matter](@/documentation/content/page.md#front-matter) 的 `path` 或 `slug` 属性来得自定义。

你可能已经注意到上面示例中名为 `_index.md` 的文件。
此文件用于存储 section 本身的元数据和内容，不被视为页面。

为了确保理解本文档其余部分中使用的术语，让我们回顾一下上面的示例。

在这种情况下，`content` 目录有三个 `sections`：`content`、`blog` 和 `landing`。`content` section 只有一个页面（`something.md`），`landing` section 没有页面，`blog` section 有 4 个页面（`cli-usage.md`、`configuration.md`、`directory-structure.md` 和 `installation.md`）。

Section 可以无限嵌套。

## 资源共置 (Asset colocation)

`content` 目录不限于标记文件。很自然地，我们希望将页面和一些相关资源（如图像或电子表格）放在一起。Zola 对 section 和页面都开箱即用地支持这种模式。

你在页面/section 目录中添加的所有非 Markdown 文件将在构建站点时与生成的页面一起复制，这允许我们使用相对路径访问它们。

具有共置资源的页面不应直接放在其 section 目录中（例如 `latest-experiment.md`），而应作为专用目录中的 `index.md` 文件（`latest-experiment/index.md`），如下所示：


```bash
└── research
    ├── latest-experiment
    │   ├── index.md
    │   └── javascript.js
    ├── _index.md
    └── research.jpg
```

通过此设置，你可以直接在 Markdown 中从 'research' section 访问 `research.jpg`，从 'latest-experiment' 页面访问 `javascript.js`：

```Markdown
查看完整程序 [这里](javascript.js)。它**真的很酷的自由软件**！
```

默认情况下，此页面的 slug 将是目录名称，因此其永久链接将是 `https://example.com/research/latest-experiment/`。

### 从资源中排除文件

可以使用配置文件中的 [ignored_content](@/documentation/getting-started/configuration.md) 设置忽略选定的资源文件。
例如，假设你有几个要在网站上链接的代码文件。
为了可维护性，你想将代码保留在与 Markdown 文件相同的目录中，但不想将构建文件夹复制到公共网站。你可以通过在配置文件中设置 `ignored_content` 来实现此目的：

（注意：`{Cargo.lock,target}` 与 `{Cargo.lock, target}` _不同_）
```
ignored_content = ["code_articles/**/{Cargo.lock,target}, *.rs"]
```

## 静态资源

除了将内容文件放置在 `content` 目录中之外，你还可以将内容文件放置在 `static` 目录中。你在 `static` 目录中放置的任何文件/目录都将不加修改地复制到 `public` 目录。

通常，你可能会将全站资源（如 CSS 文件、站点 favicon、站点徽标或全站 JavaScript）放在 static 目录的根目录中。你还可以将任何你希望不加修改地包含（即不作为 Markdown 文件解析）的 HTML 或其他文件放入 static 目录中。

请注意，static 目录提供了共置的_替代方案_。例如，假设你有以下目录结构（上面介绍的结构的简化版本）：

```bash
.
└── content
    └── blog
        ├── configuration
        │    └── index.md // -> https://mywebsite.com/blog/configuration/
        └── _index.md // -> https://mywebsite.com/blog/
```

要向 `https://mywebsite.com/blog/configuration` 页面添加图像，你有三个选项：
 *  你可以将图像保存到 `content/blog/configuration` 目录，然后从 `index.md` 页面使用相对路径链接到它。这是上面 **共置** 下描述的方法。
 *  你可以将图像保存到 `static/blog/configuration` 目录，并以与共置完全相同的方式链接到它。如果你这样做，生成的文件将与共置图像获得的文件相同；唯一的区别是所有静态文件将保存在 static 目录中，而不是 content 目录中。选择取决于你的组织需求。
 *  或者你可以将图像保存到 static 目录中的任意目录。例如，你可以将所有图像保存到 `static/images`。使用这种方法，你不能再使用相对链接。相反，你必须使用绝对链接 `images/[filename]` 来访问你的图像。这对于小型站点或将图像与多个页面关联的站点（例如，出现在每个页面上的徽标图像）可能更可取。
