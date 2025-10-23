---
layout: section
class: text-center
transition: slide-left
---

# 三、STL 算法

标准模板库算法  
高效 · 通用 · 强大

---
layout: two-cols
layoutClass: gap-4
---

## 迭代器 (Iterator)

```cpp {all|all|all|all}
#include <algorithm>

// 获取迭代器
vector<int> v = {1, 2, 3, 4, 5};
auto it = v.begin();  // 指向第一个元素
auto end = v.end();   // 指向最后一个元素之后

// 遍历容器
for (auto it = v.begin(); it != v.end(); ++it) {
    cout << *it << " ";
}

// 使用迭代器范围
sort(v.begin(), v.end());
reverse(v.begin(), v.end());

// 迭代器运算
auto it2 = v.begin() + 3;  // 随机访问迭代器
++it;   // 前进一个位置
--it;   // 后退一个位置
```

::right::

<v>

### 什么是迭代器

类似指针的对象，用于遍历容器中的元素

- 提供通用访问方式
- 隐藏底层实现细节
- 统一操作不同容器

</v>

<v>

### 迭代器类型

**输入/输出迭代器**：只读/只写  
**前向迭代器**：读写 + 前进遍历  
**双向迭代器**：前向 + 后退  
**随机访问迭代器**：双向 + 直接访问

</v>

<v>

### STL 容器支持

`vector`/`deque`: 随机访问  
  
`list`/`set`/`map`: 双向  

`stack`/`queue`: 不支持

</v>

<v>

### ⚠️ 注意事项

修改容器（增删元素）时，迭代器可能失效

- `vector` 动态扩容会使迭代器失效
- 应重新获取迭代器

</v>

---
layout: two-cols
layoutClass: gap-4
---

## Lambda 表达式

```cpp {all|1-4|6-9|11-14|16-}
// 基本语法
auto add = [](int a, int b) -> int {
    return a + b;
};

// 捕获外部变量
int x = 10;
auto f1 = [x]() { return x; };      // 按值捕获
auto f2 = [&x]() { x++; };           // 按引用捕获

// 在算法中使用
vector<int> v = {5, 2, 8, 1, 9};
sort(v.begin(), v.end(), 
     [](int a, int b) { return a > b; });  // 降序

// 复杂捕获
int y = 20;
auto f3 = [x, &y]() {    // x按值，y按引用
    return x + y;
};
auto f4 = [=]() {};      // 全部按值捕获
auto f5 = [&]() {};      // 全部按引用捕获
```

::right::

<v>

### 语法结构

```cpp
[capture](parameters) -> return_type {
    // function body
}
```

</v>

<v>

### 捕获列表

`[]`: 不捕获  
`[=]`: 按值捕获全部  
`[&]`: 按引用捕获全部  
`[x]`: 按值捕获 x  
`[&x]`: 按引用捕获 x  
`[x, &y]`: 混合捕获

</v>

<v>

### 优势

✓ 简洁，避免命名函数  
✓ 可访问外部变量  
✓ 局部使用，逻辑清晰

</v>

<v>

### 使用场景

- 自定义排序规则
- 回调函数
- 算法谓词

</v>

---
layout: two-cols
layoutClass: gap-4
---

## sort / stable_sort

```cpp {all|3-4|6-7|9-|all}
#include <algorithm>

int a[] = {0, 2, 6, 8, 4, 5, 1, 4, 6, 2, 4, 9};
sort(a + 1, a + 6);  // 排序 [1, 6) 区间

// 降序排序
sort(a, a + 10, greater<>{});

// 自定义结构体排序
struct Student {
    string name;
    int score;
};
vector<Student> students = {
    {"Alice", 90}, {"Bob", 85}, {"Carol", 90}
};

// 按分数降序
sort(students.begin(), students.end(),
     [](const Student& a, const Student& b) {
         return a.score > b.score;
     });

// 稳定排序（保持相对顺序）
stable_sort(students.begin(), students.end(),
            [](const Student& a, const Student& b) {
                return a.score > b.score;
            });
```

