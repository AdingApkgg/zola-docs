+++
title = "分类法 (Taxonomies)"
weight = 90
+++

Zola 内置了对分类法（taxonomies）的支持，这是一种根据用户定义的类别对内容进行分组的方法。

## 定义

- 分类法 (Taxonomy): 可用于对内容进行分组的类别
- 术语 (Term): 分类法中的特定组
- 值 (Value): 可以与术语关联的一段内容

## 示例：电影网站

假设你想制作一个网站来显示有关各种电影的信息。在这种情况下，你可以使用以下分类法：

- 导演 (Director)
- 类型 (Genres)
- 奖项 (Awards)
- 发行年份 (Release year)

然后，在构建时，Zola 可以为每个分类法创建页面，列出所有已知的术语并将它们链接到所有相关的内容片段。

再次假设我们有以下电影：

```txt
- 水形物语 (Shape of water)              值
  - 导演 ............................ 分类法
    - 吉尔莫·德尔·托罗 (Guillermo Del Toro) 术语
  - 类型 ............................ 分类法
    - 惊悚 (Thriller)                     术语
    - 剧情 (Drama)                        术语
  - 奖项 ............................ 分类法
    - 金球奖 (Golden globe)               术语
    - 奥斯卡金像奖 (Academy award)         术语
    - 英国电影学院奖 (BAFTA)               术语
  - 发行年份 ........................ 分类法
    - 2017                                术语

- 房间 (The Room)                       值
  - 导演 ............................ 分类法
    - 托米·韦素 (Tommy Wiseau)            术语
  - 类型 ............................ 分类法
    - 爱情 (Romance)                      术语
    - 剧情 (Drama)                        术语
  - 发行年份 ........................ 分类法
    - 2003                                术语

- 光灵 (Bright)                         值
  - 导演 ............................ 分类法
    - 大卫·阿耶 (David Ayer)              术语
  - 类型 ............................ 分类法
    - 奇幻 (Fantasy)                      术语
    - 动作 (Action)                       术语
  - 奖项 ............................ 分类法
    - 加州外景奖 (California on Location Awards) 术语
  - 发行年份 ........................ 分类法
    - 2017                                术语
```

在此示例中，`发行年份` 页面将包含指向 2003 年和 2017 年页面的链接，而 2017 年页面将列出 *水形物语* 和 *光灵*。

## 配置

一个分类法有六个变量：

- `name`: 必需的字符串，将用于 URL，通常是复数版本（即 tags, categories 等）
- `paginate_by`: 如果设置为数字，每个术语页面将按此数量分页。
- `paginate_path`: 如果设置，此路径将用于分页页面，页码将附加在其后。
例如，默认值为 `page/1`。
- `feed`: 如果设置为 `true`，将为每个术语生成一个 feed（默认为 atom）。
- `lang`: 仅当你制作多语言站点并希望指示此分类法属于哪种语言时才设置此项
- `render`: 如果设置为 `false`，则不会为分类法或单个术语渲染页面。

插入到配置文件 (`config.toml`) 中：

⚠️ 将 taxonomies 键放在主部分，而不是 `[extra]` 部分

**示例 1:** (一种语言)

```toml
taxonomies = [
    { name = "director", feed = true},
    { name = "genres", feed = true},
    { name = "awards", feed = true},
    { name = "release-year", feed = true},
]
```

**示例 2:** (多语言站点)

```toml
# 这些分类法放在主部分
taxonomies = [
    {name = "director", feed = true},
    {name = "genres", feed = true},
    {name = "awards", feed = true},
    {name = "release-year", feed = true},
]

[languages.fr]
taxonomies = [
    {name = "director", feed = true},
    {name = "genres", feed = true},
    {name = "awards", feed = true},
    {name = "release-year", feed = true},
]
```

## 使用分类法

配置完成后，你可以在内容中设置分类法，Zola 会识别它们：

**示例:**

```toml
+++
title = "Shape of water"
date = 2019-08-15 # 文章日期，不是电影日期
[taxonomies]
director=["Guillermo Del Toro"]
genres=["Thriller","Drama"]
awards=["Golden Globe", "Academy award", "BAFTA"]
release-year = ["2017"]
+++
```

## 输出路径

与 section 和页面计算输出路径的方式类似：

- 分类法名称永远不会被 slugify
- 当配置中启用 `slugify.taxonomies`（默认值为 `"on"`）时，分类法术语（例如特定标签）会被 slugify

分类法页面随后可在以下路径获得：

```txt
$BASE_URL/$NAME/ (分类法)
$BASE_URL/$NAME/$SLUG (分类法条目)
```


请注意，分类法不区分大小写，因此具有相同 slug 的术语将被合并：包含标签 "example" 的 section 和页面将显示在与包含 "Example" 的页面相同的分类法页面中。

如果你设置了 `taxonomy_root` 配置选项，所有分类法路径都将以该根路径为前缀：

```txt
$BASE_URL/$TAXONOMY_ROOT/$NAME/ (分类法)
$BASE_URL/$TAXONOMY_ROOT/$NAME/$SLUG (分类法条目)
```

例如，如果 `taxonomy_root = "blog"` 并且有一个名为 `tags` 的分类法，其中包含术语 `rust`：
- 分类法列表页面: `$BASE_URL/blog/tags/`
- 分类法术语页面: `$BASE_URL/blog/tags/rust/`

