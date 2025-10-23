---
layout: section
class: text-center
transition: slide-left
---

# 二、STL 容器

标准模板库容器  
数据结构 · 高效管理

---
layout: two-cols
layoutClass: gap-4
---

## vector 动态数组

```cpp {all|1-2|4-6|8-11|13-16|18-21|23-|all}
#include <vector>
vector<int> a = {1, 3, 5, 6, 8, 4, 3};

// 尾部操作 - O(1)
a.push_back(5);      // 尾部插入
a.pop_back();        // 尾部删除

// 查询操作 - O(1)
int len = a.size();       // 元素个数
int cap = a.capacity();   // 分配容量
bool empty = a.empty();   // 是否为空

// 访问元素 - O(1)
int x = a.front();   // 首元素
int y = a.back();    // 尾元素
cout << a.at(2) << a[2];

// 内存管理
a.reserve(22);       // 预分配容量，避免频繁扩容
a.resize(7);         // 改变大小
a.shrink_to_fit();   // 释放多余空间 - O(n)

// 中间操作 - O(n)
a.insert(a.begin() + 2, -1);  // 插入到a[2]
a.erase(a.begin() + x);       // 删除a[x]
a.clear();                    // 清空
```

::right::

<v>

- 长度可变，自动扩容
- 局部数组开在栈上，vector 开在堆上，限制小
- 不适合随机位置添删操作

ref: `std::hive`

</v>
<v></v>
<v></v>
<v></v>
<v>

使用 `at` 更安全，防止越界

</v>

<v>

扩容：
- 申请 1.5~2 倍空间（取决于编译器实现）
- 移动所有元素
- 释放旧内存

</v>

<v>

**性能陷阱**

中间插入/删除需要大量移动元素

频繁操作考虑其他容器

</v>

<v>

**特殊情况**

`vector<bool>` 是一个基于位压缩实现：
- 节省空间，操作慢
- 无法取地址、引用

替代：`bitset` `vector<int_8>` `deque<bool>`


</v>

<!--
有兴趣可以了解一下 `std::hive`
-->

---
layout: two-cols
layoutClass: gap-4
---

## string 字符串

```cpp {all|1-4|6-8|10-13|15-18|20-22|24-}
#include <string>
string s1;                    // 空字符串
string s2 = "123456789";      
string s3(s2, 2);             // 从第3位开始："3456789"

// 长度和访问
int len = s2.size();          // 或 s2.length()
cout << s2[i];                // 下标访问单个字符

// 字符串拼接与比较
string a1 = "12", a2 = "cd";
string a3 = a1 + a2;          // "12cd"
bool pd = a2 > a3;            // 字典序比较

// 输入输出
cin >> s1;                    // 读到空格/回车
getline(cin, s1);             // 读整行(含空格)
cout << s1;

// 类型转换
int num = stoi("123");        // 字符串 -> 整数
int bnum = stoi("1001", nullptr, 2) // 9

// 修改操作
s1.push_back('a');            // 尾部插入
s1.insert(s1.begin(), 'b');   // 开头插入
s1.erase(pos, len);           // 删除指定范围
s1.clear();                   // 清空
```

::right::

<v>

- 自动管理
- 傻瓜式操作

</v>

<v></v>
<v></v>

<v>

- `+` 拼接字符串
- 字典序比较

</v>

<v>

`cin`: 单词

`getline()`: 句子

</v>

<v>

**类型转换**

`stoi` (`int`)

`stod` (`double`)

`stoll` (`long long`)

支持不同进制解析

> 中间的参数会保存截止地址  
> 1001abc 会在a截止，pos = 4

<br/>

> 末尾参数填 `0`：自动判断进制，不建议

</v>

<v></v>

---
layout: two-cols
layoutClass: gap-4
---

## map 映射

```cpp {all|1-3|5-8|10-13|15-18|20-22|24-|all}
#include <map>
map<int, int> mp;              // int -> int 映射
map<char, string> m;           // char -> string 映射

// 插入和访问
mp[1] = 2;                     // 建立键值对 1 -> 2
m['a'] = "Hello World!";       // 建立键值对 a -> "Hello World!"
mp.insert({2, 6});             // 插入键值对 2 -> 6

// 查找和删除 - O(log n)
auto it = mp.find(1);          // 查找键为1，不存在返回 mp.end()
mp.erase(1);                   // 删除键为1的键值对
int cnt = mp.count(1);         // 键是否存在(返回0或1)

// 查询 - O(1)
int len = mp.size();           // 键值对个数
bool empty = mp.empty();       // 是否为空
mp.clear();                    // 清空所有键值对

// 迭代器 - O(1)
auto a = mp.begin();           // 指向第一个元素
auto b = mp.end();             // 指向最后一个元素+1

// 边界查找 - O(log n)
auto lo = mp.lower_bound(2);   // 键值 >= 2 的第一个元素
auto hi = mp.upper_bound(2);   // 键值 > 2 的第一个元素
cout << lo->first << " " << lo->second;  // 输出键和值
```

