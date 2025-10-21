---
layout: section
class: text-center
---

# 四、语言进阶特性

30 分钟 · 现代 C++ 特性

---
layout: two-cols
layoutClass: gap-4
---

## auto 类型推导



```cpp {all|1-3|5-8|10-13|15-18}
// 自动类型推导
auto x = 5;              // int
auto y = 3.14;           // double
auto s = "Hello";        // const char*

// 复杂类型简化
map<string, vector<int>> m;
auto it = m.begin();     // 代替复杂迭代器类型

// 函数返回值
auto add(int a, int b) {
    return a + b;        // 返回 int
}

// 注意事项
auto a = {1, 2, 3};      // initializer_list<int>
auto& ref = x;           // 引用
const auto& cref = x;    // 常量引用
```

::right::

<v-clicks>

### 类型推导
<div class="visual-box">
编译期自动推导类型<br>
简化代码，减少冗余<br>
不影响性能
</div>

### 使用场景
<div class="visual-box">
✓ 复杂类型（迭代器、模板）<br>
✓ Lambda 表达式<br>
✓ 范围 for 循环<br>
✗ 降低可读性的场景
</div>

### 引用与修饰符
<div class="visual-box">
<code>auto</code>: 值类型<br>
<code>auto&</code>: 引用<br>
<code>const auto&</code>: 常量引用<br>
<code>auto*</code>: 指针
</div>

</v-clicks>

---
layout: two-cols
layoutClass: gap-4
---

## Range-based for



```cpp {all|1-4|6-9|11-14|16-19}
// 基本用法
vector<int> v = {1, 2, 3, 4, 5};
for (auto x : v) {
    cout << x << " ";
}

// 引用修改
for (auto& x : v) {
    x *= 2;  // 修改原数组
}

// 常量引用（推荐）
for (const auto& x : v) {
    cout << x << " ";  // 避免拷贝
}

// 遍历 map
map<string, int> m = {{"A", 1}, {"B", 2}};
for (const auto& [key, value] : m) {
    cout << key << ": " << value << endl;
}
```

::right::

<v-clicks>

### 语法简化
<div class="visual-box">
<code>for (auto& item : container)</code><br>
自动遍历所有元素<br>
无需手动管理索引/迭代器
</div>

### 引用选择
<div class="visual-box">
<code>auto</code>: 拷贝（慢）<br>
<code>auto&</code>: 引用（可修改）<br>
<code>const auto&</code>: 常量引用（推荐）
</div>

### vs 传统循环
<div class="visual-box">
✓ 代码更简洁<br>
✓ 不易出错<br>
✓ 意图更明确<br>
✗ 无法获取索引（需要时用传统循环）
</div>

</v-clicks>

---
layout: two-cols
layoutClass: gap-4
---

## 结构化绑定



```cpp {all|1-4|6-10|12-17|19-23}
// pair 拆解
pair<int, string> p = {1, "Alice"};
auto [id, name] = p;
cout << id << " " << name;  // 1 Alice

// tuple 拆解
tuple<int, string, double> t = {1, "A", 3.14};
auto [x, y, z] = t;

// map 遍历
map<string, int> m = {{"A", 90}, {"B", 85}};
for (const auto& [key, value] : m) {
    cout << key << ": " << value << endl;
}

// array 拆解
array<int, 3> arr = {1, 2, 3};
auto [a, b, c] = arr;

// 结构体拆解
struct Point { int x, y; };
Point p = {3, 4};
auto [px, py] = p;
```

::right::

<v-clicks>

### C++17 新特性
<div class="visual-box">
从元组类型中提取值<br>
自动推导类型<br>
简化代码
</div>

### 支持的类型
<div class="visual-box">
• <code>pair</code> / <code>tuple</code><br>
• <code>array</code><br>
• 结构体（所有成员 public）<br>
• 实现 get&lt;&gt; 的自定义类型
</div>

### vs std::tie
<div class="visual-box">
<code>tie(x, y) = make_pair(1, 2);</code><br>
需要预先声明变量<br>
结构化绑定更简洁
</div>

</v-clicks>

---
layout: two-cols
layoutClass: gap-4
---

## Lambda 表达式



