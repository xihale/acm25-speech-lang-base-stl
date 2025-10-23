---
layout: section
class: text-center
transition: slide-left
---

# 四、语言进阶特性

现代 C++ 特性  
起点 · 重新定义

---
layout: two-cols
layoutClass: gap-4
---

## auto 类型推导


```cpp {all|1-5|6-10|12-15|17-}
// 自动类型推导
auto x = 5;                         // int
auto y = 3.14;                      // double
auto s = "Hello";                   // const char*
auto v = vector(5, vector(5, 0));   // vector<vector<int>>

// 复杂类型简化
map<string, vector<int>> m;
auto it = m.begin();     // 代替复杂迭代器类型
auto λ = []() -> void {};

// 函数返回值
auto add(int a, int b) -> int {
    return a + b;        // 返回 int
}

// 注意事项
auto a = {1, 2, 3};      // initializer_list<int>
auto& ref = x;           // 引用
const auto& cref = x;    // 常量引用
auto&& rval = x;         // 右值引用
```

::right::

<v>

- 自动推导  
- 减少冗余  
- 易维护
- 不影响性能  

</v>

<v></v>

<v>

考虑因素

- Lambda
- 可读性

</v>

<v>

返回值 `auto`

- 语法结构统一(语言内外)

> 不建议不写返回类型说明(可读性)

</v>

<v>

### 引用与修饰符

重点关注引用形式而非类型

</v>


---
layout: two-cols
layoutClass: gap-4
---

## Range-based for

```cpp {all|1-12|1-12|14-}
vector<int> v = {1, 2, 3, 4, 5};
for (auto x : v) {
    cout << x << " ";
}

for (auto& x : v) {
    x *= 2;  // 修改原数组
}

for (const auto& x : v) {
    cout << x << " ";  // 避免拷贝
}

map<string, int> m = {{"A", 1}, {"B", 2}};
for (const auto& [key, value] : m) {
    cout << key << ": " << value << endl;
}
```

::right::

<v>

### 语法简化

</v>

<v>

### 引用选择

`auto`: 拷贝（慢）  
`auto&`: 引用（可修改）  
`const auto&`: 常量引用（推荐）

</v>

<v>

### vs 传统循环

✓ 简洁  
✓ 不易出错  
✓ 意图更明确  
✗ 获取索引（需要时用传统循环或者 `zip`）

</v>


---
layout: two-cols
layoutClass: gap-4
---

## 结构化绑定


```cpp {all|1-4|6-12|14-18|20-22|24-}
// pair 拆解
auto p = pair{1, "Alice"}; // pair<int, const char*>
auto [id, name] = p; // id: int, name: const char*
cout << id << " " << name;  // 1 Alice

// tuple 拆解
auto t = tuple{1, "A", 3.14};
auto [n, c, pi] = t;

int _n, _pi;
auto _c = std::get<2>(t);
tie(_n, std::ignore, _pi) = t;

// map 遍历
map<string, int> m = { {"A", 90}, {"B", 85} };
for (const auto& [key, value] : m) {
    cout << key << ": " << value << endl;
}

// array 拆解
auto arr = array{1, 2, 3};
auto [a, b, c] = arr; // a = 1, b = 2, c = 3

// 结构体拆解
struct Point { int x, y; };
Point p = {3, 4};
auto [x, y] = p;
```

::right::

<v>
聚合类型：简单、明确，可见

```cpp
// 数组拆解
int arr[3] = {10, 20, 30};
auto [a, b, c] = arr;  // a=10, b=20, c=30

// 自定义结构体
struct Student {
    string name;
    int age;
    double score;
};
Student s = {"Bob", 22, 95.5};
auto [name, age, score] = s;
```

反例
```cpp
vector<int> v;
```

不能嵌套

```cpp
auto a = {1, {2, 3}};
auto [x, [y, z]] = a;
``` 
</v>

<v>

- 自动推导类型  
- 简化

```cpp
auto p = pair{1, "Alice"};
auto id = p.first; // int
auto name = p.second; // const char*
cout << id << " " << name;  // 1 Alice
```

</v>

<v></v>
<v></v>
<v></v>
<v></v>

---
layout: two-cols
layoutClass: gap-4
---

