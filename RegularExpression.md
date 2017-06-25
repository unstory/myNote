
###  正则表达式

### 1. 原子

原子是正则表达式中最基本的组成单位，每个正则表达式中至少要包含一个原子，常见的原子有以下几类：
* 普通字符作为原子
* 非打印字符作为原子
* 原子表

##### 1.1  普通字符作为原子


```python
import re
pattern = "yue"  # 普通字符作为原子
string = "http://yum.iqianyue.com"
result1 = re.search(pattern, string)
print(result1.group())
```

    yue
    

#### 1.2  非打印字符作为原子

符号  |  含义
------|--------------------
\n   |  用于匹配一个换行符
\t   |  用于匹配一个制表符


```python
import re
pattern = "\n"
string = '''http://yum.iqianyue.com
http://baidu.com'''
result1 = re.search(pattern, string)
print(result1.group())
```

    
    
    

#### 1.3  通用字符作为原子

符号    |    含义
---------|----------------------------------------------
\w     |  匹配任意一个字母、数字或下划线
\W     |  匹配除了字母、数字或下划线以外的任意一个字符
\d     |  匹配一个十进制数
\D     |  匹配非十进制数
\s     |  匹配任意一个空白符
\S     |  匹配任意一个非空白符


```python
import re
pattern = "\w\dpython\w"
string = "abcdefphp345pythony_py"
result1 = re.search(pattern, string)
print(result1.group())
```

    45pythony
    

#### 1.4  原子表

原子表由[]表示，比如[xyz]就是一个原子表，表中定义3个原子，[^]代表除了中括号里面的原子均可以匹配


```python
import re
pattern1 = "\w\dpython[xyz]\w"
pattern2 = "\w\dpython[^xyz]\w"
pattern3 = "\w\dpython[xyz]\W"
string = "abcdefphp345pythony_py"
result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string)
result3 = re.search(pattern3, string)
print("result1:", result1.group())
# print("result2:", result2.group())
# print("result3:", result3.group())
```

    result1: 45pythony_
    

### 2. 元字符

符号    |    含义
---------|----------------------------------------------
.      | 匹配除换行符以外的任意字符
^      | 匹配字符串开始的位置
$      | 匹配字符串结束的位置
*      | 匹配0次、1次或者多次前面的原子
?      | 匹配0次、1次前面的字符串
+      | 匹配1次或者多次前面的字符串
{n}    | 前面的字符串恰好出现n次
{n,}   | 前面的原子至少出现n次
{m,n}   | 前面的原子至少出现n次，至多出现m次
 竖线   | 模式选择符
()     | 模式单元符


```python
pattern = ".python..."
string = "abcdfphp345python_py"
result1 = re.search(pattern, string)
print(result1)
```

    <_sre.SRE_Match object; span=(10, 20), match='5python_py'>
    

#### 2.1  边界限制元字符

字符串的开始：^<br>
字符串的结束：$

#### 2.2  限定符

常见的限定符包括：*、?、+、{n}、{n,}、{n,m}


```python
pattern1 = "py.*n"
pattern2 = "cd{2}"
pattern3 = "cd{3}"
pattern4 = "cd{2,}"
string = "abcdddddfpyp345python_py"
result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string)
result3 = re.search(pattern3, string)
result4 = re.search(pattern4, string)
for i in range(1, 5):
    print("result" + str(i), eval("result" + str(i)))
```

    result1 <_sre.SRE_Match object; span=(9, 21), match='pyp345python'>
    result2 <_sre.SRE_Match object; span=(2, 5), match='cdd'>
    result3 <_sre.SRE_Match object; span=(2, 6), match='cddd'>
    result4 <_sre.SRE_Match object; span=(2, 8), match='cddddd'>
    

####  2.3  模式选择符

模式选择符| 


```python
pattern = "python|php"
string = "abcdfpython345php_py"
result1 = re.search(pattern, string)    # 先匹配到了python，不再往后面匹配
print(result1)
```

    <_sre.SRE_Match object; span=(5, 11), match='python'>
    

#### 2.4  模式单元符


```python
pattern1 = "(cd){1,}"
pattern2 = "cd{1,}"
string = "abcdcdcdcdcdfff"
result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string)
print(result1)
print(result2)
```

    <_sre.SRE_Match object; span=(2, 12), match='cdcdcdcdcd'>
    <_sre.SRE_Match object; span=(2, 4), match='cd'>
    

### 3. 模式修正

