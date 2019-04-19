---
translator: http://www.jobbole.com/members/q3057027161/
reviewer: http://www.jobbole.com/members/hanxiaomax/
via: https://gist.github.com/Zearin/2f40b7b9cfc51132851a
---



*__NOTE:__ This is [a question I found on StackOverflow]() which I’ve archived here, because the answer is so effing phenomenal.*  
*__注意：__ 这是一篇 StackOverflow 上的问题回答，因为这个回答很棒，所以我把它存档了* 

----

# Q: How can I make a chain of function decorators in Python?   
# 问: 怎样在 Python 中连续使用多个函数装饰器？

----

If you are not into long explanations, see [Paolo Bergantino’s answer][2].  
如果你不想看详细的解释，你可以看 [Paolo Bergantino 的回答][2]


# Decorator Basics  
# 装饰器基础

## Python’s functions are objects
## Python 的装饰器都是对象

To understand decorators, you must first understand that functions are objects in Python.
This has important consequences. Let’s see why with a simple example :  
为了理解装饰器，你首先必须知道 Python 中的函数都是 object 对象。
这非常重要。让我们通过一个例子来看看原因。   

```python
def shout(word='yes'):
    return word.capitalize() + '!'

print shout()
# outputs : 'Yes!'

# As an object, you can assign the function to a variable like any
# other object 
# 作为一个 object 对象，你可以把一个函数分配给一个变量，就像是
# 其他 object 对象一样

scream = shout

# Notice we don’t use parentheses: we are not calling the function, we are
# putting the function `shout` into the variable `scream`. 
# It means you can then call `shout` from `scream`: 
# 请注意我们并没有使用括号：因此我们没有调用函数，我们只是把函数 `shout` 赋值给变量 `scream`
# 这意味着我们可以通过 `scream` 调用 `shout` 函数

print scream()
# outputs : 'Yes!'

# More than that, it means you can remove the old name `shout`, and
# the function will still be accessible from `scream` 
# 除了这些，这还意味着你可以移除旧的函数名 `shout`,
# 之后依然可以通过 `scream` 访问函数

del shout
try:
    print shout()
except NameError as e:
    print e
    #outputs: "name 'shout' is not defined"

print scream()
# outputs: 'Yes!'
```





Okay! Keep this in mind. We’ll circle back to it shortly.   
记住上面的内容，一会我们还会用得到。

Another interesting property of Python functions is they can be defined... inside another function!  
Python 函数另一个有趣的性质在于它们可以。。。在另一个函数内部定义！  

```python
def talk():

    # You can define a function on the fly in `talk` ...
    # 你可以在 `talk` 函数临时定义一个函数
    def whisper(word='yes'):
        return word.lower() + '...'

    # ... and use it right away!
    # ... 之后直接使用这个函数

    print whisper()

# You call `talk`, that defines `whisper` EVERY TIME you call it, then
# `whisper` is called in `talk`. 
# 你可以调用 `talk` 函数，每次调用这个函数都会定义 `whisper` 函数，并且
# 在 `talk` 函数中调用 `whisper` 函数

talk()
# outputs: 
# "yes..."

# But `whisper` DOES NOT EXIST outside `talk`: 
# 但是 `whisper` 函数在 `talk` 函数外部并不存在： 

try:
    print whisper()
except NameError as e:
    print e
    #outputs : "name 'whisper' is not defined"*
    #Python's functions are objects
```

## Functions references
## 函数引用

Okay, still here? Now the fun part...   
现在是比较有趣的部分。。。

You’ve seen that functions are objects. Therefore, functions:  
你已经知道了函数是 object 对象。此外，函数还：  

- can be assigned to a variable
- can be defined in another function

- 可以像变量一样赋值
- 可以在另一个函数内部定义  

That means that **a function can `return` another function**. Have a look! ☺  
这表示 **函数可以 `return` 另一个函数**。看下面吧！☺   


