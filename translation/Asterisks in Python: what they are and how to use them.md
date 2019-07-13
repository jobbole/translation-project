---
translator: http://www.jobbole.com/members/wx1763043264/
reviewer: http://www.jobbole.com/members/hanxiaomax/
via: http://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/
---

# Asterisks in Python: what they are and how to use them

# Python 中星号的本质及其使用方式

There are a lot of places you’ll see `*` and `**` used in Python. These two operators can be a bit mysterious at times, both for brand new programmers and for folks moving from many other programming languages which may not have completely equivalent operators. I’d like to discuss what those operators are and the many ways they’re used.

在 Python 中有很多地方可以看到` * `和` ** `。在某些情形下，无论是对于新手程序员，还是从其他很多没有完全相同操作符的编程语言迁移过来的人来说，这两个操作符都可能有点神秘。因此，我想讨论一下这些操作符的本质及其使用方式。

The `*` and `**` operators have grown in ability over the years and I’ll be discussing all the ways that you can currently use these operators and noting which uses only work in modern versions of Python. So if you learned `*` and `**` back in the days of Python 2, I’d recommend at least skimming this article because Python 3 has added a lot of new uses for these operators.

多年以来，` * `和` ** `操作符的功能不断增强。在本文中，我将讨论目前这些操作符所有的使用方法，并指出哪些使用方法只能在目前的 Python 版本中应用。因此，如果你学习过 Python 2 中` * `和` ** `的使用方法，那么我建议你至少浏览一下本文，因为 Python 3 中添加了许多` * `和` ** `的新用途。

