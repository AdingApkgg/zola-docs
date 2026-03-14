+++
title = "自定义主题"
weight = 30
+++

当你的站点使用主题时，你可以在站点的 templates 文件夹中替换它的部分内容。对于任何给定的主题模板，你可以覆盖其中的单个块，或者替换整个模板。如果站点模板和主题模板冲突，站点模板将被优先考虑。无论主题模板是否冲突，主题模板仍然可以从 `theme_name/templates/` 中的任何模板访问。

## 替换模板

当你的站点使用主题时，生成的结构尽可能遵循主题的结构，即没有与主题具有相同名称和相对路径的用户定义模板；例如：有两个文件 `templates/page.html` 和 `themes/theme_name/templates/page.html`，站点模板是将要使用的那个。这种冲突导致主题的模板被忽略，而支持用户定义的模板。

## 覆盖块

如果你不想替换整个模板，而是覆盖其中的一部分，你可以 [扩展模板](https://keats.github.io/tera/docs/#inheritance) 并重新定义一些特定的块。例如，如果你想覆盖主题 page.html 中的 `title` 块，你可以在你的站点 templates 中创建一个 page.html 文件，内容如下：

```
{% extends "theme_name/templates/page.html" %}
{% block title %}{{ page.title }}{% endblock %}
```

如果你扩展 `page.html` 而不是具体的 `theme_name/templates/page.html`，它将扩展站点的 page 模板（如果存在），否则扩展主题的 page 模板。这使得从你的站点模板覆盖你的主题的基本模板成为可能，只要主题模板不在模板路径中硬编码主题名称。例如，主题中的子模板应该使用 `{% extends 'index.html' %}`，而不是 `{% extends 'theme_name/templates/index.html' %}`。
