---
layout: section
class: text-center
---

# 三、STL 算法与迭代器

15 分钟 · 高效算法库应用

---
layout: two-cols
layoutClass: gap-4
---

## sort 排序



```cpp {all|1-3|5-9|11-17}
// 基本排序
vector<int> v = {3, 1, 4, 1, 5};
sort(v.begin(), v.end());  // 1, 1, 3, 4, 5

// 降序排序
sort(v.begin(), v.end(), greater<int>());
// 5, 4, 3, 1, 1

// Lambda 自定义排序
vector<pair<int, int>> pairs = {{1,2}, {1,1}, {2,1}};
sort(pairs.begin(), pairs.end(), 
    [](auto& a, auto& b) {
        if (a.first != b.first)
            return a.first < b.first;   // 第一关键字
        return a.second < b.second;     // 第二关键字
    }
);
```

::right::

<v-clicks>

### 排序特性
<div class="visual-box">
时间复杂度: O(n log n)<br>
不稳定排序（可能改变相等元素顺序）<br>
内省排序（快排+堆排序）
</div>

### stable_sort
<div class="visual-box">
稳定排序<br>
保持相等元素的相对顺序<br>
时间复杂度: O(n log n)
</div>

### ⚠️ 严格弱序
<div class="visual-box highlight">
比较函数必须满足:<br>
• 反对称性<br>
• 传递性<br>
相等时返回 <code>false</code>
</div>

</v-clicks>

---
layout: two-cols
layoutClass: gap-4
---

## 二分查找



```cpp {all|1-5|7-11|13-18}
// lower_bound: 第一个 >= x
vector<int> v = {1, 2, 2, 3, 4};
auto it = lower_bound(v.begin(), v.end(), 2);
int pos = it - v.begin();  // 1
// v[pos] = 2 (第一个 >= 2)

// upper_bound: 第一个 > x
it = upper_bound(v.begin(), v.end(), 2);
pos = it - v.begin();  // 3
// v[pos] = 3 (第一个 > 2)

// 查找区间
auto lb = lower_bound(v.begin(), v.end(), 2);
auto ub = upper_bound(v.begin(), v.end(), 2);
int count = ub - lb;  // 2 个
// [lb, ub) 是所有等于 2 的元素
```

::right::

<v-clicks>

### lower_bound
<div class="visual-box">
返回第一个 <strong>≥ x</strong> 的位置<br>
时间复杂度: O(log n)<br>
<strong>需要有序序列</strong>
</div>

### upper_bound
<div class="visual-box">
返回第一个 <strong>> x</strong> 的位置<br>
时间复杂度: O(log n)
</div>

### 可视化
<div class="visual-box">
<code>v: [1, 2, 2, 3, 4]</code><br>
<code>lower_bound(2): ↑</code><br>
<code>&nbsp;&nbsp;&nbsp;[1, <strong>2</strong>, 2, 3, 4]</code><br>
<code>upper_bound(2):&nbsp;&nbsp;&nbsp;&nbsp;↑</code><br>
<code>&nbsp;&nbsp;&nbsp;[1, 2, 2, <strong>3</strong>, 4]</code>
</div>

</v-clicks>

---
layout: two-cols
layoutClass: gap-4
---

## 迭代器



```cpp {all|1-5|7-11|13-17}
// 迭代器遍历
vector<int> v = {1, 2, 3, 4, 5};
for (auto it = v.begin(); it != v.end(); ++it) {
    cout << *it << " ";
}

// 迭代器运算
auto it = v.begin();
it += 2;          // 前进 2 步
int dist = v.end() - v.begin();  // 距离

// 反向迭代器
for (auto it = v.rbegin(); it != v.rend(); ++it) {
    cout << *it << " ";  // 5 4 3 2 1
}
```

::right::

<v-clicks>

### 迭代器分类
<div class="visual-box">
• 输入迭代器: 只读，单次遍历<br>
• 输出迭代器: 只写<br>
• 前向迭代器: 可多次遍历<br>
• 双向迭代器: 可前后移动<br>
• 随机访问: 可跳跃访问
</div>

### 容器迭代器类型
<div class="visual-box">
<code>vector/deque/array</code>: 随机访问<br>
<code>list</code>: 双向<br>
<code>set/map</code>: 双向<br>
<code>forward_list</code>: 前向
</div>

</v-clicks>

---
layout: two-cols
layoutClass: gap-4
---

## 查找算法



```cpp {all|1-4|6-9|11-14|16-19}
// find - 查找元素
vector<int> v = {1, 2, 3, 4, 5};
auto it = find(v.begin(), v.end(), 3);
if (it != v.end()) { }  // 找到

// count - 计数
int cnt = count(v.begin(), v.end(), 3);
// cnt = 1

// find_if - 条件查找
auto it2 = find_if(v.begin(), v.end(), 
    [](int x) { return x > 3; }
);
// *it2 = 4

// binary_search - 二分查找（返回 bool）
bool found = binary_search(v.begin(), v.end(), 3);
```

