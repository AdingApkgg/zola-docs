# 同步官方文档方案

为了保持本项目与 Zola 官方文档的同步，我们提供了以下几种方案。

## 方案一：使用自动检测脚本（推荐）

本项目包含一个 Python 脚本，可以自动检测本地的英文原版文档（`.en.md`）与官方仓库的最新版本是否存在差异。

### 使用方法

在项目根目录下运行：

```bash
python3 scripts/sync_check.py
```

### 脚本功能

1. 扫描 `content/documentation` 下所有的 `.en.md` 文件。
2. 自动映射到官方 GitHub 仓库的对应文件 URL。
3. 下载最新内容并与本地文件进行比对。
4. 输出有差异的文件列表。

### 发现差异后如何处理？

如果脚本提示某个文件有差异（例如 `DIFFERENT`），你可以：
1. 打开官方对应文件的链接（脚本输出中会提供）。
2. 将官方最新内容复制到本地对应的 `.en.md` 文件中。
3. 对比 `.en.md` 和对应的 `.md`（中文翻译），更新中文翻译以反映最新的变更。

## 方案二：Git Remote 集成（进阶）

如果你熟悉 Git 操作，可以将官方仓库添加为远程源，以便更精确地查看差异。

### 设置步骤

1. 添加官方仓库作为远程源（只需执行一次）：
   ```bash
   git remote add upstream https://github.com/getzola/zola.git
   ```

2. 获取官方最新更新：
   ```bash
   git fetch upstream
   ```

3. 查看差异（比较本地文件与官方 master 分支的 docs 目录）：
   ```bash
   # 比如查看 overview.en.md 与官方版本的差异
   # 注意：官方路径通常在 docs/content/...
   git diff HEAD:content/documentation/content/overview.en.md upstream/master:docs/content/documentation/content/overview.md
   ```

## 方案三：GitHub Actions 自动化（可选）

如果需要定期自动检查，可以配置 GitHub Actions，每天定时运行 `scripts/sync_check.py`，并在发现差异时发送通知或创建 Issue。

### 示例 Workflow 配置

`.github/workflows/sync-check.yml`:

```yaml
name: Check Upstream Sync

on:
  schedule:
    - cron: '0 0 * * *' # 每天运行一次
  workflow_dispatch:

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'
          
      - name: Run sync check
        run: python3 scripts/sync_check.py
```