```cpp {all|1-4|6-10|12-16|18-22}
// 基本语法
auto add = [](int a, int b) {
    return a + b;
};

// 捕获外部变量
int x = 10;
auto f1 = [x]() { return x; };      // 值捕获
auto f2 = [&x]() { x++; };          // 引用捕获
auto f3 = [=]() { };                // 全部值捕获
auto f4 = [&]() { };                // 全部引用捕获

// 排序中使用
vector<int> v = {3, 1, 4, 1, 5};
sort(v.begin(), v.end(), 
    [](int a, int b) { return a > b; }
);

// 复杂 lambda
auto cmp = [](const pair<int,int>& a, const pair<int,int>& b) {
    return a.first < b.first;
};
```

::right::

<v-clicks>

### 语法结构
<div class="visual-box">
<code>[捕获](参数) -> 返回类型 { 函数体 }</code><br>
返回类型可省略（自动推导）
</div>

### 捕获列表
<div class="visual-box">
<code>[]</code>: 不捕获<br>
<code>[x]</code>: 值捕获 x<br>
<code>[&x]</code>: 引用捕获 x<br>
<code>[=]</code>: 值捕获全部<br>
<code>[&]</code>: 引用捕获全部<br>
<code>[=, &x]</code>: 混合
</div>

### 使用场景
<div class="visual-box">
排序、算法回调<br>
临时函数<br>
STL 算法配合
</div>

</v-clicks>

---
layout: two-cols
layoutClass: gap-4
---

## Ranges & Views



```cpp {all|1-6|8-13|15-20}
#include <ranges>
namespace rng = std::ranges;
namespace vw = std::views;

// 基本用法
vector<int> v = {1, 2, 3, 4, 5};
rng::sort(v);
rng::reverse(v);

// Views（惰性计算）
auto even = v | vw::filter([](int x) { return x % 2 == 0; });
auto doubled = even | vw::transform([](int x) { return x * 2; });
for (int x : doubled) { cout << x << " "; }

// 管道操作
auto result = v 
    | vw::filter([](int x) { return x > 2; })
    | vw::transform([](int x) { return x * x; })
    | vw::take(3);
```

::right::

<v-clicks>

### Ranges 算法
<div class="visual-box">
<code>std::ranges::sort</code><br>
<code>std::ranges::find</code><br>
不需要 begin/end<br>
直接传容器
</div>

### Views（视图）
<div class="visual-box">
惰性计算，不创建新容器<br>
可组合、链式操作<br>
高效、零开销
</div>

### 常用 Views
<div class="visual-box">
<code>filter</code>: 过滤<br>
<code>transform</code>: 映射<br>
<code>take</code>: 取前 n 个<br>
<code>drop</code>: 跳过前 n 个
</div>

</v-clicks>

---
layout: two-cols
layoutClass: gap-4
---

## bit 库



```cpp {all|1-4|6-9|11-14|16-19}
#include <bit>

// 统计 1 的个数
int x = 0b1011;  // 11
int cnt = popcount(x);  // 3

// 检测 2 的幂
bool isPow2 = has_single_bit(8);   // true
bool isPow2_2 = has_single_bit(7); // false

// 前导/尾随零
int lz = countl_zero(0b00001000);  // 4
int tz = countr_zero(0b00001000);  // 3

// 2 的幂相关
int floor = bit_floor(13);  // 8 (向下)
int ceil = bit_ceil(13);    // 16 (向上)
int width = bit_width(13);  // 4 (需要的位数)
```

::right::

<v-clicks>

### 位统计
<div class="visual-box">
<code>popcount(x)</code>: 统计 1<br>
<code>countl_zero(x)</code>: 前导 0<br>
<code>countr_zero(x)</code>: 尾随 0<br>
<code>countl_one(x)</code>: 前导 1<br>
<code>countr_one(x)</code>: 尾随 1
</div>

### 2 的幂
<div class="visual-box">
<code>has_single_bit()</code>: 是否 2^n<br>
<code>bit_floor()</code>: ≤ x 的最大 2^n<br>
<code>bit_ceil()</code>: ≥ x 的最小 2^n<br>
<code>bit_width()</code>: 表示 x 需要的位数
</div>

### 位旋转
<div class="visual-box">
<code>rotl(x, k)</code>: 循环左移<br>
<code>rotr(x, k)</code>: 循环右移
</div>

</v-clicks>

---
layout: two-cols
layoutClass: gap-4
---

