+++
title = "Docker 镜像"
weight = 90
+++

如果你必须通过 Docker 分发基于 Zola 的网站，使用多阶段构建很容易做到。

这是一个构建当前文件夹并将结果放入 docker 镜像的示例，该镜像将由 [static-web-server](https://static-web-server.net/)（一个用 rust 编写的极简主义 Web 服务器）提供服务。

当然，你可能希望将第二阶段替换为另一个静态 Web 服务器，如 Nginx 或 Apache。

```Dockerfile
FROM ghcr.io/getzola/zola:v0.17.1 as zola

COPY . /project
WORKDIR /project
RUN ["zola", "build"]

FROM ghcr.io/static-web-server/static-web-server:2
WORKDIR /
COPY --from=zola /project/public /public
```

要将你的网站构建为 docker 镜像，然后运行：

```bash
docker build -t my_website:latest .
```

要测试你的网站，只需运行 docker 镜像并浏览 [http://localhost:8000](http://localhost:8000)

```bash
docker run --rm -p 8000:80 my_website:latest
```

请注意，如果你希望能够从多个位置使用你的 docker 镜像，你必须将 `base_url` 设置为 `/`。
