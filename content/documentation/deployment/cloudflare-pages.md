+++
title = "Cloudflare Pages"
weight = 60
+++

Cloudflare 是一家云解决方案提供商，拥有庞大的专有内容分发网络 (CDN)。像 Netlify 或 Vercel 一样，Cloudflare Pages 使部署过程灵活而简单。你可以将 GitHub 仓库添加到该服务，并在每次 PR 后自动构建和托管基于 Zola 的网站。

## 逐步指南

1. 登录或创建一个新的 Cloudflare 帐户，并在右侧导航栏中选择 _"Pages"_
2. 按 _"Create a project"_ 按钮
3. 选择包含你的 Zola 网站的 GitHub 仓库并将其连接到 Cloudflare Pages
4. 点击 _"Begin setup"_
5. 输入你的项目名称。请记住，如果你想使用默认的 Pages 域名 (pages.dev)，这将是你网站未来的 URL ("yourprojectname.pages.dev")。此外，选择一个生产分支。
6. 在 _Build settings_ 中，选择 Zola 作为 _Framework preset_。_Build command_ 和 _Build output directory_ 将自动填充。
7. 切换下面的 _Environment variables_ 并添加 `ZOLA_VERSION` 作为 _变量名_。使用 `0.17.2` 或不同的 Zola 版本作为 _值_。
8. 最后，保存并部署。

你的网站现在已构建并部署到 Cloudflare 的网络！你可以在 Pages 仪表板中添加自定义域名或修改设置。

你可以在开发者门户中找到诸如 [Getting started with Cloudflare Pages](https://developers.cloudflare.com/pages/getting-started) 和 [Deploying Zola with Cloudflare Pages](https://developers.cloudflare.com/pages/how-to/deploy-a-zola-site#deploying-with-cloudflare-pages) 之类的文档和指南。

## 处理预览部署

在使用 Cloudflare Pages 时，你通常会使用预览部署在合并到主分支之前测试更改。默认情况下，这些预览部署使用不同的 URL（如 `https://your-branch-name.your-project.pages.dev`），如果你的 `base_url` 在 `config.toml` 中是硬编码的，这可能会导致资源加载问题。

要解决此问题，请修改 Cloudflare Pages 配置中的构建命令，以根据环境动态设置基本 URL：

```sh
if [ "$CF_PAGES_BRANCH" = "main" ]; then zola build; else zola build --base-url $CF_PAGES_URL; fi
```

此命令：

- 从主分支构建时使用你的 `config.toml` `base_url`
- 对所有其他分支使用预览部署 URL（由 Cloudflare Pages 自动提供为 `$CF_PAGES_URL`）

## 故障排除

一些帮助解决 Cloudflare Pages 入门问题的提示。

### `zola: not found`

如果你看到类似这样的构建输出：

```sh
23:03:54.609	> build
23:03:54.609	> zola build $BUILD_OPTS && npx tailwindcss -i ./public/input.css -o ./public/style.css -m
23:03:54.609
23:03:54.621	sh: 1: zola: not found
23:03:54.635	Failed: Error while executing user command. Exited with error code: 127
23:03:54.644	Failed: build command exited with code: 1
23:03:55.699	Failed: error occurred while running build command
```

那么这可能是由于一个 [未解决的问题](https://github.com/cloudflare/pages-build-image/issues/3#issuecomment-1646873666)。目前有两种推荐的解决方法：

#### 将 **build system version** 更改为 `v1`

在 workers & pages 仪表板中，转到以下位置：
<Your Project> Settings > Builds & deployments > Build system version > Configure build system

然后选择 `v1` 并保存。

#### 或者使用 `UNSTABLE_PRE_BUILD` 环境变量 + `asdf`

在 workers & pages 仪表板中，执行以下操作：
<Your Project> Settings > Environment variables > Edit variables

并添加一个环境变量 `UNSTABLE_PRE_BUILD`，值为以下内容并保存。

```sh
asdf plugin add zola https://github.com/salasrod/asdf-zola && asdf install zola latest && asdf global zola latest
```
