+++
title = "归档 (Archive)"
weight = 90
+++

Zola 没有内置的方法来显示归档页面（按年份排序显示所有文章标题的页面）。但是，这可以直接在模板中完成：

```jinja
{% for year, posts in section.pages | group_by(attribute="year") %}
    <h2>{{ year }}</h2>

    <ul>
    {% for post in posts %}
        <li><a href="{{ post.permalink }}">{{ post.title }}</a></li>
    {% endfor %}
    </ul>
{% endfor %}
```

此代码段假设文章按日期排序，并且你想按降序显示归档。如果你想按升序显示文章，你需要进一步处理页面列表：
```jinja
{% set posts_by_year = section.pages | group_by(attribute="year") %}
{% set_global years = [] %}
{% for year, ignored in posts_by_year %}
    {% set_global years = years | concat(with=year) %}
{% endfor %}
{% for year in years | reverse %}
    {% set posts = posts_by_year[year] %}
    {# (same as the previous snippet) #}
{% endfor %}
```
