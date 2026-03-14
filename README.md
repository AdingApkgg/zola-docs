# Zola 中文文档

[Zola](https://www.getzola.org/) 是一个快速的静态网站生成器，它是一个单一的二进制文件，没有任何依赖。

本项目是 [Zola 官方文档](https://github.com/getzola/zola/tree/master/docs) 的中文翻译版本。

## 本地预览

1. [安装 Zola](https://www.getzola.org/documentation/getting-started/installation/)
2. 克隆本仓库：
   ```bash
   git clone https://github.com/AdingApkgg/zola-docs.git
   cd zola-docs
   ```
3. 运行开发服务器：
   ```bash
   zola serve
   ```
4. 访问 `http://127.0.0.1:1111`

## 部署到 Cloudflare Pages

本项目已配置 `wrangler.toml` 和 `build.sh` 以支持在 Cloudflare Pages 上自动构建。

由于 Cloudflare Pages V2 构建环境不再预装 Zola，我们使用 `build.sh` 脚本在构建时自动下载并安装 Zola。

1. 在 Cloudflare Pages 中创建一个新项目，并连接到你的 GitHub 仓库。
2. **Build command** 设置为 `bash build.sh`（如果未自动检测）。
3. **Build output directory** 设置为 `public`。


## 贡献

欢迎提交 Pull Request 改进翻译或报告问题。

## 许可证

MIT License
