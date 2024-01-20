# python learning notes：

1. 注释：每行开头加上`#`或用`"""`或`'''`，比如：

    ```
    '''
    这是个注释
    '''
    ```
    
    - 好的注释：
        - Clarity: Comments should clarify the code, not complicate it. They are best used to explain the ***why***, not the how.

        - Avoid Overuse: ***Don’t state the obvious*** in comments; write ***self-explanatory code*** as much as possible

        - ==不懂，待找一些例子==Code Documentation: For larger projects, use comments for documentation. Python also supports docstrings (triple-quoted strings) that can be used to document modules, classes, functions, and methods.
2. 变量：直接赋值，不用给出数据类型。
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
3. 字符串：被`'`或`"`或`'''`或`"""`包裹
操作符：连接，重复，取字符，切割。
```python
# 连接，直接用+
name = Rose
x = "Hello" + "," + name + "!" # Hello,Rose!

# 重复，用*
repeat_name = name * 3 # RoseRoseRose

# 取字符，用x[num]
get_num = name[0] # R

# 分割，用[start_num:end_num]，取的是索引start_num开始到end_num-1的字符
sub_name = name[1:3] # os
```
==需要理解==字符串的不可变性，感觉是字符串本身，是不可以改变的，比如不能改变字符串的某一个字符的值。可以改变的是名字指向的地方。

Python中的六个数据类型。不可变的：数字，字符串，元组；可变的：列表，字典，集合。

不可变数据类型：当变量的值改变，对应的内存地址也会改变。

可变数据类型：当变量的值改变，对应的内存地址不会改变。


