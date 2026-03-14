+++
title = "安装"
weight = 10
+++

Zola 在 [GitHub 发布页面](https://github.com/getzola/zola/releases) 上提供了适用于 MacOS、Linux 和 Windows 的预构建二进制文件。

### macOS

Zola 可通过 [Brew](https://brew.sh) 获取：

```sh
$ brew install zola
```

Zola 也可通过 [MacPorts](https://www.macports.org) 获取：

```sh
$ sudo port install zola
```

### Arch Linux

Zola 已收录在官方 Arch Linux 仓库中。

```sh
$ pacman -S zola
```

### Alpine Linux

自 Alpine v3.13 起，Zola 已收录在官方 Alpine Linux 社区仓库中。

如有必要，请参阅 Alpine Wiki 的这一部分，了解如何启用社区仓库：https://wiki.alpinelinux.org/wiki/Repositories#Enabling_the_community_repository

```sh
$ apk add zola
```

### Debian

Zola 可在 [barnumbirr/zola-debian](https://github.com/barnumbirr/zola-debian) 获取。
下载适用于您的 Debian 版本的最新 `.deb` 包，然后运行：

```sh
$ sudo dpkg -i zola_<version>_amd64_debian_<debian_version>.deb
```

### Gentoo

Zola 可通过 [GURU](https://wiki.gentoo.org/wiki/Project:GURU) 获取。

请参阅最终用户文档以了解如何[启用](https://wiki.gentoo.org/wiki/Project:GURU/Information_for_End_Users#Adding_the_GURU_repository) GURU 仓库。之后只需运行：

```sh
$ sudo emerge --ask www-apps/zola
```

### Void Linux

Zola 已收录在官方 Void Linux 仓库中。

```sh
$ sudo xbps-install zola
```

### FreeBSD

Zola 已收录在官方软件包仓库中。

```sh
$ pkg install zola
```

### OpenBSD

Zola 已收录在官方软件包仓库中。

```sh
$ doas pkg_add zola
```

### openSUSE

#### openSUSE Tumbleweed

Zola 已[收录](https://software.opensuse.org/package/zola?baseproject=ALL)在官方 openSUSE Tumbleweed 主 OSS 仓库中。

```sh
$ sudo zypper install zola
```

#### openSUSE Leap

Zola 已[收录](https://software.opensuse.org/package/zola?baseproject=ALL)在官方实验性 _utilities_ 仓库中。

```sh
$ sudo zypper addrepo https://download.opensuse.org/repositories/utilities/15.6/utilities.repo
$ sudo zypper refresh
$ sudo zypper install zola
```

### pkgsrc

Zola 已收录在官方软件包仓库中，可通过 [pkgin](https://pkgin.net/) 安装。

```sh
$ pkgin install zola
```

### Snapcraft

Zola 可在 snapcraft 上获取：

```sh
$ snap install --edge zola
```

### Flatpak

Zola 作为 flatpak 可在 [flathub](https://flathub.org) 上获取：

```sh
$ flatpak install flathub org.getzola.zola
```

要使用 zola：

```sh
$ flatpak run org.getzola.zola [command]
```

为了避免每次都输入这个命令，可以在 `~/.bashrc` 中创建一个别名：

```sh
$ alias zola="flatpak run org.getzola.zola"
```

### NixOS / Nixpkgs

Zola 已[收录](https://search.nixos.org/packages?show=zola&query=zola)
在 nixpkgs 仓库中。如果您使用的是 NixOS，可以通过将以下内容添加到 `/etc/nixos/configuration.nix` 来安装 Zola：

```
environment.systemPackages = [
  pkgs.zola
];
```

如果您在其他操作系统中使用 Nix 作为包管理器，可以使用以下命令安装：

```
nix-env -iA nixpkgs.zola
```

### 通过 Github Actions

Zola 可以通过 [taiki-e/install-action](https://github.com/taiki-e/install-action) 在 GHA 工作流中安装。
只需将其添加到您的 CI 配置中，例如：

```yaml
jobs:
  foo:
    steps:
      - uses: taiki-e/install-action@v2
        with:
          tool: zola@0.19.1
      # ...
```

查看 action 仓库以获取文档和更多示例。

### Docker

Zola 可在 [GitHub 容器注册表](https://github.com/getzola/zola/pkgs/container/zola)上获取。
它没有 `latest` 标签，您需要指定[特定的版本来拉取](https://github.com/getzola/zola/pkgs/container/zola/versions)。

```sh
$ docker pull ghcr.io/getzola/zola:v0.19.1
```

#### 构建 (Build)

```sh
$ docker run -u "$(id -u):$(id -g)" -v $PWD:/app --workdir /app ghcr.io/getzola/zola:v0.19.1 build
```

#### 服务 (Serve)

```sh
$ docker run -u "$(id -u):$(id -g)" -v $PWD:/app --workdir /app -p 8080:8080 ghcr.io/getzola/zola:v0.19.1 serve --interface 0.0.0.0 --port 8080 --base-url localhost
```

您现在可以浏览 http://localhost:8080。

#### 多阶段构建

由于 Zola docker 镜像中没有 shell，如果您想在 Dockerfile 中使用它，必须使用
`RUN` 的 exec 形式，如下所示：

```Dockerfile
FROM ghcr.io/getzola/zola:v0.19.1 as zola

COPY . /project
WORKDIR /project
RUN ["zola", "build"]
```

## Windows

Zola 可以使用官方 Winget 命令安装：

```sh
$ winget install getzola.zola
```

也可以在 [Scoop](https://scoop.sh) 上获取：

```sh
$ scoop install zola
```

以及 [Chocolatey](https://chocolatey.org/)：

```sh
$ choco install zola
```

Zola 在 PowerShell ISE 中无法工作。

## 从源码构建

要从源码构建 Zola，您需要安装 [Rust 和 Cargo](https://www.rust-lang.org/)。

在终端中，您现在可以运行以下命令：

```sh
$ cargo install --locked --git https://github.com/getzola/zola
$ zola --version
```

如果您遇到类似 `error: failed to run custom build command for 'ring v0.16.20'` 的编译错误，可以尝试以下命令：

```sh
$ cargo install --locked --no-default-features --features=native-tls --git https://github.com/getzola/zola
```

Cargo 会将 `zola` 二进制文件安装在 `~/.cargo/bin/` 中。
如果需要，您可以将其移动到站点的仓库中。
