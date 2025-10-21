---
layout: two-cols
layoutClass: gap-4
---

## 同步示例

```cpp {all|1-2|4-7|9-12}
// 自动类型推导
auto x = 5;              // int
auto y = 3.14;           // double

// 复杂类型简化
map<string, vector<int>> m;
auto it = m.begin();     // 代替复杂迭代器类型

// 函数返回值
auto add(int a, int b) {
    return a + b;        // 返回 int
}
```

::right::

<v-click at="0">

### 类型推导
<div class="visual-box">
编译期自动推导类型<br>
简化代码，减少冗余
</div>

</v-click>

<v-click at="1">

### 使用场景
<div class="visual-box">
✓ 复杂类型（迭代器、模板）<br>
✓ Lambda 表达式
</div>

</v-click>

<v-click at="2">

### 引用与修饰符
<div class="visual-box">
<code>auto</code>: 值类型<br>
<code>auto&</code>: 引用
</div>

</v-click>

---
