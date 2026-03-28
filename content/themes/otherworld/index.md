
+++
title = "otherworld"
description = "蒸汽波美学风格主题"
template = "theme.html"
date = 2024-03-24T14:05:03+10:00

[taxonomies]
theme-tags = []

[extra]
created = 2024-03-24T14:05:03+10:00
updated = 2024-03-24T14:05:03+10:00
repository = "https://git.blek.codes/blek/otherworld.git"
homepage = "https://git.blek.codes/blek/otherworld"
minimum_version = "0.1.0"
license = "GPL-3-only"
demo = "https://world.blek.codes"

[extra.author]
name = "blek!"
homepage = "https://blek.codes"
+++        

<p align='center'>
    <img src='banner.webp'>
</p>

<h1 align='center'>
    otherworld - a zola theme
</h1>

你可以在[这里](https://world.blek.codes)查看演示。

## 使用方式

### 前置条件
1. 一套 Linux 系统。你也可以在 Windows 上使用，但本指南以 Linux 系统为核心。
2. 你需要安装这些程序：`git` 和 `zola`。
3. 一些创意，以及 HTML 和 SCSS 基础技能。

### 步骤
#### 1. 克隆仓库
（也就是下载主题）

假设你的网站目录名是 `daftpunk`。它会在下面命令中多次出现，你应替换为自己的网站名称。

```sh
$ git clone git@git.blek.codes:blek/otherworld.git daftpunk
$ cd daftpunk
```

#### 2. open an another terminal
在同一目录下运行：

```sh
$ zola serve
```

#### 3. 编辑 `content` 目录中的文件……

……按照 [zola 文档](https://www.getzola.org/documentation/getting-started/overview) 进行。

## 如何禁用加载效果
前往 `content/index.md`，在 `+++` 区块中将 `extra.noload` 设置为 `true`。

示例如下：
```toml
+++
title = "Welcome"

[extra]
noload = true
+++
```

        
