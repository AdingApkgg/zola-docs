+++
title = "Edgio"
weight = 50
+++

如果你没有 Edgio 帐户，可以在 [这里](https://app.layer0.co/signup) 注册。

## 手动部署

对于命令行手动部署，请按照以下步骤操作：

1. 安装 Edgio CLI: 

```bash
npm i -g @edgio/cli
```

2. 在你的项目根目录创建一个包含以下内容的 package.json：

```bash
npm init -y
```

3. 使用以下命令初始化你的项目：

```bash
edgio init
```

4. 将项目根目录下的 routes.js 更新为以下内容：

```js
// This file was added by edgio init.
// You should commit this file to source control.

import { Router } from '@edgio/core/router'

export default new Router().static('public')
```

5. 构建你的 zola 应用：

```bash
zola build
```

6. 部署！

```bash
edgio deploy
```
