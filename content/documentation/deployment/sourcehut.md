+++
title = "Sourcehut Pages"
weight = 15
+++

在 [Sourcehut Pages][srht] 上部署你的静态 Zola 网站非常简单。

你需要在 Zola 项目的根文件夹中创建一个 `.build.yml` 清单文件，并将更改推送到 Sourcehut git/hg 仓库。
要创建你的 `.build.yml` 文件，你可以从 [模板][srht-tpl] 开始或使用以下示例：
``` yaml
image: alpine/edge
packages:
  - hut
  - zola
oauth: pages.sr.ht/PAGES:RW
environment:
  site: your_username.srht.site
sources:
  - https://git.sr.ht/~your_username/my-website
tasks:
  - build: |
      cd my-website
      zola build
  - package: |
      cd my-website
      tar -C public -cvz . > ../site.tar.gz
  - upload: |
      hut pages publish -d $site site.tar.gz
```

此清单将克隆你的源代码，构建网站并将生成的静态文件上传到你在 `site` 中指定的域。
为了发布网站，构建清单使用 `hut`，这是一个命令行工具，负责自动生成身份验证令牌，因此你无需执行任何其他操作。

从此模板中，你需要自定义变量 `site` 为将托管你的网站的域，以及 `sources` 指向你的 Sourcehut git/hg 公共 URL（在此示例中，`my-website` 是仓库的名称）。

然后提交并推送你的更改：
``` sh
$ git push
Enumerating objects: 5, done.
...
remote: Build started:
remote: https://builds.sr.ht/~your_username/job/430625 [.build.yml]
To git.sr.ht:~your_username/www
   fbe9afa..59ae556  master -> master
```

构建作业将自动触发。
请注意，Sourcehut 返回指向构建页面的直接链接，你可以在其中检查进度和成功状态。

默认情况下，你可以使用 Sourcehut Pages 的子域来托管你的静态网站 - `your_username.srht.site`。
如果你想使用自定义域名（例如 "blog.mydomain.org"），你需要配置 DNS 记录以指向 Sourcehut 服务器。
有关如何执行此操作的说明可在 [Sourcehut][srht-custom-domain] 上找到。

[srht]: https://srht.site
[srht-tpl]: https://git.sr.ht/~sircmpwn/pages.sr.ht-examples
[srht-custom-domain]: https://srht.site/custom-domains
