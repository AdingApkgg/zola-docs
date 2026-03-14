+++
title = "搜索"
weight = 100
+++

Zola 可以从 section 和页面内容构建搜索索引，以供 JavaScript 库（如 [elasticlunr](http://elasticlunr.com/) 或 [fuse](https://www.fusejs.io)）使用。

要启用它，你只需要在 `config.toml` 中设置 `build_search_index = true`，Zola 就会为所有未从搜索索引中排除的页面生成 `default_language` 设置的索引。

如果你正在编写非英语站点，在 `config.toml` 中设置 `default_language` 非常重要；索引构建管道因语言而异。

由于每个站点都不同，Zola 不会对你的搜索功能做出任何假设，也不提供执行实际搜索和显示结果的 JavaScript/CSS 代码。你可以查看本网站是如何实现的（使用 elasticlunr）以获得灵感：[search.js](https://github.com/getzola/zola/tree/master/docs/static/search.js)。


## 配置搜索索引

在某些情况下，默认索引策略并不合适。你可以在 [搜索配置](@/documentation/getting-started/configuration.md) 中自定义要包含的字段以及是否截断内容。

## 索引格式

### Elasticlunr

兼容 [elasticlunr](http://elasticlunr.com/)。还会生成 `elasticlunr.min.js`。

```toml
# config.toml
[search]
index_format = "elasticlunr_javascript" # or "elasticlunr_json"
```

如果你使用的语言不是英语，你还需要包含相应的 JavaScript 词干提取器 (stemmer) 文件。
有关详细信息，请参阅 <https://github.com/weixsong/lunr-languages#in-a-web-browser>。

### Fuse

兼容 [fuse.js](https://www.fusejs.io/) 和 [tinysearch](https://github.com/tinysearch/tinysearch)。

```toml
# config.toml
[search]
index_format = "fuse_javascript" # or "fuse_json"
```
