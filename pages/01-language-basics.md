---
layout: section
class: text-center
---

# 一、语言基础

55 分钟 · C++ 核心语法与常见陷阱

---
layout: two-cols
layoutClass: gap-4
---

## 头文件与基本结构

```cpp {all|1|3-5|7-8}
#include <bits/stdc++.h>

using namespace std;

int main() {
    // 单行注释
    /* 多行注释 */
    
    return 0;
}
```

::right::

<v-click at="1">

### 万能头文件
<div class="visual-box">
✓ 包含所有标准库<br>
✗ 编译速度较慢<br>
→ 竞赛常用，项目慎用
</div>

</v-click>

<v-click at="2">

### 命名空间
<div class="visual-box">
<code>std::</code> 标准库命名空间<br>
<code>using namespace std;</code> 简化代码
</div>

</v-click>

<v-click at="3">

### main 函数
<div class="visual-box">
返回 0 表示程序正常结束
</div>

</v-click>

---
layout: two-cols
layoutClass: gap-4
---

## 数据类型



```cpp {all|1-3|5-7|9-11}
// 整数类型
int a = 100;           // 4 字节
long long b = 1e18;    // 8 字节

// 浮点类型
double x = 0.1;
long double y = 3.14159265358979323846;

// 字符类型
char ch = 'A';         // ASCII: 65
char digit = '0' + 5;  // '5'
```

::right::

<v-click at="1">

### 整数范围
<div class="visual-box">
<code>int</code>: -2³¹ ~ 2³¹-1<br>
<code>long long</code>: -2⁶³ ~ 2⁶³-1
</div>

</v-click>

<v-click at="2">

### ⚠️ 浮点数陷阱
<div class="visual-box highlight">
<code>0.1 + 0.2 ≠ 0.3</code><br>
精度误差！避免 <code>==</code> 比较
</div>

</v-click>

<v-click at="3">

### ASCII 码
<div class="visual-box">
'A' = 65, 'a' = 97<br>
'0' = 48, '9' = 57
</div>

</v-click>

---
layout: two-cols
layoutClass: gap-4
---

## 类型转换与溢出



```cpp {all|1-3|5-8|10-13}
// 隐式转换
int i = 10;
double d = i / 3;      // 3.0 (整数除法)
double d2 = i / 3.0;   // 3.333...

// unsigned 溢出（定义明确）
unsigned int u = 0;
u = u - 1;             // 4294967295 (循环)

// signed 溢出（未定义行为！）
int x = INT_MAX;
x = x + 1;             // UB! 可能是负数或其他
```

::right::

<v-clicks>

### 隐式转换规则
<div class="visual-box">
整数 / 整数 = 整数<br>
整数 / 浮点 = 浮点
</div>

### unsigned 溢出
<div class="visual-box">
<code>0 - 1 = UINT_MAX</code><br>
<code>UINT_MAX + 1 = 0</code><br>
行为定义明确（循环）
</div>

### ⚠️ signed 溢出
<div class="visual-box highlight">
未定义行为 (UB)<br>
编译器可能优化出错<br>
→ 使用 <code>long long</code>
</div>

</v-clicks>

---
layout: two-cols
layoutClass: gap-4
---

## 未定义行为



```cpp {all|1-3|5-7|9-11}
// 1. signed 溢出
int x = INT_MAX + 1;   // UB!

// 2. 数组越界
int arr[10];
arr[100] = 1;          // UB!

// 3. 空指针解引用
int* p = nullptr;
*p = 10;               // UB!
```

::right::

<v-clicks>

### 什么是 UB？
<div class="visual-box highlight">
Undefined Behavior<br>
未定义行为 = 不可预测<br>
可能崩溃、出错或看似正常
</div>

### 常见 UB 情况
<div class="visual-box">
• signed 整数溢出<br>
• 数组越界访问<br>
• 空指针解引用<br>
• 除以零<br>
• 未初始化变量
</div>

### 如何避免？
<div class="visual-box">
→ 使用 <code>long long</code><br>
→ 检查数组边界<br>
→ 使用前初始化
</div>

</v-clicks>

---
layout: two-cols
layoutClass: gap-4
---

## 输入输出



