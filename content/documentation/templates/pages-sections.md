+++
title = "Sections 和 Pages"
weight = 20
+++

Pages 和 Sections 的模板非常相似。

## Page 变量

Zola 将尝试加载 `templates/page.html` 模板，如果使用了主题则加载主题的 `page.html` 模板，或者渲染内置模板（空白页面）。

无论你决定渲染哪个模板，你都会在模板中获得一个 `page` 变量，其中包含以下字段：

```ts
// Markdown 内容的 HTML 输出
content: String;
title: String?;
description: String?;
date: String?;
updated: String?;
slug: String;
path: String;
authors: Array<String>;
draft: Bool;
// 路径，按 '/' 分割
components: Array<String>;
permalink: String;
summary: String?;
taxonomies: HashMap<String, Array<String>>;
extra: HashMap<String, Any>;
toc: Array<Header>,
// 简单的字数统计，对于没有空格的语言无效
word_count: Number;
// 基于 https://help.medium.com/hc/en-us/articles/214991667-Read-time
reading_time: Number;
// 更早 / 更轻
lower: Page?;
// 更晚 / 更重
higher: Page?;
// 仅当页面有日期时才设置年/月/日，月/日是 1 索引的
year: Number?;
month: Number?;
day: Number?;
// 共置资产的路径，相对于 content 目录
assets: Array<String>;
// 父 section 直到 index section 的相对路径，用于 `get_section` Tera 函数
// 第一项是 index section，最后一项是父 section
// 这在渲染页面内容后填充，因此在 shortcodes 中将为空
ancestors: Array<String>;
// 从 `content` 目录到 markdown 文件的相对路径
relative_path: String;
// 从 `content` 目录到共置 index.md markdown 文件目录的相对路径
// 如果文件不是共置的，则为 Null。
colocated_path: String?;
// 页面的语言（如果有）。默认为配置 `default_language`
lang: String;
// 有关该内容的所有可用语言的信息，包括当前页面
translations: Array<TranslatedContent>;
// 链接此页面的所有 pages/sections：它们的永久链接和标题（如果有）
backlinks: Array<{permalink: String, title: String?}>;
```

## Section 变量

默认情况下，Zola 将尝试加载 `templates/index.html` 用于 `content/_index.md`，以及 `templates/section.html` 用于其他 `_index.md` 文件。如果没有，它将渲染内置模板（空白页面）。

无论你决定渲染哪个模板，你都会在模板中获得一个 `section` 变量，其中包含以下字段：

```ts
// Markdown 内容的 HTML 输出
content: String;
title: String?;
description: String?;
path: String;
// 路径，按 '/' 分割
components: Array<String>;
permalink: String;
extra: HashMap<String, Any>;
// 直接在此 section 中的页面。默认情况下，页面不排序。请在相应 section 的 _index.md 文件中将 "sort_by"
// 变量设置为 "date" 或 "weight" 以分别按日期和权重排序。
pages: Array<Page>;
// 此 section 的直接子 section，按子 section 权重排序
// 这仅包含要在 `get_section` 内置函数中使用的路径，以便在你需要时获取实际的 section 对象
subsections: Array<String>;
toc: Array<Header>,
// Unicode 字数统计
word_count: Number;
// 基于 https://help.medium.com/hc/en-us/articles/214991667-Read-time
reading_time: Number;
// 共置资产的路径，相对于 content 目录
assets: Array<String>;
// 父 section 直到 index section 的相对路径，用于 `get_section` Tera 函数
// 第一项是 index section，最后一项是父 section
// 这在渲染页面内容后填充，因此在 shortcodes 中将为空
ancestors: Array<String>;
// 从 `content` 目录到 markdown 文件的相对路径
relative_path: String;
// section 的语言（如果有）。默认为配置 `default_language`
lang: String;
// 有关该内容的所有可用语言的信息
translations: Array<TranslatedContent>;
// 链接此页面的所有 pages/sections：它们的永久链接和标题（如果有）
backlinks: Array<{permalink: String, title: String?}>;
// 此 section 是否生成 feed。如果设置，取自 front-matter
generate_feeds: bool;
// 此 section 是否透明。如果设置，取自 front-matter
transparent: bool;
// 每个分页器的项目数（如果定义）
paginate_by: Number?;
// 如果分页中的项目顺序颠倒（默认为 false）
paginate_reversed: bool;
```

当使用 `get_section` Tera 函数时，有关分页的信息很有用，因为该函数不可用 `paginator`。

有关 `paginator` 变量的更多信息，请参阅 [分页模板文档](@/documentation/templates/pagination.md)。

## 目录

Page 和 section 模板都有一个 `toc` 变量，对应于 `Header` 数组。
`Header` 具有以下字段：

```ts
// hX 级别
level: 1 | 2 | 3 | 4 | 5 | 6;
// 生成的 slug id
id: String;
// 标题文本
title: String;
// 直接指向标题的链接，使用插入的锚点
permalink: String;
// 此标题下的所有较低级别标题
children: Array<Header>;
```

## 翻译内容

Pages 和 sections 都有一个 `translations` 字段，对应于 `TranslatedContent` 数组。如果你的站点没有使用多种语言，这将始终是一个空数组。
`TranslatedContent` 具有以下字段：

```ts
// 该内容的语言代码，如果是默认语言则为空
lang: String?;
// 该内容的标题（如果有）
title: String?;
// 该内容的永久链接
permalink: String;
// markdown 文件的路径；用于通过 `get_page` 函数检索完整页面。
path: String;
```
