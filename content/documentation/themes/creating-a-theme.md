+++
title = "创建主题"
weight = 30
+++

创建主题就像使用 Zola 创建普通站点一样，只是你会想要使用许多 [Tera 块](https://keats.github.io/tera/docs#inheritance) 以允许用户轻松修改它。

## 入门

如前所述，主题就像任何站点一样；首先运行 `zola init MY_THEME_NAME`。

将该站点变成主题所需的唯一事情是添加一个 `theme.toml` 配置文件，其中包含以下字段：

```toml
name = "my theme name"
description = "A classic blog theme"
# 允许快速搜索的可选标签
tags = []
license = "MIT"
homepage = "https://github.com/getzola/hyde"
# 所需的 Zola 最低版本
min_version = "0.4.0"
# 可选的实时演示 URL
demo = ""

# 任何变量都可以在最终用户的 `config.toml` 中被覆盖
# 你不需要在变量前加上主题名称，但由于这将与用户数据合并，因此最好使用某种前缀或嵌套
# 使用 snake_casing 以与 Zola 的其余部分保持一致
[extra]

# 主题作者信息：你！
[author]
name = "Vincent Prouillet"
homepage = "https://vincent.is"

# 如果这是从另一个静态站点引擎移植的主题，请在此处提供原始作者的信息
[original]
author =  "mdo"
homepage = "https://markdotto.com/"
repo = "https://www.github.com/mdo/hyde"
```

你可以用作示例的一个简单主题是 [Hyde](https://github.com/Keats/hyde)。

## 开发主题

由于主题只是一个站点，你可以简单地使用 `zola serve` 并对你的主题进行更改，实时重新加载将按预期工作。

确保提交每个目录（包括 `content`），以便其他人能够从你的仓库构建主题。

## 提交主题到图库

如果你希望你的主题出现在本网站的 [主题](@/themes/_index.md) 部分，请确保主题满足以下三个要求：

- 有一个 `screenshot.png` 展示主题在运行中的样子，最大尺寸约为 2000x1000
- 有一个详细的 `README.md` 解释如何使用主题以及任何其他重要信息
- 质量相当高

当你的主题准备好后，你可以按照 README 中的流程将其提交到 [主题仓库](https://github.com/getzola/themes)。
