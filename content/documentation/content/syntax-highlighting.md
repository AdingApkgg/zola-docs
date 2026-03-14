+++
title = "语法高亮"
weight = 80
+++

Zola 带有内置的语法高亮显示，但你首先需要在 [配置](@/documentation/getting-started/configuration.md) 中启用它。

完成后，Zola 将自动高亮显示你内容中的所有代码块。Markdown 中的代码块如下所示：

````
```rust
let highlight = true;
```
````

你可以将 `rust` 替换为另一种语言，或者不放任何东西以使文本被解释为纯文本。

Zola 使用 [Giallo](https://github.com/getzola/giallo)，这是一个使用 VSCode 语法和主题的库。

你可以在 README 中看到支持的语言和主题的完整列表：<https://github.com/getzola/giallo?tab=readme-ov-file#built-in>

如果不支持你想要高亮的主题或语言，你可以找到 JSON 语法文件和 JSON 主题文件，将它们复制到你站点的某个位置，并通过 `[markdown.highlighting]` section 中的 `extra_grammars` 和 `extra_themes` 从配置中加载它们。
你可以在 https://textmate-grammars-themes.netlify.app/ 查看支持的主题列表。

在任何情况下，你需要将以下 CSS 添加到你的站点 CSS 中，以便正确显示：

```css
.giallo-l {
    display: inline-block;
    min-height: 1lh;
    width: 100%;
}
.giallo-ln {
    display: inline-block;
    user-select: none;
    margin-right: 0.4em;
    padding: 0.4em;
    min-width: 3ch;
    text-align: right;
    opacity: 0.8;
}
```

## 主题选择

你可以选择使用单个主题或浅色/深色主题。

如果你想要单个主题，请使用配置的 `[markdown.highlighting]` section 中的 `theme` 键。

如果你想要双重主题，请使用 `light_theme` 和 `dark_theme` 键：

```toml
light_theme = "github-light"                                                                                     
dark_theme = "github-dark"
```

## 渲染样式

默认渲染样式是 `inline`，这意味着颜色直接设置在具有十六进制值的 `<span>` 元素上，例如单个主题的 `<span style="color: #83A598;">base_url</span>` 和双重主题的 `<span style="color: light-dark(#076678, #83A598);">base_url</span>`。[light-dark()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark) CSS 函数将自动使用用户的首选配色方案，无法从 JS 覆盖它。

如果你想要一个浅色/深色主题切换按钮或有禁止内联样式的规则，你可以将 `markdown.highlighting.style` 设置为 `class`，以便渲染器改用 CSS 类，并为静态文件夹中的每个主题生成一个 CSS 文件，如下所示：

- 单个主题 -> `giallo.css`
- 双重主题：浅色 -> `giallo-light.css`, 深色 -> `giallo-dark.css`

HTML 将类似于 `<span class="z-support z-type z-property-name z-css">  user-select</span>`。

然后你可以像这样支持浅色和深色模式：

```css
@import url("giallo-dark.css") (prefers-color-scheme: dark);
@import url("giallo-light.css") (prefers-color-scheme: light);
```

或者，你可以在基本模板中引用样式表以减少请求链：

```html
<head>
  <!-- Other content -->
  <link id="giallo-dark" rel="stylesheet" type="text/css" href="/giallo-dark.css" media="(prefers-color-scheme: dark)" />
  <link id="giallo-light" rel="stylesheet" type="text/css" href="/giallo-light.css" media="(prefers-color-scheme: light)" />
</head>
```

## 标注 (Annotations)

你可以使用额外的注释来定制代码块的显示方式：

- `linenos` 启用行号。

````
```rust,linenos
use highlighter::highlight;
let code = "...";
highlight(code);
```
````

- `linenostart` 指定第一行的编号（默认为 1）
  
````
```rust,linenos,linenostart=20
use highlighter::highlight;
let code = "...";
highlight(code);
```
````

- `hl_lines` 高亮行。你必须指定要高亮的行的包含范围列表，由 ` ` (空格) 分隔。范围是 1 索引的，`linenostart` 不会影响这些值，它总是指代码块行号。
  
````
```rust,hl_lines=1 3-5 9
use highlighter::highlight;
let code = "...";
highlight(code);
```
````

- `hide_lines` 隐藏行。你必须指定要隐藏的行的包含范围列表，由 ` ` (空格) 分隔。范围是 1 索引的。

````
```rust,hide_lines=1-2
use highlighter::highlight;
let code = "...";
highlight(code);
```
````

- `name` 指定代码块关联的名称。
  
````
```rust,name=mod.rs
use highlighter::highlight;
let code = "...";
highlight(code);
```
````

这是一个使用了所有选项的示例：`scss, linenos, linenostart=10, hl_lines=3-4 8-9, hide_lines=2 7`。

```scss, linenos, linenostart=10, hl_lines=3-4 8-9, hide_lines=2 7
pre mark {
  // If you want your highlights to take the full width
  display: block;
  color: currentcolor;
}
pre table td:nth-of-type(1) {
  // Select a colour matching your theme
  color: #6b6b6b;
  font-style: italic;
}
```

第 2 行和第 7 行是注释，在最终输出中不显示。
