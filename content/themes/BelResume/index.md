
+++
title = "BelResume"
description = "精美、现代、极简的单页简历站点"
template = "theme.html"
date = 2025-04-30T17:15:25+05:30

[taxonomies]
theme-tags = ['minimal', 'resume']

[extra]
created = 2025-04-30T17:15:25+05:30
updated = 2025-04-30T17:15:25+05:30
repository = "https://github.com/cx48/BelResume.git"
homepage = "https://github.com/cx48/BelResume"
minimum_version = "0.20.0"
license = "MIT"
demo = "https://cx48.github.io/BelResume/"

[extra.author]
name = "cx48"
homepage = "https://cx48.dev"
+++        

# BelResumé

***一个精美、现代、极简的单页简历站点***

基于 [Zola](https://getzola.org/) 构建，使用 Tailwind CSS 与 Font Awesome 进行样式设计。

> “Bel” 在法语中意为“美丽”——这就是你的美丽简历！

## 预览

[BelResumé](https://cx48.github.io/BelResume/) can be deployed for free using GitHub Pages or Vercel
[BelResumé](https://cx48.github.io/BelResume/) 可免费部署到 GitHub Pages 或 Vercel。

#### Light Mode

![Light Mode](https://raw.githubusercontent.com/cx48/BelResume/refs/heads/main/static/images/light.png)

#### Dark Mode

![Dark Mode](https://raw.githubusercontent.com/cx48/BelResume/refs/heads/main/static/images/dark.png)

#### PageSpeed Insights

![PageSpeed](https://raw.githubusercontent.com/cx48/BelResume/refs/heads/main/static/images/pagespeed.png)

## 项目结构

- **config.toml**：站点元数据  
- **static/**：`css/style.css`, `js/script.js`  
- **templates/index.html**：主布局（调用所有 partial）  
- **templates/partials/**：简历各模块
  - `header.html`：姓名、职位、联系方式
  - `experience.html`：工作经历（公司、角色、成果）
  - `education.html`：学校、学位、专业方向
  - `projects.html`：关键项目摘要与标签
  - `skills.html`：技能进度条（可调宽度）
  - `certifications.html`：证书名称 + 颁发机构 + 年份
  - `languages.html`：语言能力（进度条与标签）
  - `awards.html`：奖项名称 + 年份 + 颁发方

## 快速开始

1. **安装 Zola**：[https://getzola.org/documentation/getting-started/installation/](https://getzola.org/documentation/getting-started/installation/) 

2. **克隆仓库**：
   ```bash
   git clone https://github.com/cx48/BelResume
   cd BelResume
   ```

3. **本地运行**：
   ```bash
   zola serve
   ```

   对 `partials/` 下 HTML 做必要修改后，访问 [http://127.0.0.1:1111](http://127.0.0.1:1111)。

4. **构建静态站点**：
   ```bash
   zola build
   ```
   所有输出文件位于 `/public`。

## 部署指南

> 部署到 GitHub Pages

1. 运行 Zola 构建：
   ```bash
   zola build
   ```

2. 将 `public/` 目录内容提交并推送到 `gh-pages` 分支

3. 在 GitHub 仓库设置中，从 `/public` 目录或 `gh-pages` 分支启用 Pages

4. 你的网站将发布在 `https://yourusername.github.io/BelResume/`

> 部署到 Vercel

1. 登录 [Vercel](https://vercel.com) 并导入 GitHub 仓库

2. 将 **Build Command** 设置为：
   ```bash
   zola build
   ```

3. 将 **Output Directory** 设置为：
   ```bash
   public
   ```

4. 将 **Framework Preset** 设置为 `Other`

5. 点击 **Deploy**

每次推送后，Zola 会自动构建并从 `public/` 目录提供内容。

## 自定义指南

更新简历时，只需打开 `partials/` 下对应 HTML 文件并按需修改。

### 1. **config.toml**  
Update site-wide metadata:
```toml
title = "John Doe"
description = "Senior Software Engineer"
base_url = "https://yourdomain.com"
```

### 2. **partials/header.html**
Edit your name, role, email, phone, location, LinkedIn link. Example:
```html
<h1 class="text-3xl font-bold">John Doe</h1>
<h2 class="text-xl text-[var(--primary)] font-semibold">Senior Software Engineer</h2>
```

### 3. **partials/experience.html**
Replace job titles, companies, durations, and bullet points.
```html
<h3 class="font-semibold">Senior Developer</h3>
<span>2020–Present</span>
<ul>
  <li>Improved system performance by 30%</li>
</ul>
```

### 4. **partials/education.html**
List your degrees, schools, GPA or honors:
```html
<h3>Master of CS</h3>
<p>Stanford University — GPA: 3.9</p>
```

### 5. **partials/projects.html**
List project names, stacks used, short descriptions.
```html
<h3>E-commerce Platform</h3>
<span class="tag">React</span> <span class="tag">Node.js</span>
```

### 6. **partials/skills.html**
Update skill bars by adjusting the width in `style="width: 90%"`.
```html
<h3>JavaScript</h3>
<div class="progress" style="width: 95%"></div>
```

### 7. **partials/certifications.html**
List certificates with name, organization, and date:
```html
<h3>AWS Certified Architect</h3>
<p>Amazon – 2022</p>
```

### 8. **partials/languages.html**
Change language names, levels, and progress widths:
```html
<span>English</span> <span>Native</span>
<div style="width: 100%"></div>
```

### 9. **partials/awards.html**
Highlight awards with name and source:
```html
<h3>Best Hackathon Project</h3>
<p>DefCon 2025</p>
```

## 联系方式

如有反馈、问题，或只是想打个招呼：  
欢迎 [提交 issue](https://github.com/cx48/BelResume/issues) 或直接联系。

> 联系方式请查看我的 GitHub 主页

        
