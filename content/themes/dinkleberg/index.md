
+++
title = "dinkleberg"
description = "Gutenberg 的 Rust BR 主题"
template = "theme.html"
date = 2019-10-18T00:30:44-03:00

[taxonomies]
theme-tags = []

[extra]
created = 2019-10-18T00:30:44-03:00
updated = 2019-10-18T00:30:44-03:00
repository = "https://github.com/rust-br/dinkleberg.git"
homepage = "https://github.com/rust-br/dinkleberg"
minimum_version = "0.4.0"
license = "MIT"
demo = "https://rust-br.github.io/blog/"

[extra.author]
name = "Guilherme Diego"
homepage = "https://github.com/guidiego"
+++        

![753986_1](https://user-images.githubusercontent.com/10289071/40806112-dd79ae78-64f6-11e8-8f24-63f387d5bb8f.jpg) 

Gutenberg 的 Rust BR 博客模板

## 特性
- 一种用于基本单词的 i18n，如："Next", "Previous", "Pages", "Categories"
- 额外配置中的博客标题和 Logo
- 通过配置自动侧边栏链接
- 基于 Medium 的简单设计
- 使用结构化数据和其他功能的 SEO

## 配置
```toml
[extra]
blog_logo="/imgs/common/logo.png" #将出现在顶部标题
blog_title="rust::br::Blog" #将出现在 logo 后的顶部标题

## i18n 单词
label_tags = "Tags"
label_tag = "Tag"
label_categories = "Categorias"
label_category = "Categoria"
label_relative_posts = "Postagens Relacionadas"
label_next = "Próxima"
label_previous = "Anterior"
label_page = "Página"
label_of = "de"
label_minutes = "minutos"

og_image="" # 将出现在社交媒体上的图片
og_alt_image="" # og_image 的替代文本
og_site_name="" # Open Graphic 的站点名称
keywords="" # SEO 关键词

educational_use="knowledge share" # 可选
copyright_year="2018" # 可选

fb_app_id="???" # 可选，Facebook App Id 以帮助指标
twitter_username="@???" # 可选，Twitter 用户以帮助指标

## 侧边栏自动链接
sidebar = [
    {name = "Social", urls=[
        {name="Telegram", url="https://t.me/rustlangbr"},
        {name="Github", url="https://github.com/rust-br"},
    ]},
    {name = "Divida Conhecimento!", urls=[
        {name="Contribuir!", url="https://rust-br.github.io/blog/hello-world"}
    ]}
]

```

此配置与我们在 [RustBR 博客](https://rust-br.github.io/blog) 上使用的配置相同

### Favicon 和其他东西
默认情况下，Dinkleberg 等待你在 static 的根目录下拥有所有图标，你可以使用网站 [https://www.favicon-generator.org/](https://www.favicon-generator.org/) 生成该包并将其放入你的 `/static` 中 :D