::right::

<v>

### 函数原型

```cpp
sort(begin, end, cmp);
stable_sort(begin, end, cmp);
```

- `begin/end`: 迭代器范围
- `cmp`: 比较函数（可选，默认升序排序）

`O(n log n)`

</v>
<v></v>
<v></v>
<v>

### sort vs stable_sort

**sort**
- 不保证稳定性
- 速度更快

**stable_sort**
- 保证相等元素的相对顺序
- 略慢，但更可预测

</v>

---
layout: two-cols
layoutClass: gap-4
---

## lower_bound / upper_bound

```cpp {all|1-2|4-10|12-15}
vector<int> v = {1, 1, 4, 4, 4, 5, 5};
sort(v.begin(), v.end());  // 必须先排序

// lower_bound: 第一个 >= val 的位置
auto it1 = lower_bound(v.begin(), v.end(), 4);
cout << "lower: " << (it1 - v.begin());  // 输出 2

// upper_bound: 第一个 > val 的位置
auto it2 = upper_bound(v.begin(), v.end(), 4);
cout << "upper: " << (it2 - v.begin());  // 输出 5

// 计算某值出现次数
int cnt = upper_bound(v.begin(), v.end(), 4) 
        - lower_bound(v.begin(), v.end(), 4);
cout << "count: " << cnt;  // 输出 3
```

::right::

<v>

`O(log n)` - 二分查找

> 先排序！

返回迭代器（或指针）

- 找到：指向目标位置
- 未找到：指向插入位置


| 函数 | 行为 |
|------|---------|
| `lower_bound` | 第一个 ≥ val |
| `upper_bound` | 第一个 > val |

</v>


---
layout: two-cols
layoutClass: gap-4
---

## 其他常用算法

<v>

```cpp
// find: 查找元素
vector<int> v = {1, 2, 3, 4, 5};
auto it = find(v.begin(), v.end(), 3);
if (it != v.end()) 
    cout << "找到: " << *it;
```

</v>

<v>

```cpp
// reverse: 反转序列
reverse(v.begin(), v.end());
// v = {5, 4, 3, 2, 1}
```

</v>

<v>

```cpp
// unique: 去重（需先排序）
vector<int> v2 = {1, 1, 2, 2, 3, 3};
sort(v2.begin(), v2.end());
v2.erase(unique(v2.begin(), v2.end()), 
         v2.end());
// v2 = {1, 2, 3}
```

</v>

<v>

```cpp
// count: 计数
vector<int> v3 = {1, 2, 3, 2, 2};
int cnt = count(v3.begin(), v3.end(), 2);
// cnt = 3
```

</v>

<v>

```cpp
// accumulate: 求和
#include <numeric>
vector<int> v4 = {1, 2, 3, 4, 5};
int sum = accumulate(v4.begin(), v4.end(), 0);
// sum = 15

// 自定义累积操作
int product = accumulate(v4.begin(), v4.end(), 1,
    [](int a, int b) { return a * b; });
// product = 120
```

</v>

::right::

<v>

### find

线性查找，`O(n)`

返回指向第一个匹配元素的迭代器

- 找到：指向元素
- 未找到：返回 `end()`

</v>

<v>

### reverse

原地反转序列，`O(n)`

直接修改容器内容

常用于反转字符串、数组

</v>

<v>

### unique

移除**连续**的重复元素，`O(n)`

⚠️ **必须先排序**才能完全去重

返回新的逻辑末尾，配合 `erase` 删除

</v>

<v>

### count

统计值出现次数，`O(n)`

遍历整个范围计数

适用于任何容器

</v>

<v>

### accumulate

累积运算，`O(n)`

需要 `#include <numeric>`

- 默认：求和
- 可自定义：乘积、最大值等

第三个参数是初始值

</v>