+++
title = "Sitemap"
weight = 60
+++

Zola 将在 `templates` 目录中查找 `sitemap.xml` 文件，或者使用内置的文件。

如果你的站点超过 30,000 个页面，它将自动将链接拆分为多个 sitemap，正如 [Google](https://support.google.com/webmasters/answer/183668?hl=zh-Hans) 推荐的那样：

> 所有格式都将单个 sitemap 限制为 50MB（未压缩）和 50,000 个 URL。
> 如果你的文件较大或 URL 较多，则必须将列表拆分为多个 sitemap。
> 你可以选择创建一个 sitemap 索引文件（指向 sitemap 列表的文件）并将该单个索引文件提交给 Google。

在这种情况下，Zola 将使用名为 `split_sitemap_index.xml` 的模板来渲染索引 sitemap。

`sitemap.xml` 模板获得一个变量：

- `entries`: 站点的所有页面，作为 `SitemapEntry` 列表

`SitemapEntry` 具有以下字段：

```ts
permalink: String;
updated: String?;
extra: Hashmap<String, Any>?;
```

`split_sitemap_index.xml` 也获得一个变量：

- `sitemaps`: 指向 sitemaps 的永久链接列表
