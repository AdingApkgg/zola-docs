+++
title = "CLI 使用"
weight = 15
+++

Zola 只有 4 个命令：`init`, `build`, `serve` 和 `check`。

你可以通过运行 `zola --help` 查看整个程序的帮助，通过运行 `zola <cmd> --help` 查看特定命令的帮助。

## init

在询问几个基本配置问题后，在给定目录创建 Zola 使用的目录结构。
在这些提示中所做的任何选择都可以通过修改 `config.toml` 轻松更改。

```bash
$ zola init my_site
$ zola init
```

如果 `my_site` 目录已经存在，Zola 只有在该目录仅包含隐藏文件（点文件被忽略）时才会填充它。如果没有传递 `my_site` 参数，Zola 将尝试填充当前目录。

如果你想尝试填充非空目录并且很勇敢，你可以使用 `zola init --force`。请注意，这**不会**覆盖现有的文件夹或文件；在这些情况下，你会得到一个 `File exists (os error 17)` 错误或类似的错误。

你可以直接在一个新文件夹中初始化 git 仓库和 Zola 站点：

```bash
$ git init
$ zola init
```

## build

这将在 `public` 目录中构建整个站点（如果此目录已存在，则会将其删除）。

```bash
$ zola build
```

你可以通过向 `base-url` 标志传递新 URL 来覆盖配置中的 `base_url`。

```bash
$ zola build --base-url $DEPLOY_URL
```

这很有用，例如当你想要将站点的预览部署到动态 URL 时，例如 Netlify 部署预览。

你可以通过向 `output-dir` 标志传递另一个值来覆盖默认输出目录 `public`。如果此目录已存在，系统将提示用户是否替换该文件夹；你可以通过传递 `--force` 标志来覆盖此提示。

```bash
$ zola build --output-dir $DOCUMENT_ROOT
```

你可以像这样指向 `config.toml` 以外的配置文件（请注意，`config` 选项的位置很重要）：

```bash
$ zola --config config.staging.toml build
```

你也可以使用 `root` 标志处理不同目录中的项目。如果使用 `root` 标志构建“树外”项目，你可能希望将其与 `output-dir` 标志结合使用。（请注意，像 `config` 一样，位置很重要）：

```bash
$ zola --root /path/to/project build
```

默认情况下，草稿不会被加载。如果你希望包含它们，请传递 `--drafts` 标志。

## serve

这将使用本地服务器构建并服务站点。如果你想要与默认值 (`127.0.0.1:1111`) 不同的设置，你也可以指定要使用的接口/端口组合。

你还可以使用 `--interface` 和 `-u`/`--base-url` 分别为接口和 base_url 指定不同的地址，例如，如果你在 Docker 容器中运行 Zola。

> 默认情况下，本地网络中的设备**无法**访问服务的页面。当你想要在移动设备或平板电脑上测试页面交互和布局时，这可能很重要。但是，如果你将接口设置为 `0.0.0.0`，本地网络中的设备将能够通过请求服务页面的机器的本地 IP 地址和使用的端口来访问服务的页面。
>
> 为了使一切正常工作，你可能还需要将 `base-url` 标志更改为你的本地 IP 或将其设置为 `/` 以使用基于服务器的相对路径。

使用 `--open` 标志自动在你的 Web 浏览器中打开本地托管的实例。

在开始之前，Zola 将删除输出目录（默认情况下为项目根目录中的 `public`）以从干净的状态开始。

如果你指定了目录但也使用了 `output-dir` 标志，Zola 将不会使用指定的目录，如果它已经存在，除非使用了 `--force` 标志。

```bash
$ zola serve
$ zola serve --port 2000
$ zola serve --interface 0.0.0.0
$ zola serve --interface 0.0.0.0 --port 2000
$ zola serve --interface 0.0.0.0 --base-url 127.0.0.1
$ zola serve --interface 0.0.0.0 --base-url /
$ zola serve --interface 0.0.0.0 --port 2000 --output-dir www/public
$ zola serve --open
```

`serve` 命令将监视你的所有内容，并在可能的情况下提供无需硬刷新的实时重新加载。如果你在 Windows 上使用 WSL2，请确保将网站存储在 WSL 文件系统中。

某些更改无法自动处理，因此实时重新加载可能并不总是有效。如果你没有看到你的更改或收到错误，请尝试重新启动 `zola serve`。

默认情况下，实时重新加载将去抖动一整秒，以便更优雅地处理快速连续对输入文件的多次更改。你可以使用 `--debounce <duration_ms>` 标志控制该去抖动持续时间。
你可以使用 `-d1` 来（实际上）完全禁用它：由于技术原因（并保持简单），不支持 0 的“去抖动”。

你也可以像这样指向 `config.toml` 以外的配置文件（请注意，`config` 选项的位置很重要）：

```bash
$ zola --config config.staging.toml serve
```

默认情况下，草稿不会被加载。如果你希望包含它们，请传递 `--drafts` 标志。

## check

check 子命令将尝试构建所有页面，就像 build 命令一样，但不会将任何结果写入磁盘。此外，它还会通过尝试获取 Markdown 文件中的所有外部链接来检查它们（模板文件中的链接不被检查）。

你可以通过 `--skip-external-links` 标志跳过所有外部链接的链接检查。

默认情况下，草稿不会被加载。如果你希望包含它们，请传递 `--drafts` 标志。

## 彩色输出

如果你的终端支持，将使用彩色输出。

*注意*：当输出重定向到管道或文件时（即，当标准输出不是 TTY 时），着色会自动禁用。

你可以通过导出以下两个环境变量之一来禁用此行为：

- `NO_COLOR` (值无关紧要)
- `CLICOLOR=0`

要强制使用颜色，你可以设置以下环境变量：

- `CLICOLOR_FORCE=1`

## 额外信息

Zola 可以通过 `RUST_LOG` 变量提供有关其行为的详细日志记录：

- 要查看来自 Zola 的计时信息，请设置 `RUST_LOG=zola=info,site=debug`。
- 要查看调试信息，请设置 `RUST_LOG=debug`。*注意*：输出将**非常嘈杂**，请谨慎使用。
- 要完全禁用所有日志输出，请设置 `RUST_LOG=off`。

有关 `RUST_LOG` 的完整参考，请参阅 [env_logger 文档](https://docs.rs/env_logger/0.11.8/env_logger/#enabling-logging)。