```cpp {all|1-3|5-8|10-13}
// 基本输入输出
int n;
cin >> n;
cout << n << endl;

// 优化输入输出速度
ios::sync_with_stdio(false);
cin.tie(nullptr);

// endl vs '\n'
cout << "Hello" << endl;  // 刷新缓冲区
cout << "World" << '\n';  // 不刷新（更快）
```

::right::

<v-clicks>

### 流操作
<div class="visual-box">
<code>cin</code>: 标准输入<br>
<code>cout</code>: 标准输出<br>
<code>cerr</code>: 标准错误
</div>

### ⚡ 加速技巧
<div class="visual-box highlight">
<code>sync_with_stdio(false)</code><br>
关闭 C/C++ 同步<br>
<code>cin.tie(nullptr)</code><br>
解除 cin/cout 绑定<br>
→ 输入输出提速 10x
</div>

### endl vs '\n'
<div class="visual-box">
<code>endl</code>: 换行 + 刷新缓冲<br>
<code>'\n'</code>: 仅换行（推荐）
</div>

</v-clicks>

---
layout: two-cols
layoutClass: gap-4
---

## 函数参数求值顺序



```cpp {all|1-4|6-11}
// 未定义的求值顺序
int i = 0;
// UB: i++ 的顺序不确定
printf("%d %d\n", i++, i++);

// 正确做法
int a = i++;
int b = i++;
printf("%d %d\n", a, b);  // 0 1
```

::right::

<v-clicks>

### ⚠️ 无序求值
<div class="visual-box highlight">
函数参数的求值顺序<br>
<strong>未定义</strong><br>
可能从左到右<br>
也可能从右到左
</div>

### 示例分析
<div class="visual-box">
<code>f(i++, i++)</code><br>
可能输出: 0 1<br>
也可能: 1 0<br>
甚至: 0 0 或 1 1
</div>

### 解决方案
<div class="visual-box">
→ 拆分为多个语句<br>
→ 避免副作用表达式
</div>

</v-clicks>

---
layout: two-cols
layoutClass: gap-4
---

## 花式操作



```cpp {all|1-2|4-7|9-12}
#define int long long
signed main() {
    int a = 1e18;  // 实际是 long long
    return 0;
}

// Lambda 表达式 - 临时函数
auto add = [](int a, int b) {
    return a + b;
};
int sum = add(3, 5);  // 8
```

::right::

<v-clicks>

### 竞赛技巧
<div class="visual-box highlight">
<code>#define int long long</code><br>
→ 全局替换 int 为 long long<br>
→ 避免溢出<br>
⚠️ main 要用 <code>signed</code>
</div>

### Lambda 快速映射
<div class="visual-box">
临时创建小函数<br>
语法: <code>[捕获](参数) { 函数体 }</code>
</div>

### 使用场景
<div class="visual-box">
• 排序自定义比较<br>
• 算法回调函数<br>
• 临时逻辑封装
</div>

</v-clicks>

---
layout: two-cols
layoutClass: gap-4
---

## 数学函数



```cpp {all|1-4|6-9|11-14}
// 基本运算
int a = abs(-5);        // 5
double p = pow(2, 10);  // 1024.0
double s = sqrt(16);    // 4.0

// 三角函数
double pi = acos(-1);
double x = sin(pi / 2); // 1.0
double y = cos(0);      // 1.0

// 对数
double ln = log(2.718); // ≈1 (自然对数)
double lg = log10(100); // 2 (常用对数)
```

::right::

<v-clicks>

### 基本函数
<div class="visual-box">
<code>abs(x)</code>: 绝对值<br>
<code>pow(x, y)</code>: x 的 y 次方<br>
<code>sqrt(x)</code>: 平方根
</div>

### 三角函数
<div class="visual-box">
<code>sin / cos / tan</code><br>
<code>asin / acos / atan</code><br>
参数单位: 弧度
</div>

### 对数函数
<div class="visual-box">
<code>log(x)</code>: ln(x)<br>
<code>log10(x)</code>: lg(x)<br>
<code>log2(x)</code>: log₂(x)
</div>

</v-clicks>

---
layout: two-cols
layoutClass: gap-4
---

## 位运算



