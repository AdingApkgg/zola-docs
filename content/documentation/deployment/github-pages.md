+++
title = "GitHub Pages"
weight = 30
+++

你有 2 个选项部署到 GitHub Pages：

- 使用 Pages Artifacts 并通过 GitHub Actions 处理发布
- 使用不同的分支（例如 `gh-pages`），在其中提交生成的文件

如果你需要使用自己的自定义域名，请遵循来自 <https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages> 的 GitHub 文档。

## Pages Artifacts

Zola 有一个官方 action：<https://github.com/getzola/github-pages>

按照它的 README 操作（不要忘记在设置中启用 GitHub Action 源），你应该可以通过 CI 让你的站点运行起来。

## 分支发布

对于这种方法，还有另一个 action：<https://github.com/shalzz/zola-deploy-action>