```python
def getTalk(kind='shout'):

    # We define functions on the fly
    # 我们临时定义一个函数
    def shout(word='yes'):
        return word.capitalize() + '!'

    def whisper(word='yes'):
        return word.lower() + '...'

    # Then we return one of them
    # 然后我们返回上面两个函数中的一个
    if kind == 'shout':
        # We don’t use '()'. We are not calling the function;
        # instead, we’re returning the function object
        # 我们并没有使用 '()' 。因此我们并没有调用函数； 
        # 相反，我们返回了函数对象  
        return shout  
    else:
        return whisper

# How do you use this strange beast?  
# 你该怎样使用这个奇怪的功能呢？  

# Get the function and assign it to a variable   
# 调用这个函数，然后把结果赋值给一个变量 
talk = getTalk()      

# You can see that `talk` is here a function object:   
# 你可以看到 `talk` 是一个函数对象：  
print talk
#outputs : <function shout at 0xb7ea817c>

# The object is the one returned by the function:  
# 这个对象是由一个函数返回的
print talk()
#outputs : Yes!

# And you can even use it directly if you feel wild:  
# 如果你觉得奇怪的话，你甚至可以直接使用它
print getTalk('whisper')()
#outputs : yes...
```

But wait...there’s more!  
但等等...还有一些内容！  

If you can `return` a function, you can pass one as a parameter:  
如果你可以 `return` 一个函数，那么你也可以把函数当作参数传递：   

```python
def doSomethingBefore(func): 
    print 'I do something before then I call the function you gave me'
    print func()

doSomethingBefore(scream)
#outputs: 
#I do something before then I call the function you gave me  
#Yes!
```

Well, you just have everything needed to understand decorators. You see, decorators are “wrappers”, which means that **they let you execute code before and after the function they decorate** without modifying the function itself.   
好，你已经掌握了装饰器所需的全部知识。正如你所见，装饰器是“包装器”，也就是说 **它们允许你在它们装饰的函数的前面和后面运行其他代码** ，而不必修改函数本身。   


## Handcrafted decorators
## 动手制作装饰器 

How you’d do it manually:  
你应该怎样动手制作：   

```python
# A decorator is a function that expects ANOTHER function as parameter  
# 装饰器是把其他函数作为参数的函数
def my_shiny_new_decorator(a_function_to_decorate):

    # Inside, the decorator defines a function on the fly: the wrapper.
    # This function is going to be wrapped around the original function
    # so it can execute code before and after it.
    # 在装饰器内部，装饰器临时创建了一个函数： 包装器。
    # 这个函数把原来的函数包装起来
    # 因此它可以在原函数的前面和后面执行其他代码。  
    def the_wrapper_around_the_original_function():

        # Put here the code you want to be executed BEFORE the original 
        # function is called
        # 把你想在原函数被调用前执行的代码写在这里
        print 'Before the function runs'

        # Call the function here (using parentheses)
        # 在这里调用原函数（使用括号）
        a_function_to_decorate()

        # Put here the code you want to be executed AFTER the original 
        # function is called
        # 把你想在原函数调用后执行的代码写在这里
        print 'After the function runs'

    # At this point, `a_function_to_decorate` HAS NEVER BEEN EXECUTED.
    # We return the wrapper function we have just created.
    # The wrapper contains the function and the code to execute before
    # and after. It’s ready to use!
    # 到目前为止，`a_function_to_decorate` 还从未执行过。
    # 我们返回刚刚创建的包装器
    # 包装器中包含了原函数和在原函数之前/之后执行的代码。现在已经可以使用了！  
    return the_wrapper_around_the_original_function

# Now imagine you create a function you don’t want to ever touch again. 
# 现在想象一下你创建了一个函数，你不想再改动它了。   
def a_stand_alone_function():
    print 'I am a stand alone function, don’t you dare modify me'

a_stand_alone_function() 
#outputs: I am a stand alone function, don't you dare modify me  

# Well, you can decorate it to extend its behavior.
# Just pass it to the decorator, it will wrap it dynamically in 
# any code you want and return you a new function ready to be used:  
# 好的，你可以装饰这个函数来扩展它的功能
# 只需要把它传递给装饰器，之后就会动态地包装在你需要的任何代码中，然后返回一个满足你需求的新函数：   

a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function_decorated()
#outputs:
#Before the function runs
#I am a stand alone function, don't you dare modify me
#After the function runs
```

Now, you probably want that every time you call `a_stand_alone_function`, `a_stand_alone_function_decorated` is called instead. That’s easy, just overwrite `a_stand_alone_function` with the function returned by `my_shiny_new_decorator`:   
现在，你希望每次你调用 `a_stand_alone_function` 的时候，实际上 `a_stand_alone_function_decorated` 会被调用。也就是说，这只是用 `my_shiny_new_decorator` 返回的函数重写了 `a_stand_alone_function` 函数：  

```python
a_stand_alone_function = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function()
#outputs:
#Before the function runs
#I am a stand alone function, don’t you dare modify me
#After the function runs

# And guess what? That’s EXACTLY what decorators do!
# 你猜怎样着？这实际上就是装饰器的原理！

```