::right::

<v>

**键值对映射**

- 类似函数对应关系
- 每个键对应一个值
- 键类型必须可比较大小


内部基于红黑树实现

</v>

<v>

**访问方式**

- `mp[key]` 直接访问/创建
- `find()` 安全查找
- `first` 访问键，`second` 访问值

</v>

<v></v>
<v></v>
<v></v>
<v></v>
<v>

**性能特点**

- 插入/删除/查找：O(log n)
- 空间换时间
- 键唯一(重复键会覆盖)


**注意**

访问不存在的键会自动创建(值为默认值)

用 `find()` 避免意外插入

</v>

---
layout: two-cols
layoutClass: gap-4
---

## tuple 元组

```cpp {all|3-5|7-9|11-18|20-|all}
#include <tuple>

// pair 二元组
pair<string, int> p = make_pair("wang", 1);  // 声明并初始化
int x = p.second;                            // 访问元素

// tuple 元组 - pair 的泛化
tuple<int, int, string> t1(2, 3, "pq");      // 声明三元组并初始化
t1 = make_tuple(1, 1, "Hello");              // 赋值

// 访问元素 - 使用 get<index>
int l1 = get<0>(t1);                         // 获取第一个元素
get<0>(t1) = 1;                              // 修改第一个元素

// 解包 - tie 或结构化绑定 (C++17)
int a, b; string c;
tie(a, b, c) = t1;                           // 依次赋值给变量
auto [xx, yy, zz] = t1;                      // 结构化绑定

// pair 转 tuple
tuple<string, int> t3 {p};                   // pair 转为二元 tuple
```

::right::

<v></v>
<v>

**`pair` 二元组**