If you’re newer to Python and you’re not yet familiar with keyword arguments (a.k.a. named arguments), I’d recommend reading my article on [keyword arguments in Python](https://treyhunner.com/2018/04/keyword-arguments-in-python/) first.

如果你是新接触 Python 不久，还不熟悉关键字参数(亦称为命名参数)，我建议你首先阅读我有关[Python中的关键字参数](https://treyhunner.com/2018/04/keyword-arguments-in-python/)的文章。

## What we’re not talking about

## 不属于我们讨论范围的内容

When I discuss `*` and `**` in this article, I’m talking about the `*` and `**` *prefix* operators, not the *infix* operators.

在本文中， 当我讨论` * `和` ** `时，我指的是` * `和` ** `  *前缀* 操作符，而不是 *中缀* 操作符。

So I’m not talking about multiplication and exponentiation:

也就是说，我讲述的不是乘法和指数运算：

```
>>> 2 * 5
10 
>>> 2 ** 5 
32
```

## So what are we talking about?

## 那么我们在讨论什么内容呢?

We’re talking about the `*` and `**` prefix operators, that is the `*` and `**` operators that are used before a variable. For example:

我们讨论的是` * `和` ** `前缀运算符，即在变量前使用的` * `和` ** `运算符。例如:

```
>>> numbers = [2, 1, 3, 4, 7]
>>> more_numbers = [*numbers, 11, 18]
>>> print(*more_numbers, sep=', ')
2, 1, 3, 4, 7, 11, 18 
```

Two of the uses of `*` are shown in that code and no uses of `**` are shown.

上述代码中展示了` * `的两种用法，没有展示` ** `的用法。

This includes:

1. Using `*` and `**` to pass arguments to a function
2. Using `*` and `**` to capture arguments passed into a function
3. Using `*` to accept keyword-only arguments
4. Using `*` to capture items during tuple unpacking
5. Using `*` to unpack iterables into a list/tuple
6. Using `**` to unpack dictionaries into other dictionaries

这其中包括：

1. 使用`*`和`**`向函数传递参数
2. 使用`*`和`**`捕获被传递到函数中的参数
3. 使用`*`接受只包含关键字的参数
4. 使用`*`在元组解包时捕获项
5. 使用`*`将迭代项解压到列表/元组中
6. 使用`**`将字典解压到其他字典中

Even if you think you’re familiar with all of these ways of using `*` and `**`, I recommend looking at each of the code blocks below to make sure they’re all things you’re familiar with. The Python core developers have continued to add new abilities to these operators over the last few years and it’s easy to overlook some of the newer uses of `*` and `**`.

即使你认为自己已经熟悉`*` 和 `**`的所有使用方法，我还是建议你查看下面的每个代码块，以确保都是你熟悉的内容。在过去的几年里，Python 核心开发人员不断地为这些操作符添加新的功能，对于使用者来说很容易忽略`*` 和 `**`'的一些新用法。

## Asterisks for unpacking into function call

## 星号用于将可迭代对象拆分并分别作为函数参数

When calling a function, the `*` operator can be used to unpack an iterable into the arguments in the function call:

当调用函数时，` * `运算符可用于将一个迭代项解压缩到函数调用中的参数中：

```
>>> fruits = ['lemon', 'pear', 'watermelon', 'tomato']
>>> print(fruits[0], fruits[1], fruits[2], fruits[3])
lemon pear watermelon tomato 
>>> print(*fruits)
lemon pear watermelon tomato 
```

That `print(*fruits)` line is passing all of the items in the `fruits` list into the `print` function call as separate arguments, without us even needing to know how many arguments are in the list.

` print(*fruits) `代码行将` fruits `列表中的所有项作为独立的参数传递给` print `函数调用，甚至不需要我们知道列表中有多少个参数。

The `*` operator isn’t just syntactic sugar here. This ability of sending in all items in a particular iterable as separate arguments wouldn’t be possible without `*`, unless the list was a fixed length.

` * `运算符在这里远不止是语法糖而已。要想用一个特定的迭代器将所有项作为独立的参数传输，若不使用` * `是不可能做到的，除非列表的长度是固定的。

Here’s another example:

下面是另一个例子：

```
def transpose_list(list_of_lists):
	return [
        list(row)
        for row in zip(*list_of_lists)
	] 
```

Here we’re accepting a list of lists and returning a “transposed” list of lists.

这里我们接受一个二维列表并返回一个“转置”的二维列表。

```
>>> transpose_list([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
[[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
```

The `**` operator does something similar, but with keyword arguments. The `**` operator allows us to take a dictionary of key-value pairs and unpack it into keyword arguments in a function call.

` ** `操作符完成了类似的操作，只不过使用了关键字参数。` ** `运算符允许我们获取键-值对字典，并在函数调用中将其解压为关键字参数。

```
>>> date_info = {'year': "2020", 'month': "01", 'day': "01"} 
>>> filename = "{year}-{month}-{day}.txt".format(**date_info) 
>>> filename '2020-01-01.txt' `
```

From my experience, using `**` to unpack keyword arguments into a function call isn’t particularly common. The place I see this most is when practicing inheritance: calls to `super()` often include both `*` and `**`.

根据我的经验，使用` ** `将关键字参数解压缩到函数调用中并不常见。我最常看到它的地方是在实现继承时：对` uper() `的调用通常包括` * `和` ** `。

Both `*` and `**` can be used multiple times in function calls, as of Python 3.5.

如 Python 3.5 那样，在函数调用中，` * `和` ** `都可以被多次使用。

Using `*` multiple times can sometimes be handy:

有时，多次使用` * `会很方便:

```
>>> fruits = ['lemon', 'pear', 'watermelon', 'tomato'] 
>>> numbers = [2, 1, 3, 4, 7] 
>>> print(*numbers, *fruits) 
2 1 3 4 7 lemon pear watermelon tomato `
```

Using `**` multiple times looks similar:

多次使用` ** `也可以达到相似的效果:

```
>>> date_info = {'year': "2020", 'month': "01", 'day': "01"} 
>>> track_info = {'artist': "Beethoven", 'title': 'Symphony No 5'} 
>>> filename = "{year}-{month}-{day}-{artist}-{title}.txt".format( 
...     **date_info,
...     **track_info,
... ) 
>>> filename 
'2020-01-01-Beethoven-Symphony No 5.txt' 
```

You need to be careful when using `**` multiple times though. Functions in Python can’t have the same keyword argument specified multiple times, so the keys in each dictionary used with `**` must be distinct or an exception will be raised.

不过，在多次使用` ** `时需要特别小心。Python 中的函数不能多次指定相同的关键字参数，因此在每个字典中与` ** `一起使用的键必须能够相互区分，否则会引发异常。

## Asterisks for packing arguments given to function

## 星号用于压缩被传递到函数中的参数

When defining a function, the `*` operator can be used to capture an unlimited number of positional arguments given to the function. These arguments are captured into a tuple.

在定义函数时，` * `运算符可用于捕获传递给函数的位置参数。位置参数的数量不受限制，捕获后被存储在一个元组中。

```
from random import randint  

def roll(*dice):     
	return sum(randint(1, die) for die in dice)
```

This function accepts any number of arguments:

这个函数接受的参数数量不受限制：

```
>>> roll(20) 
18 
>>> roll(6, 6) 
9 
>>> roll(6, 6, 6) 
8
```

Python’s `print` and `zip` functions accept any number of positional arguments. This argument-packing use of `*` allows us to make our own function which, like `print` and `zip`, accept any number of arguments.

Python 的` print `和` zip `函数接受的位置参数数量不受限制。` * `的这种参数压缩用法，允许我们创建像` print `和` zip `一样的函数，接受任意数量的参数。

The `**` operator also has another side to it: we can use `**` when defining a function to capture any keyword arguments given to the function into a dictionary:

` ** `运算符也有另外一个功能：我们在定义函数时，可以使用` ** ` 捕获传进函数的任何关键字参数到一个字典当中:

```
def tag(tag_name, **attributes):
	attribute_list = [
    	f'{name}="{value}"'
        for name, value in attributes.items()
    ]     
    return f"<{tag_name} {' '.join(attribute_list)}>" 
```

That `**` will capture any keyword arguments we give to this function into a dictionary which will that `attributes` arguments will reference.

` ** ` 将捕获我们传入这个函数中的任何关键字参数，并将其放入一个字典中，该字典将引用` attributes `参数。

```
>>> tag('a', href="http://treyhunner.com")
'<a href="http://treyhunner.com">' 
>>> tag('img', height=20, width=40, src="face.jpg") 
'<img height="20" width="40" src="face.jpg">' 
```

## Positional arguments with keyword-only arguments

## 只有关键字参数的位置参数

As of Python 3, we now have a special syntax for accepting keyword-only arguments to functions. Keyword-only arguments are function arguments which can *only* be specified using the keyword syntax, meaning they cannot be specified positionally.

在 Python 3 中，我们现在拥有了一种特殊的语法来接受只有关键字的函数参数。只有关键字的参数是*只能* 使用关键字语法来指定的函数参数，也就意味着不能按照位置来指定它们。

To accept keyword-only arguments, we can put named arguments after a `*` usage when defining our function:

在定义函数时，为了接受只有关键字的参数，我们可以将命名参数放在` * `后：

```
def get_multiple(*keys, dictionary, default=None):
	return [
    	dictionary.get(key, default)
        for key in keys
    ]
```

The above function can be used like this:

上面的函数可以像这样使用：

```
>>> fruits = {'lemon': 'yellow', 'orange': 'orange', 'tomato': 'red'} 
>>> get_multiple('lemon', 'tomato', 'squash', dictionary=fruits, default='unknown'）
['yellow', 'red', 'unknown'] 
```

The arguments `dictionary` and `default` come after `*keys`, which means they can *only* be specified as [keyword arguments](https://treyhunner.com/2018/04/keyword-arguments-in-python/). If we try to specify them positionally we’ll get an error:

参数` dictionary `和` default `在` *keys `后面，这意味着它们*只能* 被指定为[关键字参数](https://treyhunner.com/2018/04/keyword-arguments-inpython/)。如果我们试图按照位置来指定它们，我们会得到一个报错：

```
>>> fruits = {'lemon': 'yellow', 'orange': 'orange', 'tomato': 'red'} 
>>> get_multiple('lemon', 'tomato', 'squash', fruits, 'unknown') 
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: get_multiple() missing 1 required keyword-only argument: 'dictionary' 
```

This behavior was introduced to Python through [PEP 3102](https://www.python.org/dev/peps/pep-3102/).

这种行为是通过 [PEP 3102](https://www.python.org/dev/peps/pep-3102/) 被引入到 Python 中的。

## Keyword-only arguments without positional arguments

## 没有位置参数关键字的参数

That keyword-only argument feature is cool, but what if you want to require keyword-only arguments without capturing unlimited positional arguments?

只使用关键字参数的特性很酷，但是如果您希望只使用关键字参数而不捕获无限的位置参数呢?

Python allows this with a somewhat strange `*`-on-its-own syntax:

Python 使用一种有点奇怪的 单独`*` 语法来实现：

```
def with_previous(iterable, *, fillvalue=None):
	"""Yield each iterable item along with the item before it."""     
	previous = fillvalue     
	for item in iterable:         
		yield previous, item         
		previous = item 
```

This function accepts an `iterable` argument, which can be specified positionally (as the first argument) or by its name and a `fillvalue` argument which is a keyword-only argument. This means we can call `with_previous` like this:

这个函数接受一个` 迭代器`参数，可以按照位置或名字来指定此参数（作为第一个参数），以及关键字参数`fillvalue`，这个填充值参数只使用关键字。这意味着我们可以像下面这样调用 with_previous：

```
>>> list(with_previous([2, 1, 3], fillvalue=0)) 
[(0, 2), (2, 1), (1, 3)] 
```

But not like this:

但像这样就不可以：

```
>>> list(with_previous([2, 1, 3], 0))
Traceback (most recent call last):  
File "<stdin>", line 1, in <module> 
TypeError: with_previous() takes 1 positional argument but 2 were given `
```

This function accepts two arguments and one of them, `fillvalue` *must be specified as a keyword argument*.

这个函数接受两个参数，其中` fillvalue`参数*必须被指定为关键字参数*。

I usually use keyword-only arguments used while capturing any number of positional arguments, but I do sometimes use this `*` to enforce an argument to only be specified positionally.

我通常在获取任意数量的位置参数时只使用关键字参数，但我有时使用这个` * `强制按照位置指定一个参数。

Python’s built-in `sorted` function actually uses this approach. If you look at the help information on `sorted` you’ll see the following:

实际上，Python 的内置` sorted `函数使用了这种方法。如果你查看` sorted `的帮助信息，将看到以下信息：

```
>>> help(sorted) 
Help on built-in function sorted in module builtins: 

sorted(iterable, /, *, key=None, reverse=False)     
	Return a new list containing all items from the iterable in ascending order.  
	A custom key function can be supplied to customize the sort order, and the     
	reverse flag can be set to request the result in descending order. 
```

There’s an ` * `-on-its-own, right in the documented arguments for `sorted`.

在` sorted `的官方说明中，有一个单独的` * `参数。

## Asterisks in tuple unpacking

## 星号用于元组拆包

Python 3 also added a new way of using the `*` operator that is only somewhat related to the `*`-when-defining-a-function and `*`-when-calling-a-function features above.

Python 3 还新添了一种 `*` 运算符的使用方式，它只与上面定义函数时和调用函数时`*`的使用方式相关。

The `*` operator can also be used in tuple unpacking now:

现在，`*`操作符也可以用于元组拆包：

```
>>> fruits = ['lemon', 'pear', 'watermelon', 'tomato'] 
>>> first, second, *remaining = fruits 
>>> remaining 
['watermelon', 'tomato'] 
>>> first, *remaining = fruits 
>>> remaining 
['pear', 'watermelon', 'tomato'] 
>>> first, *middle, last = fruits 
>>> middle 
['pear', 'watermelon'] 
```

If you’re wondering “where could I use this in my own code”, take a look at the examples in my article on [tuple unpacking in Python](https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/). In that article I show how this use of the `*` operator can sometimes be used as an alternative to sequence slicing.

如果你想知道什么情况下可以在你自己的代码中使用它，请查看我关于 [Python 中的 tuple 解包](https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/) 文章中的示例。在那篇文章中，我将展示如何使用` * `操作符作为序列切片的替代方法。

Usually when I teach `*` I note that you can only use one `*` expression in a single multiple assignment call. That’s technically incorrect because it’s possible to use two in a nested unpacking (I talk about nested unpacking in my tuple unpacking article):

通常当我教` * `的时候，我告诉大家只能在多重赋值语句中使用一个` * `表达式。实际来说这是不正确的，因为可以在嵌套解包中使用两个` * `（我在元组解包文章中讨论了嵌套解包）：

```
>>> fruits = ['lemon', 'pear', 'watermelon', 'tomato'] 
>>> ((first_letter, *remaining), *other_fruits) = fruits 
>>> remaining 
['e', 'm', 'o', 'n'] 
>>> other_fruits
['pear', 'watermelon', 'tomato'] 
```

I’ve never seen a good use for this though and I don’t think I’d recommend using it even if you found one because it seems a bit cryptic.

但是，我从来没见过它有什么实际用处，即使你因为它看起来有点神秘而去寻找一个例子，我也并不推荐这种使用方式。

The PEP that added this to Python 3.0 is [PEP 3132](https://www.python.org/dev/peps/pep-3132/) and it’s not a very long one.

将此添加到 Python 3.0 中的 PEP 是 [PEP 3132](https://www.python.org/dev/peps/pep-3132/)，其篇幅不是很长。

## Asterisks in list literals

## 列表文字中的星号

Python 3.5 introduced a ton of new `*`-related features through [PEP 448](https://www.python.org/dev/peps/pep-0448/). One of the biggest new features is the ability to use `*` to dump an iterable into a new list.

Python 3.5 通过 [PEP 448](https://www.python.org/dev/peps/pep-0448/) 引入了大量与`*`相关的新特性。其中最大的新特性之一是能够使用`*`将迭代器转储到新列表中。

Say you have a function that takes any sequence and returns a list with the sequence and the reverse of that sequence concatenated together:

假设你有一个函数，它以任一序列作为输入，返回一个列表，其中该序列和序列的倒序连接在了一起：

```
def palindromify(sequence):   
	return list(sequence) + list(reversed(sequence)) 
```

This function needs to convert things to lists a couple times in order to concatenate the lists and return the result. In Python 3.5, we can type this instead:

此函数需要多次将序列转换为列表，以便连接列表并返回结果。在 Python 3.5 中，我们可以这样编写函数：

```
def palindromify(sequence):  
	return [*sequence, *reversed(sequence)] 
```

This code removes some needless list calls so our code is both more efficient and more readable.

这段代码避免了一些不必要的列表调用，因此我们的代码更高效，可读性更好。

Here’s another example:

下面是另一个例子：

```
def rotate_first_item(sequence):     
	return [*sequence[1:], sequence[0]] 
```

That function returns a new list where the first item in the given list (or other sequence) is moved to the end of the new list.

该函数返回一个新列表，其中给定列表(或其他序列)中的第一项被移动到了新列表的末尾。

This use of the `*` operator is a great way to concatenate iterables of different types together. The `*` operator works for any iterable, whereas using the `+` operator only works on particular sequences which have to all be the same type.

`*` 运算符的这种使用是将不同类型的迭代器连接在一起的好方法。`*` 运算符适用于连接任何种类的迭代器，然而 `+` 运算符只适用于类型都相同的特定序列。

This isn’t just limited to creating lists either. We can also dump iterables into new tuples or sets:

除了创建列表存储迭代器以外，我们还可以将迭代器转储到新的元组或集合中：

```
>>> fruits = ['lemon', 'pear', 'watermelon', 'tomato'] 
>>> (*fruits[1:], fruits[0]) 
('pear', 'watermelon', 'tomato', 'lemon') 
>>> uppercase_fruits = (f.upper() for f in fruits) 
>>> {*fruits, *uppercase_fruits}
{'lemon', 'watermelon', 'TOMATO', 'LEMON', 'PEAR', 'WATERMELON', 'tomato', 'pear'} 
```

Notice that the last line above takes a list and a generator and dumps them into a new set. Before this use of `*`, there wasn’t previously an easy way to do this in one line of code. There was a way to do this before, but it wasn’t easy to remember or discover:

注意，上面的最后一行使用了一个列表和一个生成器，并将它们转储到一个新的集合中。在此之前，并没有一种简单的方法可以在一行代码中完成这项工作。曾经有一种方法可以做到这一点，可是并不容易被记住或发现：

```
>>> set().union(fruits, uppercase_fruits) 
{'lemon', 'watermelon', 'TOMATO', 'LEMON', 'PEAR', 'WATERMELON', 'tomato', 'pear'} 
```

## Double asterisks in dictionary literals

## 两个星号用于字典文本

PEP 448 also expanded the abilities of `**` by allowing this operator to be used for dumping key/value pairs from one dictionary into a new dictionary:

PEP 448 还通过允许将键/值对从一个字典转储到一个新字典扩展了`**`操作符的功能：

```
>>> date_info = {'year': "2020", 'month': "01", 'day': "01"} 
>>> track_info = {'artist': "Beethoven", 'title': 'Symphony No 5'} 
>>> all_info = {**date_info, **track_info} 
>>> all_info
{'year': '2020', 'month': '01', 'day': '01', 'artist': 'Beethoven', 'title': 'Symphony No 5'} 
```

I wrote another article on how this is now the [idiomatic way to merge dictionaries in Python](https://treyhunner.com/2016/02/how-to-merge-dictionaries-in-python/).

我还写了另一篇文章：[在Python中合并字典的惯用方法](https://treyhunner.com/2016/02/howtomerdictionaries-python/)。

This can be used for more than just merging two dictionaries together though.

不过，`**`操作符不仅仅可以用于合并两个字典。

For example we can copy a dictionary while adding a new value to it:

例如，我们可以在复制一个字典的同时添加一个新值：

```
>>> date_info = {'year': '2020', 'month': '01', 'day': '7'} 
>>> event_info = {**date_info, 'group': "Python Meetup"} 
>>> event_info 
{'year': '2020', 'month': '01', 'day': '7', 'group': 'Python Meetup'} 
```

Or copy/merge dictionaries while overriding particular values:

或者在复制/合并字典的同时重写特定的值：

```
>>> event_info = {'year': '2020', 'month': '01', 'day': '7', 'group': 'Python Meetup'} 
>>> new_info = {**event_info, 'day': "14"}
>>> new_info
{'year': '2020', 'month': '01', 'day': '14', 'group': 'Python Meetup'} 
```

## Python’s asterisks are powerful

## Python 的星号非常强大

Python’s `*` and `**` operators aren’t just syntactic sugar. Some of the things they allow you to do could be achieved through other means, but the alternatives to `*` and `**`tend to be more cumbersome and more resource intensive. And some of the features they provide are simply impossible to achieve without them: for example there’s no way to accept any number of positional arguments to a function without `*`.

Python 的 `*` 和 `**` 运算符不仅仅是语法糖。 `*` 和 `**` 运算符允许的某些操作可以通过其他方式实现，但是往往更麻烦和更耗费资源。而且 `*` 和 `**` 运算符提供的某些特性没有替代方法实现：例如，函数在不使用 `*` 时就无法接受任意数量的位置参数。

After reading about all the features of `*` and `**`, you might be wondering what the names for these odd operators are. Unfortunately, they don’t really have succinct names. I’ve heard `*` called the “packing” and “unpacking” operator. I’ve also heard it called “splat” (from the Ruby world) and I’ve heard it called simply “star”.

在阅读了`*` 和 `**` 运算符的所有特性之后，您可能想知道这些奇怪操作符的名称。不幸的是，它们的名字并不简练。我听说过`*` 被称为“打包”和“拆包“运算符。我还听说过其被称为“splat”(来自 Ruby 世界)，也听说过被简单地称为“star”。

I tend to call these operators “star” and “double star” or “star star”. That doesn’t distinguish them from their infix relatives (multiplication and exponentiation), but context usually makes it obvious whether we’re talking about prefix or infix operators.

我倾向于称这些操作符为“星”和“双星”或“星星”。这种叫法并不能区分它们和它们的中缀关系(乘法和指数运算)，但是通常我们可以从上下文清楚地知道是在讨论前缀运算符还是中缀运算符。

If you don’t understand `*` and `**` or you’re concerned about memorizing all of their uses, don’t be! These operators have many uses and memorizing the specific use of each one isn’t as important as getting a feel for when you might be able to reach for these operators. I suggest using this article as **a cheat sheet** or to making your own cheat sheet to help you use `*` and `**` in Python.

请勿在不理解`*` 和 `**` 运算符的前提下记住它们的所有用法！这些操作符有很多用途，记住每种操作符的具体用法并不重要，重要的是了解你何时能够使用这些操作符。我建议使用这篇文章作为一个**备忘单**或者制作你自己的备忘单来帮助你在 Python 中使用解`*` 和 `**` 。

## Like my teaching style?

## 喜欢我的教学风格吗？

Want to learn more about Python? I share my favorite Python resources and answer Python questions every week through live chats. Sign up below and I’ll answer **your questions** about how to make your Python code more descriptive, more readable, and more Pythonic.

想了解更多关于 Python 的知识吗？我每周通过实时聊天分享我最喜欢的 Python 资源、回答 Python 问题。在下方注册，我将回答你提出的关于如何使 Python 代码更具有描述性、可读性和更 Python 化的**问题**。
