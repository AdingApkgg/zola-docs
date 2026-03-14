+++
title = "Fly.io"
weight = 70
+++

如果你没有 fly.io 帐户，可以在 [这里](https://fly.io/app/sign-up) 注册。

然后按照 [这里](https://fly.io/docs/hands-on/install-flyctl/) 的说明安装 `flyctl` 工具。

创建一个 `Dockerfile`：

```Dockerfile
FROM ghcr.io/getzola/zola:v0.17.2 AS builder

WORKDIR /app
COPY . .
RUN ["zola", "build"]

FROM joseluisq/static-web-server:2
COPY --from=builder /app/public /public
ENV SERVER_PORT 8080
```

你现在可以运行 `fly launch`。它将检测 `Dockerfile` 并在很大程度上自动配置所有内容。填写必要的信息，但在 (1) 启动任何数据库和 (2) 立即部署时说“no”。

记下分配给你的应用的 hostname。

如果你已经有一个 Zola 站点，你现在必须确保 `config.toml` 中的 `base_url` 使用你的应用的 hostname（或任何指向该应用的域名）正确设置：

    base_url = "https://white-snow-9922.fly.dev"

如果你没有现有站点，请使用 `zola init -f` 初始化一个，并记住设置正确的 `base_url`。

你现在准备好启动你的站点了！运行 `flyctl deploy` 并玩得开心！

最后，要从 GitHub 设置站点的持续部署，请遵循 [此指南](https://fly.io/docs/app-guides/continuous-deployment-with-github-actions/) 的步骤 4-8。对你站点的任何更改现在都将自动推送。