```cpp {all|1-6|8-11|13-16}
// 基本位运算
int a = 5;      // 0101
int b = 3;      // 0011
int c = a & b;  // 0001 = 1 (AND)
int d = a | b;  // 0111 = 7 (OR)
int e = a ^ b;  // 0110 = 6 (XOR)

// 移位运算
int f = 1 << 3;  // 1000 = 8 (左移)
int g = 8 >> 2;  // 0010 = 2 (右移)
int h = ~a;      // 取反

// 常用技巧
bool isPow2 = (n & (n-1)) == 0;  // 判断 2 的幂
int lowbit = n & (-n);           // 最低位 1
int cnt = __builtin_popcount(n); // 统计 1 的个数
```

::right::

<v-clicks>

### 位运算符
<div class="visual-box">
<code>&</code> 按位与 (AND)<br>
<code>|</code> 按位或 (OR)<br>
<code>^</code> 按位异或 (XOR)<br>
<code>~</code> 按位取反 (NOT)<br>
<code><<</code> 左移 <code>>></code> 右移
</div>

### 快速运算
<div class="visual-box">
<code>n << k</code> = n × 2^k<br>
<code>n >> k</code> = n ÷ 2^k
</div>

### 常用技巧
<div class="visual-box">
<code>n & 1</code>: 判断奇偶<br>
<code>n & (n-1)</code>: 清除最低位 1<br>
<code>__builtin_popcount</code>: 统计 1
</div>

</v-clicks>

---
layout: two-cols
layoutClass: gap-4
---

## 复杂度分析



```cpp {all|1-4|6-9|11-14|16-19}
// O(1) - 常数时间
int x = arr[0];

// O(n) - 线性时间
for (int i = 0; i < n; i++) {
    sum += arr[i];
}

// O(n log n) - 对数线性
sort(arr, arr + n);

// O(n²) - 平方时间
for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++)
        // ...

// O(2^n) - 指数时间（慢！）
// 递归暴力枚举
```

::right::

<v-clicks>

### 时间复杂度
<div class="visual-box">
O(1) < O(log n) < O(n) <<br>
O(n log n) < O(n²) < O(2^n)
</div>

### 常见数据规模
<div class="visual-box">
n ≤ 10: O(n!)<br>
n ≤ 20: O(2^n)<br>
n ≤ 500: O(n³)<br>
n ≤ 5000: O(n²)<br>
n ≤ 10⁶: O(n log n)<br>
n ≤ 10⁸: O(n)
</div>

### 空间复杂度
<div class="visual-box">
数组大小、递归深度<br>
通常要求 ≤ 256MB
</div>

</v-clicks>

---
layout: two-cols
layoutClass: gap-4
---

## 结构体



```cpp {all|1-8|10-13|15-18}
// 定义结构体
struct Point {
    int x, y;
    
    // 成员函数
    double dist() {
        return sqrt(x*x + y*y);
    }
};

// 使用结构体
Point p = {3, 4};
double d = p.dist();  // 5.0

// 作为容器元素
vector<Point> points;
points.push_back({1, 2});
```

::right::

<v-clicks>

### 自定义类型
<div class="visual-box">
组合多个数据成员<br>
可以包含成员函数<br>
类似简化的 class
</div>

### 初始化方式
<div class="visual-box">
<code>Point p = {3, 4};</code><br>
<code>Point p{3, 4};</code><br>
<code>Point p; p.x = 3; p.y = 4;</code>
</div>

### 与 STL 结合
<div class="visual-box">
可作为 vector、set 等元素<br>
需要定义比较操作<br>
重载 <code>operator<</code>
</div>

</v-clicks>

---
layout: two-cols
layoutClass: gap-4
---

## 自定义比较



```cpp {all|1-9|11-16|18-22}
// 方法1: 重载 operator<
struct Point {
    int x, y;
    bool operator<(const Point& p) const {
        if (x != p.x) return x < p.x;
        return y < p.y;
    }
};
```

::right::

<v-clicks>

### 三种方式
<div class="visual-box">
1️⃣ 重载 <code>operator<</code><br>
2️⃣ 自定义比较函数<br>
3️⃣ Lambda 表达式（后面讲）
</div>

### 重载运算符
<div class="visual-box">
用于 set、map、sort<br>
定义默认排序规则<br>
<code>const</code> 修饰符必须加
</div>

### Lambda 比较
<div class="visual-box">
临时、灵活<br>
适合一次性使用<br>
代码更简洁
</div>

</v-clicks>

---
layout: center
class: text-center
---

## 第一部分完成

语言基础 ✓

下一部分：STL 容器