## 投影 Projection



```cpp {all|1-7|9-15|17-22}
// 传统排序
struct Person {
    string name;
    int age;
};
vector<Person> people = {{"Alice", 25}, {"Bob", 20}};
sort(people.begin(), people.end(), 
    [](const Person& a, const Person& b) {
        return a.age < b.age;
    }
);

// C++20 投影
ranges::sort(people, {}, &Person::age);
// 直接指定按哪个成员排序

// 多个投影
ranges::sort(people, ranges::greater{}, &Person::age);
// 降序排列

// 配合 views
auto names = people | views::transform(&Person::name);
```

::right::

<v-clicks>

### 什么是投影？
<div class="visual-box">
指定排序/比较的"关键字"<br>
简化自定义比较<br>
使用成员指针
</div>

### 语法
<div class="visual-box">
<code>ranges::sort(容器, 比较器, 投影)</code><br>
比较器: <code>{}</code> 默认 less<br>
投影: <code>&Type::member</code>
</div>

### 优势
<div class="visual-box">
✓ 代码更简洁<br>
✓ 意图更明确<br>
✓ 减少 lambda 样板代码<br>
✓ 配合 ranges 强大
</div>

</v-clicks>

---
layout: two-cols
layoutClass: gap-4
---

## 实战技巧



```cpp {all|1-5|7-11|13-17|19-23}
// 快速输入输出
ios::sync_with_stdio(false);
cin.tie(nullptr);

// 避免溢出
#define int long long
signed main() { }

// 容器初始化
vector<int> v(n);  // n 个默认值
vector<int> v(n, x);  // n 个 x

// 去重
sort(v.begin(), v.end());
v.erase(unique(v.begin(), v.end()), v.end());

// 快速幂
auto qpow = [](long long a, long long b, long long mod) {
    long long res = 1;
    for (; b; b >>= 1, a = a * a % mod)
        if (b & 1) res = res * a % mod;
    return res;
};
```

::right::

<v-clicks>

### 竞赛模板
<div class="visual-box">
头文件: <code>bits/stdc++.h</code><br>
快速 IO: <code>sync_with_stdio</code><br>
<code>#define int long long</code>
</div>

### 常用操作
<div class="visual-box">
排序 + 去重<br>
二分查找<br>
前缀和<br>
差分
</div>

### Lambda 工具函数
<div class="visual-box">
快速幂<br>
GCD/LCM<br>
自定义比较<br>
临时映射
</div>

</v-clicks>

---
layout: two-cols
layoutClass: gap-4
---

## 代码风格



```cpp {all|1-6|8-13|15-20}
// 使用 const 引用遍历
for (const auto& item : container) {
    // 避免拷贝
}

// 使用 emplace 而非 push
v.emplace_back(args...);  // 原位构造
// 而非 v.push_back(Type(args...));

// 预留空间
vector<int> v;
v.reserve(n);  // 避免多次扩容

// 结构化绑定
for (const auto& [key, value] : map) {
    // 清晰的变量名
}

// 使用 ranges (C++20)
ranges::sort(v);  // 简洁
```

::right::

<v-clicks>

### 性能优化
<div class="visual-box">
✓ 使用 <code>reserve</code> 预留空间<br>
✓ 使用 <code>emplace</code> 原位构造<br>
✓ 使用 <code>const auto&</code> 避免拷贝<br>
✓ 选择合适的容器
</div>

### 代码可读性
<div class="visual-box">
✓ 结构化绑定<br>
✓ auto 简化类型<br>
✓ 范围 for 循环<br>
✓ Lambda 临时函数
</div>

### 现代 C++ 特性
<div class="visual-box">
优先使用 C++17/20 特性<br>
代码更简洁、更安全<br>
性能不打折扣
</div>

</v-clicks>

---
layout: center
class: text-center
---

## 课程完成！

<div class="mt-8 text-2xl">
✅ 语言基础<br>
✅ STL 容器<br>
✅ STL 算法<br>
✅ 现代 C++ 特性
</div>

<div class="mt-12 text-xl opacity-70">
高效 · 简洁 · 实用
</div>

---
layout: center
class: text-center
---

# 谢谢！

有问题欢迎提问

<div class="mt-8 opacity-50">
ACM C++ 语言基础与 STL
</div>
