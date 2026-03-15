
+++
title = "Docsascode_theme"
description = "一个与文档即代码方法相关的现代简单 Zola 主题"
template = "theme.html"
date = 2023-05-06T17:56:31+02:00

[taxonomies]
theme-tags = []

[extra]
created = 2023-05-06T17:56:31+02:00
updated = 2023-05-06T17:56:31+02:00
repository = "https://github.com/codeandmedia/zola_docsascode_theme.git"
homepage = "https://github.com/codeandmedia/zola_docsascode_theme"
minimum_version = "0.10.0"
license = "MIT"
demo = "https://docsascode.codeandmedia.com"

[extra.author]
name = "Roman Soldatenkov"
homepage = "https://codeandmedia.com"
+++        

**演示: [docsascode.codeandmedia.com](http://docsascode.codeandmedia.com)**

我的灵感来自于 [Linode 的方法](https://www.linode.com/2020/01/17/docs-as-code-at-linode/) 来创建和管理文档。他们称之为 _文档即代码方法。_ 因此，我的目标是制作一种简单高效的方法，通过 Markdown、Git 和可选的 Docker/k8s 处理任何类型的文档和文章。

该仓库包含一个 [Zola](https://www.getzola.org/)（我见过的最好的静态站点生成器）主题和一个用于构建 Nginx-alpine Docker 镜像的 dockerfile。你可以将一个 [带有演示内容的镜像](https://hub.docker.com/r/codeandmedia/docsascode-theme) 拉取到你的 Docker 中

```
codeandmedia/docsascode-theme:latest
```

如果你在 MacBook M1 处理器 \ Raspberry Pi4 64bit \ Amazon Graviton 或其他 ARM64 上使用 Docker - 只需 fork ARM64 分支或 push

```
codeandmedia/docsascode-theme-arm64:latest
```

## 优势

* 亮色 / 暗色切换器
* 默认 tags 和 authors 分类法
* 搜索
* 移动端和桌面端均有用的 UI

## 6 步构建你的知识库/文档仓库

1. Fork 仓库
2. 删除演示内容并添加你自己的（我在下面解释了如何构建它）
3. 在 config.toml 中更改网站名称和域名，并在根目录的 _index.md 中更改标题
4. 将你的仓库连接到 dockerhub
5. 构建你的 docker 镜像或设置 [自动构建](https://docs.docker.com/docker-hub/builds/)
6. 以你自己的方式托管构建好的 docker 镜像

但是，zola 是令人惊叹的静态站点生成器，所以你可以随意

1. 下载所有仓库文件
2. 再次删除演示内容并添加你自己的
3. 在 config.toml/index.md 中更改名称和域名
4. 设置 zola (win, linux, mac)
5. 执行 zola build
6. 将构建好的 html 输出托管在任何你想去的地方

Zola 支持 Netlify 和其他类似服务，或者你可以决定创建自己的 CI/CD 流程。

## 如何构建你的内容

你所有的文章都应该在 _content_ 文件夹内。任何图片、视频、其他静态文件都应该在 _static_ 内。

### 文件夹

每个文件夹都应该包含 _index.md，像这样

```toml
+++
title = "Docsascode title"
description = "Description is optional"
sort_by = "date" # sort by weight or date
insert_anchor_links = "right" # if you want § next to headers
+++
```
每个文件夹都是网站的一个版块，这意味着如果你创建文件夹 foo，它将被视为 _yoursitedomain.com/foo_

该主题支持文件夹中的文件夹以及一个文件夹中的文章 + 文件夹（参见 _content_ 中的示例）。所以你可以在文件夹内存储其他文件夹并在 index 中描述一些具体细节。

### 页面

一个页面应该开始于

```toml
+++
title = "File and folders in folder"
date = 2020-01-18 # or weight 
description = "Description"
insert_anchor_links = "right"

[taxonomies] #all taxonomies is optional
tags = ["newtag"]
authors = ["John Doe"]
+++
```

Zola 允许创建草稿：

```toml 
draft = true
```

此外，默认情况下你有两个分类法：_tags_ 和 _authors_。它是可选的，不一定需要在所有页面上使用。你可以添加你自己的分类法：

1. 复制 tags 或 authors 文件夹并将其重命名为你的分类法
2. 将你的分类法添加到 config.toml
3. 向 page.html 模板代码添加类似

```rust
    {%/* if page.taxonomies.yourtaxonomynameplural */%}
      <ul>
      {%/* for tag in page.taxonomies.yourtaxonomynameplural */%}
        <li><a href="{{/* get_taxonomy_url(kind="yourtaxonomynameplural", name=yourtaxonomyname) | safe */}}" >{{/* yourtaxonomyname */}}</a></li>
      {%/* endfor */%}
      </ul>
    {%/* endif */%}
```

完成。我告诉过你 Zola 很棒 :)

无论如何，你可以根据自己的意愿用 Zola 重写主题（[文档链接](https://www.getzola.org/documentation/getting-started/installation/)）
