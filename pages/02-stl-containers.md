---
layout: section
class: text-center
---

# 二、STL 容器

30 分钟 · 标准模板库数据结构

---
layout: two-cols
layoutClass: gap-4
---

## vector 动态数组



```cpp {all|1-2|4-7|9-12|14-17}
// 构造
vector<int> v;
vector<int> v2(10, 0);  // 10 个 0

// 添加元素
v.push_back(1);         // 尾部插入
v.emplace_back(2);      // 原位构造
v.pop_back();           // 删除尾部

// 访问
int x = v[0];           // 下标访问
int y = v.front();      // 第一个
int z = v.back();       // 最后一个

// 大小
int n = v.size();       // 元素个数
int cap = v.capacity(); // 容量
```

::right::

<v-clicks>

### 基本特性
<div class="visual-box">
动态数组，自动扩容<br>
随机访问 O(1)<br>
尾部插入 O(1)*<br>
中间插入 O(n)
</div>

### 容量管理
<div class="visual-box">
<code>size()</code>: 当前元素数<br>
<code>capacity()</code>: 已分配空间<br>
<code>reserve(n)</code>: 预留空间<br>
<code>shrink_to_fit()</code>: 收缩容量
</div>

### ⚠️ 迭代器失效
<div class="visual-box highlight">
插入导致扩容 → 失效<br>
删除元素 → 失效
</div>

</v-clicks>

---
layout: two-cols
layoutClass: gap-4
---

## vector 扩容机制



```cpp {all|1-5|7-12|14-18}
// 扩容示例
vector<int> v;
v.reserve(100);  // 预留 100 容量
// 避免多次扩容

// 迭代器失效示例
vector<int> v = {1, 2, 3};
int& ref = v[0];
v.push_back(4);  // 可能扩容
// ref 可能失效！

// vector<bool> 特殊化
vector<bool> vb(10);
vb[0] = true;
bool& b = vb[0];  // 错误！返回代理对象
// 位压缩存储，不是真正的 bool&
```

::right::

<v-clicks>

### 扩容策略
<div class="visual-box">
通常扩容为原来的 1.5x 或 2x<br>
需要重新分配内存<br>
复制所有元素
</div>

### 性能优化
<div class="visual-box">
<code>reserve()</code> 预留空间<br>
避免多次扩容<br>
<code>emplace_back</code> 原位构造
</div>

### vector&lt;bool&gt; 陷阱
<div class="visual-box highlight">
位压缩存储节省空间<br>
返回代理对象而非引用<br>
无法取地址<br>
→ 考虑用 <code>vector&lt;char&gt;</code>
</div>

</v-clicks>

---
layout: two-cols
layoutClass: gap-4
---

## string 字符串



```cpp {all|1-3|5-8|10-13|15-18}
// 基本操作
string s = "Hello";
s += " World";      // 拼接
s[0] = 'h';         // 修改

// 子串
string sub = s.substr(0, 5);  // "Hello"
string sub2 = s.substr(6);    // "World"

// 查找
int pos = s.find("World");    // 6
if (pos != string::npos) { }  // 找到

// 转换
int num = stoi("123");        // 123
long long ll = stoll("1e18");
double d = stod("3.14");
string str = to_string(456);  // "456"
```

::right::

<v-clicks>

### 常用操作
<div class="visual-box">
<code>substr(pos, len)</code>: 子串<br>
<code>find(str)</code>: 查找<br>
<code>size() / length()</code>: 长度<br>
<code>empty()</code>: 是否为空
</div>

### 类型转换
<div class="visual-box">
<code>stoi / stol / stoll</code><br>
<code>stof / stod</code><br>
<code>to_string()</code>
</div>

### 字符串拼接
<div class="visual-box">
<code>s1 + s2</code><br>
<code>s += "text"</code><br>
<code>s.append(str)</code>
</div>

</v-clicks>

---
layout: two-cols
layoutClass: gap-4
---

---
layout: two-cols
layoutClass: gap-4
---

## array 固定数组



```cpp {all|1-3|5-8|10-13}
// 构造
array<int, 5> arr = {1, 2, 3, 4, 5};

// 访问
int x = arr[0];
int y = arr.at(1);   // 带边界检查
arr[2] = 10;

// 大小
int n = arr.size();  // 5
arr.fill(0);         // 全部填充 0
```

::right::

<v-clicks>

### 特点
<div class="visual-box">
固定大小，编译期确定<br>
栈上分配<br>
无运行时开销
</div>

### vs C 数组
<div class="visual-box">
✓ 知道自己的大小<br>
✓ 支持 STL 算法<br>
✓ 安全的复制/赋值<br>
✓ 可以作为函数返回值
</div>

