
+++
title = "halve-z"
description = "复古双栏主题"
template = "theme.html"
date = 2026-02-19T18:51:13-05:00

[taxonomies]
theme-tags = []

[extra]
created = 2026-02-19T18:51:13-05:00
updated = 2026-02-19T18:51:13-05:00
repository = "https://github.com/charlesrocket/halve-z.git"
homepage = "https://github.com/charlesrocket/halvez"
minimum_version = "0.21.0"
license = "MIT"
demo = "https://halve-z.netlify.app/"

[extra.author]
name = "-k"
homepage = "https://failsafe.monster/"
+++        

# `halve-z`
[![Netlify Status](https://api.netlify.com/api/v1/badges/352a12ed-cdba-4545-9256-9fb698f5a94f/deploy-status?branch=trunk)](https://app.netlify.com/sites/halve-z/deploys)

一个用于 **Zola** 的双栏主题。

![logo](https://raw.githubusercontent.com/charlesrocket/halve-z/trunk/static/favicon-32x32.png)

## 特性

这是 [Halve](https://github.com/TaylanTatli/Halve) (**Jekyll**) 的 _复古_ 移植版。它具有：

* 搜索
* 分类法
* PWA（动态缓存/离线模式）
* 通知
* 自动配色方案
* 目录 (ToC)
* 分页
* 媒体短代码
* SEO
* CSP
* 项目卡片
* 评论 ([Mastodon](https://mastodon.social)/[Cactus](https://gitlab.com/cactus-comments/)/[Giscus](https://github.com/giscus/giscus))
* 阅读时间

## 安装

使用 `git` 添加主题子模块：

```sh
git submodule add https://github.com/charlesrocket/halve-z themes/halve-z
```

### 更新

使用以下命令将主题更新到最新版本：

```
git submodule update --recursive --remote
```

## 配置

1. 将主题的 [config.toml](https://github.com/charlesrocket/halve-z/blob/trunk/config.toml) 复制到你的项目根目录。根据需要设置变量，并在配置文件的 **顶部** 添加 `theme = "halve-z"`。
2. 复制内容以开始：

```
cp -R -f themes/halve-z/content/ content/
```

## 使用

查看演示 [文章](https://halve-z.netlify.app/posts/)。
