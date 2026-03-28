
+++
title = "Lekhz"
description = "专注文字的极简个人作品集主题，支持深色模式"
template = "theme.html"
date = 2026-02-09T23:49:29-05:00

[taxonomies]
theme-tags = ['minimal', 'clean', 'blog', 'responsive', 'personal', 'simple', 'minimalist', 'portfolio', 'text-focussed', 'dark', 'dark-mode', 'rss']

[extra]
created = 2026-02-09T23:49:29-05:00
updated = 2026-02-09T23:49:29-05:00
repository = "https://github.com/ba11b0y/lekhz.git"
homepage = "https://github.com/ba11b0y/lekhz"
minimum_version = "0.38"
license = "MIT"
demo = ""

[extra.author]
name = "Rahul Tiwari"
homepage = "https://ba11b0y.github.io/rahul/"
+++        

# lekhz

lekhz 是一个适用于 Zola 的简洁、极简且快速的个人网站模板。
从 Hugo 主题 [lekh](https://github.com/ba11b0y/lekh) 移植而来。

<img width="1461" alt="lekhz-dark" src="https://github.com/user-attachments/assets/c4ce7b2b-e55b-4bd9-bb58-c3bb6480700c" />



## 目录

- 功能
- 安装
- 自定义

## 功能
* 社交媒体链接
* 支持 Markdown
* 易于个性化
* RSS 订阅
* 深色模式（直接借鉴自 https://www.gwern.net/）
* GoatCounter 访问统计（分析）。了解更多请见[这里](https://goatcounter.com)

## 安装

如果你还没有站点，请先创建一个新的 Zola 站点。

```bash
zola init my-site
cd my-site
git init
```

将主题作为子模块添加：

```bash
git submodule add https://github.com/ba11b0y/lekhz.git themes/lekhz
```
**OR**

克隆主题

```bash
cd themes
git clone https://github.com/ba11b0y/lekhz.git
```

然后在 `config.toml` 中启用：

```toml
theme = "lekhz"
```

开始使用前，将 `content` 文件夹内容复制到你的新站点。

```bash
cp -r themes/lekhz/content/* content/
```

## 自定义选项

在 `config.toml` 的 `[extra]` 区块中添加以下配置：

```toml
[extra]
lekhz_name = "Rahul Tiwari"
lekhz_about = "About me description here"
lekhz_email = "jprrahultiwari@gmail.com"
lekhz_resume = "resume.pdf"
lekhz_post_limit = 3
lekhz_goatcounter_code = ""
# Example profiles configuration
lekhz_profiles = [
    { name = "GitHub", url = "https://github.com/ba11b0y" },
    { name = "Twitter", url = "https://x.com/ba11b0y" },
    { name = "LinkedIn", url = "https://www.linkedin.com/in/ba11b0y/" },
    { name = "Goodreads", url = "https://www.goodreads.com/user/show/91520565-rahul-tiwari"}
]
```

## 更多截图

<img width="1451" alt="light-lekhz" src="https://github.com/user-attachments/assets/d120cdd4-3aa2-4e2d-9889-83e97034d9ba" />

<img width="1461" alt="lekhz-posts" src="https://github.com/user-attachments/assets/688bdfa9-dfdb-4ee6-8b94-1e60e5f93261" />




        
