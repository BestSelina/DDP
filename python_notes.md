# python learning notes：
[TOC]

## 变量和简单数据类型
### 注释：每行开头加上`#`或用`"""`或`'''`，比如：

    ```
    '''
    这是个注释
    '''
    ```
    
    - 好的注释：
        - Clarity: Comments should clarify the code, not complicate it. They are best used to explain the ***why***, not the how.

        - Avoid Overuse: ***Don’t state the obvious*** in comments; write ***self-explanatory code*** as much as possible

        - ==不懂，待找一些例子==Code Documentation: For larger projects, use comments for documentation. Python also supports docstrings (triple-quoted strings) that can be used to document modules, classes, functions, and methods.
### 变量：直接赋值，不用给出数据类型。
命名规则：以大小写字母或_开头，除第一个外，数字可以在任何位置。
好的变量名字：`lower_case_with_underscores`
常量的不变是人默认的，尽管实际上是可以变的，大写字母加_
**惊喜之处**：
```python
x, y, z = 1, 2, 3
```
==特别用法==：
```python
x, y = y, x # 交换x和y的值
```
### 字符串：被`'`或`"`或`'''`或`"""`包裹
#### 操作符：连接，重复，取字符，切割。
```python
# 连接，直接用+
name = "Rose"
x = "Hello" + "," + name + "!" # Hello,Rose!

# 重复，用*
repeat_name = name * 3 # RoseRoseRose

# 取字符，用x[num]
get_num = name[0] # R

# 分割，用[start_num:end_num]，取的是索引start_num开始到end_num-1的字符
sub_name = name[1:3] # os
```
==需要理解==字符串的不可变性，感觉是字符串本身，是不可以改变的，比如不能改变字符串的某一个字符的值。可以改变的是名字指向的地方。

> Python中的六个数据类型。不可变的：数字，字符串，元组；可变的：列表，字典，集合。
不可变数据类型：当变量的值改变，对应的内存地址也会改变。
可变数据类型：当变量的值改变，对应的内存地址不会改变。

#### string函数：

```python
# upper()全部转大写，lower()全部转小写。
name = "Rose"
upper_name = name.upper() # ROSE
lower_name = name.lower() # rose

# strip()去除字符串头尾的空格，\t，\n，\r（只能头尾），也可以去除指定字符，eg.str.strip("0")。
whitespace_name = "  Rose  \t \n \r"
stripped_name = whitespace_name.strip() # Rose

# find()找到子字符串，replace()替换字符串的一部分
name.find("os") # 1
new_name = name.replace("os", "osi") # Rosie

# split()切割字符串成list，join()拼接字符串，""内是什么就以什么连接，没有就直接拼在一起；是空格，" "，就以空格连接；是","，就以,连接。
name_string = "Rose, Jennie, Jisoo, Lisa"
name_list = name_string.split(", ") # ['Rose', 'Jennie', 'Jisoo', 'Lisa']
name_new_string = " ".join(name_list) # Rose Jennie Jisoo Lisa
```

#### 在字符串中插入变量（三个方法依次进阶）：
1. Old Style String Formatting (% Operator)-原始方法：字符串中`%s`等代替变量的位置，然后最后要加上`% (,)`
```python
name = "Rose"
age = 27
print("Hello, %s. You are %d years old." % (name, age)) # Hello, Rose. You are 27 years old.
```
2. The str.format() Method：用`{}`代替变量的位置，然后最后加上`.format(,)`
==You can use indexes or keywords in the placeholders to specify the order or specific variables to format.==
```python
print("Hello, {}. You are {} years old." .format(name, age)) # Hello, Rose. You are 27 years old.
```
3. Formatted String Literals (F-strings)：f或F引导，然后字符串中用`{变量}`。
***The expressions inside the braces are evaluated at runtime, which allows embedding of variables, expressions, and even function calls.***
```python
print(f"Hello, {name}. You are {age} years old.") # Hello, Rose. You are 27 years old.
print(f"1 + 1 = { 1 + 1 }") # 1 + 1 = 2
print(f"upper name is {name.upper()}") # upper name is ROSE
```

#### 常见的语法错误：结尾不加"或'

#### 转义符：
##### `\`加上想要的字符：`\n`, `\t`, `\\`, `\'`, `\"`, `\r`, `\b`, `\f`...
```python
print("Hello\tworld!\npath: \"C:\\Users\\Username.\"")
# Hello   world!
# path: "C:\Users\Username."
```
##### 用`r`来忽略字符串中的转义字符：
```python
print(r"C:\Users\Username") # C:\Users\Username
```
##### python 3默认支持Unicode

### 数字
#### int：正负数和0
#### float：有小数点的，也可以科学计数法。
#### 算数运算：+, -, *, / (**结果是浮点数**), // (整除，结果是整数), % （取余数）, ** （幂）
```python
print(7/3, 7//3, 7 % 3, 3 ** 4) # 2.3333333333333335 2 1 81
```
#### 隐式类型转换：整数和浮点数计算时，自动将整数转成浮点数，结果也就是浮点数
除法的结果永远是浮点数，哪怕能整除，结果也是浮点数。
#### 对于长数字，可以用下划线
```python
billion = 1_000_000_000
```
#### 数字的函数
```python
# round()，将浮点数舍入到最接近的整数或小数位数。
print(round(3.14159), round(3.14159, 1), round(3.14159, 2)) # 3 3.1 3.14

# int()，将值转换为整数，注意是直接截断小数部分。
print(int(8.999)) # 8

# float()，将值转换为浮点数。
print(float(8)) # 8.0

# abs()，返回数字的绝对值。
print(abs(-0.001)) # 0.001
```
进阶的，有库：`math`, `statistics`, `random`。

### 输入和输出
#### print()
可以一次性打印多个值：在`print()`中用`,`隔开，打印时每个值之间有空格。空格可以改成别的，用`sep`参数。
可以用之前提到的f-strings等方法和连接方法打印。
每个`print()`另起一行来打印。可以改，用`end`参数。
```python
x = 10
print("The value of x is", x) # The value of x is 10
print("Hello", "World", sep="-", end="!")
print(" This is on the same line.") # Hello-World! This is on the same line.
```
#### input()
***它返回的结果是个字符串***
()中是显示给用户的信息
可以用`try-except`来处理意外的输入格式。

### 类型转换（显式）
常用类型转换函数：
`str()`：转成字符串
`int()`：转成整数
`float()`：转成浮点数
`bool()`：转成布尔值（true or false）
`list()`：转成list，对于字符串，tuple，range等时。
`tuple()`：转成tuple
`set()`：转成set
`dict()`：转成字典

## 条件和控制流
### 布尔值
