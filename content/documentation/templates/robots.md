+++
title = "Robots.txt"
weight = 70
+++

Zola 将在 `templates` 目录中查找 `robots.txt` 文件，或者使用内置的文件。

Robots.txt 是所有模板中最简单的：它只获得 `config`，默认值是大多数站点想要的：

```jinja
User-agent: *
Disallow:
Allow: /
Sitemap: {{/* get_url(path="sitemap.xml") */}}
```

该文件可以像其他模板一样扩展和展开，例如使用 Tera 的 `include` 标签：

```jinja
User-agent: *
Disallow:
Allow: /
Sitemap: {{/* get_url(path="sitemap.xml") */}}

{% include "path/to/other/robots.txt" %}
```
