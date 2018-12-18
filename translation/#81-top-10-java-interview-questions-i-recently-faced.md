---
translator: http://www.jobbole.com/members/q2451432615/
reviewer: http://www.jobbole.com/members/hanxiaomax/
via: https://dzone.com/articles/top-10-java-interview-questions-that-i-recently-fa
---

by Zoltan Raffai     ·  Aug. 27, 18 · Java Zone · Presentation     

Recently, I participate in a few Java-based interviews to keep me fresh. Suddenly, I had an idea that I would like to share my experiences with you all. I hope I can help by sharing the top 10 Java interview questions that I faced in the recent months.

最近，我参加了一些 Java 面试以保持新鲜感。我突然萌生了一个想法，就是向大家分享我的经历。我会在此分享最近几个月我在 Java 面试中遇到最多的十个问题，希望能帮助到大家。

## [Top 10 Java Interview Questions I Recently Faced](https://dzone.com/articles/top-10-java-interview-questions-that-i-recently-fa)

## 常被问到的十个 Java 面试题

In this presentation, I tried to collect you the most interesting and common questions. Furthermore, I will provide you with the correct answers. 

在这篇文章中，我试图收录最有趣和最常见的问题。此外，我将为您提供正确的答案。

So, let’s take a look at these questions.

接下来，就让我们来看看这些问题。

### 1. Evaluate Yourself on a Scale of 10 — How Good Are you in Java?

### 以满分十分来评估自己————你有多擅长 Java？   

This is a very tricky one if you are not exactly sure about yourself or your level of proficiency in Java. If that sounds familiar, you should shoot a bit lower. After this, you will probably get questions according to the level you've admitted to. Hence, if you, for example, said 10 and cannot answer a fairly difficult question, it will be a drawback. 

如果你并不完全确信你自己或是你对 Java 的熟练程度，那么这会是一个非常棘手的问题。如果有这种情况，你应该把打分调低一点。之后，你大概会得到与你承认的水平相符的问题。因此，假如你给自己满分，却不能回答一个有点难的问题，那将会对你不利。

### 2. Explain the Differences Between Java 7 and 8.

### 阐述 Java 7 和 Java 8 的区别。   