## Decorators demystified
## 装饰器解密

The previous example, using the decorator syntax:   
和前面相同的例子，但是使用了装饰器语法：  

```python
@my_shiny_new_decorator
def another_stand_alone_function():
    print 'Leave me alone'

another_stand_alone_function()  
#outputs:  
#Before the function runs
#Leave me alone
#After the function runs
```

Yes, that’s all, it’s that simple. `@decorator` is just a shortcut to:  
就是这样，装饰器就是这么简单。 `@decorator` 只是下面形式的简写：   

```python
another_stand_alone_function = my_shiny_new_decorator(another_stand_alone_function)
```

Decorators are just a pythonic variant of the [decorator design pattern][3]. There are several classic design patterns embedded in Python to ease development (like iterators).   
装饰器只是一个 pythonic 的[装饰器设计模式][3]的变种。Python 中内置了许多种传统的设计模式来简化开发过程（例如迭代器）。  

Of course, you can accumulate decorators:  
当然，你可以叠加多个装饰器：  

```python
def bread(func):
    def wrapper():
        print "</''''''\>"
        func()
        print "<\______/>"
    return wrapper

def ingredients(func):
    def wrapper():
        print '#tomatoes#'
        func()
        print '~salad~'
    return wrapper

def sandwich(food='--ham--'):
    print food

sandwich()
#outputs: --ham--
sandwich = bread(ingredients(sandwich))
sandwich()
#outputs:
#</''''''\>
# #tomatoes#
# --ham--
# ~salad~
#<\______/>
```

Using the Python decorator syntax:  
使用 Python 的装饰器语法：  

```python
@bread
@ingredients
def sandwich(food='--ham--'):
    print food

sandwich()
#outputs:
#</''''''\>
# #tomatoes#
# --ham--
# ~salad~
#<\______/>
```

The order you set the decorators MATTERS:  
你设置装饰器的顺序很重要：    

```python
@ingredients
@bread
def strange_sandwich(food='--ham--'):
    print food

strange_sandwich()
#outputs:
##tomatoes#
#</''''''\>
# --ham--
#<\______/>
# ~salad~
```

----

# Now: to answer the question...  
# 现在：是时候回答问题了。。。 

As a conclusion, you can easily see how to answer the question:   
现在你很容易就知道怎样回答这个问题了：   

```python
# The decorator to make it bold
# 生成粗体(bold)的装饰器
def makebold(fn):
    # The new function the decorator returns
    # 装饰器返回的新函数
    def wrapper():
        # Insertion of some code before and after
        # 在之前和之后插入其他代码
        return '<b>' + fn() + '</b>'
    return wrapper

# The decorator to make it italic
# 生成斜体的装饰器
def makeitalic(fn):
    # The new function the decorator returns
    # 装饰器返回的新函数
    def wrapper():
        # Insertion of some code before and after
        # 在函数执行前后插入一些代码
        return '<i>' + fn() + '</i>'
    return wrapper

@makebold
@makeitalic
def say():
    return 'hello'

print say() 
#outputs: <b><i>hello</i></b>

# This is the exact equivalent to 
# 和上面完全等价的形式
def say():
    return 'hello'
say = makebold(makeitalic(say))

print say() 
#outputs: <b><i>hello</i></b>
```

You can now just leave happy, or burn your brain a little bit more and see advanced uses of decorators.   
现在你该放下轻松的心态，好好看看装饰器的高级使用方法了。

----

# Taking decorators to the next level 
# 把装饰器传到下一层去

## Passing arguments to the decorated function
## 把参数传递给被装饰的函数

```python
# It’s not black magic, you just have to let the wrapper 
# pass the argument: 
# 这并不是黑魔法，你只是让包装器传递参数而已

def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2):
        print 'I got args! Look:', arg1, arg2
        function_to_decorate(arg1, arg2)
    return a_wrapper_accepting_arguments

# Since when you are calling the function returned by the decorator, you are
# calling the wrapper, passing arguments to the wrapper will let it pass them to 
# the decorated function
# 因为当你调用装饰器返回的函数时，实际上你在调用包装器，把参数传递给包装器，这也就完成了把参数传递给装饰器函数
@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print 'My name is', first_name, last_name
    
print_full_name('Peter', 'Venkman')
# outputs:
#I got args! Look: Peter Venkman
#My name is Peter Venkman
```

## Decorating methods
## 装饰器方法

