+++
title = "目录"
weight = 60
+++

每个页面/section 将根据 markdown 生成的标题自动为其自身生成目录。

它可以通过 `page.toc` or `section.toc` 变量在模板中使用。
你可以查看 [模板变量](@/documentation/templates/pages-sections.md#table-of-contents) 文档以获取有关其结构的信息。

下面是一个使用该字段渲染两级目录的示例：

```jinja
{% if page.toc %}
    <ul>
    {% for h1 in page.toc %}
        <li>
            <a href="{{ h1.permalink | safe }}">{{ h1.title }}</a>
            {% if h1.children %}
                <ul>
                    {% for h2 in h1.children %}
                        <li>
                            <a href="{{ h2.permalink | safe }}">{{ h2.title }}</a>
                        </li>
                    {% endfor %}
                </ul>
            {% endif %}
        </li>
    {% endfor %}
    </ul>
{% endif %}
```

虽然在此示例中标题排列整齐，但它同样适用于不连贯的标题。

请注意，标题中所有现有的 HTML 标签都**不**会出现在目录中，以避免各种问题。