::right::

<v-clicks>

### 线性查找
<div class="visual-box">
<code>find(begin, end, value)</code><br>
<code>find_if(begin, end, pred)</code><br>
时间复杂度: O(n)
</div>

### 计数
<div class="visual-box">
<code>count(begin, end, value)</code><br>
<code>count_if(begin, end, pred)</code><br>
时间复杂度: O(n)
</div>

### 二分查找
<div class="visual-box">
<code>binary_search()</code>: 返回 bool<br>
<code>lower_bound()</code>: 返回位置<br>
<code>upper_bound()</code>: 返回位置<br>
<strong>需要有序</strong>，O(log n)
</div>

</v-clicks>

---
layout: two-cols
layoutClass: gap-4
---

## 修改算法



```cpp {all|1-4|6-9|11-15|17-20}
// reverse - 反转
vector<int> v = {1, 2, 3, 4, 5};
reverse(v.begin(), v.end());
// v: 5, 4, 3, 2, 1

// unique - 去重（需要先排序）
v = {1, 1, 2, 2, 3};
auto last = unique(v.begin(), v.end());
v.erase(last, v.end());  // v: 1, 2, 3

// fill - 填充
fill(v.begin(), v.end(), 0);
// v: 0, 0, 0

// rotate - 旋转
v = {1, 2, 3, 4, 5};
rotate(v.begin(), v.begin() + 2, v.end());
// v: 3, 4, 5, 1, 2
```

::right::

<v-clicks>

### 序列操作
<div class="visual-box">
<code>reverse()</code>: 反转<br>
<code>rotate()</code>: 旋转<br>
<code>fill()</code>: 填充<br>
<code>swap()</code>: 交换
</div>

### unique 去重
<div class="visual-box highlight">
⚠️ 只移除<strong>连续</strong>重复元素<br>
返回新逻辑末尾<br>
需要配合 <code>erase</code><br>
<strong>通常先 sort</strong>
</div>

### 使用示例
<div class="visual-box">
<code>sort(v.begin(), v.end());</code><br>
<code>v.erase(unique(v.begin(), v.end()), v.end());</code>
</div>

</v-clicks>

---
layout: two-cols
layoutClass: gap-4
---

## 数值算法



```cpp {all|1-5|7-11|13-17}
// accumulate - 求和
#include <numeric>
vector<int> v = {1, 2, 3, 4, 5};
int sum = accumulate(v.begin(), v.end(), 0);
// sum = 15

// accumulate - 自定义操作
int product = accumulate(v.begin(), v.end(), 1,
    [](int a, int b) { return a * b; }
);
// product = 120

// min/max_element - 最值
auto minIt = min_element(v.begin(), v.end());
auto maxIt = max_element(v.begin(), v.end());
int minVal = *minIt;  // 1
int maxVal = *maxIt;  // 5
```

::right::

<v-clicks>

### 数值算法
<div class="visual-box">
需要 <code>#include &lt;numeric&gt;</code><br>
<code>accumulate()</code>: 累积<br>
<code>partial_sum()</code>: 前缀和<br>
<code>adjacent_difference()</code>: 差分
</div>

### 最值查找
<div class="visual-box">
<code>min_element()</code><br>
<code>max_element()</code><br>
<code>minmax_element()</code><br>
返回<strong>迭代器</strong>
</div>

### accumulate 用法
<div class="visual-box">
初始值很重要！<br>
<code>0</code>: 求和<br>
<code>1</code>: 求积
</div>

</v-clicks>

---
layout: two-cols
layoutClass: gap-4
---

## 算法与容器配合



```cpp {all|1-6|8-13|15-20}
// begin/end 辅助函数
vector<int> v = {3, 1, 4, 1, 5};
sort(begin(v), end(v));

// 数组也可用
int arr[] = {3, 1, 4, 1, 5};
sort(begin(arr), end(arr));

// 范围算法（C++20）
#include <ranges>
namespace rng = std::ranges;
rng::sort(v);
rng::reverse(v);

// all_of / any_of / none_of
bool all = all_of(v.begin(), v.end(), 
    [](int x) { return x > 0; }
);
```

::right::

<v-clicks>

### begin/end 函数
<div class="visual-box">
统一接口<br>
<code>std::begin() / std::end()</code><br>
适用于数组、容器
</div>

### 逻辑判断
<div class="visual-box">
<code>all_of()</code>: 全部满足<br>
<code>any_of()</code>: 任一满足<br>
<code>none_of()</code>: 全不满足
</div>

### C++20 Ranges
<div class="visual-box">
<code>std::ranges::sort(v)</code><br>
更简洁的语法<br>
视图（惰性计算）
</div>

</v-clicks>

---
layout: center
class: text-center
---

## 第三部分完成

STL 算法与迭代器 ✓

下一部分：语言进阶特性
