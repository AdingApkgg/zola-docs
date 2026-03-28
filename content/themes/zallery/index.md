
+++
title = "zallery"
description = "Zola 画廊主题"
template = "theme.html"
date = 2025-07-14T19:59:26-05:00

[taxonomies]
theme-tags = []

[extra]
created = 2025-07-14T19:59:26-05:00
updated = 2025-07-14T19:59:26-05:00
repository = "https://github.com/gamingrobot/zallery.git"
homepage = "https://github.com/gamingrobot/zallery"
minimum_version = "0.19.0"
license = "MIT"
demo = "https://gamingrobot.github.io/zallery-demo"

[extra.author]
name = "Morgan Creekmore"
homepage = "https://creekmore.dev"
+++        

# Zallery theme for Zola

适用于 [Zola](https://getzola.org) 的画廊与作品集主题。

Demo Site: [gamingrobot.github.io/zallery-demo](https://gamingrobot.github.io/zallery-demo/)  
Personal Portfolio: [gamingrobot.art](https://gamingrobot.art/)

## 截图

| Light mode | Dark mode |
| :------: | :-----------: |
| ![light mode](screenshot-light.jpg) | ![dark mode](screenshot-dark.jpg) |

## 功能

- 深色与浅色模式
- 自动生成移动端友好图片
- 自动生成缩略图
- 自动转换图片格式
- 图片放大按钮
- 作品“上一张/下一张”按钮
- 支持 [medium-zoom](https://github.com/francoischalifour/medium-zoom)
- 支持 [ModelViewer](https://modelviewer.dev/) 和 [Sketchfab](https://sketchfab.com/)
- 支持视频嵌入
- 支持 OpenGraph 与 Twitter 嵌入
- 响应式与移动端友好

## 安装

将主题克隆到 themes 目录：

```bash
git clone https://github.com/gamingrobot/zallery.git themes/zallery
```

注意：建议将 `themes/zallery` 下的 `config.toml` 复制到站点根目录。

然后在 `config.toml` 中将主题设置为 `zallery`：

```toml
theme = "zallery"
```

## 自定义

若要自定义主题颜色，需要将 `_variables.scss` 复制到站点 `sass` 目录，并创建 `zallery.scss`：

```scss
@import 'variables';
@import '../themes/zallery/sass/imports';
```

See the demo site for an example: [github.com/gamingrobot/zallery-demo/tree/master/sass](https://github.com/gamingrobot/zallery-demo/tree/master/sass)

## 配置项

### 菜单项

自定义头部导航链接。

```toml
[extra]
menu = [
    {url = "atom.xml", name = "Feed"},
    {url = "https://github.com/gamingrobot/zallery", name = "Github"},
]
```

### 浏览器地址栏主题色

用于设置移动端浏览器地址栏颜色。

```toml
[extra]
theme_color = "#313131"
```

### 作者链接

版权区域作者名对应链接。

```toml
[extra]
author_url = "https://example.com"
```

### 封面图

主画廊页面用于 OpenGraph 与 Twitter 嵌入的封面图。

```toml
[extra]
cover_image = "img/cover.webp"
```

### 版权与 Powered by

To hide the copyright set this to `true`

```toml
[extra]
hide_copyright = false
```

To hide the "Powered by Zola & Zallery" set this to `true`

```toml
[extra]
hide_poweredby = false
```

### 画廊

Settings for the gallery view's thumbnails

```toml
[extra]
thumbnail_size = 400 # size in pixels, you may need to adjust the media queries in _gallery.scss
thumbnail_format = "webp" # auto, jpg, png, webp
thumbnail_quality = 100 # value in percentage, only for webp and jpg
```

### `img` 短代码设置

Settings for the `img` shortcode, allowing for automatic conversion and creating mobile friendly images

```toml
[extra]
covert_images = false # set to true to convert images to to the format in the image_format setting
create_mobile_images = false # set to true to create mobile friendly versions of the image
image_format = "webp" # auto, jpg, png, webp
image_quality = 90 # value in percentage, only for webp and jpg
```

### Frontmatter 设置

These settings are for the frontmatter on each artwork

```toml
[extra]
thumbnail = "image.jpg" # image to resize into a thumbnail and cover image
modelviewer = true # enable modelviewer javascript for this artwork
```

### JavaScript 库

#### ModelViewer

设为 `true` 启用 [modelviewer](https://modelviewer.dev/) 支持。也可在作品 frontmatter 或 `config.toml` 中设置。

```toml
[extra]
modelviewer = true
```

#### JSZoom

设为 `true` 启用 [javascript zoom](https://github.com/francoischalifour/medium-zoom) 支持。

```toml
[extra]
jszoom = true
```

#### GoatCounter

填写 goatcounter 标签以启用 [goatcounter](https://www.goatcounter.com/) 支持。

```toml
[extra]
goatcounter = ""
```

## 短代码

### `img`

```jinja2
{{/* img(src="image.jpg", mobile_src="image-mobile.jpg", alt="alt text", text="text", fit="") */}}
```

- `src` (required) - Image path
- `mobile_src` (optional) - Mobile friendly version
- `alt` (optional) - Alt text
- `text` (optional) - Text to put under the image (if `alt` is not specified, text will be use for alt text)
- `fit` (optional) - Defaults to `fit-view`, can be set to `max-width` to make the image fill the width of the page

### `video`

```jinja2
{{/* video(src="image.jpg", autoplay=false) */}}
```

- `src` (required) - Video path
- `autoplay` (optional) - Set to `true` to enable autoplay
- `loop` (optional) - Set to `true` to enable looping

### `youtube` / `vimeo`

```jinja2
{{/* youtube(id="", autoplay=false) */}}
{{/* vimeo(id="", autoplay=false) */}}
```

- `id` (required) - Id of the video
- `autoplay` (optional) - Set to `true` to enable autoplay

### `model`

Note: Requires `modelviewer` to be enabled in `config.toml`

```jinja2
{{/* model(src="image.jpg", skybox="", poster="") */}}
```

- `src` (required) - Model path
- `skybox` (optional) -  Skybox HDR
- `poster` (optional) - Image to show when loading
- `alt` (optional) - Alt text

### `sketchfab`

```jinja2
{{/* sketchfab(id="") */}}
```

- `id` (required) - Id of the model

        
