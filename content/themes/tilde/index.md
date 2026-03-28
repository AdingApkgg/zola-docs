
+++
title = "tilde"
description = "匹配 Dracula Tilde CSS 风格的简洁主题"
template = "theme.html"
date = 2023-10-25T10:44:26-05:00

[taxonomies]
theme-tags = []

[extra]
created = 2023-10-25T10:44:26-05:00
updated = 2023-10-25T10:44:26-05:00
repository = "https://git.sr.ht/~savoy/tilde"
homepage = "https://git.sr.ht/~savoy/tilde"
minimum_version = "0.4.0"
license = "GPLv3"
demo = "https://savoy.srht.site/blog-demo"

[extra.author]
name = "savoy"
homepage = "https://tilde.team/~savoy/"
+++        

# tilde

适用于 [Zola](https://www.getzola.org/) 静态站点生成器的轻量极简博客主题。

在线演示地址：
[https://savoy.srht.site/blog-demo](https://savoy.srht.site/blog-demo)

![](screen_index.png)

![](screen_post.png)

## 安装

[主题文档](https://www.getzola.org/documentation/themes/installing-and-using-themes/)

将本仓库克隆到站点的 `themes` 目录，或将其作为子模块添加：

```bash
# Clone into themes
$ git clone https://git.sr.ht/~savoy/tilde themes/tilde
# Add as a submodule
$ git submodule add https://git.sr.ht/~savoy/tilde themes/tilde
```

## Configuration

该主题提供以下配置项：

```toml
[extra]

homepage = "" # author homepage
subtitle = "" # blog subtitle
git_source = "" # blog source code
author = "" # author name
email = "" # author email
license = "" # blog license
```

        