### 使用场景
<div class="visual-box">
固定大小数据<br>
性能敏感代码<br>
替代 C 数组
</div>

</v-clicks>

---
layout: two-cols
layoutClass: gap-4
---

## set / multiset



```cpp {all|1-5|7-11|13-17}
// set: 元素唯一
set<int> s;
s.insert(3);
s.insert(1);
s.insert(2);  // 自动排序: 1, 2, 3

// 查找
if (s.count(2)) { }          // 存在
auto it = s.find(2);         // 查找迭代器
auto lb = s.lower_bound(2);  // >= 2
auto ub = s.upper_bound(2);  // > 2

// 删除
s.erase(2);              // 删除值
s.erase(s.begin());      // 删除迭代器

// multiset: 允许重复
```

::right::

<v-clicks>

### 基本特性
<div class="visual-box">
红黑树实现<br>
自动排序<br>
插入/删除/查找 O(log n)
</div>

### 查找操作
<div class="visual-box">
<code>count(x)</code>: 是否存在<br>
<code>find(x)</code>: 查找<br>
<code>lower_bound(x)</code>: ≥x<br>
<code>upper_bound(x)</code>: >x
</div>

### set vs multiset
<div class="visual-box">
<code>set</code>: 元素唯一<br>
<code>multiset</code>: 允许重复
</div>

</v-clicks>

---
layout: two-cols
layoutClass: gap-4
---

## map / multimap



```cpp {all|1-5|7-11|13-16}
// 基本操作
map<string, int> m;
m["Alice"] = 90;
m["Bob"] = 85;
m.insert({"Carol", 95});

// 访问
int score = m["Alice"];     // 90
// 不存在则创建默认值
int x = m["David"];         // 0

// 查找
if (m.count("Alice")) { }
auto it = m.find("Bob");
if (it != m.end()) {
    cout << it->second;
}
```

::right::

<v-clicks>

### operator[] 特性
<div class="visual-box highlight">
不存在则<strong>插入</strong>默认值<br>
<code>m["key"]</code> 可能修改容器<br>
查找建议用 <code>find()</code>
</div>

### 遍历
<div class="visual-box">
按键自动排序<br>
<code>for (auto& [k, v] : m)</code><br>
C++17 结构化绑定
</div>

### map vs multimap
<div class="visual-box">
<code>map</code>: 键唯一<br>
<code>multimap</code>: 键可重复<br>
multimap 无 <code>operator[]</code>
</div>

</v-clicks>

---
layout: two-cols
layoutClass: gap-4
---

## unordered_set / unordered_map



```cpp {all|1-5|7-11|13-17}
// 无序集合（哈希表）
unordered_set<int> us;
us.insert(1);
us.insert(2);
// 无序存储

// 无序映射
unordered_map<string, int> um;
um["key"] = 100;

// 性能优化
um.reserve(1000);  // 预留空间
// 避免频繁 rehash

// 装载因子
float lf = um.load_factor();
```

::right::

<v-clicks>

### 哈希表实现
<div class="visual-box">
插入/删除/查找 O(1) 平均<br>
最坏 O(n) (哈希冲突)<br>
<strong>无序</strong>存储
</div>

### vs 有序容器
<div class="visual-box">
✓ 更快的查找<br>
✓ 更快的插入<br>
✗ 无序<br>
✗ 不支持 lower_bound
</div>

### 性能优化
<div class="visual-box">
<code>reserve(n)</code> 预留空间<br>
避免 rehash<br>
装载因子 < 1.0
</div>

</v-clicks>

---
layout: two-cols
layoutClass: gap-4
---

## stack / queue / priority_queue



```cpp {all|1-5|7-11|13-18}
// 栈 (LIFO)
stack<int> st;
st.push(1);
int top = st.top();
st.pop();

// 队列 (FIFO)
queue<int> q;
q.push(1);
int front = q.front();
q.pop();

// 优先队列（大顶堆）
priority_queue<int> pq;
pq.push(3);
pq.push(1);
pq.push(2);
int top = pq.top();  // 3
```

::right::

<v-clicks>

### 容器适配器
<div class="visual-box">
基于其他容器实现<br>
限制接口功能<br>
特定数据结构语义
</div>

### 特点对比
<div class="visual-box">
<code>stack</code>: 后进先出<br>
<code>queue</code>: 先进先出<br>
<code>priority_queue</code>: 优先级
</div>

### 底层容器
<div class="visual-box">
<code>stack</code>: deque (默认)<br>
<code>queue</code>: deque (默认)<br>
<code>priority_queue</code>: vector
</div>