To be honest, there are a lot of differences. Here, if you can list the most significant ones, it should be enough. You should explain the new features in Java 8. For the full list, visit the original website here: [Java 8 JDK](https://www.oracle.com/technetwork/java/javase/8-whats-new-2157071.html).

实话说，两者有很多不同。如果你能列出最重要的，应该就足够了。你应该解释 Java 8 中的新功能。想要获得完整清单，请访问官网：[Java 8 JDK](https://www.oracle.com/technetwork/java/javase/8-whats-new-2157071.html)。

The most important ones that you should know are:

你应该知道以下几个重点：

- **Lambda expressions**, a new language feature, has been introduced in this release. Lambda expressions enable you to treat functionality as a method argument or code as data. Lambda expressions let you express instances of single-method interfaces (referred to as functional interfaces) more compactly.   
 **lambda 表达式**，Java 8 版本引入的一个新特性。lambda 表达式允许你将功能当作方法参数或将代码当作数据。lambda 表达式还能让你以更简洁的方式表示只有一个方法的接口 (称为函数式接口) 的实例。

- **Method references** provide easy-to-read lambda expressions for methods that already have a name.   
 **方法引用**为已命名方法提供了易于阅读的 lambda 表达式。

- **Default methods** enable new functionality to be added to the interfaces of libraries and ensure binary compatibility with code written for older versions of those interfaces.   
 **默认方法**支持将新功能添加到类库中的接口，并确保与基于这些接口的旧版本的代码的二进制兼容性。

- **Repeating annotations** provide the ability to apply the same annotation type more than once to the same declaration or type use.  
 **重复注解**支持在同一声明或类型上多次应用同一注解类型。

- **Type annotations** provide the ability to apply an annotation anywhere a type is used and not just on a declaration. Used with a pluggable type system, this feature enables improved type checking of your code.    
 **类型注解**支持在任何使用类型的地方应用注解，而不仅限于声明。此特性与可插入型系统一起使用时，可增强对代码的类型检查。

### 3. Which Type of Collections Do you Know About?

### 你了解哪些集合类型？

Here you should know about the most important ones:

你应该知道以下几个最重要的类型：

- `ArrayList` 
- `LinkedList` 
- `HashMap` 
- `HashSet`

After this, you will probably get some questions about when you should use this specific one, what are the benefits over the other one, how it stores data, and what data structure is working behind the scenes.

之后，你可能会被问到这样一些问题，比如何时应该使用此种特定类型，它比其他的好在哪里，它是怎么存储数据的以及隐匿在其后的数据结构是什么。

Here, the best way is to learn about these collection types as much as possible, because the variety of questions is almost inexhaustible.

最好的方法是尽可能多地了解这些集合类型，因为这类问题几乎是无穷尽的。

### 4. What Methods Does the Object Class Have?

### Object 类包含哪些方法？

This a very common question asked to determine how familiar you are with the basics. These are the methods that every object has:

这是一个非常常见的问题，用来确定你对基础知识的熟悉程度。以下是每个对象都具有的方法:

The `Object` class, in the `java.lang` package, sits at the top of the class hierarchy tree. Every class is a descendant, direct or indirect, of the `Object` class. Every class you use or write inherits the instance methods of `Object`. You need not use any of these methods, but, if you choose to do so, you may need to override them with code that is specific to your class. The methods inherited from `Object` that are discussed in this section are:

在`java.lang`包中，`Object`类位于类层次结构的顶端。每个类都是`Object`类直接或间接的子类。你使用或编写的每个类都继承了`Object`类中的实例方法。你并不需要使用这些方法中的任何一种，但是，如果你选择这样做，则可能需要用你的类的特定代码来重写这些方法。以下是本节所讨论的从`Object`类中继承的方法:

- `protected Object clone() throws CloneNotSupportedException`  
Creates and returns a copy of this object.  
创建并返回此对象的副本。

- `public boolean equals(Object obj)`  
Indicates whether some other object is “equal to” this one.   
判断另一对象与此对象是否「相等」。

- `protected void finalize() throws Throwable`    
Called by the garbage collector on an object when garbage collection determines that there are no more references to the object.        
当垃圾回收机制确定该对象不再被调用时，垃圾回收器会调用此方法。

- `public final Class getClass()`  
Returns the runtime class of an object.   
返回此对象的运行时类。

- `public int hashCode()`  
Returns a hash code value for the object.   
返回此对象的散列码值。

- `public String toString()`  
Returns a string representation of the object.  
返回此对象的字符串表示形式。

The `notify`, `notifyAll`, and `wait` methods of `Object` all play a part in synchronizing the activities of independently running threads in a program, which is discussed in a later lesson and won’t be covered here. There are five of these methods:

`Object`类的`notify`，`notifyAll`和`wait`方法都在同步程序中独立运行线程的活动方面发挥了作用，这将在后面的课程中讨论，在此不做介绍。其中有五种方法:

- `public final void notify()`
- `public final void notifyAll()`
- `public final void wait()`
- `public final void wait(long timeout)`
- `public final void wait(long timeout, int nanos)`

### 5. Why Is the String Object Immutable in Java?

### 为什么 String 对象是不可变的？

1. [String pool](https://www.journaldev.com/797/what-is-java-string-pool) is possible only because String is immutable in Java. This way, Java Runtime saves a lot of Java heap space, because different String variables can refer to the same String variable in the pool. If String is not immutable, then String interning would not have been possible, because if any variable would have changed the value, it would have been reflected in other variables.    
[字符串池](https://www.journaldev.com/797/what-is-java-string-pool)之所以可能，就是因为字符串在 Java 中是不可变的。由此 Java 运行时环境节省了大量堆空间，因为不同的 String 变量可以引用池中的同一 String 变量。如果 String 不是不可变的, 则字符串驻留（[String interning](https://en.wikipedia.org/wiki/String_interning)）将是不可能的，因为一旦任一变量更改所引用的String对象的值，它也会反映在其他变量中。

2. If String is not immutable, then it would cause a severe security threat to the application. For example, database usernames and passwords are passed as String to get the database connection, in-[socket programming](https://www.journaldev.com/741/java-socket-programming-server-client) host, and port details passed as String. Since String is immutable, it's value can’t be changed. Otherwise, any hacker could change the referenced value to cause security issues in the application.      
如果字符串不是不可变的，那么它可能会对应用程序造成严重的安全威胁。例如，数据库用户名和密码都作为 String 传递以获取数据库连接，[Socket 编程](https://www.journaldev.com/741/java-socket-programming-server-client)的主机和端口信息也是如此。由于字符串是不可变的，因此其值不能被更改。否则，任何黑客都可以篡改其引用的值，这会导致应用程序中的安全问题。

3. Since String is immutable, it is safe for [multithreading](https://www.journaldev.com/1079/multithreading-in-java), and a single String instance can be shared across different threads. This avoids the usage of synchronization for thread safety; Strings are implicitly thread safe.       
由于 String 是不可变的，因此它对与[多线程处理](https://www.journaldev.com/1079/multithreading-in-java)来说是安全的，并且可以在不同的线程之间共享单个 String 实例。这避免了为线程安全使用同步；字符串是隐式线程安全的。

4. Strings are used in the [Java classloader](https://www.journaldev.com/349/java-classloader), and immutability provides security that the correct class is getting loaded by the `Classloader`. For example, think of an instance where you are trying to load the `java.sql.Connection`  class but the referenced value is changed to `myhacked.Connection` class and can do unwanted things to your database.  
字符串被用在 Java 类加载器中，其不可变性为[类加载器](https://www.journaldev.com/349/java-classloader)加载正确的类提供了安全性。否则的话，请考虑这样一个危险的情况，在你尝试加载`java.sql.Connection`类时，你引用的值却被更改为`myhacked.Connection`，并且它能对数据库执行你不需要的操作。

5. Since String is immutable, its hashcode is cached at the time of creation, and it doesn’t need to be calculated again. This makes it a great candidate for a key in a map, and it’s processing is fast than other `HashMap` key objects. This is why String is the most-used object of `HashMap` keys.     
由于 String 是不可变的，因此在它被创建时其散列码就被缓存，不需要再次计算。这使得它成为映射中键的理想对象，它的处理速度比其他`HashMap`键类型快。这就是为什么 String 是`HashMap`中最常用的键类型。

[Why is String immutable in Java?](https://www.journaldev.com/802/string-immutable-final-java) Click here to learn more.

[为什么 Java 中的字符串不可变？](https://www.journaldev.com/802/string-immutable-final-java)点击这里了解更多。

### 6. What Is the Difference Between Final, Finally, and Finalize?

### final，finally，和 finalize 三者之间有什么不同？

This question is my favorite one.

这是我最喜欢的问题。

- The `final` keyword is used in several contexts to define an entity that can only be assigned once.   
`final`关键字用于在多个语境下定义只能分配一次的实体。

- **The Java** `finally` **block** is a block that is used to execute important code, such as closing connection, stream, etc. The Java `finally` block is always executed, whether the exception is handled or not. Java `finally` block follows the `try` or `catch` block.    
**`finally`代码块**是用于执行重要代码 (如关闭连接、流等) 的代码块。无论是否处理异常，`finally`代码块总会被执行。`finally`代码块紧随`try`代码块或`catch`代码块。

- This is a **method** that the `GarbageCollector` always calls just **before** the deletion/destroying the object, which is eligible for Garbage Collection to perform **clean-up activity**.    
这是在删除或销毁对象**之前**垃圾回收器总会调用的**方法**，该方法使得垃圾回收机制能够执行**清理活动**。

### 7. What Is the Diamond Problem?

### 什么是菱形继承问题？

The diamond problem reflects why we are not allowed to do multiple inheritances in Java. If there are two class that have a shared superclass with a specific method, it is overridden in both subclasses. Then, if you decide to inherit from that two `subClasses` , then if you would like to call that method, the language can’t decide which one you would like to call.

菱形继承问题反映了为什么在 Java 中我们不被允许实现多继承。如果有两个类共同继承一个有特定方法的超类，那么该方法会被两个子类重写。然后，如果你决定同时继承这两个子类，那么在你调用该重写方法时，编译器不能识别你要调用哪个子类的方法。

![blockchain](https://i2.wp.com/www.zoltanraffai.com/blog/wp-content/uploads/2018/08/diamond-problem-multiple-inheritance.png?w=570&ssl=1)

We refer to this problem as the _diamond problem_. It gets its name from the above image, which describes the caveat.

我们把这个问题称为 _菱形继承问题_ 。上图对它作了说明，它也得名于此。

### 8. How Can You Make a Class Immutable?

### 如何使一个类不可变？

I think this is a quite difficult question. You need to do several modifications on your class to achive immutability:

我认为这是一个相当困难的问题。您需要对类进行多次修改，以实现不可变性:

1. Declare the class as final so it can’t be extended.   
将类声明为`final`，使其无法被继承。
1. Make all fields private so that direct access is not allowed.   
所有域都用`private`修饰，不允许直接访问。
1. Don’t provide setter methods for variables.  
不提供变量的`setter`方法。
1. Make all **mutable fields final** so that it’s value can be assigned only once.  
所有**可变域**都用`final`修饰, 使它的值只能分配一次。
1. Initialize all the fields via a constructor performing a deep copy.  
通过构造函数执行深克隆初始化所有域。
1. Perform cloning of objects in the getter methods to return a copy rather than returning the actual object reference.  
对`getter`方法获取的对象执行克隆以返回副本，而不是返回实际的对象引用。

### 9. What Does Singleton Mean?

### 什么是单例模式？

A singleton is a class that allows only a single instance of itself to be created and gives access to that created instance. It contains static variables that can accommodate unique and private instances of itself. It is used in scenarios when a user wants to restrict instantiation of a class to only one object. This is helpful usually when a single object is required to coordinate actions across a system.

单例模式是指一个类仅允许创建其自身的一个实例，并提供对该实例的访问权限。它包含静态变量，可以容纳其自身的唯一和私有实例。它被应用于这种场景——用户希望类的实例被约束为一个对象。在需要单个对象来协调整个系统时，它会很有帮助。

### 10. What Is a Dependency Injection?

### 什么是依赖注入？

This is the **number one question** you have to know if you work in Java EE or Spring. You can check out my article explaining this further here: [What is a Dependency Injection?](https://www.zoltanraffai.com/blog/different-dependency-injection-techniques/)

这是你必须知道的**首要问题**, 无论你是使用 Java EE 还是 Spring 框架。你可以看看我的文章，其中进一步地解释了这一点: [什么是依赖注入？](https://www.zoltanraffai.com/blog/different-dependency-injection-techniques/)

### Summary

### 总结

In this article, we talked about the top 10 Java interview questions, which are, I think, the most important nowadays based on my experiences. If you know about these, I’m sure that you will have a big advantage during your recruitment process.

在本文中,我们讨论了最常见的十个 Java 面试题——在我看来这是根据我的经验总结出的时下最重要的问题。如果你了解这些问题，我相信你能在面试中获得很大的优势。

Hope I could help you! If you have similar experiences in this topic, or you have some success stories, don’t hesitate to share them in the comments below.

希望我可以帮助到你！如果你有关于这个话题的类似经验，或者有一些成功的故事，不要犹豫，在下面的评论区中分享它们。

Cheers!

再见！
