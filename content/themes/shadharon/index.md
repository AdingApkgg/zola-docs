
+++
title = "shadharon"
description = "由 Zola 驱动的简单博客主题"
template = "theme.html"
date = 2023-10-27T18:58:30+01:00

[taxonomies]
theme-tags = []

[extra]
created = 2023-10-27T18:58:30+01:00
updated = 2023-10-27T18:58:30+01:00
repository = "https://github.com/syedzayyan/shadharon.git"
homepage = "https://github.com/syedzayyan/shadharon"
minimum_version = "0.4.0"
license = "MIT"
demo = "https://syedzayyan.github.io/shadharon"

[extra.author]
name = "Syed Zayyan Masud"
homepage = "https://syedzayyan.com"
+++        

# Shadharon

由 [Zola](getzola.org) 驱动的简单博客主题。在此处查看 [在线预览](https://shadharon.syedzayyan.com/)。

> 名称源自孟加拉语单词 - সাধারণ，翻译为“通用的”

<details open>
  <summary>暗色主题</summary>

  ![blog-dark](https://raw.githubusercontent.com/syedzayyan/shadharon/main/screenshot.png)
</details>

<details close>
  <summary>亮色主题</summary>
  
  ![light-dark](https://raw.githubusercontent.com/syedzayyan/shadharon/main/screenshot-light.png)
</details>

## 特性

- [X] 主题（亮色、暗色）。默认主题为暗色，导航栏中有切换器
- [X] 项目页面
- [x] 社交链接
- [x] 标签

## 安装

0. 初始化 Git 仓库（如果尚未初始化）

1. 下载主题
```
git submodule add https://github.com/syedzayyan/shadharon themes/shadharon
```

2. 将 `theme = "shadharon"` 添加到你的 `config.toml`

3. 复制示例内容

```
cp -R themes/shadharon/content/. content
```

## 自定义

1. 有关自定义，请参阅 config.toml 文件，其中包含注释。

2. 要自定义主页上的横幅，需要修改 content/posts/_index.md。具体来说是 `extra` 下的 desc 变量。你也可以将其删除以移除横幅。对于关于页面或任何其他页面，"content" 目录中的 .md 文件即可。

你可以添加样式表来覆盖主题：

```toml
[extra]
stylesheets = [
    "override.css",
]
```

这些文件名相对于站点的根目录。在此示例中，两个 CSS 文件将位于 `static` 文件夹中。


## 参考

此主题灵感来自
- [apollo](https://github.com/not-matthias/apollo).  
- [Tania's Website](https://tania.dev/)
- [Anpu Zola Theme](https://github.com/zbrox/anpu-zola-theme)
