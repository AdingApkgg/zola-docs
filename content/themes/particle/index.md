
+++
title = "particle"
description = "Zola 的 Particle 主题"
template = "theme.html"
date = 2023-05-11T00:52:07+02:00

[taxonomies]
theme-tags = []

[extra]
created = 2023-05-11T00:52:07+02:00
updated = 2023-05-11T00:52:07+02:00
repository = "https://github.com/svavs/particle-zola.git"
homepage = "https://github.com/svavs/particle-zola"
minimum_version = "0.16.1"
license = "MIT"
demo = "https://particle-zola.vercel.app/"

[extra.author]
name = "Silvano Sallese"
homepage = "https://svavs.github.io/"
+++        

# Particle Jekyll 主题的 Zola 移植版

![](./screenshot.jpg)

这是一个简单而极简的 Zola 模板，专为想要展示其作品集的开发者设计。

主题特性：

- Gulp
- SASS
- Sweet Scroll
- Particle.js
- BrowserSync
- Font Awesome 和 Devicon 图标
- Google Analytics
- 信息自定义

## 基本设置

1. [安装 Zola](https://getzola.com)
2. 克隆 particle 主题：`git clone https://github.com/svavs/particle-zola.git`
3. 编辑 `config.toml` 以个性化你的站点。

## 站点和用户设置

你必须在 `config.toml` 的 `[extra]` 部分填写一些信息来自定义你的站点。

```
# 站点设置
description = "A blog about lorem ipsum dolor sit amet"

# 用户设置
username = "Lorem Ipsum"
user_description = "Anon Developer at Lorem Ipsum Dolor"
user_title = "Anon Developer"
email = "my@email.com"
twitter_username = "lorem_ipsum"
github_username = "lorem_ipsum"
gplus_username = "lorem_ipsum"
```

## 颜色和粒子自定义
- 颜色自定义
  - 编辑 sass 变量 (`_vars.scss`)
- 粒子自定义
  - 编辑 app.js 中的 particle 函数中的 json 数据
  - 参考 [Particle.js](https://github.com/VincentGarreau/particles.js/) 获取帮助

要自定义项目列表和关于部分，你需要编辑 `templates/content.html` 模板文件。
在未来的版本中将提供更简单的方法。

## 问题

有任何问题，请提交 [GitHub Issue](https://github.com/svavs/particle-zola/issues/new)。

## 许可证

此主题是免费和开源软件，根据 MIT 许可证分发。所以随意以任何你想要的方式使用此 Jekyll 主题。

## 致谢

此主题的部分设计灵感来自这些优秀的人
- [Nathan Randecker](https://github.com/nrandecker/particle)
- [Willian Justen](https://github.com/willianjusten/will-jekyll-template)
- [Vincent Garreau](https://github.com/VincentGarreau/particles.js/)
