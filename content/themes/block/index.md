
+++
title = "Block"
description = "Blog/Black theme for Zola"
template = "theme.html"
date = 2026-01-28T12:43:48+05:30

[taxonomies]
theme-tags = []

[extra]
created = 2026-01-28T12:43:48+05:30
updated = 2026-01-28T12:43:48+05:30
repository = "https://github.com/ssiyad/block"
homepage = "https://github.com/ssiyad/block"
minimum_version = "0.21.0"
license = "GPLv3"
demo = "https://block-zola.netlify.app/"

[extra.author]
name = "Sabu Siyad"
homepage = "https://ssiyad.com"
+++        

# Block

纯黑、以博客为中心的 [Zola](https://www.getzola.org/) 主题，由 [TailwindCSS](https://tailwindcss.com/) 驱动。

演示: https://block-zola.netlify.app/

![截图](./screenshot.png)

## 设置

在你的 zola 站点目录中

- 获取主题

    ```bash
    git submodule add https://github.com/ssiyad/block themes/block
    ```

- 构建 CSS

    ```bash
    cd themes/block
    npm ci
    npm run css:build
    ```

- 构建你的站点

    ```bash
    cd ../..
    zola build
    ```

## 变量

你可以在 `config.toml` 中使用以下变量。

```toml
[extra.intro]
heading = "Blog/Black theme for Zola"
subheading = "Thoughts, stories and ideas."
avatar_url = "https://picsum.photos/200"

[extra.footer]
license_text = ""
```

查看 [theme.toml](./theme.toml) 了解更多信息。

## 块

你可以通过遵循 [这里](https://www.getzola.org/documentation/themes/extending-a-theme/#overriding-a-block) 的说明覆盖单个块。

示例：`templates/base_layout.html`

```html
{%/* extends "block/templates/base_layout.html" */%}

{%/* block license_text */%}
  <div>
    The content for this site is
    <a
      href="https://creativecommons.org/licenses/by-sa/2.0/"
      target="_blank"
      class="font-medium"
      >CC-BY-SA</a
    >. The
    <a
      href="https://github.com/ssiyad/ssiyad.github.io"
      target="_blank"
      class="font-medium"
      >code for this site</a
    >
    is
    <a
      href="https://www.gnu.org/licenses/gpl-3.0.en.html"
      target="_blank"
      class="font-medium"
      >GPLv3</a
    >.
  </div>
{%/* endblock */%}
```

## 自我推销

喜欢这个项目吗？给它一个星！⭐，并传播出去！🚀。如果你感觉特别慷慨，请在 [GitHub](https://github.com/ssiyad) 上关注 [Sabu Siyad](https://ssiyad.com)。谢谢！