One nifty thing about Python is that methods and functions are really the same.  The only difference is that methods expect that their first argument is a reference to the current object (`self`).   
关于 Python 的一个优点就是方法和函数本质本质上是一样的。二者唯一的区别就是方法的第一个参数是对当前对象的引用 (`self`)。  

That means you can build a decorator for methods the same way! Just remember to take `self` into consideration:  
这意味着你可以按照同样的方式为方法创建装饰器！只要记得考虑 `self` 就可以了：  

```python
def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie = lie - 3 # very friendly, decrease age even more :-)  
        return method_to_decorate(self, lie)
    return wrapper


class Lucy(object):
    def __init__(self):
        self.age = 32
    
    @method_friendly_decorator
    def sayYourAge(self, lie):
        print 'I am {0}, what did you think?'.format(self.age + lie)
        
l = Lucy()
l.sayYourAge(-3)
#outputs: I am 26, what did you think?
```

If you’re making general-purpose decorator--one you’ll apply to any function or method, no matter its arguments--then just use `*args, **kwargs`:   
如果你在创建通用的装饰器 -- 一个适用于任何函数或者方法的装饰器，无论参数是什么 -- 那么只要使用 `*args, **kwargs`就可以了:  

```python
def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    # The wrapper accepts any arguments
    # 包装器接受任何参数
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print 'Do I have args?:'
        print args
        print kwargs
        # Then you unpack the arguments, here *args, **kwargs
        # If you are not familiar with unpacking, check:
        # http://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/
        # 接下来解包参数，也就是这里的 *args, **kwargs
        # 如果你不熟悉解包，可以浏览这个：
        # http://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/
        function_to_decorate(*args, **kwargs)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print 'Python is cool, no argument here.'

function_with_no_argument()
#outputs
#Do I have args?:
#()
#{}
#Python is cool, no argument here.

@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print a, b, c
    
function_with_arguments(1,2,3)
#outputs
#Do I have args?:
#(1, 2, 3)
#{}
#1 2 3 
 
@a_decorator_passing_arbitrary_arguments
def function_with_named_arguments(a, b, c, platypus='Why not ?'):
    print 'Do {0}, {1} and {2} like platypus? {3}'.format(
    a, b, c, platypus)

function_with_named_arguments('Bill', 'Linus', 'Steve', platypus='Indeed!')
#outputs
#Do I have args ? :
#('Bill', 'Linus', 'Steve')
#{'platypus': 'Indeed!'}
#Do Bill, Linus and Steve like platypus? Indeed!


class Mary(object):
    def __init__(self):
        self.age = 31
    
    @a_decorator_passing_arbitrary_arguments
    def sayYourAge(self, lie=-3): # You can now add a default value  你可以在这里添加默认值
        print 'I am {0}, what did you think?'.format(self.age + lie)

m = Mary()
m.sayYourAge()
#outputs
# Do I have args?:
#(<__main__.Mary object at 0xb7d303ac>,)
#{}
#I am 28, what did you think?
```

## Passing arguments to the decorator
## 把参数传递给装饰器

Great, now what would you say about passing arguments to the decorator itself?   
太棒了，现在你对于把参数传递给装饰器本身有什么看法呢？

This can get somewhat twisted, since a decorator must accept a function as an argument. Therefore, you cannot pass the decorated function’s arguments directly to the decorator.  
这可能有点奇怪，因为装饰器必须接收一个函数作为参数。因此，你可能无法直接把装饰器函数作为参数传递给另一个装饰器。  


Before rushing to the solution, let’s write a little reminder:   
在得到答案之前，让我们写一个小的例子：   

```python
# Decorators are ORDINARY functions
# 装饰器是普通函数
def my_decorator(func):
    print 'I am an ordinary function'
    def wrapper():
        print 'I am function returned by the decorator'
        func()
    return wrapper

# Therefore, you can call it without any '@'
# 因此你可以在没有任何 '@' 的情况下调用它

def lazy_function():
    print 'zzzzzzzz'

decorated_function = my_decorator(lazy_function)
#outputs: I am an ordinary function  
            
# It outputs 'I am an ordinary function', because that’s just what you do:
# calling a function. Nothing magic.  
# 上面的函数输出 'I am an ordinary function' ,因为这实际上就是我们直接调用函数的结果。没什么好奇怪的。  

@my_decorator
def lazy_function():
    print 'zzzzzzzz'
    
#outputs: I am an ordinary function
```

