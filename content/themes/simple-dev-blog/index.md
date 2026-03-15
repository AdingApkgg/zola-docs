
+++
title = "simple-dev-blog"
description = "一个简单的开发者博客主题，无 javascript，预渲染链接页面和 SEO 标签。"
template = "theme.html"
date = 2023-11-07T09:25:21+10:00

[taxonomies]
theme-tags = []

[extra]
created = 2023-11-07T09:25:21+10:00
updated = 2023-11-07T09:25:21+10:00
repository = "https://github.com/bennetthardwick/simple-dev-blog-zola-starter.git"
homepage = "https://github.com/bennetthardwick/simple-dev-blog-zola-starter"
minimum_version = "0.4.0"
license = "MIT"
demo = "https://simple-dev-blog-zola-starter.netlify.app/"

[extra.author]
name = "Bennett Hardwick"
homepage = "https://bennett.dev"
+++        

![preview image](https://i.imgur.com/IWoJtkF.png)

# simple-dev-blog-zola-starter

一个适用于 Zola 的简单开发者博客主题。它不使用 JavaScript，预渲染导航、博客文章和标签之间的链接，并添加常用的 SEO 标签。

你可以在 [这里](https://simple-dev-blog-zola-starter.netlify.app/) 查看在线演示。

## 如何开始

要创建一个新的 Zola 站点，首先下载 CLI 并将其安装到你的系统上。此主题需要 Zola 0.14 或更高版本。

你可以在 [Zola 网站上](https://www.getzola.org/documentation/getting-started/installation/) 找到安装说明。

1. 安装 Zola CLI 后，运行以下命令创建一个新站点：

   ```sh
   zola init my_amazing_site
   cd my_amazing_site
   ```

2. 创建站点后，像这样安装 "Simple Dev Blog" 主题：

   ```sh
   git clone --depth=1 \
     https://github.com/bennetthardwick/simple-dev-blog-zola-starter \
     themes/simple-dev-blog
   ```

3. 现在在你的 `config.toml` 文件中，通过设置 `theme = "simple-dev-blog"` 选择主题。

4. 此主题使用 `tags` 分类法，在你的 `config.toml` 文件中设置 `taxonomies = [ { name = "tags" } ]`

5. 通过运行 `cp themes/simple-dev-blog/content/* ./content -r` 复制主题中的默认内容

6. 就是这样！现在通过运行以下命令构建你的站点，并导航到 `127.0.0.1:111`:

   ```sh
   zola serve
   ```

你应该现在有一个快速简单的开发者博客在运行了，玩得开心！

## 自定义

查看此仓库中的 `config.toml` 和 `theme.toml` 以获取思路，以下是所有选项的列表：

### 全局

以下选项应位于 `config.toml` 的 `[extra]` 下

- `accent_light` - 你的站点强调色的较浅阴影
- `accent` - 你的站点强调色
- `blog_path` - 你的博客路径（默认为 `blog`）
- `default_og_image` - 页面的默认 og:image 路径
- `footer_about` - 页脚的 markdown 内容
- `icon` - 内容文件夹中站点图标的路径
  - 例如，要添加文件 `icon.png`，你应该将其放在 `content/icon.png`
- `nav` - 见 `theme.toml`，你的站点的导航链接
- `not_found_message` - 404 页面的 markdown 内容
- `profile_large` - 内容文件夹中个人资料图片的大型垂直版本的路径
- `profile_small` - 内容文件夹中个人资料图片的小型版本的路径

### 页面

以下选项应位于每个页面的 `[extra]` 部分下

- `thumbnail` - 该页面的 og:image 路径
