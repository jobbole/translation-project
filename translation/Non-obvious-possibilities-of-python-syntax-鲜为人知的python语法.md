# Non-obvious possibilities of python syntax
# 鲜为人知的 python 语法

鲜为人知的python语法 [阅读原文 »](https://medium.com/@chipiga86/non-obvious-possibilities-of-python-syntax-a95a7210aaaf)


Hi! All of us (ok not all :)) know [python](https://www.python.org/) as wide-used, simple-to-read, easy-to-start programming language.   

所有人（好吧，不是所有人）都知道 [python](https://www.python.org/) 是一门用途广泛、易读、而且容易入门的编程语言。  

But at the same time python syntax allows to make really strange things.    
但同时 python 语法也允许我们做一些很奇怪的事情。    

## Rewrite multiline function with lambda  
## 使用 lambda 表达式重写多行函数  

As it’s known python lambda doesn’t support multiline code. But it can be simulated.  
众所周知 python 的 lambda 表达式不支持多行代码。但是可以模拟出多行代码的效果。  

```python
def f():
    x = 'string'
    if x.endswith('g'):
        x = x[:-1]
    r = ''
    for i in xrange(len(x)):
        if x[i] != 'i':
            r += x[i]
    return r
f()
-> 'strn'
```

Sounds strange but above function can be replaced with **lambda**-function:   
虽然看起来很奇怪，但是上面的函数可以使用下面的 **lambda** 表达式函数代替：   

```python
(lambda: ([x for x in ['string']], x.endswith('g') and [x for x in [x[:-1]]], [r for r in ['']], [x[i] != 'i' and [r for r in [r+x[i]]] for i in xrange(len(x))], r)[-1])()
-> 'strn'
```  

Never do that in production code :)    
永远不要在生产环境写这样的代码 :)  

## Ternary operator  
## 三元运算符 

Modern python gives you simple intuitive syntax:   
现代的 python 提供了更简便的语法:   

```python
b if a else c   
```   


But it also can be rewritten via:   
也可以通过下面的方式重写：  

```python
(a and [b] or [c])[0]

(b, c)[not a]
```  

Btw, next variant is incorrect:    
顺便说一下，下面的变体是错误的：   

```python
a and b or c
True and [] or [1] -> [1], but: [] if True else [1] -> []
``` 

## Remove repeated symbols via list comprehension  
## 通过列表推导式移除重复的元素 

Let’s transform string `x = 'tteesstt'` to `'test'`.   
让我们来把字符串  `x = 'tteesstt'` 转换成  `'test'` 吧。

1. compare a symbol with previous in original string:   
2. 在原字符串中和上一个字符比较：

```python
''.join(['' if i and j == x[i-1] else j for i,j in enumerate(x)])
```   

1.  save previous symbol in temporary variable: 
2.  把前一个字符保存到临时变量中：

```python
''.join([('' if i == a else i, [a for a in [i]])[0] for a in [''] for i in x])
''.join([('' if i == a.pop() else i, a.append(i))[0] for a in [['']] for i in x])
```

3. compare a symbol with previous in new string:    
3. 在新字符串中和上一个字符比较：

```python
[(not r.endswith(i) and [r for r in [r+i]], r)[-1] for r in [''] for i in x][-1]
```  

4.  via reduce & lambda:     
4. 通过 reduce 函数和 lambda 表达式：

```python
reduce(lambda a, b: a if a.endswith(b) else a + b, x)
```

## Fibonacci via list comprehension  
## 通过列表推导式获得斐波拉契数列  

1. save temporary values in list:    
1. 把中间值保存在列表中 

```python
[(lambda: (l[-1], l.append(l[-1] + l[-2]))[0])() for l in [[1, 1]] for x in xrange(19)]
[(l[-1], l.append(l[-1] + l[-2]))[0] for l in [[1, 1]] for x in xrange(19)]
```   

2. save temporary values in dict:   
2. 把中间值保存到字典中: 

