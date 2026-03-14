+++
title = "多语言站点"
weight = 130
+++

Zola 支持拥有多种语言的站点。

## 配置

首先，你需要将想要支持的语言添加到你的 `config.toml` 中。例如：

```toml
[languages.fr]
generate_feeds = true # 法语内容将会有 feed
build_search_index = true
taxonomies = [
    {name = "auteurs"},
    {name = "tags"},
]

[languages.fr.translations]
summary = "Mon blog"

[languages.it]
# 意大利语没有任何分类法/feed/搜索索引

[languages.it.translations]
summary = "Mio blog"

# 默认语言的翻译没有 languages.code 前缀
[translations]
summary = "My blog"
```

注意：默认情况下，不包含中文和日文搜索索引。你可以通过使用 `cargo build --features indexing-ja --features indexing-zh` 构建 `zola` 来包含支持。
还请注意，启用中文索引将使二进制文件大小增加大约 5 MB，而启用日文索引将使二进制文件大小增加大约 70 MB，因为字典非常大。

## 内容

一旦添加了语言，你就可以开始翻译你的内容了。Zola 使用文件名来检测语言：

- `content/an-article.md`: 这将是默认语言
- `content/an-article.fr.md`: 这将是法语

如果文件名中的语言代码不对应于配置的语言之一或默认语言，将显示错误。

如果你的默认语言在目录中有一个 `_index.md`，你需要添加一个带有相应 front-matter 选项的 `_index.{code}.md` 文件，因为没有语言回退。

## 输出

Zola 输出翻译后的内容，其基本 URL 为 `{base_url}/{code}/`。
唯一的例外是如果你直接在 front matter 中设置翻译页面的 `path`。
