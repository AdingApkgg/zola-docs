
+++
title = "emily_zola_theme"
description = "一个适用于 Zola 的 KISS 主题"
template = "theme.html"
date = 2023-11-05T15:26:56+09:00

[taxonomies]
theme-tags = []

[extra]
created = 2023-11-05T15:26:56+09:00
updated = 2023-11-05T15:26:56+09:00
repository = "https://github.com/kyoheiu/emily_zola_theme.git"
homepage = "https://github.com/kyoheiu/emily_zola_theme"
minimum_version = "0.14.1"
license = "MIT"
demo = "https://emily-zola-theme.netlify.app/"

[extra.author]
name = "Kyohei Uto"
homepage = "https://github.com/kyoheiu"
+++        

# emily_zola_theme

![screenshot01](/static/images/ss01.png)


一个适用于 Zola（用 Rust 编写的静态站点生成器）的 KISS 主题。

特性：
- 简单且干净
- 移动端友好
- MathJax 支持

演示站点在 [这里](https://emily-zola-theme.netlify.app/)。

## 使用

```
cd YOUR_SITE_DIRECTORY/themes
git clone https://github.com/kyoheiu/emily_zola_theme.git
```

并在 `config.toml` 中将主题名称设置为 `emily_zola_theme`。

```
theme = "emily_zola_theme"
```

## 示例文章

在 `YOUR_SITE_DIRECTORY/themes/emily_zola_theme/content` 中。

## MathJax 支持

要使用 MathJax，请在 `.md` 文件的 Front Matter 中添加以下行。`[extra]` 是强制性的：

```
[extra]
math = true
```

## 如何自定义
除了默认值外，你还可以轻松自定义以下部分：

- 作者姓名（出现在页脚）
- 头部图标（出现在页眉）
- favicon
- 头部图标大小（默认宽度：70px）
- `index.html` 中的文章数（默认 5）

在 `themes/emily_zola_theme/theme.toml` 中设置你自己的，或者要覆盖，复制 `[extra]` 块，将其粘贴到你的 `config.toml` 中并进行编辑。
