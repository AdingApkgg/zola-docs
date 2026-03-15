
+++
title = "zola-hacker"
description = "Hacker 是一个 Zola 主题"
template = "theme.html"
date = 2026-03-08T12:41:26-04:00

[taxonomies]
theme-tags = []

[extra]
created = 2026-03-08T12:41:26-04:00
updated = 2026-03-08T12:41:26-04:00
repository = "https://github.com/en9inerd/zola-hacker"
homepage = "https://github.com/en9inerd/zola-hacker"
minimum_version = "0.19.1"
license = "MIT"
demo = "https://zola-hacker.enginerd.io/"

[extra.author]
name = "Vladimir Loskutov"
homepage = "https://github.com/en9inerd"
+++        

# Zola Hacker 主题

Zola Hacker 是一个极简的 Zola 主题，灵感来自 Jekyll 的 [Hacker theme](https://pages-themes.github.io/hacker/)。它是为想要写博客的开发者设计的。

## 演示

[在线预览](https://zola-hacker.enginerd.io/).

## 要求

在使用此主题之前，你需要安装 [Zola](https://www.getzola.org/documentation/getting-started/installation/) ≥ 0.19.1。

## 快速开始

```bash
git clone git@github.com:en9inerd/zola-hacker.git
cd zola-hacker
zola serve
# 在浏览器中打开 http://127.0.0.1:1111/
```

## 安装

刚才我们展示了如何直接运行主题。现在我们开始逐步在现有站点中安装主题。

### 第一步：创建一个新的 Zola 站点

```bash
zola init mysite
```

### 第二步：安装 Zola Hacker 主题

下载此主题到你的 themes 目录：

```bash
cd mysite/themes
git clone git@github.com:en9inerd/zola-hacker.git
```

或者作为子模块安装：

```bash
cd mysite
git init  # 如果你的项目已经是 git 仓库，请忽略此命令
git submodule add git@github.com:en9inerd/zola-hacker.git themes/hacker
```

### 第三步：配置

在站点目录下的 `zola.toml` 中启用主题：

```toml
theme = "hacker"
```

或者将 `zola.toml` 从主题目录复制到你的项目根目录：

```bash
cp themes/hacker/zola.toml zola.toml
```

### 第四步：添加新内容

你可以将 content 从主题目录复制到你的项目中：

```bash
cp -r themes/hacker/content .
```

你可以根据需要修改或添加新文章到 `content/posts`、`content/pages` 或其他内容目录中。

### 第五步：运行项目

只需在项目根路径下运行 `zola serve`：

```bash
zola serve
```

此命令将启动 Zola 开发 Web 服务器，默认访问地址为 `http://127.0.0.1:1111`。保存的更改将在浏览器中实时重新加载。

## 自定义

你可以自定义配置、模板和内容。查看此仓库中的 `zola.toml`、`theme.toml`、`content` 文件和模板文件以获取灵感。

### 全局配置

你可以在 `zola.toml` 中自定义一些配置选项。

#### `extra` 选项之前的配置选项

在 `zola.toml` 中设置 tags 分类法：

```toml
taxonomies = [
    { name = "tags" },
]
```

#### `extra` 下的配置选项

以下选项应位于 `zola.toml` 的 `[extra]` 下

- `language_code` - 设置 HTML 文件语言（默认为 `en-US`）
- `title_separator` - 站点标题的分隔符，如 `|` 和 `-`（默认为 `|`）
- `logo` - logo 图片路径
- `google_analytics` - Google Analytics 跟踪 ID
- `timeformat` - 博客文章发布日期的时间格式
- `timezone` - 博客文章发布日期的时区
- `edit_page` - 是否显示文章的 github 仓库编辑页面
- `menu` - 设置站点的菜单项
- `contact_form_script_id` - 基于 [Google Script](https://github.com/en9inerd/learn-to-send-email-via-google-script-html-no-server) 的联系表单脚本 ID
- `[extra.github]` - 设置站点的 GitHub 元数据
- `[extra.giscus]` - 设置站点的 Giscus 设置以启用评论。请使用 [Giscus](https://giscus.app/) 网站上的自己的设置
- `[extra.opengraph]` - 设置站点的 Open Graph 元数据
- `[extra.pgp_key]` - 在某些页面的页脚设置 pgp 密钥
- `social_links` - 在页脚设置社交媒体链接
...

### 模板

所有页面都扩展自 `base.html`，你可以根据需要自定义它们。

### 短代码

该主题提供了一些短代码来帮助你编写内容：

`contact_form`
`contact_form` 短代码基于 [Google Apps Mail](https://github.com/en9inerd/learn-to-send-email-via-google-script-html-no-server) 无需服务器发送电子邮件。
它依赖于 `zola.toml` 中的 `contact_form_script_id`。

```markdown
{{/* contact_form() */}}
```

`cv`
`cv` 短代码用于在页面中显示简历。简历数据以 yaml 格式存储在 `data/cv` 目录中。

```markdown
{{/* cv() */}}
```

`github_avatar`
`github_avatar` 短代码用于显示 GitHub 头像图片。它依赖于 `zola.toml` 中的 `extra.github.username`。此外，你可以传递 size 作为参数。

```markdown
{{/* github_avatar(size=100) */}}
```

`projects`
`projects` 短代码用于显示 GitHub 仓库。它依赖于 `zola.toml` 中的 `extra.github.username` 和页面 front matter 中的 `extra.repo_names` 来过滤仓库。

```markdown
{{/* projects() */}}
```

## 报告问题

我们使用 GitHub Issues 作为 **Zola Hacker Theme** 的官方 bug 追踪器。请搜索 [现有 issues](https://github.com/en9inerd/zola-hacker/issues)。可能已经有人报告了同样的问题。

如果你的问题或想法尚未解决，[打开一个新 issue](https://github.com/en9inerd/zola-hacker/issues/new)。

## 许可证

**Zola Hacker Theme** 根据 [MIT 许可证](https://github.com/en9inerd/zola-hacker/blob/master/LICENSE) 分发。
