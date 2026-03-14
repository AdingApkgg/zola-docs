+++
title = "GitLab Pages"
weight = 40
+++

我们将使用 GitLab CI/CD 中的 GitLab Runner 在 GitLab Pages 上托管站点。

## 配置你的仓库

可以将你的 Zola 站点托管在 GitLab 提供的 SaaS 实例 (<https://gitlab.com>) 或自托管实例上。

建议在 GitLab 上创建一个仅包含你的 Zola 项目的仓库。[Zola 的目录结构](https://www.getzola.org/documentation/getting-started/directory-structure/) 应该位于你的仓库的根目录中。

有关如何在 GitLab 上创建和管理仓库的信息，请参阅：

<https://docs.gitlab.com/ee/user/project/repository/>

## 确保 runner 可以访问你的主题

根据你添加主题的方式，你的仓库可能不包含它。
确保添加主题的最佳方法是使用子模块。
执行此操作时，请确保使用 URL 的 `https` 版本。

```bash
git submodule add {THEME_URL} themes/{THEME_NAME}
```

例如，这可能看起来像：

```bash
git submodule add https://github.com/getzola/hyde.git themes/hyde
```

## 设置 GitLab Runner

GitLab Runner 需要知道如何创建你的站点，以便将其部署到 GitLab Pages 服务器。

我们为你提供了一个模板来轻松完成此任务。
在你的仓库根目录中创建一个名为 `.gitlab-ci.yml` 的文件，并复制下面模板的内容。

确保在 `ZOLA_VERSION` 变量中指定 Zola 的版本。

```yaml
stages:
  - deploy

default:
  image: debian:stable-slim

variables:
  # 当策略设置为 "recursive" 时，runner 将能够拉取你的 Zola 主题。
  GIT_SUBMODULE_STRATEGY: "recursive"

  # 确保在此处指定 Zola 的版本。
  # 使用 semver 格式 (x.y.z) 指定版本。
  # 例如："0.17.2" 或 "0.18.0"。
  ZOLA_VERSION:
    description: "The version of Zola used to build the site."
    value: ""

pages:
  stage: deploy
  script:
    - |
      apt-get update
      DEBIAN_FRONTEND=noninteractive apt-get install --assume-yes --no-install-recommends wget ca-certificates
      zola_url="https://github.com/getzola/zola/releases/download/v${ZOLA_VERSION}/zola-v${ZOLA_VERSION}-x86_64-unknown-linux-gnu.tar.gz"
      if ! wget --quiet --spider $zola_url; then
        echo "A Zola release with the specified version could not be found."
        exit 1
      fi
      wget $zola_url
      tar -xzf *.tar.gz
      ./zola build --base-url $CI_PAGES_URL

  artifacts:
    paths:
      # 这是其内容将被部署到 GitLab Pages 服务器的目录。
      # GitLab Pages 默认期望一个具有此名称的目录。
      - public

  rules:
    # 此规则使你的网站仅当你推送到仓库的默认分支（例如 "master" 或 "main"）时才发布和更新。
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
```

请记住，此模板假设你在 GitLab Runner 上使用 [Docker executor](https://docs.gitlab.com/runner/executors/docker.html)。
随意根据你的工作流程和特定要求调整文件。

当你将此文件推送到仓库的默认分支（例如 "master" 或 "main"）后，你的站点将准备就绪。GitLab CI/CD 管道将确保你的站点自动发布和更新。

在 GitLab 的左侧栏中，导航到 **Deploy > Pages** 以在 **Access pages** 部分找到你的网站的 URL。

有关如何在 GitLab Pages 上托管你的站点的更多信息，请参阅 [GitLab 官方文档](https://docs.gitlab.com/ee/user/project/pages/)。
