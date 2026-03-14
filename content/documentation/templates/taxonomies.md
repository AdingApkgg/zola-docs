+++
title = "分类法 (Taxonomies)"
weight = 40
+++

Zola 将在 `templates` 目录中查找以下特定于分类法的文件：

- `$TAXONOMY_NAME/single.html`
- `$TAXONOMY_NAME/list.html`

如果未找到它们，它将尝试回退到以下通用模板文件：
- `taxonomy_single.html`
- `taxonomy_list.html`

仅当至少存在一个 `render` 设置为 `true` 的分类法时，才需要分类法模板。

首先，`TaxonomyTerm` 具有以下字段：

```ts
name: String;
slug: String;
path: String;
permalink: String;
pages: Array<Page>;
page_count: Number;
```

并且 `TaxonomyConfig` 具有以下字段：

```ts
name: String,
paginate_by: Number?;
paginate_path: String?;
feed: Bool;
render: Bool;
```


### 分类法列表 (`list.html`)

此模板从不分页，因此在所有情况下都会获得以下变量。

```ts
// 站点配置
config: Config;
// 来自配置的分类法数据
taxonomy: TaxonomyConfig;
// 该页面的当前完整永久链接
current_url: String;
// 该页面的当前路径
current_path: String;
// 该分类法的所有术语
terms: Array<TaxonomyTerm>;
// 当前页面的语言
lang: String;
```


### 单个术语 (`single.html`)
```ts
// 站点配置
config: Config;
// 来自配置的分类法数据
taxonomy: TaxonomyConfig;
// 该页面的当前完整永久链接
current_url: String;
// 该页面的当前路径
current_path: String;
// 正在渲染的当前术语
term: TaxonomyTerm;
// 当前页面的语言
lang: String;
```

分页的分类法术语还将获得一个 `paginator` 变量；有关更多详细信息，请参阅 [分页页面](@/documentation/templates/pagination.md)。