It’s exactly the same: `my_decorator` is called. So when you `@my_decorator`, you are telling Python to call the function *labelled by the variable “`my_decorator`”*.  
结果是一模一样的：`my_decorator` 被调用了。因此当你使用 `@my_decorator` 时，Python 会调用 *“`my_decorator`” 变量所代表的函数*。  

This is important! The label you give can point directly to the decorator—**or not**.   
这很重要！你提供的这个变量可以指向装饰器，**也可以不指向**。  

Let’s get evil. ☺  
让我们增加点难度。 ☺   


```python
def decorator_maker():
    
    print 'I make decorators! I am executed only once: '+\
          'when you make me create a decorator.'
            
    def my_decorator(func):
        
        print 'I am a decorator! I am executed only when you decorate a function.'
               
        def wrapped():
            print ('I am the wrapper around the decorated function. '
                  'I am called when you call the decorated function. '
                  'As the wrapper, I return the RESULT of the decorated function.')
            return func()
        
        print 'As the decorator, I return the wrapped function.'
        
        return wrapped
    
    print 'As a decorator maker, I return a decorator'
    return my_decorator
            
# Let’s create a decorator. It’s just a new function after all.  
# 让我们创建一个装饰器。本质上是一个新函数  
new_decorator = decorator_maker()       
#outputs:
#I make decorators! I am executed only once: when you make me create a decorator.
#As a decorator maker, I return a decorator

# Then we decorate the function
# 然后我们装饰下面这个函数
            
def decorated_function():
    print 'I am the decorated function.'
   
decorated_function = new_decorator(decorated_function)
#outputs:
#I am a decorator! I am executed only when you decorate a function.
#As the decorator, I return the wrapped function
     
# Let’s call the function:
# 调用这个函数
decorated_function()
#outputs:
#I am the wrapper around the decorated function. I am called when you call the decorated function.
#As the wrapper, I return the RESULT of the decorated function.
#I am the decorated function.
```

No surprise here.   
没什么意料之外的事情发生。  

Let’s do EXACTLY the same thing, but skip all the pesky intermediate variables:  
我们再做一次上面的事情，只不过这一次取消掉所有的中间变量：  

```python
def decorated_function():
    print 'I am the decorated function.'
decorated_function = decorator_maker()(decorated_function)
#outputs:
#I make decorators! I am executed only once: when you make me create a decorator.
#As a decorator maker, I return a decorator
#I am a decorator! I am executed only when you decorate a function.
#As the decorator, I return the wrapped function.

# Finally:
# 最后：  
decorated_function()    
#outputs:
#I am the wrapper around the decorated function. I am called when you call the decorated function.
#As the wrapper, I return the RESULT of the decorated function.
#I am the decorated function.
```

Let’s make it *even shorter*:  
让它*更短一下*：  

```python
@decorator_maker()
def decorated_function():
    print 'I am the decorated function.'
#outputs:
#I make decorators! I am executed only once: when you make me create a decorator.
#As a decorator maker, I return a decorator
#I am a decorator! I am executed only when you decorate a function.
#As the decorator, I return the wrapped function.

#Eventually:  
#最后： 
decorated_function()    
#outputs:
#I am the wrapper around the decorated function. I am called when you call the decorated function.
#As the wrapper, I return the RESULT of the decorated function.
#I am the decorated function.
```

Hey, did you see that? We used a function call with the `@` syntax! :-)  
你注意到了吗？我们调用了一个 `@` 语法的函数！ :-)    

So, back to decorators with arguments. If we can use functions to generate the decorator on the fly, we can pass arguments to that function, right?  
所以，回到装饰器的参数上面来。如果我们可以使用函数生成一个临时的装饰器，我们也可以把参数传递给那个函数，对吗？  