所谓模式修正符，即可以在不改变正则表达式的情况下，通过模式修正符改变正则表达式的含义，从而实现一些匹配结果的调整等功能，常见的模式修正符如下：

符号  | 含义
--|--
I  | 匹配时忽略大小写
M  | 多行匹配
L  | 做本地化识别匹配
U  |  根据Unicode字符及解析字符
S  |  让.匹配包括换行符，即用了该模式修正后，"."匹配就可以匹配任意字符串


```python
pattern = "python"
string = "ajdkjlPython"
result1 = re.search(pattern, string)
result2 = re.search(pattern, string, re.I)  # 忽略大小写
print(result1)
print(result2)
```

    None
    <_sre.SRE_Match object; span=(6, 12), match='Python'>
    

### 4. 贪婪模式和懒惰模式

总的来说，贪婪模式就是尽可能多的匹配，懒惰模式就是尽可能少的匹配


```python
pattern1 = "p.*y"  #贪婪模式
pattern2 = "p.*?y"  #懒惰模式
string = "abcdfphp345pythony_py"
result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string)
print(result1)
print(result2)
```

    <_sre.SRE_Match object; span=(5, 21), match='php345pythony_py'>
    <_sre.SRE_Match object; span=(5, 13), match='php345py'>
    

### 5. Python正则函数

#### 5.1  re.compile

对正则表达式进行预编译,预编译后可以使匹配速度更快

<b>usage:</b>&nbsp;&nbsp;re.compile(pattern)

#### 5.2  re.match

<b>usage:</b>&nbsp;&nbsp;re.match(pattern, string, flag)

<font color="red"><b>note:</b></font>&nbsp;&nbsp;match会从string的<b>起始位置</b>开始匹配，如果不满足则返回None


```python
pattern = "py.*?n"
string1 = "python"
string2 = "apython"
result1 = re.match(pattern, string1)
result2 = re.match(pattern, string2)
print(result1)
print(result2)
```

    <_sre.SRE_Match object; span=(0, 6), match='python'>
    None
    

#### 5.3  re.search

<b>usage:</b>&nbsp;&nbsp;re.search(pattern, string, flag)

<font color="red"><b>note:</b></font>&nbsp;&nbsp;search会扫描整个string，如果不满足则返回None


```python
pattern = "py.*?n"
string1 = "python"
string2 = "apython"
result1 = re.search(pattern, string1)
result2 = re.search(pattern, string2)
print(result1)
print(result2)
```

    <_sre.SRE_Match object; span=(0, 6), match='python'>
    <_sre.SRE_Match object; span=(1, 7), match='python'>
    

#### 5.4  re.findall


```python
string = "hellopythonhipythonxyzabcpythond"
pattern = re.compile(".python.")
result = re.findall(pattern, string)
print(result)
```

    ['opythonh', 'ipythonx', 'cpythond']
    

#### 5.5  re.sub

<b>usage:</b>&nbsp;&nbsp;re.sub(pattern, rep, string, max)


```python
string = "hellomypythonhipythonuser"
pattern = "python"
result1 = re.sub(pattern, "php", string)
result2 = re.sub(pattern, "java", string, 1)
print(result1)
print(result2)
```

    hellomyphphiphpuser
    hellomyjavahipythonuser
    

#### 5.6  re.split

<b>usage:</b>&nbsp;&nbsp;re.split(pattern, string, maxsplit=0, flags=0)


```python
pattern = "\d"
string = "1xyz2abc4myphp"
result = re.split(pattern, string)
print(result)
```

    ['', 'xyz', 'abc', 'myphp']
    

### 6. 实例解析

#### 6.1  匹配.com或者.cn后缀的url网站


```python
pattern = "[a-zA-Z]+://[^\s]*[.com|.cn]"
string = "<a href='http://www.baidu.com'>百度首页</a>"
result = re.search(pattern, string)
print(result)
```

    <_sre.SRE_Match object; span=(9, 29), match='http://www.baidu.com'>
    

#### 6.2  匹配电话号码


```python
pattern = "\d{4}-\d{7}|\d{3}-\d{8}"
string = "021-43953958940385940388"
result = re.search(pattern, string)
print(result)
```

    <_sre.SRE_Match object; span=(0, 12), match='021-43953958'>
    

#### 6.3  匹配电子邮件地址


```python
string = "myEmail2075234323@qq.com"
pattern = "\w+@\w+\.((com)|(cn))"
result = re.search(pattern, string)
print(result)
```

    <_sre.SRE_Match object; span=(0, 24), match='myEmail2075234323@qq.com'>
    
