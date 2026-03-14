+++
title = "Zeabur"
weight = 50
+++

在本教程中，我们将指导你将 Zola 站点部署到 [Zeabur](https://zeabur.com) 的过程。Zeabur 提供无缝的部署体验，具有自动 SSL 证书和全球边缘网络交付。让我们开始吧！

## 先决条件

- 本地机器上的 Zola 站点项目。
- 一个 GitHub 帐户和托管在 GitHub 上的 Zola 站点项目仓库。
- 一个 Zeabur 帐户。如果你没有，请在 [这里](https://zeabur.com/login) 注册。

## 第一步：在 Zeabur 上创建项目

1. 登录到你的 Zeabur 帐户。
2. 导航到仪表板并点击 **Create Project** 按钮。
3. 按照屏幕上的说明设置新项目。

## 第二步：将你的 Zola 文件推送到 GitHub

1. 如果你还没有在你的 Zola 项目文件夹中初始化 Git 仓库：

    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    ```

2. 将你的 Zola 项目推送到 GitHub：

    ```bash
    git remote add origin <your-github-repo-url>
    git branch -M main
    git push -u origin main
    ```

将 `<your-github-repo-url>` 替换为你的 GitHub 仓库的 URL。

## 第三步：在 Zeabur 上创建服务

1. 回到你的 Zeabur 仪表板，点击 **Create Service**。
2. 选择 **git** 选项以连接你的 GitHub 仓库。

## 第四步：选择你的 Zola 仓库

1. 从仓库列表中，选择你的 Zola 项目所在的仓库。

## 第五步：自动部署

Zeabur 将自动检测到你正在部署 Zola 项目，并将为你处理部署过程，无需任何额外的配置。

要使用特定版本的 Zola，请在项目设置中将 [`ZOLA_VERSION`](https://zeabur.com/docs/environment/variables) 环境变量设置为有效的发布标签，例如 `0.17.2`。

## 第六步：域名绑定

1. 部署完成后，将域名绑定到你的服务。
2. 你可以选择使用免费的 `.zeabur.app` 子域或绑定你自己的自定义域名。
3. Zeabur 将自动为你的域名提供免费的 SSL 证书，确保你的访问者安全浏览。

## 第七步：你的站点已上线！

恭喜！你的 Zola 站点现已部署并上线，通过 Zeabur 的边缘网络提供服务。

你现在可以在你设置的域名上访问你的网站。
