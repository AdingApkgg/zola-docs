+++
title = "安装和使用主题"
weight = 20
+++


## 安装主题

安装主题的最简单方法是将其仓库克隆到 `themes` 目录中：

```bash
$ cd themes
$ git clone <theme repository URL>
```

使用 Git 或其他 VCS 克隆仓库将允许你轻松更新。或者，你可以手动下载文件并将它们放在文件夹中。

你可以在 [此处](@/themes/_index.md) 找到主题列表。

## 使用主题

既然你的 `themes` 目录中有了主题，你需要通过在 [配置文件](@/documentation/getting-started/configuration.md) 中设置 `theme` 变量来告诉 Zola 使用它。主题名称必须是你克隆主题的目录的名称。
例如，如果你在 `themes/simple-blog` 中克隆了一个主题，则配置文件中要使用的主题名称是 `simple-blog`。还要确保将变量放在 `.toml` 层级的顶层，而不是放在像 [extra] 或 [markdown] 这样的字典之后。
有些主题需要额外的配置才能正常工作。请务必按照你选择的主题文档中的说明正确配置主题。

## 自定义主题

可以通过在你的 `templates` 或 `static` 目录中创建具有相同路径和名称的文件来覆盖主题中的任何文件。这有几个例子，假设主题名称是 `simple-blog`：

```
templates/pages/post.html -> replace themes/simple-blog/templates/pages/post.html
templates/macros.html -> replace themes/simple-blog/templates/macros.html
static/js/site.js -> replace themes/simple-blog/static/js/site.js
```

如果主题定义了一些块，你也可以通过扩展它来选择仅覆盖页面的一部分。如果我们想在上面的示例中仅更改 `post.html` 页面中的单个块，我们可以这样做：

```
{% extends "simple-blog/templates/pages/post.html" %}

{% block some_block %}
Some custom data
{% endblock %}
```

大多数主题还将提供一些旨在被覆盖的变量。这发生在 [配置文件](@/documentation/getting-started/configuration.md) 的 `extra` section 中。
假设一个主题使用 `show_twitter` 变量并默认将其设置为 `false`。如果你想将其设置为 `true`，你可以像这样更新你的 `config.toml`：

```toml
[extra]
show_twitter = true
```

你可以直接在 `themes` 目录中修改文件，但这会使更新主题变得更加困难，并且实时重新加载不适用于这些文件。
