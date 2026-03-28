
+++
title = "terminus"
description = "适用于 Zola 的复古深色双色调主题"
template = "theme.html"
date = 2026-03-07T15:47:17+01:00

[taxonomies]
theme-tags = ['dark', 'blog', 'minimal', 'personal', 'responsive', 'seo']

[extra]
created = 2026-03-07T15:47:17+01:00
updated = 2026-03-07T15:47:17+01:00
repository = "https://github.com/ebkalderon/terminus.git"
homepage = "https://github.com/ebkalderon/terminus"
minimum_version = "0.22.0"
license = "MIT"
demo = "https://ebkalderon.github.io/terminus/"

[extra.author]
name = "Eyal Kalderon"
homepage = "https://eyalkalderon.com"
+++        

# Terminus

一个注重无障碍的 [Zola](https://github.com/getzola/zola) 主题，采用深色配色和复古终端风格，支持多语言、零必需 JavaScript、优雅连字字体，以及满分基线 Lighthouse 评分。

**Try the demo now:** https://ebkalderon.github.io/terminus/

![Screenshot of the Terminus demo website on a desktop browser](https://github.com/user-attachments/assets/ae7c378b-2987-4dbd-a84e-7d272e8856bc)

Terminus 大体移植自 Radek Kozieł 的 [Terminal Theme for
Hugo](https://github.com/panr/hugo-theme-terminal) but with several key
differences. Credit to the [zerm](https://github.com/ejmg/zerm) and
[tabi](https://github.com/welpo/tabi) themes for inspiring some of these
changes.
Hugo](https://github.com/panr/hugo-theme-terminal)，但做了若干关键改动。也感谢 [zerm](https://github.com/ejmg/zerm) 和 [tabi](https://github.com/welpo/tabi) 主题带来的灵感。

* 更好的无障碍体验（最低目标：WCAG 2.2 AA）
* 移动优先设计，响应式表现更佳
* 页脚社交媒体图标
* 支持 [GitHub-style alerts]
* 更友好的 SEO（更好的 OpenGraph 支持，后续计划加入 Schema.org）
* 不显示文章封面预览，界面更简洁

[GitHub-style alerts]: https://ebkalderon.github.io/terminus/blog/shortcodes/#alert-shortcode

## 功能

- [x] Perfect baseline Lighthouse score (Performance, Accessibility, Best Practices and SEO).
- [x] [Social media icons in footer](./theme.toml#L70-L73)
- [x] [Custom shortcodes](https://ebkalderon.github.io/terminus/blog/shortcodes/)
- [x] Copy button on code blocks
- [ ] [Comprehensive documentation] (still working on it!)
- [ ] Searchable archive page
- [ ] Projects portfolio page
- [ ] Site navigation submenus
- [x] Customizable [color schemes](./theme.toml#L22-L27)
- [x] [KaTeX](https://katex.org/) support for mathematical notation

[Comprehensive documentation]: https://ebkalderon.github.io/terminus/

## 快速开始

### 手动安装

1. Initialize a Git repository in your [Zola project directory], if you haven't
   already:
   ```bash
   git init
   ```
2. Add the theme as a Git submodule:
   ```
   git submodule add https://github.com/ebkalderon/terminus.git themes/terminus
   ```
3. Enable the theme in your `config.toml`:
   ```toml
   theme = "terminus"
   ```
4. Set a website `title` in your  `config.toml`:
   ```toml
   title = "Your Site Title"
   ```
5. Create a text file named `content/_index.md`. This file controls how your
   home page looks and behaves. Choose _exactly one_ of the following options:
   1. **Serve blog posts from `/`:**
      ```markdown
      +++
      title = "Home"
      paginate_by = 5  # Show 5 posts per page.
      +++
      ```
   2. **Serve posts from a different path, e.g. `blog/`:**
      ```markdown
      +++
      title = "Home"

      [extra]
      section_path = "blog/_index.md"  # Where to find your posts.
      max_posts = 5  # Show 5 posts and a link to blog section on home page.
      +++
      ```

[Zola project directory]: https://www.getzola.org/documentation/getting-started/cli-usage/#init

### 更新 Terminus

如以 Git 子模块方式安装，可运行以下命令更新 Terminus：

```bash
git submodule update --remote themes/terminus
```

## 许可证

本项目基于 [MIT license](./LICENSE) 发布。

        
