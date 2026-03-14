+++
title = "分页"
weight = 30
+++

有两样东西可以分页：section 和分类法术语 (taxonomy term)。

除了 [概览页面](@/documentation/templates/overview.md) 中提到的常用变量外，这两种类型都获得一个 `Pager` 类型的 `paginator` 变量：

```ts
// 每个分页器的项目数
paginate_by: Number;
// 分页的基本 URL：section 永久链接 + 分页路径
// 你可以将其与一个整数连接以获取指向给定分页页面的链接。
base_url: String;
// 总共有多少个分页页面
number_pagers: Number;
// 第一个分页页面的永久链接
first: String;
// 最后一个分页页面的永久链接
last: String;
// 上一个分页页面的永久链接（如果有）
previous: String?;
// 下一个分页页面的永久链接（如果有）
next: String?;
// 当前分页页面的所有页面
pages: Array<Page>;
// 我们在哪个分页页面上，1 索引
current_index: Number;
// 所有分页页面的总页数
total_pages: Number;
```

**如果 `paginate_by` 未设置为正数，则不会定义该变量。**

一个 pager 是分页的一页；如果你有 100 个页面并且 paginate_by 设置为 10，你将有 10 个 pagers，每个包含 10 个页面。

## Section

分页的 section 获得与普通 [section 页面](@/documentation/templates/pages-sections.md#section-variables) 相同的 `section` 变量，减去它的页面。页面在 `paginator.pages` 中。

## 分类法术语 (Taxonomy term)

除了 `paginator` 变量外，分页的分类法还获得两个变量：

- 一个 `TaxonomyConfig` 类型的 `taxonomy` 变量
- 一个 `TaxonomyTerm` 类型的 `term` 变量。

有关类型的详细版本，请参阅 [分类法页面](@/documentation/templates/taxonomies.md)。

## SEO

最好不要在 sitemap 中包含分页页面，因为它们是非规范页面。
要在 sitemap 中排除分页页面，请在 `config.toml` 中将 `exclude_paginated_pages_in_sitemap` 设置为 `all`。

## 示例

这是一个来自主题的示例，说明如何在页面上使用分页（本例中为 `index.html`）：

```jinja
<div class="posts">
    {% for page in paginator.pages %}
        <article class="post">
            {{ post_macros::title(page=page) }}
            <div class="post__summary">
                {{ page.summary | safe }}
            </div>
            <div class="read-more">
                <a href="{{ page.permalink }}">Read more...</a>
            </div>
        </article>
    {% endfor %}
</div>
<nav class="pagination">
    {% if paginator.previous %}
        <a class="previous" href="{{ paginator.previous }}">‹ Previous</a>
    {% endif %}
    {% if paginator.next %}
        <a class="next" href="{{ paginator.next }}">Next ›</a>
    {% endif %}
</nav>
```
