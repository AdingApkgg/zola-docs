+++
title = "Codeberg Pages"
weight = 50
+++

我们将使用 Codeberg 托管的 Woodpecker CI 在 Codeberg Pages 上托管站点。

## 配置你的仓库

你需要 Codeberg 上创建一个仅包含你的 Zola 项目的仓库。[Zola 目录结构](https://www.getzola.org/documentation/getting-started/directory-structure/) 应该位于你的仓库的根目录中。

有关如何在 Codeberg 上创建和管理仓库的信息，请参阅 <https://docs.codeberg.org/getting-started/first-repository/>。

## 确保 Woodpecker CI 可以访问你的主题

根据你添加主题的方式，你的仓库可能不包含它。确保添加主题的最佳方法是使用子模块。确保使用 URL 的 `https` 版本。

```bash
git submodule add <theme_url> themes/<theme_name>
```

例如，这可能看起来像：

```bash
git submodule add https://github.com/getzola/hyde.git themes/hyde
```

## 设置 Woodpecker CI

假设你可以访问 [Codeberg 的 Woodpecker CI](https://docs.codeberg.org/ci/)，我们可以构建站点并在每次提交时自动将其部署到 [Codeberg Pages](https://codeberg.page)。

首先，将以下示例 [Zola CI 文件](https://codeberg.org/Codeberg-CI/examples/src/branch/main/Zola/.woodpecker.yaml) 放在你的项目的根目录中：

```yaml
# 排除在 pages 分支上运行管道
when:
  branch:
    exclude: pages

# 递归克隆以完全克隆作为 Git 子模块给出的主题
clone:
  git:
    image: woodpeckerci/plugin-git
    settings:
      recursive: true

steps:
  # 构建 Zola 静态文件
  build:
    image: alpine:edge
    commands:
      - apk add zola
      - zola build
    when:
      event: [push, pull_request]

  publish:
    image: bitnami/git
    environment:
      CBMAIL:
        from_secret: "mail"
      CBTOKEN:
        from_secret: "codeberg_token"
    commands:
      # 配置 Git
      - git config --global user.email "$${CBMAIL}"
      - git config --global user.name "Woodpecker CI"
      # 克隆输出分支
      - git clone --branch pages https://$${CBTOKEN}@codeberg.org/$CI_REPO.git $CI_REPO_NAME
      # 进入输出分支
      - cd $CI_REPO_NAME
      # 删除旧文件
      - git rm -r "*" || true # 如果没有要删除的内容，不要失败
      # 复制构建步骤的输出
      - cp -ar ../public/. .
      # 提交并推送所有静态文件与源提交哈希
      - git add --all
      - git commit -m "Woodpecker CI ${CI_COMMIT_SHA} [SKIP CI]" --allow-empty
      - git push
    when:
      event: [push]
```

然后将以下 secrets 添加到 [Woodpecker](https://ci.codeberg.org/)：

- `mail`: 你在 Codeberg 使用的电子邮件地址。
- `codeberg_token`: 具有 `write:repository` 权限的 [Codeberg 访问令牌](https://docs.codeberg.org/advanced/access-token/)。

完成后，你可以通过向仓库推送一些内容来触发 CI，Woodpecker 将构建站点并将生成的站点复制到 `pages` 分支，它将在 `https://<user>.codeberg.page/<repository>` 上可用。

对于 [自定义域名](https://docs.codeberg.org/codeberg-pages/using-custom-domain/)，在 `./static/` 目录中创建 `.domains` 文件，以便将其复制到生成的构建中。

有关 Codeberg Pages 的更多信息，请参阅 [官方 Codeberg 文档](https://docs.codeberg.org/codeberg-pages/)。