```python
def decorator_maker_with_arguments(decorator_arg1, decorator_arg2):
    
    print 'I make decorators! And I accept arguments:', decorator_arg1, decorator_arg2
            
    def my_decorator(func):
        # The ability to pass arguments here is a gift from closures.
        # If you are not comfortable with closures, you can assume it’s ok,
        # or read: http://stackoverflow.com/questions/13857/can-you-explain-closures-as-they-relate-to-python  
        # 传递参数的能力来自于闭包
        # 如果你不了解闭包，那也没关系，
        # 或者你也可以阅读 http://stackoverflow.com/questions/13857/can-you-explain-closures-as-they-relate-to-python  
        print 'I am the decorator. Somehow you passed me arguments:', decorator_arg1, decorator_arg2
               
        # Don’t confuse decorator arguments and function arguments!
        # 不要混淆装饰器参数和函数参数！  
        def wrapped(function_arg1, function_arg2):
            print ('I am the wrapper around the decorated function.\n'
                  'I can access all the variables\n'
                  '\t- from the decorator: {0} {1}\n'
                  '\t- from the function call: {2} {3}\n'
                  'Then I can pass them to the decorated function'
                  .format(decorator_arg1, decorator_arg2,
                          function_arg1, function_arg2))
            return func(function_arg1, function_arg2)
        
        return wrapped
    
    return my_decorator

@decorator_maker_with_arguments('Leonard', 'Sheldon')
def decorated_function_with_arguments(function_arg1, function_arg2):
    print ('I am the decorated function and only knows about my arguments: {0}'
           ' {1}'.format(function_arg1, function_arg2))
          
decorated_function_with_arguments('Rajesh', 'Howard')
#outputs:
#I make decorators! And I accept arguments: Leonard Sheldon
#I am the decorator. Somehow you passed me arguments: Leonard Sheldon
#I am the wrapper around the decorated function. 
#I can access all the variables 
#	- from the decorator: Leonard Sheldon 
#	- from the function call: Rajesh Howard 
#Then I can pass them to the decorated function
#I am the decorated function and only knows about my arguments: Rajesh Howard
```

Here it is: a decorator with arguments. Arguments can be set as variable:  
最后得到的就是：带参数的装饰器。参数可以设置为变量：  

```python
c1 = 'Penny'
c2 = 'Leslie'

@decorator_maker_with_arguments('Leonard', c1)
def decorated_function_with_arguments(function_arg1, function_arg2):
    print ('I am the decorated function and only knows about my arguments:'
           ' {0} {1}'.format(function_arg1, function_arg2))

decorated_function_with_arguments(c2, 'Howard')
#outputs:
#I make decorators! And I accept arguments: Leonard Penny
#I am the decorator. Somehow you passed me arguments: Leonard Penny
#I am the wrapper around the decorated function. 
#I can access all the variables 
#	- from the decorator: Leonard Penny 
#	- from the function call: Leslie Howard 
#Then I can pass them to the decorated function
#I am the decorated function and only knows about my arguments: Leslie Howard
```

As you can see, you can pass arguments to the decorator like any function using this trick. You can even use `*args, **kwargs` if you wish. But remember decorators are called **only once**. Just when Python imports the script. You can’t dynamically set the arguments afterwards. When you do `import x`, **the function is already decorated**, so you can’t change anything.   
如你所见，你可以使用这个技巧向装饰器传递参数，就像是向普通函数传递一样。如果你愿意的话，你甚至可以使用 `*args, **kwargs`。但记住，装饰器只会被调用**一次**。只在 Python 导入脚本的时候运行。在这之后你就无法动态设置参数了。当你执行 `import x` 之后，**函数已经被装饰了**,因此之后你无法改变任何东西。   

----

# Let’s practice: decorating a decorator
# 练习： 装饰一个装饰器 

Okay, as a bonus, I’ll give you a snippet to make any decorator accept generically any argument. After all, in order to accept arguments, we created our decorator using another function.   
好的，作为奖励，我会提供你一段代码允许装饰器接收任何参数。毕竟，为了接收参数，我们会用另一个函数创建装饰器。   

We wrapped the decorator.  
我们包装一下装饰器。  

Anything else we saw recently that wrapped function?  
我们最近看到的有包装函数的还有什么呢？

Oh yes, decorators!
对了，就是装饰器！  

Let’s have some fun and write a decorator for the decorators:  
让我们做点有趣的事，写一个装饰器的装饰器：   

```python
def decorator_with_args(decorator_to_enhance):
    """ 
    This function is supposed to be used as a decorator.
    It must decorate an other function, that is intended to be used as a decorator.
    Take a cup of coffee.
    It will allow any decorator to accept an arbitrary number of arguments,
    saving you the headache to remember how to do that every time.
    """
    """
    这个函数是被用作装饰器。
    它会装饰其他函数，被装饰的函数也是一个装饰器。
    喝杯咖啡吧。
    它允许任何装饰器接收任意个参数，
    这样你就不会为每次都要考虑怎样处理而头疼了
    """
    # We use the same trick we did to pass arguments
    # 我们使用同样的技巧来传递参数
    def decorator_maker(*args, **kwargs):
       
        # We create on the fly a decorator that accepts only a function
        # but keeps the passed arguments from the maker.
        # 我们创建一个仅可以接收一个函数的临时装饰器
        # 但无法从 maker 传递参数 
        def decorator_wrapper(func):
       
            # We return the result of the original decorator, which, after all, 
            # IS JUST AN ORDINARY FUNCTION (which returns a function).
            # Only pitfall: the decorator must have this specific signature or it won’t work: 
            # 原装饰器返回的结果
            # 其实只是一个普通函数（这个函数返回一个函数）。
            # 唯一的陷阱是： 装饰器必须有特定的格式，否则无法运行：   
            return decorator_to_enhance(func, *args, **kwargs)
        
        return decorator_wrapper
    
    return decorator_maker
```