</v-clicks>

---
layout: two-cols
layoutClass: gap-4
---

## deque 双端队列



```cpp {all|1-2|4-9|11-14}
// 构造
deque<int> dq;

// 两端操作
dq.push_front(1);    // 头部插入
dq.push_back(2);     // 尾部插入
dq.pop_front();      // 头部删除
dq.pop_back();       // 尾部删除

// 访问
int x = dq[0];       // 随机访问
int y = dq.front();
int z = dq.back();
```

::right::

<v-clicks>

### 特点
<div class="visual-box">
双端插入/删除 O(1)<br>
随机访问 O(1)<br>
中间插入/删除 O(n)
</div>

### vs vector
<div class="visual-box">
✓ 头部操作高效<br>
✓ 地址相对稳定<br>
✗ 内存不连续<br>
✗ 缓存性能较差
</div>

### 使用场景
<div class="visual-box">
需要两端操作<br>
滑动窗口<br>
队列实现
</div>

</v-clicks>

---
layout: two-cols
layoutClass: gap-4
---

## pair / tuple



```cpp {all|1-4|6-9|11-15|17-20}
// pair - 二元组
pair<int, string> p = {1, "Alice"};
int id = p.first;
string name = p.second;

// make_pair
auto p2 = make_pair(2, "Bob");

// tuple - 多元组
tuple<int, string, double> t = {1, "A", 3.14};
int x = get<0>(t);
string s = get<1>(t);
double d = get<2>(t);

// 结构化绑定 (C++17)
auto [id, name, score] = t;
```

::right::

<v-clicks>

### pair 用途
<div class="visual-box">
返回两个值<br>
map 的元素类型<br>
组合数据
</div>

### tuple 用途
<div class="visual-box">
返回多个值<br>
多关键字排序<br>
<code>get&lt;i&gt;(t)</code> 访问
</div>

### 结构化绑定
<div class="visual-box highlight">
C++17 特性<br>
<code>auto [a, b, c] = tuple</code><br>
简化代码，提高可读性
</div>

</v-clicks>

---
layout: two-cols
layoutClass: gap-4
---

## bitset 位集合



```cpp {all|1-4|6-10|12-16}
// 构造
bitset<8> bs;        // 00000000
bitset<8> bs2(5);    // 00000101
bitset<8> bs3("1010");

// 操作
bs.set(0);           // 设置第 0 位
bs.reset(1);         // 清除第 1 位
bs.flip(2);          // 翻转第 2 位
bool b = bs.test(0); // 测试第 0 位

// 转换与统计
int cnt = bs.count();       // 1 的个数
string str = bs.to_string();
unsigned long n = bs.to_ulong();
```

::right::

<v-clicks>

### 特点
<div class="visual-box">
固定长度位集合<br>
高效位操作<br>
空间压缩
</div>

### 位操作
<div class="visual-box">
<code>set(i)</code>: 置 1<br>
<code>reset(i)</code>: 置 0<br>
<code>flip(i)</code>: 翻转<br>
<code>test(i)</code>: 测试
</div>

### 实用方法
<div class="visual-box">
<code>count()</code>: 统计 1<br>
<code>any() / none() / all()</code><br>
<code>to_string() / to_ulong()</code>
</div>

</v-clicks>

---
layout: two-cols
layoutClass: gap-4
---

## 容器使用技巧



```cpp {all|1-4|6-9|11-14|16-19}
// 初始化列表
vector<int> v = {1, 2, 3, 4, 5};
set<int> s = {3, 1, 2};

// 范围构造
vector<int> v2(v.begin(), v.end());
set<int> s2(v.begin(), v.end());

// auto 和 范围 for
for (auto& x : v) {
    cout << x << " ";
}

// swap 技巧
vector<int> temp;
v.swap(temp);  // 快速清空并释放内存
// 等价于 vector<int>().swap(v);
```

::right::

<v-clicks>

### 初始化
<div class="visual-box">
初始化列表: <code>{...}</code><br>
范围构造: <code>(begin, end)</code><br>
大小构造: <code>(n, value)</code>
</div>

### 遍历
<div class="visual-box">
范围 for: <code>for (auto& x : c)</code><br>
迭代器: <code>for (auto it = ...)</code><br>
索引: <code>for (int i = 0; ...)</code>
</div>

### 性能技巧
<div class="visual-box">
<code>swap</code> 交换容器 O(1)<br>
<code>emplace</code> 原位构造<br>
<code>reserve</code> 预留空间
</div>

</v-clicks>

---
layout: center
class: text-center
---

## 第二部分完成

STL 容器 ✓

下一部分：STL 算法与迭代器