```python
[i for x in [(lambda: (l['a'], l.update({'a': l['a'] + l['b']}), l['b'], l.update({'b': l['a'] + l['b']}))[::2])() for l in [{'a': 1, 'b': 1}] for x in xrange(10)] for i in x]
[i for x in [(l['a'], l.update({'a': l['a'] + l['b']}), l['b'], l.update({'b': l['a'] + l['b']}))[::2] for l in [{'a': 1, 'b': 1}] for x in xrange(10)] for i in x]
```  

3. via reduce & lambda:  
3. 通过 reduce 函数和 lambda 表达式：

```python
reduce(lambda a, b: a + [a[-1] + a[-2]], xrange(10), [1, 1])
reduce(lambda a, b: a.append(a[-1] + a[-2]) or a, xrange(10), [1, 1])
``` 

4. the quickest variant:   
4. 速度最快的变体：  

```python
[l.append(l[-1] + l[-2]) or l for l in [[1, 1]] for x in xrange(10)][0]
```

## Eternal cycle with list comprehension  
## 使用列表推导式产生死循环
`[a.append(b) for a in [[None]] for b in a]`  

## List slice tricks   
## 列表切片技巧 

1. copy list:   
1. 复制列表： 

```python
l = [1, 2, 3]
m = l[:]
m
-> [1, 2, 3]
```

2. remove/replace any number of elements:  
2. 移除/替换 列表中的任意元素：

```python
l = [1, 2, 3]
l[1:-1] = [4, 5, 6, 7]
l
-> [1, 4, 5, 6, 7, 3]
```

3. add elements to begin of list:   
3. 在列表的开头添加元素：

```python
l = [1, 2, 3]
l[:0] = [4, 5, 6]
l
-> [4, 5, 6, 1, 2, 3]
```

4. add elements to end of list:
4. 在列表的尾部添加元素： 

```python
l = [1, 2, 3]
l[-1:] = [l[-1], 4, 5, 6]
l
-> [1, 2, 3, 4, 5, 6]
```

5. reverse list:  
5. 反转列表：

```python
l = [1, 2, 3]
l[:] = l[::-1]
``` 

## Replace method byte code  
## 替换方法字节码

Python prohibits to replace instance method, making it as read-only property:   
Python 阻止替换类实例中的方法，因为 python 给类实例中的方法赋予了只读属性：   

```python
class A(object):
    def x(self):
        print "hello"
a = A()
def y(self):
    print "world"
a.x.im_func = y
-> TypeError: readonly attribute
``` 

But it can be replaced on byte-code level:  
但是可以在字节码的层面上进行替换：   

```python
a.x.im_func.func_code = y.func_code
a.x()
-> 'world'
```   

**Note!** It has influence not only to current instance but to class (if to be precise to function which is bound with class) and all other instances too:   
**注意！** 这不仅对当前的实例有影响，而且对整个类都有影响（准确的说是与这个类绑定的函数）（译者注:此处应该是笔误，推测作者原意是:准确的说是与这个函数绑定的所有类），并且所有其他的实例也会受到影响：   

```python
new_a = A()
new_a.x()
-> 'world'
```

## Mutable object as default function argument  
## 让可变元素作为函数参数默认值   

To assign mutable object as default value to function argument is very dangerous and there are a lot of tricky questions on interviews about that. But it can be helpful as cache mechanism.   
把可变对象作为函数参数的默认值是非常危险的一件事，并且在面试中有大量关于这方面棘手的面试问题。但这一点对于缓存机制非常有帮助。

1. Factorial: 
2. 阶乘函数：

```python
def f(n, c={}):
    if n in c:
        return c[n]
    if (n < 2):
        r = 1
    else:
        r = n * f(n - 1)
    c[n] = r
    return r
f(10)
-> 3628800
f.func_defaults
({1: 1,
  2: 2,
  3: 6,
  4: 24,
  5: 120,
  6: 720,
  7: 5040,
  8: 40320,
  9: 362880,
  10: 3628800},)
```


2. Fibonacci: 
2. 斐波拉契数列：   

```python
def fib(n, c={}):
    if n in c:
        return c[n]
    if (n < 2):
        r = 1
    else:
        r = fib(n - 2) + fib(n - 1)
    c[n] = r
    return r
fib(10)
-> 89
fib.func_defaults[0].values()
-> [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```