It can be used as follows: 
可以像下面这样使用：   

```python        
# You create the function you will use as a decorator. And stick a decorator on it :-)
# Don’t forget, the signature is `decorator(func, *args, **kwargs)`   
# 创建一个用作装饰器的函数。然后加上一个装饰器  :-)  
# 不要忘记，格式是  `decorator(func, *args, **kwargs)`  
@decorator_with_args 
def decorated_decorator(func, *args, **kwargs): 
    def wrapper(function_arg1, function_arg2):
        print 'Decorated with', args, kwargs
        return func(function_arg1, function_arg2)
    return wrapper
    
# Then you decorate the functions you wish with your brand new decorated decorator.  
# 然后用全新的装饰器装饰你的函数。    

@decorated_decorator(42, 404, 1024)
def decorated_function(function_arg1, function_arg2):
    print 'Hello', function_arg1, function_arg2

decorated_function('Universe and', 'everything')
#outputs:
#Decorated with (42, 404, 1024) {}
#Hello Universe and everything

# Whoooot!
```

I know, the last time you had this feeling, it was after listening a guy saying: “before understanding recursion, you must first understand recursion”. But now, don’t you feel good about mastering this?   
我知道，上次你有这种感觉，是在听一个人说：“在理解递归之前，你必须首先理解递归” 时。但现在，掌握了这个之后你不觉得很棒吗？   

----

# Best practices: decorators
# 最佳实践： 装饰器

- Decorators were introduced in Python 2.4, so be sure your code will be run on >= 2.4. 
- Decorators slow down the function call. Keep that in mind.
- **You cannot un-decorate a function.** (There *are* hacks to create decorators that can be removed, but nobody uses them.) So once a function is decorated, it’s decorated *for all the code*.
- Decorators wrap functions, which can make them hard to debug.  (This gets better from Python >= 2.5; see below.) 
- 装饰器在 Python 2.4 引进，因此确保你的代码运行的 Python 版本 >=2.4 
- 装饰器会拖慢函数调用速度。请牢记
- **你无法解除装饰一个函数。** （确实 *有* 一些技巧可以创建允许解除装饰的装饰器，但是没人会使用它们。）因此一旦函数被装饰了，*所有这个函数的代码*就都装饰了。
- 装饰器包装函数，会使得函数更难调试。 （从 Python >=2.5 有所好转；看下文。）  

The `functools` module was introduced in Python 2.5. It includes the function `functools.wraps()`, which copies the name, module, and docstring of the decorated function to its wrapper.    
`functools` 模块在 Python 2.5 引进。模块中包含了函数 `functools.wraps()` ，这个函数会把被装饰函数的名字，模块名，docstring 都复制到它的包装器中。  

(Fun fact: `functools.wraps()` is a decorator! ☺)  
（有趣的事情是： `functools.wraps()` 是个装饰器！☺）

```python
# For debugging, the stacktrace prints you the function __name__
# 至于调试，stacktrace 输出函数的 __name__
def foo():
    print 'foo'
    
print foo.__name__
#outputs: foo
    
# With a decorator, it gets messy    
# 有了装饰器之后，有点混乱   
def bar(func):
    def wrapper():
        print 'bar'
        return func()
    return wrapper

@bar
def foo():
    print 'foo'

print foo.__name__
#outputs: wrapper

# `functools` can help with that 
# `functools` 可以改善上面的情况

import functools

def bar(func):
    # We say that `wrapper`, is wrapping `func`
    # and the magic begins
    # 我们认为 `wrapper` 正在包装 `func` 
    # 神奇的事情发生了 
    @functools.wraps(func)
    def wrapper():
        print 'bar'
        return func()
    return wrapper

@bar
def foo():
    print 'foo'

print foo.__name__
#outputs: foo
```

----

# How can the decorators be useful?  
# 怎样使装饰器变得有用？  

