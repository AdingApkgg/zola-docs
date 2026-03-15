
+++
title = "Papaya"
description = "一个用于博客和项目的干净 Zola 主题"
template = "theme.html"
date = 2023-07-27T22:20:55-07:00

[taxonomies]
theme-tags = []

[extra]
created = 2023-07-27T22:20:55-07:00
updated = 2023-07-27T22:20:55-07:00
repository = "https://github.com/justint/papaya.git"
homepage = "https://github.com/justint/papaya"
minimum_version = "0.16.1"
license = "MIT"
demo = "https://justintennant.me/papaya"

[extra.author]
name = "Justin Tennant"
homepage = "https://justintennant.me"
+++        

# Papaya

一个用于博客和项目的干净 [Zola](https://getzola.org) 主题，分叉自 [Anpu](https://github.com/zbrox/anpu-zola-theme)。

## 预览

**演示站点**: [https://justintennant.me/papaya/](https://justintennant.me/papaya/)

![index light/dark](https://raw.githubusercontent.com/justint/papaya/main/pics/blendedindex.png)

<p align="center">
  <img alt="Light Projects" src="https://raw.githubusercontent.com/justint/papaya/main/pics/projects.png" width="45%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img alt="Dark Projects" src="https://raw.githubusercontent.com/justint/papaya/main/pics/projects_dark.png" width="45%">
</p>

<p align="center">
  <img alt="Light Project" src="https://raw.githubusercontent.com/justint/papaya/main/pics/project.png" width="45%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img alt="Dark Project" src="https://raw.githubusercontent.com/justint/papaya/main/pics/project_dark.png" width="45%">
</p>

## 特性

- 博客文章
- 项目页面
- 自动亮色/暗色模式
- 分类和标签
- 可选的多语言支持
- 可自定义的部分和导航菜单链接
- 文章/项目的特色图片
- 智能图片嵌入短代码 (`{{/* img() */}}`)
- GitHub 仓库 star/fork 计数
- [Open Graph Protocol](https://ogp.me/) 标签
- [Utterances](https://utteranc.es/) 支持
- 社交/联系链接
- 100% Google Lighthouse 评分

## 安装

1. 克隆此仓库到你的 `themes` 文件夹：
    
    ```bash
    git clone https://github.com/justint/papaya.git themes/papaya
    ```

2. 将 `config.toml` 中的主题设置设置为 `papaya`：

    ```toml
    theme = "papaya"
    ```

3. 从 papaya 的 [`config.toml`](https://github.com/justint/papaya/blob/main/config.toml) 复制以下部分和键（及其内容/值）并粘贴到你站点的 `config.toml` 中：

   - `[languages]`
     - `[languages.en]`
     - `[languages.en.translations]`
   - `[extra.cdn]`
     - `font_awesome`

4. 在你的 `content` 目录中，添加新的 `blog` 和 `projects` 目录。将 Papaya 的 `content/blog` 中的 `_index.md` 文件复制到你的 `content/blog` 中，并将 Papaya 的 `content/projects` 中的 `_index.md` 和 `categories.json` 文件复制到你的 `content/projects` 中。
 
   你的 `content` 目录结构应该如下所示：
   ```
   content
   ├── blog
   │  └── _index.md
   └── projects
      └── _index.md
      └── categories.json
   ```
 
5. _(可选)_ 要启用 GitHub 仓库 star/fork 计数（默认禁用以避免触及 API 速率限制），请在执行 `zola serve`/`zola build` 之前将 `$ZOLA_ENV` 环境变量设置为 `prod`。
   
   对于 csh/tsch:
   ```shell
   setenv ZOLA_ENV prod
   ```
   
   对于 bash/ksh/zsh:
   ```shell
   export ZOLA_ENV=prod
   ```

## 自定义

以下是 Papaya 的可自定义功能：

- 项目分类
- 亮色/暗色模式
- 多语言支持
- 部分和导航菜单链接
- 文章/项目日期格式
- 文章/项目特色图片
- Open Graph Protocol 区域设置/个人资料信息
- Utterances
- 社交/联系链接

### 项目分类

在你的 `content/projects/categories.json` 中，你可以指定项目的分类。文件的格式如下：

```json
{
   "title": "keyword"
}
```

- `"title"`: 在项目页面上为每个分类分组显示的标题文本。
- `"keyword"`: 你将在项目页面中使用的分类法术语。

一个项目可以有多个分类，并且将在配置的每个分类中显示一次。

没有分类的项目将显示在项目页面的“其他”分类列表中。如果你不想显示“其他”分类，你可以将 `templates/projects.html` 复制到你自己的 `templates` 目录，并删除/注释掉“其他”分类的代码。

示例 `categories.json`:

```json
{
  "Software": "software",
  "Films": "film"
}
```

示例项目页面 Front Matter：

```toml
title = "Example software project"
date = 2021-08-11

[taxonomies]
categories = ["software"]
```

上面的示例项目页面将被分组并显示在项目页面的“Software”分类中。

### 亮色/暗色模式

Papaya 主题可以在 `config.toml` 中设置为 `"light"`, `"dark"`, 或 `"auto"` 模式。

在 `"auto"` 中，亮色和暗色模式由 `prefers-color-scheme` CSS 媒体特性隐式选择。主题将根据查看者的操作系统或用户代理设置自动切换。

### 多语言支持

目前 Zola 具有基本的国际化 (`i18n`) 支持，你可以阅读更多关于 [zola 的多语言站点文档](https://www.getzola.org/documentation/content/multilingual/) 的内容。

要编写多语言站点，请遵循以下步骤（本例中为英语和中文）：

1. 在你的 `config.toml` 中添加 `default_language` 配置以及 `[languages.zh]` 和 `[languages.en]` 部分：

    ```toml
    default_language = "en"

    [languages]

    [languages.en]

    [languages.zh]
    title = "中文标题"
    description = "中文描述"
    ```

    在 `[languages.zh]` 部分下，你可以覆盖默认配置，如 `title`, `description` 等。

2. 在 `[languages.zh.translations]` 和 `[languages.en.translations]` 部分添加所有关键字的翻译（有关所有关键字的列表，请参阅 Papaya 的 [`config.toml`](config.toml)）：

    ```toml
    [languages]

    [languages.en]

    [languages.en.translations]
    projects = "Projects"
    blog = "Blog"
    about = "About"
    recent_projects = "Recent Projects"
    more_projects = "More Projects"
    recent_blog_posts = "Recent Blog Posts"
    more_blog_posts = "More blog posts"
    ...

    [languages.zh]

    [languages.zh.translations]
    projects = "项目"
    blog = "博文"
    about = "关于"
    recent_projects = "近期项目"
    more_projects = "更多项目"
    recent_blog_posts = "近期博文"
    more_blog_posts = "更多博文"
    ...
    ```

3. 在每个版块中添加一个 `_index.zh.md` 文件。

   例如：添加 `content/blog/_index.zh.md` 和 `content/projects/_index.zh.md`。

4. 为每个你想翻译的页面提供一个 `{page-name}.zh.md`（或者如果页面有目录，则是 `index.zh.md`）。

   例如：添加 `content/blog/what-is-zola.zh.md` 和 `content/blog/blog-with-image/index.zh.md`。

6. 添加一个 `content/categories.zh.json` 文件。例如：

    ```json
    {
        "软件": "software",
        "电影": "film"
    }
    ```

现在你将拥有一个支持英语和中文的网站！由于 `config.toml` 中的 `default_language` 设置为 "en"，通过访问 `{base_url}` 你将看到此博客的英文版本。你可以通过访问 `{base_url}/zh` 来访问中文版本。

页面（文章或项目）可以用两种语言提供，也可以仅用一种语言提供，并且页面不必用默认语言提供。

### 部分和导航菜单链接

导航菜单由 `config.toml` 中的 `menu_items` 列表构建。例如：
```toml
[extra]

menu_items = [
   { name = "projects", url = "$LANG_BASE_URL/projects", show_recent = true, recent_items = 3, recent_trans_key = "recent_projects", more_trans_key = "more_projects" },
   { name = "blog", url = "$LANG_BASE_URL/blog", show_recent = true, recent_items = 3, recent_trans_key = "recent_blog_posts", more_trans_key = "more_blog_posts" },
   { name = "tags", url = "$LANG_BASE_URL/tags" },
   { name = "about", url = "$LANG_BASE_URL/about" },
]
```

`menu_item` 可以是以下两种之一：

- **指向版块的链接。** 版块链接可以选择配置为在首页上显示其最近创作的项目。参见 配置版块菜单项。

- **指向 URL 的链接。** 参见 配置 URL 菜单项

#### 配置版块菜单项

每当内容部分中的目录（或子目录）包含 `_index.md` 文件时，就会创建一个版块；请参阅 [Zola 关于版块的文档](https://www.getzola.org/documentation/content/section/)。

Papaya 默认有两个版块：`projects` 和 `blog`。你可以添加其他版块或更改版块名称。例如，你可以添加一个名为 _Diary_ 的版块。为了添加此版块，你需要：

1. 在 `content/` 中创建一个名为 `diary` 的目录。

2. 在 `content/diary/` 内创建一个 `_index.md`，例如：

    ```toml
    +++
    title = "Diary"
    render = true
    # diary 将使用 blog.html 作为其模板
    template = "blog.html"
    +++
    ```

版块可以添加到导航菜单中，并可选地配置为在首页上显示其最近创作的项目。要将版块添加到导航菜单：

1. 在你的 `config.toml` 的 `[extra]` 部分下，将你的版块添加到 `menu_items`：

    ```toml
    [extra]
    menu_items = [
        ...
        { name = "diary", url = "$LANG_BASE_URL/diary" }
    ]
    ```
   
2. 在你的 `config.toml` 的 `[languages.<code>.translations]` 部分下，添加你的版块名称翻译键：

   ```toml
   [languages]
   
   [languages.en]
   
   [languages.en.translations]
   diary = "Diary"
   
   [languages.zh]

   [languages.zh.translations]
   diary = "日记"
   ```

   这将在导航菜单中添加一个指向你的新 _Diary_ 版块的简单超链接。

要在首页上也显示 _Diary_ 版块的最近创作项目：

1. 向你的菜单项添加以下属性：

   - `show_recent`: 将版块的最近项目列表添加到你的首页。
   - `recent_items`: 要显示的最近项目数。
   - `recent_trans_key`: 最近项目列表标题文本的翻译键。
   - `more_trans_key`: 指向版块的超链接文本的翻译键。

   例如：

   ```toml
   [extra]
   menu_items = [
       ...
       { name = "diary", url = "$LANG_BASE_URL/diary", show_recent = true, recent_items = 3, recent_trans_key = "recent_diary", more_trans_key = "more_diary" }
   ]
   ```

2. 在你的 `config.toml` 的 `[languages.<code>.translations]` 部分下，添加你的版块名称、`recent_trans_key` 和 `more_trans_key` 翻译键：

    ```toml
    [languages]

    [languages.en]

    [languages.en.translations]
    diary = "Diary"
    recent_diary = "Recent Diaries"
    more_diary = "More Diaries"

    [languages.zh]

    [languages.zh.translations]
    diary = "日记"
    recent_diary = "近期日记"
    more_diary = "更多日记"
    ```
   
   这将在导航菜单中添加一个指向你的新 _Diary_ 版块的超链接，并在你的首页上列出 _Diary_ 版块的三个最新项目。

#### 配置 URL 菜单项

如果你想在导航菜单中添加一个简单的链接，请添加一个带有 `name` 和 `url` 的项目。例如：

```toml
[extra]
sections = [
    ...
    { name = "tag", url = "$LANG_BASE_URL/tags" }
]
```

必须在你的 `config.toml` 中为链接的 `name` 添加翻译键：

```toml
[languages]

[languages.en]

[languages.en.translations]
tag = "Tag"

[languages.zh]

[langauges.zh.translations]
tag = "标签"
```

如果你在链接的 URL 中包含 `$BASE_URL`，它将被替换为你站点的基本 URL，`$LANG_BASE_URL` 将被替换为你站点的特定语言基本 URL。

### 文章/项目日期格式

你可以在不同的语言中使用不同的日期格式。你需要为每种语言的翻译部分设置 `date_format` 值。

示例：

```toml
[languages]

[languages.en]

[languages.en.translations]
date_format = "%e %B %Y"

[languages.zh]

[languages.zh.translations]
date_format = "%Y 年 %m 月 %d 日"
```

格式化使用 Tera 中的标准 `date` 过滤器。你可以使用的日期格式选项列在 [chrono crate 文档](https://tera.netlify.app/docs/#date) 中。

### 文章/项目特色图片

文章和项目可以有特色图片，显示在页面顶部，位于页面内容之前。

```toml
[extra]
featured_image = "image.jpg"
featured_image_alt = "A lodge overlooks a forested mountain range."
```

![特色图片](pics/featured_image.png)

特色图片也可以扩展到视口的整个宽度：

```toml
[extra]
featured_image = "image.jpg"
featured_image_alt = "A lodge overlooks a forested mountain range."
featured_image_extended = true
```

![特色图片，扩展](pics/featured_image_extended.png)

### Open Graph Protocol 区域设置/个人资料信息

在你的 `config.toml` 中，你可以添加一个 `[extra.ogp]` 部分来指定你的 Open Graph Protocol 区域设置和个人资料信息。

Open Graph Protocol 让你控制你的网站内容在社交媒体网站上的显示方式。

有关 Open Graph Protocol 和有效属性值的更多信息，请访问官方 [网站](https://ogp.me/)。

示例：

```toml
[extra.ogp]
locale = "en_US"
first_name = "Papaya"
last_name = "Tiliqua"
gender = "female"
username = "tiliquasp"
```

### Utterances

[Utterances](https://utteranc.es/) 是一个基于 GitHub issues 构建的评论小部件。启用后，Papaya 可以在你的博客文章中显示 GitHub issues 作为评论。

要启用：

1. 按照 [utterances](https://utteranc.es/) 网站上的说明进行操作。

2. 一旦你到了“Enable Utterances”步骤，将以下键输入到你的 `config.toml` 中：

   ```toml
   [extra.utterances]
   enabled = true
   repo = "yourname/yourrepository" # 在这里放入你的仓库短路径
   post_map = "pathname"
   label = "utterances"
   theme = "preferred-color-scheme"
   ```

### 社交/联系链接

在你的 `config.toml` 中，你可以添加一个 `[extra.social]` 部分来指定你的社交网络/联系人帐户。更改这些将更新你网站页脚上显示的链接。

示例：

```toml
[extra.social]
email = "papaya@tiliqua.sp"
github = "papaya"
linkedin = "papayatiliqua"
twitter = "papayathehisser"
```

如果你想包含其他自定义社交网站，你可以将它们添加到 `other`：

示例：

```toml
[extra.social]
other = [
    { name = "BTC", font_awesome = "fa-brands fa-btc", url = "https://www.bitcoin.com/" }
]
```

`font_awesome` 属性指定 Font Awesome 类；你可以在 [Font Awesome](https://fontawesome.com/) 中找到它们。请注意，不同版本的 Font Awesome 可能包含不同的图标集；你可以通过更新 `[extra.cdn]` 部分中的 CDN 路径来更改 Font Awesome 的版本：

```toml
[extra]

[extra.cdn]
font_awesome = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta2/css/all.min.css"
```

## 图片嵌入短代码

Papaya 包含一个用于在文章中嵌入图片的短代码：

```
img(path, alt, caption, class, extended_width_pct, quality)
```

你可以使用 `./<image-path>` 指定相对于当前 markdown 文件的图片相对路径。

### 参数

- `path`: 图片的路径。它可以是：
  - 完整路径 (例如: `https://somesite.com/my-image.jpg`), 
  - 相对于 [目录结构](https://www.getzola.org/documentation/getting-started/directory-structure/) 中的 `content` 目录 (例如: `@/projects/project-1/my-image.jpg`), 或
  - 相对于当前 markdown 文件 (例如: `./my-image.jpg`).
- `alt`: _(可选)_ 图片的替代文本。
- `caption`: _(可选)_ 图片的标题。支持文本/HTML/Tera 模板。
- `class`: _(可选)_ 分配给图片的任何 CSS 类。多个类应用空格分隔 (`" "`).
- `quality`: _(可选)_ 图片的 JPEG 或 WebP 质量，百分比。仅在编码 JPEG 或 WebP 时使用；默认值为 `90`。
- `extended_width_pct`: _(可选)_ 图片宽度应超出其默认图形宽度的百分比，最高可达最大配置像素宽度。

   范围是 `0.0-1.0`，或 `-1` 表示文档宽度。

   最大像素宽度可以在你的 `config.toml` 中使用 `extra.images.max_width` 属性定义（默认为 2500px）。

   有关更多详细信息和示例，请参阅 扩展宽度图片 部分。

使用此短代码相对于常规 Markdown/HTML 图片嵌入的好处是：

- 使用 Zola 的 [图片处理功能](https://www.getzola.org/documentation/content/image-processing/) 自动调整图片大小以获得最佳性能
- 图片和标题为你✨预先设计样式✨
- 图片的宽度可以扩展到超过文档的宽度（参见：扩展宽度图片）
- 需要编写的 HTML/CSS 样板代码更少


### 扩展宽度图片

使用 `img` 短代码嵌入到页面的图片可以配置为扩展到超过文档宽度。这对于以更高分辨率显示宽/横向图片特别好。

默认情况下，使用 `img` 短代码嵌入的图片将作为带有默认边距的 `figure` 插入：

```js
{{/* img(path="image.jpg", 
       alt="A very cute leopard gecko.", 
       caption="A very cute leopard gecko. Default sizing.") */}}
```

![默认大小的图片](pics/img_default.png)

使用 `extended_width_pct` 参数，我们可以指定图片应扩展到其默认图形宽度之外的百分比，最高可达你配置的最大图片宽度（`config.extra.images.max_width`，默认为 2500px）。

这是一个 `extended_width_pct=0.1` 的示例：

```js
{{/* img(path="image.jpg", 
       alt="A very cute leopard gecko.", 
       caption="A very cute leopard gecko. extended_width_pct=0.1",
       extended_width_pct=0.1) */}}
```

![扩展 0.1 的图片](pics/img_0.1.png)

图片现在以大 10% 的宽度显示，同时保持其原始纵横比。

这是一个更宽的示例：

```js
{{/* img(path="image.jpg", 
       alt="A very cute leopard gecko.", 
       caption="A very cute leopard gecko. extended_width_pct=0.2",
       extended_width_pct=0.2) */}}
```

![扩展 0.2 的图片](pics/img_0.2.png)

图片的分辨率将调整为你配置的最大图片宽度，并在网页上显示为视口的最大宽度。

你还可以通过将 `extended_width_pct` 设置为 `-1` 来强制图片宽度匹配文档宽度：

```js
{{/* img(path="image.jpg", 
       alt="A very cute leopard gecko.", 
       caption="A very cute leopard gecko. extended_width_pct=-1",
       extended_width_pct=-1) */}}
```

![固定为文档宽度的图片](pics/img_-1.png)

## 为什么叫 "Papaya"?

🦎
