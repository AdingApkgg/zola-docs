
+++
title = "Seagull"
description = "一个 Zola 主题"
template = "theme.html"
date = 2025-10-17T11:40:15+02:00

[taxonomies]
theme-tags = []

[extra]
created = 2025-10-17T11:40:15+02:00
updated = 2025-10-17T11:40:15+02:00
repository = "https://git.42l.fr/HugoTrentesaux/seagull.git"
homepage = "https://git.lacontrevoie.fr/HugoTrentesaux/seagull"
minimum_version = "0.17.0"
license = "AGPL"
demo = "https://seagull.coinduf.eu/"

[extra.author]
name = "Hugo Trentesaux"
homepage = "https://trentesaux.fr/"
+++        

# Seagull

一个 Zola 主题。

![gull](./static/img/gull_rect.svg)

## 安装

将主题作为 git 子模块添加：

```bash
git submodule add --name seagull https://git.lacontrevoie.fr/HugoTrentesaux/seagull.git themes/seagull
```

在你的 `config.toml` 中启用主题：

```
theme = "seagull"
```

在 `sass` 目录中添加 `_variables.sass` 文件：

```sh
mkdir sass
touch sass/_variables.sass
```

在 `content` 目录中添加 `_index.md` 文件。

## 功能

可在演示站查看功能： https://seagull.coinduf.eu/ 。

你可以通过 `/sass/_variables.sass` 文件自定义主题。

使用该主题构建的网站示例：

- https://scientifiquesenrebellion.fr/
- https://labasetoulouse.fr/
- https://trentesaux.fr/

## 支持

如果你在 [Zola forum](https://zola.discourse.group/) 中 @ 我（[@HugoTrentesaux](https://zola.discourse.group/u/hugotrentesaux/summary)），我会按需提供支持。

## 构建网站

由于为支持主题自定义使用了一种技巧，在构建 seagull 站点本身之前，你需要先创建一个空文件：

```sh
mkdir ../../sass
touch ../../sass/_variables.sass
```
        
