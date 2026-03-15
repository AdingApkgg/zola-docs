
+++
title = "Anpu"
description = "Hugo Anubis 主题的移植版"
template = "theme.html"
date = 2025-12-14T11:16:37Z

[taxonomies]
theme-tags = []

[extra]
created = 2025-12-14T11:16:37Z
updated = 2025-12-14T11:16:37Z
repository = "https://github.com/zbrox/anpu-zola-theme.git"
homepage = "https://github.com/zbrox/anpu-zola-theme"
minimum_version = "0.11.0"
license = "MIT"
demo = "https://anpu-zola-theme.vercel.app"

[extra.author]
name = "Rostislav Raykov"
homepage = "https://zbrox.com"
+++        

# Anpu theme for Zola

这是 Hugo 主题 [Anubis](https://github.com/Mitrichius/hugo-theme-anubis/tree/master/layouts) 的 [Zola](https://getzola.org) 移植版。

## 截图

| 亮色模式 | 暗色模式 |
| :------: | :-----------: |
| ![亮色模式网站截图](screenshot-light.png) | ![暗色模式网站截图](screenshot-dark.png) |

## 使用

为了使用该主题，你需要将此仓库克隆到你的 `themes` 文件夹中：

```bash
git clone https://github.com/zbrox/anpu-zola-theme.git themes/anpu
```

然后在 `config.toml` 中将主题设置设置为 `anpu`：

```toml
theme = "anpu"
```

此主题需要 `tags` 和 `categories` 分类法。

```toml
taxonomies = [
    { name = "categories" },
    { name = "tags" },
]
```

## 如何自定义

你可以自定义两件事：

- 要包含在菜单中的链接
- 文章的日期格式

### 菜单链接

在你的 `config.toml` 的 `[extra]` 部分下，你需要设置 `anpu_menu_links` 列表。

示例：

```toml
[extra]
anpu_menu_links = [
    { url = "$BASE_URL/about/", name = "About" },
]
```

如果你在链接的 url 中包含 `$BASE_URL`，它将被替换为你站点的 base url。

### 日期格式

在你的 `config.toml` 的 `[extra]` 部分下，你需要设置 `anpu_date_format` 值。

示例：

```toml
[extra]
anpu_date_format = "%e %B %Y"
```

格式化使用 Tera 中的标准 `date` 过滤器。你可以使用的日期格式选项列在 [chrono crate 文档](https://tera.netlify.app/docs/#date) 中。

## 归属

使用的图标是 [UXWing](https://uxwing.com/license/) 收藏的一部分。

## 许可证

源代码在 [MIT](LICENSE) 下可用。