## Ranges

```cpp {all|3-6|3-6|7-10|11-13|14-}
using rng = std::ranges;

// 基本算法（直接操作容器）
vector<int> v = {5, 2, 8, 1, 9};
rng::sort(v);  // 不需要 begin/end

// 查找
auto it = rng::find(v, 8);
if (it != v.end()) cout << "找到: " << *it;

// 反转
rng::reverse(v);

// 其他常用算法
rng::count(v, 5);          // 统计元素
rng::min(v);               // 最小值
rng::max(v);               // 最大值
```

::right::

<v>

抽象为区间操作
</v>
<v>

### 初始数列

```cpp
{5, 2, 8, 1, 9}
```

</v>

<v>

### 排序后

```cpp
{1, 2, 5, 8, 9}
```

</v>

<v>

### 查找 8

```cpp
{1, 2, 5, [8], 9}
      找到 ↑
```

</v>

<v>

### 反转

```cpp
{9, 8, 5, 2, 1}
```

</v>

<v>

### 统计与查找

```cpp
count(5) = 1
min() = 1
max() = 9
```

</v>

---
layout: two-cols
layoutClass: gap-4
---

## Views - 惰性视图

```cpp {all|3|5-8|10-13|15-16|18-19|21-24}
namespace vw = std::views;

vector<int> v = {1, 2, 3, 4, 5, 6};

// filter
auto even = v | vw::filter([](int x) { 
    return x % 2 == 0; 
});

// transform
auto squared = v | vw::transform([](int x) { 
    return x * x; 
});

// reverse: 反转
auto rev = v | vw::reverse;

auto taken = v | vw::take(3);
auto dropped = v | vw::drop(2);

auto result = v
    | vw::filter([](int x) { return x % 2 == 0; })
    | vw::transform([](int x) { return x * x; })
    | vw::take(2);
```

::right::

<v>
简洁、高效、易读

- 惰性
- pipe 相比函数嵌套
</v>

<v>

```cpp
{1, 2, 3, 4, 5, 6}
```

</v>

<v>

```cpp
{2, 4, 6}
```

</v>

<v>

```cpp
{1, 4, 9, 16, 25, 36}
```

</v>

<v>

```cpp
{6, 5, 4, 3, 2, 1}
```
</v>

<v>
```cpp
taken   = [1, 2, 3];
dropped = [3, 4, 5, 6];
```
</v>

<v>
```cpp
{4, 16}
```
</v>

---
layout: two-cols
layoutClass: gap-4
---

## bit 库

```cpp {all|3-5|7-11|12-17|18-22}
#include <bit>

// 位统计 - popcount
int x = 0b1011;
int cnt = popcount(x);  // 结果: 3

// 前导零与尾随零
int val = 0b1000;  // 0b000...1000 (32位整数)
countl_zero(val);      // 前导零: 28
countr_zero(val);      // 尾随零: 3
bit_width(val);        // 有效位宽: 4

// 幂次对齐
int n = 13;     //    0b01101
bit_floor(n);   // 8  0b01000
bit_ceil(n);    // 16 0b10000
bit_width(n);   // 4  (1101)

// 位旋转
uint8_t byte = 0b11010000;
rotl(byte, 2);  // 0b01000011
rotr(byte, 2);  // 0b00110100
```

::right::

<v></v>
<v></v>
<v></v>
<v></v>
<v>
常用于密码学和哈希算法
</v>


---
layout: two-cols
layoutClass: gap-4
---

## 投影 Projection

```cpp {all|1-5|7-11|13-14}
struct Person {
    string name;
    int age;
};
vector<Person> people = {{"Alice", 25}, {"Bob", 20}};

// 传统写法：需要 lambda
sort(people.begin(), people.end(), 
    [](auto& a, auto& b) {
        return a.age < b.age;
    });

// 投影写法：直接指定成员
ranges::sort(people, {}, &Person::age);
```

::right::

<v>

直接指定要处理的对象

</v>
<v></v>
<v></v>
<v>

### 简洁 + 优雅

少写代码，意图更清晰

`ranges::sort(容器, 比较器, 投影)`

- 比较器: `{}` 默认比较器
- 投影: `&Type::member`

</v>