**Now the big question:** What can I use decorators for?   
**现在最大的问题是：** 我可以用装饰器来干嘛？  

Seem cool and powerful, but a practical example would be great. Well, there are 1000 possibilities. Classic uses are extending a function behavior from an external lib (you can’t modify it), or for debugging (you don’t want to modify it because it’s temporary).   
装饰器看起来很酷，很强大，但有一个实用的例子就更好了。大概有 1000 种可能的例子。常见的使用方法是扩展一个外部库函数（你无法修改）的行为，或者用来调试外部库函数（你不想修改它，因为它是临时函数）。   

You can use them to extend several functions in a DRY’s way, like so:   
你可以使用装饰器以 DRY(Don't Repeat Yourself,不重复自己) 的方式扩展函数，就像这样：  

```python
def benchmark(func):
    """
    A decorator that prints the time a function takes
    to execute.
    """
    """
    一个用来输出函数执行时间的装饰器
    """
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print func.__name__, time.clock()-t
        return res
    return wrapper


def logging(func):
    """
    A decorator that logs the activity of the script.
    (it actually just prints it, but it could be logging!)
    """
    """
    一个用来记录脚本活动的装饰器。
    （实际上只是打印出来，但可以输出到日志！）
    """
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print func.__name__, args, kwargs
        return res
    return wrapper


def counter(func):
    """
    A decorator that counts and prints the number of times a function has been executed
    """
    """
    一个用来统计并输出函数执行次数的装饰器
    """
    def wrapper(*args, **kwargs):
        wrapper.count = wrapper.count + 1
        res = func(*args, **kwargs)
        print '{0} has been used: {1}x'.format(func.__name__, wrapper.count)
        return res
    wrapper.count = 0
    return wrapper

@counter
@benchmark
@logging
def reverse_string(string):
    return str(reversed(string))

print reverse_string('Able was I ere I saw Elba')
print reverse_string('A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a jar, sore hats, a peon, a canal: Panama!')

#outputs:
#reverse_string ('Able was I ere I saw Elba',) {}
#wrapper 0.0
#wrapper has been used: 1x 
#ablE was I ere I saw elbA
#reverse_string ('A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a jar, sore hats, a peon, a canal: Panama!',) {}
#wrapper 0.0
#wrapper has been used: 2x
#!amanaP :lanac a ,noep a ,stah eros ,raj a ,hsac ,oloR a ,tur a ,mapS ,snip ,eperc a ,)lemac a ro( niaga gab ananab a ,gat a ,nat a ,gab ananab a ,gag a ,inoracam ,elacrep ,epins ,spam ,arutaroloc a ,shajar ,soreh ,atsap ,eonac a ,nalp a ,nam A
```

Of course the good thing with decorators is that you can use them right away on almost anything without rewriting. DRY, I said:  
当然，装饰器的优点就在于你可以在不重写函数的前提下，使用在几乎任何函数上。DRY（Don't Repeat Yourself,不要重复你自己)，正如我说的：  

```python
@counter
@benchmark
@logging
def get_random_futurama_quote():
    from urllib import urlopen
    result = urlopen('http://subfusion.net/cgi-bin/quote.pl?quote=futurama').read()
    try:
        value = result.split('<br><b><hr><br>')[1].split('<br><br><hr>')[0]
        return value.strip()
    except:
        return 'No, I’m ... doesn’t!'

    
print get_random_futurama_quote()
print get_random_futurama_quote()

#outputs:
#get_random_futurama_quote () {}
#wrapper 0.02
#wrapper has been used: 1x
#The laws of science be a harsh mistress.
#get_random_futurama_quote () {}
#wrapper 0.01
#wrapper has been used: 2x
#Curse you, merciful Poseidon!
```

Python itself provides several decorators: `property`, `staticmethod`, etc.   
Python 本身提供了几种装饰器：  `property` ，`staticmethod`，等

- Django uses decorators to manage caching and view permissions. 
- Twisted to fake inlining asynchronous functions calls.
- Django 使用装饰器来管理缓存，查看权限。 
- Twisted 用它来伪造内联异步函数调用。   

This really is a large playground.  
装饰器的用途确实很广。  


  [1]: http://stackoverflow.com/questions/231767/can-somebody-explain-me-the-python-yield-statement/231855#231855
  [2]: http://stackoverflow.com/questions/739654/understanding-python-decorators#answer-739665
  [3]: http://en.wikipedia.org/wiki/Decorator_pattern
 
