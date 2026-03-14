+++
title = "Azure Static Web Apps"
weight = 60
+++

[Azure Static Web Apps](https://learn.microsoft.com/en-us/azure/static-web-apps/overview) 是一项托管的 Azure 服务，用于处理从 GitHub 或 Azure DevOps 仓库的更改自动部署静态站点内容。我们将介绍如何配置通过 GitHub Actions 将你的站点部署到 Azure Static Web Apps。

### 设置 Azure Static Web Apps
按照 [官方文档](https://learn.microsoft.com/en-us/azure/static-web-apps/get-started-portal?tabs=vanilla-javascript&pivots=github) 在 Azure 门户中配置静态 Web 应用程序，选择 `GitHub` 作为代码托管平台，但 `Build Details` 部分除外。

相反，对于 `Build Details` 部分，将 App location 设置为 `./public`，因为这是 `zola build` 默认写入站点内容的位置。将其他框留空。

创建 Web 应用程序后，记下 Azure 自动创建的域，并将你的仓库的 `config.toml` 中的 `base_url` 更新为该 URL。


### 配置 GitHub Actions
Azure 应该已经在你的 GitHub 仓库中的 `.github/workflows` 下创建了一个 GitHub Actions YAML 文件，并配置了用于将你的应用程序部署到 Azure 的 secrets。现在我们需要更新工作流以安装 Zola 并构建你的站点。


```yaml
# .github/workflows/azure-static-web-apps-<web-app-name>
name: Azure Static Web Apps CI/CD

on:
  push:
    branches:
      - main
  pull_request:
    types: [opened, synchronize, reopened, closed]
    branches:
      - main

jobs:
  build_and_deploy_job:
    if: github.event_name == 'push' || (github.event_name == 'pull_request' && github.event.action != 'closed')
    runs-on: ubuntu-latest
    name: Build and Deploy Job
    steps:
      - uses: actions/checkout@v3
        with:
          submodules: true
          lfs: false
      - uses: taiki-e/install-action@v2
        with:
          tool: zola@0.21.0
      - name: Build Static Site
        run: zola build
      - name: Build And Deploy
        id: builddeploy
        uses: Azure/static-web-apps-deploy@v1
        with:
          azure_static_web_apps_api_token: ${{ secrets.AZURE_STATIC_WEB_APPS_API_TOKEN_<WEB_APP_NAME>}}
          repo_token: ${{ secrets.GITHUB_TOKEN }} # 用于 Github 集成（即 PR 评论）
          action: "upload"
          ###### Repository/Build Configurations - These values can be configured to match your app requirements. ######
          # 有关 Static Web App 工作流配置的更多信息，请访问：https://aka.ms/swaworkflowconfig
          app_location: "./public" # App 源代码路径
          api_location: "" # Api 源代码路径 - 可选
          output_location: "" # 构建的 app 内容目录 - 可选
          ###### End of Repository/Build Configurations ######

  close_pull_request_job:
    if: github.event_name == 'pull_request' && github.event.action == 'closed'
    runs-on: ubuntu-latest
    name: Close Pull Request Job
    steps:
      - name: Close Pull Request
        id: closepullrequest
        uses: Azure/static-web-apps-deploy@v1
        with:
          azure_static_web_apps_api_token: ${{ secrets.AZURE_STATIC_WEB_APPS_API_TOKEN<WEB_APP_NAME> }}
          action: "close"

```
推送 YAML 更改后，GitHub 将自动启动工作流部署你的站点！
