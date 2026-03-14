+++
title = "Netlify"
weight = 20
+++

如果你没有 Netlify 帐户，你可以[注册](https://app.netlify.com)一个。


## 自动部署

进入管理界面后，你可以从 Git 提供商（GitHub、GitLab 或 Bitbucket）添加站点。在此过程结束时，你可以选择项目的部署设置：

 - build command: `zola build` (在变量中用你要使用的版本替换版本号)
 - publish directory: `public` 目录所在的路径
 - image selection: 使用最新的
 - Environment variables: `ZOLA_VERSION` 值为例如 `0.13.0`

通过此设置，你的站点应该在每次提交到 master 时自动部署。对于 `ZOLA_VERSION`，你可以使用 GitHub 仓库中任何标记的 `release` 版本。Netlify 将自动获取标记的版本并使用它来构建你的站点。

但是，如果你想使用 Netlify 提供的所有功能，你还应该发布 pull requests 的临时站点。

这是通过在你的仓库中添加以下 `netlify.toml` 文件并在管理界面中删除构建命令/发布目录来完成的。

```toml
[build]
# 这假设 Zola 站点在一个 docs 文件夹中。如果不是，你不需要
# 有 `base` 变量，但你需要 `publish` 和 `command` 变量。
base    = "docs"
publish = "docs/public"
command = "zola build"

[build.environment]
# 设置你要使用的版本名称，Netlify 将自动使用它。
ZOLA_VERSION = "0.13.0"

# 部署分支预览的魔法。
# 我们需要用 Netlify 分配给我们的预览站点的任何 url 覆盖 base url。
# 我们使用 Netlify 环境变量 `$DEPLOY_PRIME_URL` 来做到这一点。

[context.deploy-preview]
command = "zola build --base-url $DEPLOY_PRIME_URL"
```

## 手动部署

如果你更喜欢使用非标记发布的 Zola 版本（例如，在从源代码构建 Zola 并进行修改后），那么你需要手动将 `public` 文件夹部署到 Netlify。你可以通过 Netlify 的 Web GUI 或命令行来执行此操作。

对于命令行手动部署，请按照以下步骤操作：
 1.  从你的 Netlify 帐户的设置部分生成一个 `Personal Access Token`（*不是* OAuth 应用程序）。
 2.  使用 `zola build` 构建你的站点。
 3.  创建一个包含 `public` 目录的 zip 文件夹。
 4.  运行下面的 `curl` 命令，填写你的 PERSONAL_ACCESS_TOKEN_FROM_STEP_1, FILE_NAME.zip 和 SITE_NAME。
 5.  (可选) 删除 zip 文件夹。

```bash
curl -H "Content-Type: application/zip" \
     -H "Authorization: Bearer PERSONAL_ACCESS_TOKEN_FROM_STEP_1" \
     --data-binary "@FILE_NAME.zip" \
     https://api.netlify.com/api/v1/sites/SITE_NAME.netlify.com/deploys
```
