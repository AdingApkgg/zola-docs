+++
title = "Cloudflare Workers"
weight = 60
+++

Cloudflare 是一家云解决方案提供商，拥有庞大的专有内容分发网络 (CDN)。像 Netlify 或 Vercel 一样，Cloudflare Workers 使部署过程灵活而简单。你可以将 GitHub 仓库添加到该服务，并在每次 PR 后自动构建和托管基于 Zola 的网站。

## 准备你的仓库

在创建 Cloudflare Worker 之前，你必须为 [Wrangler](https://developers.cloudflare.com/workers/wrangler/) 添加配置，以便在调用默认命令 `npx wrangler deploy` 时构建你的站点。

### 创建构建脚本

首先，你需要一个构建脚本，用于从 GitHub Releases 获取并提取 Zola。如果你的站点仓库有子模块，例如主题，执行子模块更新也是必要的，因为 Cloudflare 不会递归克隆仓库。让我们将脚本命名为 `build.sh` 并将其添加到仓库的根目录。

```bash
#!/usr/bin/env bash
main() {
    ZOLA_VERSION=0.22.1

    curl -sLJO "https://github.com/getzola/zola/releases/download/v${ZOLA_VERSION}/zola-v${ZOLA_VERSION}-x86_64-unknown-linux-gnu.tar.gz"
    tar -xf zola-v${ZOLA_VERSION}-x86_64-unknown-linux-gnu.tar.gz

    git submodule update --init --recursive

    ./zola build
}

set -euo pipefail
```

### 添加 wrangler 配置

其次，使用 `wrangler.toml`（也在项目的根目录）将 Wrangler 指向构建脚本和生成站点的目标目录。`name` 和 `compatibility_date` 是 Wrangler 必需的。[^1] 只需使用你的站点名称和当前日期。

```toml
name = "blog"
compatibility_date = "2026-01-22"

[build]
command = "./build.sh"

[assets]
directory = "./public"
```

## 创建 Worker

1. 登录或创建一个新的 Cloudflare 帐户，并在导航栏中选择 _"Workers and Pages"_
2. 按 _"Create a project"_ 按钮
3. 选择包含你的 Zola 网站的 GitHub 或 GitLab 仓库并将其连接到 Cloudflare Workers
4. 保持默认设置并点击 _"Deploy"_

你的网站现在已构建并部署到 Cloudflare 的网络！你可以在 Workers 仪表板中添加自定义域名或修改设置。

你可以在 [使用 Cloudflare 仪表板创建 Workers 应用程序](https://developers.cloudflare.com/workers/get-started/dashboard/) 中找到更多文档。

[^1]: https://developers.cloudflare.com/workers/wrangler/configuration/#inheritable-keys
