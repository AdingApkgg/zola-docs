+++
title = "Sass"
weight = 110
+++

Sass 是一种流行的 CSS 预处理器，它添加了特殊功能（如变量、嵌套规则）以方便维护大型 CSS 规则集。如果你好奇 Sass 是什么以及为什么它对你的静态站点样式有用，以下链接可能会让你感兴趣：

* [Sass 官方网站](https://sass-lang.com/)
* [为什么选择 Sass?](https://alistapart.com/article/why-sass), 作者 Dan Cederholm

它目前使用 [grass](https://github.com/connorskees/grass)，这是一个大致等同于 dart-sass 的 Rust 实现。

## 在 Zola 中使用 Sass

Zola 总是编译主题目录中的 Sass 文件。
但是，为了让 Zola 处理 `sass` 文件夹中的文件，你需要在 `config.toml` 中设置 `compile_sass = true`。

Zola 处理 `sass` 文件夹中任何带有 `sass` 或 `scss` 扩展名的文件，并将处理后的输出放入具有相同文件夹结构和基本名称的 `css` 文件中，并存入 `public` 文件夹：

```bash
.
└── sass
    ├── style.scss // -> ./public/style.css
    ├── indented_style.sass // -> ./public/indented_style.css
    ├── _include.scss # 此文件不会被放入 `public` 文件夹，但其他文件可以 @import 它。
    ├── assets
    │   ├── fancy.scss // -> ./public/assets/fancy.css
    │   ├── same_name.scss // -> ./public/assets/same_name.css
    │   ├── same_name.sass # 冲突！这与上面的文件具有相同的基本名称，因此 Zola 将返回错误。
    │   └── _common_mixins.scss # 此文件不会被放入 `public` 文件夹，但其他文件可以 @import 它。
    └── secret-side-project
        └── style.scss // -> ./public/secret-side-project/style.css
```

名称中带有前导下划线的文件不会被放置在 `public` 文件夹中，但仍可用作 `@import` 依赖项。有关更多信息，请参阅 [Sass 基础](https://sass-lang.com/guide) 的 "Partials" section。

带有 `scss` 扩展名的文件使用 "Sassy CSS" 语法，而带有 `sass` 扩展名的文件使用 "缩进" 语法：<https://sass-lang.com/documentation/syntax>。
如果同一文件夹中存在具有相同基本名称的 `scss` 和 `sass` 文件，Zola 将返回错误以避免混淆——见上面的示例。
