
+++
title = "resume"
description = "简历主题"
template = "theme.html"
date = 2021-09-04T01:10:58+08:00

[taxonomies]
theme-tags = []

[extra]
created = 2021-09-04T01:10:58+08:00
updated = 2021-09-04T01:10:58+08:00
repository = "https://github.com/AlongWY/zola-resume.git"
homepage = "https://github.com/alongwy/zola-resume"
minimum_version = "0.11.0"
license = "MIT"
demo = "https://resume.alongwy.top"

[extra.author]
name = "Feng Yunlong"
homepage = "https://www.alongwy.top"
+++        

# Zola Resume

[Chinese Version](README.CN.md)

Redesigned form [hugo resume](https://github.com/eddiewebb/hugo-resume).
基于 [hugo resume](https://github.com/eddiewebb/hugo-resume) 重新设计。

## 功能
+ 基本形态为单页网站，支持左侧导航自动滚动定位。
+ 提供独立的项目/出版物页面以展示更多细节。
+ 内置客户端搜索页面（`/search`）。
+ 提供 `/admin` 端点，授权用户可通过可视化编辑器编辑并回写 Markdown，体验类似 Wordpress/CMS。

## 快速开始

```bash
git clone git@github.com:alongwy/zola-resume.git
cd zola-resume
zola serve
# open http://127.0.0.1:1111/
```

## 安装
上面展示了直接运行主题的方法。下面是在已有站点中分步安装主题。

### 第一步：创建新的 zola 站点

```bash
zola init mysite
```

### 第二步：安装 zola-resume
将主题下载到 `themes` 目录：

```bash
cd mysite/themes
git clone git@github.com:alongwy/zola-resume.git
```

或作为子模块安装：

```bash
cd mysite
git init  # if your project is a git repository already, ignore this command
git submodule add git@github.com:alongwy/zola-resume.git themes/zola-resume
```

### 第三步：配置
在站点目录的 `config.toml` 中启用主题：

```toml
theme = "zola-resume"
```

或将主题目录中的 `config.toml.example` 复制到项目根目录：

```bash
cp themes/zola-resume/config.toml.example config.toml
```

#### CMS 配置

```bash
cp themes/zola-resume/static/admin/config.yml static/admin/config.yml
```

并修改以下内容：

```yaml
# static/admin/config.yml

backend:
  name: github
  repo: USERNAME/REPO
  branch: BRANCH
  cms_label_prefix: netlify-cms/
  site_domain: DOMAIN.netlify.com
```

### 第四步：添加内容
你可以将主题目录中的内容复制到项目：

```
cp -r themes/zola-resume/data .
cp -r themes/zola-resume/content .
```

你可以按需在 `content/blog`、`content/projects` 或其他内容目录中修改或新增文章。

### 第五步：运行项目
在项目根目录运行 `zola serve`：

```
zola serve
```

这会启动 Zola 开发服务器，默认地址为 http://127.0.0.1:1111。保存改动后浏览器会自动热重载。

## 示例

![screenshot](https://raw.githubusercontent.com/alongwy/zola-resume/master/screenshot.png)

See [along's site](https://resume.alongwy.top) for a live example.

## 配置与使用

这个主题结合了自定义分区与数据文件来驱动内容展示。

### 摘要
编辑主页面 `contents/_index.md`，填写简短个人介绍/摘要。

### 数据文件
数据文件用于首页上的结构化内容展示。

- [data/certifications.json](https://github.com/AlongWY/zola-resume/blob/main/data/certifications.json)
- [data/social.json](https://github.com/AlongWY/zola-resume/blob/main/data/social.json)
- [data/skills.json](https://github.com/AlongWY/zola-resume/blob/main/data/skills.json)
- [data/experience.json](https://github.com/AlongWY/zola-resume/blob/main/data/experience.json)
- [data/education.json](https://github.com/AlongWY/zola-resume/blob/main/data/education.json)

### 项目/开源

通过不同分类来区分你是发起者还是协作者。

### 出版物
与项目类似，在 `publications` 下创建，包含论文、演讲、文章等。

### 博客 / 文章
与普通文章类似，在 `blog` 下创建，记录思考与随笔等内容。
**This template does not support a `posts` folder**

### 模板参数

除上述内容外，大部分个人信息通过 [`config.toml`](https://github.com/AlongWY/zola-resume/blob/main/config.toml) 的 `extra` 配置，或在使用 CMS 时于 “Settings” 集合中维护。

## 使用 Netlify CMS 编辑
**Does not require deployment to Netlify!**

[Netlify CMS](https://www.netlifycms.org/) 是一个开源项目，可为 Hugo 等静态站点工具提供 CMS 式编辑体验。本主题已在 [static/admin](https://github.com/AlongWY/zola-resume/tree/main/static/admin) 提供完整集成与使用指引。

## 致谢

本项目将 Feng Yunlong 的 Hugo Resume 主题移植到 Zola。


        
