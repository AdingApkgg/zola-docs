
+++
title = "PaperMod"
description = "一个快速、干净、响应式的主题，移植到 Zola。"
template = "theme.html"
date = 2025-07-15T07:56:50Z

[taxonomies]
theme-tags = []

[extra]
created = 2025-07-15T07:56:50Z
updated = 2025-07-15T07:56:50Z
repository = "https://github.com/cydave/zola-theme-papermod.git"
homepage = "https://github.com/cydave/zola-theme-papermod"
minimum_version = "0.4.0"
license = "MIT"
demo = "https://cydave.github.io/zola-theme-papermod/"

[extra.author]
name = "cydave"
homepage = "https://github.com/cydave"
+++        

# Zola PaperMod

![](screenshot.png)


一个正在进行的 [hugo-PaperMod](https://github.com/adityatelange/hugo-PaperMod) 主题（由 [@adityatelange](https://github.com/adityatelange) 制作）到 [Zola](https://www.getzola.org/) 的移植版。

由于 Zola 0.19 引入的配置更改，目前仅支持 Zola 0.19.1 及更高版本。

演示 @ https://cydave.github.io/zola-theme-papermod/


## 特性

+ [x] 博客文章归档
+ [x] 博客文章 RSS 订阅
+ [x] 标签
+ [x] 基于标签的 RSS 订阅
+ [x] 可选：自定义分类法
+ [x] 亮色 / 暗色主题切换（具有可配置的默认偏好）
+ [x] 代码片段的语法高亮（Zola 内置语法高亮）
+ [x] 自定义导航
+ [ ] 3 种模式：
    + [ ] 常规模式
    + [ ] 首页信息模式
    + [ ] 个人资料模式
+ [x] 代码复制按钮
+ [x] 搜索页面
+ [ ] SEO 元数据
+ [ ] 语言切换器（多语言支持）


## 安装

1. 下载主题

```
git submodule add https://github.com/cydave/zola-theme-papermod themes/papermod
```

2. 将 `theme = "papermod"` 添加到你的 zola `config.toml`
3. 复制示例内容以开始

```
cp -r themes/papermod/content content
```


## 选项

Papermod 自定义项存在于指定的 `extra.papermod` 部分下。
请参阅 [config.toml](config.toml) 了解可用选项。


## 贡献

如果你想帮助将 hugo-PaperMod 移植到 Zola，请随意选择一个功能并开始工作。所有帮助，无论多小的贡献，都非常感激。
