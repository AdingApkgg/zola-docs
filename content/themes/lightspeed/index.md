
+++
title = "lightspeed"
description = "一个在 Lighthouse 评分中获得满分的 Zola 主题"
template = "theme.html"
date = 2025-07-05T15:37:03+02:00

[taxonomies]
theme-tags = []

[extra]
created = 2025-07-05T15:37:03+02:00
updated = 2025-07-05T15:37:03+02:00
repository = "https://github.com/carpetscheme/lightspeed.git"
homepage = "https://github.com/carpetscheme/lightspeed"
minimum_version = "0.20.0"
license = "MIT"
demo = "https://carpetscheme.github.io/lightspeed"

[extra.author]
name = "carpetscheme"
homepage = "https://github.com/carpetscheme"
+++        

# Light Speed

一个小型 Zola 主题，移植自 [Light Speed Jekyll](https://github.com/bradleytaunt/lightspeed)。

* 在 Google Lighthouse 审计中获得满分
* 只有约 700 字节的 CSS
* 无 JavaScript

演示: [carpetscheme.github.io/lightspeed](https://carpetscheme.github.io/lightspeed)

-----

## 目录

- 安装
- 选项
  - 标题
  - 页脚菜单
  - Sass
- 原作
- 许可证

## 安装

下载此主题到你的 `themes` 目录：

```bash
$ cd themes
$ git clone https://github.com/carpetscheme/lightspeed.git
```

然后在你的 `config.toml` 中启用它：

```toml
theme = "lightspeed"
```

文章应直接放置在 `content` 文件夹中。

要按日期排序文章索引，请在索引部分 `content/_index.md` 中启用排序：

```toml
sort_by = "date"
```

## 选项

### 标题

在配置中设置标题和描述以出现在站点页眉中：

```toml
title = "Different strokes"
description = "for different folks"

```

### 页脚菜单

在 `extra` 中设置一个键为 `footer_links` 的字段：

```toml
[extra]

footer_links = [
    {url = "$BASE_URL/about", name = "About"},
    {url = "$BASE_URL/atom.xml", name = "RSS"},
    {url = "https://example.com", name = "Example"},
]
```

通过将页面放置在 content 目录的子文件夹中并在 Front Matter 中指定路径来创建页面，例如 `$BASE_URL/about`：

```toml
path = "about"
```

可以通过 `footer_credits` 选项禁用页脚对 Zola 和 Lightspeed 的致谢。

### Sass

样式从 sass 编译并内联导入到页眉中。

你可以通过在配置中启用 sass 编译来覆盖样式：

```toml
compile_sass = true
```

并将替换的 `style.scss` 文件放置在你的 sass 文件夹中。

## 原作

此模板基于 Bradley Taunt 的 Jekyll 模板 [Light Speed Jekyll](https://github.com/bradleytaunt/lightspeed)。

## 许可证

根据 [MIT 许可证](LICENSE.md) 开源。

本项目开源，但在 `content` 中找到的示例文章除外。
