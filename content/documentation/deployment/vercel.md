+++
title = "Vercel"
weight = 50
+++

Vercel（以前叫 Zeit）类似于 Netlify，使你的站点部署变得易如反掌。
站点由 Vercel 托管，只要我们向选定的生产分支（例如 master）推送提交，就会自动部署。

如果你没有 Vercel 帐户，可以在 [这里](https://vercel.com/signup) 注册。

## 自动部署

注册后，你可以从 Git 提供商（Github、GitLab 或 Bitbucket）导入你的站点。
导入仓库时，Vercel 将尝试找出你的站点使用的框架。

如果它没有默认为 Zola：

- 将 "Framework Preset" 设置为 **Zola**。

默认情况下，Vercel 选择输出目录为 `public`。如果你使用不同的目录，请在 "Build and Output Settings" 下拉菜单下指定输出目录。
你可以通过 [他们的文档](https://vercel.com/docs) 了解更多关于如何设置自定义域名以及如何充分利用 Vercel 的信息。

点击蓝色的 "Deploy" 按钮后，就可以开始了！

要使用特定版本的 Zola，请在项目设置中将 [`ZOLA_VERSION`](https://vercel.com/docs/deployments/environments#specifying-framework-versions) 环境变量设置为有效的发布标签，例如 `0.17.2`。

## 故障排除

### `GLIBC_X.XX` not found

这是因为 Vercel 的构建镜像不包含 Zola 所需的 `glibc` 版本。
Vercel 为不同的 Node.js 版本提供 [不同的构建镜像](https://vercel.com/docs/builds/build-image)，因此即使 Zola 与 Node.js 没有任何关系，你也可以从项目设置中升级 Node.js 版本，使 Vercel 使用较新的构建环境，从而允许 Zola 正常工作。

如果你的项目是在默认 Node.js 版本为 `20.x` 时创建的，将 Node.js 版本升级到 `22.x`（这是新的默认值）应该适用于 Zola 版本高达 `0.19.2`（含）而无需进一步配置。

由于 Vercel 不提供更新的镜像，当使用内置的 Zola 框架预设时，后续版本的 Zola 将无法再次工作。但是，从 Zola 版本 `0.21.0` 开始，发布了静态链接的 `musl` 二进制文件，这在 glibc 不足的系统（如 Vercel 的构建镜像）中提供了最高的兼容性。要使用 `musl` 编译的二进制文件，你必须确保 Vercel [不使用其内置的 Zola 预设，而是你自己提供二进制文件。](#using-a-custom-zola-binary)

## 其他选项

### 启用尾随斜杠

访问没有尾随斜杠的页面可能会破坏相对路径，因此你可能希望配置 Vercel 始终重定向带有尾随斜杠的路径。默认情况下，Vercel 上未启用重定向到尾随斜杠。

例如，如果你有一个 `about.md` 文件，并且当访问没有尾随斜杠的路径（如 `/about`）时，Vercel 将重定向带有尾随斜杠，结果为 `/about/`。
带有文件扩展名的路径将不会重定向到尾随斜杠，例如，如果你有一个名为 `favicon.ico` 的静态文件，它将保持原样。

要启用该功能，请在你的 git 仓库根目录中创建一个名为 `vercel.json` 的文件（如果尚未存在），并设置此选项：

```json
{
    "trailingSlash": true
}
```

### 首选干净 URL

启用后，所有 HTML 文件将在没有文件扩展名的情况下提供服务。例如，如果你有一个 `about.md` 文件，Zola 将生成一个 `about/index.html` 文件，但你可能希望 Vercel 将文件作为 `/about` 提供，而不带其 `index.html` 后缀。

要启用该功能，请在你的 git 仓库根目录中创建一个名为 `vercel.json` 的文件（如果尚未存在），并设置此选项：

```json
{
    "cleanUrls": true
}
```

### 使用自定义 Zola 二进制文件

如果你想自己提供 Zola 二进制文件以获得完全控制，而不是让 Vercel 使用其受控的 Zola 预设，请将 "Framework Preset" 设置为 "Other"。这将使 Vercel 不再自动使用 `ZOLA_VERSION` 变量。
然后，将 "Install Command" 设置为：

```bash
echo "${ZOLA_VERSION:-"latest"}" | sed '/^latest$/!s/\(.*\)/tags\/v\1/' | xargs -I% curl -fsSL "https://api.github.com/repos/getzola/zola/releases/%" | grep -oP "\"browser_download_url\": ?\"\\K(.+linux-${ZOLA_LIBC:-"musl"}\\.tar\\.gz)" | xargs curl -fsSL | tar -xz
```

此命令将从 GitHub API 获取的文件 URL 下载 Zola 并解压缩。
这样我们就可以继续使用相同的 `ZOLA_VERSION` 环境变量名称来固定到特定的 Zola 版本（与 Vercel 的做法相同） - 或者将其设置为 `latest` 以便每当在 Vercel 上启动部署时始终拉取最新版本。

我们在命令中默认也会拉取 `musl` 二进制文件，因此我们不再需要担心 Vercel 的构建镜像。但是，如果你想使用旧版本（低于 `0.21.0`，没有提供 `musl` 二进制文件），你需要创建一个名为 `ZOLA_LIBC` 的新环境变量并将其设置为 `gnu`。

除了将 "Install Command" 设置为上述内容外，你还需要将 "Build Command" 设置为 `./zola build`，这样我们就可以使用之前在本地下载的 Zola 二进制文件构建我们的站点。

如果你更喜欢使用 `vercel.json`（这会覆盖仪表板中设置的选项），你可以使用此配置：

```json
{
    "framework": null,
    "installCommand": "echo \"${ZOLA_VERSION:-\"latest\"}\" | sed '/^latest$/!s/\\(.*\\)/tags\\/v\\1/' | xargs -I% curl -fsSL \"https://api.github.com/repos/getzola/zola/releases/%\" | grep -oP \"\\\"browser_download_url\\\": ?\\\"\\K(.+linux-${ZOLA_LIBC:-\"musl\"}\\\\.tar\\\\.gz)\" | xargs curl -fsSL | tar -xz",
    "buildCommand": "./zola build",
    "outputDirectory": "public"
}
```

如果你想使用自己的 fork 并使用在那里发布的二进制文件，你可以根据自己的意愿修改命令。

## 另请参阅

请参阅 [Vercel 自己的文档](https://vercel.com/docs/projects/project-configuration) 以获取 `vercel.json` 中的所有可用选项。