- 两个元素的结构体
- `first` 和 `second` 访问 (`tuple` 只能 `get<>()`
- 常与其他容器配合使用

</v>

<v>

**`tuple` 元组**

- `pair` 的泛化版本
- 可封装任意数量、不同类型的对象
- 可用作结构体替代

</v>

<v>

**访问方式**

- `get<index>(tuple)` 获取元素
- `tie()` 解包到变量
- `auto [x,y,z]` 结构化绑定 (C++17)

</v>
<v></v>

<v>

**应用场景**

- 返回多个值
- 临时数据打包
- 替代简单结构体

</v>

---
layout: two-cols
layoutClass: gap-4
---

## stack 栈

```cpp {all}
#include <stack>
stack<int> s;

// 基本操作 - O(1)
s.push(x);            // 入栈
int y = s.top();      // 访问栈顶(不删除)
s.pop();              // 出栈

// 查询 - O(1)
int len = s.size();
bool empty = s.empty();

// 单调栈应用(P5788)
for (int i = 1; i <= n; i++) {
    // 找右边第一个更大的数
    while (!s.empty() && 
           a[i] > s.top()) {
        ans[s.top()] = i;    // 记录答案
        s.pop();
    }
    s.push(i);
}
```

::right::

<v>

**后进先出(LIFO)**

最后进入的元素最先出来

只能操作栈顶元素

**操作限制**

✓ 栈顶：访问、插入、删除  
✗ 无法随机访问  
✗ 遍历需逐个弹出(破坏结构)

</v>

---
layout: two-cols
layoutClass: gap-4
---

## queue 队列

```cpp {all}
#include <queue>
queue<int> q;

// 入队和出队 - O(1)
q.emplace(2);         // 队尾插入, 推荐这种
q.push(2);
q.pop();              // 队首删除

// 访问和查询 - O(1)
int x = q.front();    // 队首元素
int y = q.back();     // 队尾元素
int len = q.size();
bool empty = q.empty();
```

::right::

<v>

**先进先出(FIFO)**

队尾插入，队首删除

模拟排队过程

队首：只能查询和删除
队尾：只能查询和插入

单向流动，无法回退

</v>

---
layout: two-cols
layoutClass: gap-4
---

## deque 双端队列

```cpp {all|1-2|4-6|8-10|12-16|18-|all}
#include <deque>
deque<int> q;

// 两端插入 - O(1)
q.push_back(2);       // 尾部插入
q.push_front(3);      // 头部插入

// 两端删除 - O(1)
q.pop_back();         // 删除队尾
q.pop_front();        // 删除队首

// 访问和查询 - O(1)
int x = q.front();    // 队首元素
int y = q.back();     // 队尾元素
int len = q.size();   // 元素个数
bool empty = q.empty();

// 中间操作 - O(n)
q.erase(q.begin() + 1);          // 删除指定位置
q.erase(q.begin() + l, 
        q.begin() + r);          // 删除区间[l,r)
q.clear();                       // 清空
```

::right::

<v>

**双端操作**

首尾都可以高效插入删除

是 `queue` 的超集

</v>
<v></v>

<v>

**性能特点**

- 两端操作：O(1)
- 随机访问：O(1)
- 中间插删：O(n)

</v>

<v>

**经典应用**

单调队列(滑动窗口)：
```cpp
// 维护窗口最小值
while (!q.empty() && a[i] < q.back())
    q.pop_back();
q.push_back(a[i]);
if (q.front() < i - k + 1)
    q.pop_front();
```

> 例题：P1886

</v>
<v></v>
<v></v>
<v>

**使用场景**

✓ 滑动窗口最值  
✓ 单调队列优化  
✓ 需要两端操作  
✗ 只需单端操作用 `stack`/`queue`

</v>

---
layout: two-cols
layoutClass: gap-4
---

## set 集合

```cpp {all|1-3|5-8|10-13|15-17|19-}
#include <set>
set<int> s;                   // 默认升序
set<int, greater<int>> s2;    // 降序

// 插入和删除 - O(log n)
s.insert(3);                  // 重复元素不会插入
s.erase(3);                   // 删除元素
s.clear();                    // 清空

// 查找 - O(log n)
auto it = s.find(3);          // 找不到返回 s.end()
int cnt = s.count(3);         // 是否存在(返回0或1)

// 边界查找 - O(log n)
auto lo = s.lower_bound(3);   // >= 3 的第一个
auto hi = s.upper_bound(3);   // > 3 的第一个
cout << *lo;                  // 解引用获取值

// multiset：允许重复
multiset<int> ms = {4, 2, 5, 2, 1};
ms.count(2);                  // 返回 2
// 输出顺序：1 2 2 4 5
```

::right::

<v>

基于红黑树实现

插入/删除/查找都是 `O(log n)`

- 元素唯一(自动去重)
- 自动排序(默认升序)
- 不支持下标访问
- 不支持修改元素值

</v>

<v></v>
<v></v>
<v></v>


<v>

**边界查找**

```cpp
lower_bound(x)  // >= x 第一个
upper_bound(x)  // > x 第一个
```

找前驱后继的利器

</v>

<v>

**set vs multiset**

`set`：元素唯一  

`multiset`：允许重复

其他操作完全相同

</v>

<v>

**使用场景**

✓ 动态维护有序集合  
✓ 去重  
✓ 快速查找/插入/删除  
✗ 不适合频繁修改元素值

</v>

---
layout: two-cols
layoutClass: gap-4
---

## array 固定数组

```cpp {all|4-8|10-11|13-|all}
#include <array>
array<int, 110> arr{1, 2, 3, 4};  // 固定大小

// 访问元素
int x = arr[1];       // 不检查越界
int y = arr.at(2);    // 检查越界，抛异常
arr.front() = 4;      // 首元素
arr.back() = 6;       // 尾元素

// 填充
arr.fill(5);          // 所有元素赋值为5

// 比较操作
array<int, 110> b{9, 8, 7};
bool pd = arr < b;    // 字典序比较

// size() 和 empty() 意义不大
// 因为大小固定
```

::right::

<v>

- 性能高
- 提供 STL 容器接口
- 编译期确定大小
- 栈上分配(小数组)
- 不可扩展/收缩
- 零开销封装

</v>

<v>

`arr[i]`：快速但不安全

`arr.at(i)`：安全但略慢

推荐：确定不越界用 `[]`

</v>
<v></v>
<v></v>
<v>

**array vs vector**

`array`：固定大小，栈上

`vector`：动态大小，堆上

`array` 性能更好但不灵活

</v>

---
layout: section
class: text-center
---

# 容器选择指南

根据需求选择最合适的容器

---
layout: two-cols
layoutClass: gap-4
---

## 容器特性对比

| 容器 | 核心特点 | 时间复杂度 |
|------|---------|-----------|
| `vector` | 动态数组 | 随机访问 `O(1)` |
| `string` | 字符串 | 拼接 `O(n)` |
| `deque` | 双端队列 | 两端 `O(1)` |
| `stack` | 栈 | 栈顶 `O(1)` |
| `queue` | 队列 | 队首队尾 `O(1)` |
| `set` | 有序集合 | 查找 O`(log n)` |
| `array` | 固定数组 | 访问 `O(1)` |



---
layout: end
class: text-center
---

# 谢谢

STL 容器 · 高效编程的基石
