# ACM C++ 语言基础与 STL 课程

基于 [Slidev](https://github.com/slidevjs/slidev) 的交互式幻灯片课程。

## 🚀 快速开始

```bash
# 安装依赖
pnpm install
# 或
bun install

# 启动开发服务器
pnpm dev
# 或
bun run dev

# 访问 http://localhost:3030
```

## ✨ 特性

### 左右同步功能

本项目实现了**代码高亮与解释块的完美同步 + 替换显示**：

- **左侧**：代码块使用 `{all|1|3-5|7-8}` 语法，每次点击高亮不同的代码行
- **右侧**：解释块使用 `<v-click at="X" hide="Y">` 精确控制显示和隐藏时机
- **效果**：点击一次，左边跳转到下一个高亮块，右边**前一个解释消失**，**新的解释出现**

### 实现方式

将原来的 `<v-clicks>` 替换为独立的 `<v-click at="X" hide="X+1">`：

```markdown
## 示例

\```cpp {all|1-2|4-5|7-8}
// 第一部分
代码1

// 第二部分
代码2

// 第三部分
代码3
\```

::right::

<v-click at="1" hide="2">
### 解释1
第一部分的说明
</v-click>

<v-click at="2" hide="3">
### 解释2
第二部分的说明
</v-click>

<v-click at="3">
### 解释3
第三部分的说明（最后一个不需要 hide）
</v-click>
```

**关键点**：
- 代码高亮有 N 个状态（包括 `all`）
- 右侧解释块从 `at="1"` 开始（对应第二个状态）
- 每个块添加 `hide="X+1"` 使其在下次点击时消失
- **最后一个块不需要 `hide` 属性**
- 同一时间右侧只显示一个解释块

## 🛠️ 批量转换工具

### 1. 转换 v-clicks 为 v-click at

将 `<v-clicks>` 转换为独立的 `<v-click at="X">`：

```bash
python3 convert_clicks_simple.py pages/your-file.md
```

### 2. 添加 hide 属性（替换显示效果）

自动为所有 `v-click` 添加 `hide` 属性：

```bash
python3 add_hide_attr.py pages/*.md
```

这会让每次点击时，前一个解释块消失，新的解释块出现。

## 📝 编辑幻灯片

编辑 [slides.md](./slides.md) 或 `pages/*.md` 文件来修改内容。

## 📚 了解更多

- [Slidev 文档](https://sli.dev/)
- [Slidev 点击动画](https://sli.dev/guide/animations.html#click-animations)
