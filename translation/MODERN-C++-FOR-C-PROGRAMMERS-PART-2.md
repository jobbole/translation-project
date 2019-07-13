---
editor: hanxiaomax
published: false
title: MODERN C++ FOR C PROGRAMMERS-PART-2
---

## Namespaces
## 命名空间

Namespaces allow things with identical names to live side by side. This is of immediate relevance to us since C++ defines a lot of functions and classes that might collide with names you are already using in C. Because of this, the C++ libraries live in the std:: namespace, making it far easier to compile your C code as C++.

命名空间允许相同命名的事物（变量，函数，类）同时存在。这和我们息息相关是因为 C++ 定义了很多函数和类，以至于可能会有和 C 语言同名函数产生命名冲突的可能。因此 C++ 标准库被定义在`std::`命名空间中，这使得我们将 C 语言代码看作 C++ 代码进行编译变得更加简单。

To save a lot of typing, it is possible to import the entire std:: namespace with using namespace std, or to select individual names: using std::thread.

为了减少繁琐的输入，我们可以使用 `using namespace std` 直接将 `std::`导入，或者可以选择单独的名字 `using std::thread`。

C++ does have some keywords itself like this, class, throw, catch and reinterpret_cast that could collide with existing C code.

C++ 也有一些自己的关键字，例如`this`,`class`,`throw`,`catch`和`reinterpret_cast`，这些也可以和已经存在的 C 代码产生冲突。


## Classes
## 类

An older name of C++ was ‘C with classes’, and consisted of a translator that converted this new C++ into plain C. Interestingly enough this translator itself was written in ‘C with classes’.

C++ 有个曾用名，叫做“有类的C语言” （C with classes），同时它包含一个可以将 C++ 翻译为 C 的翻译器。有意思的是，这个翻译器就是使用“有类的C语言”编写的。

Most advanced C projects already use classes almost exactly like C++. In its simplest form, a class is nothing more than a struct with some calling conventions. (Inheritance & virtual functions complicate the picture, and these optional techniques will be discussed in part 3).

很多高级的 C 语言项目都已经在使用类了，几乎和 C++ 完全一样。对于一个类来讲，其最简单的形式其实就是一个结构体外加一些调用的规则（继承和虚函数使其变得更加复杂，这些非必须的技术我们会在第三篇文章中讨论）。

Typical modern C code will define a struct that describes something and then have a bunch of functions that accept a pointer to that struct as the first parameter:

一个典型的现代 C 语言代码会定义一个结构体来描述一个对象，并且定义一系列的函数，其第一个参数的类型就是该结构体类型的指针。

```cpp
struct Circle
{
	int x, y;
	int size;
	Canvas* canvas;
	...
};

void setCanvas(Circle* circle, Canvas* canvas);
void positionCircle(Circle* circle, int x, int y);
void paintCircle(Circle* circle);
```


Many C projects will in fact even make (part of) these structs opaque, indicating that there are internals that API users should not see. This is done by forward declaring a struct in the .h, but never defining it. The sqlite3 handle is a great example of this technique.

事实上，很多 C 语言项目会将结构体的一部分设置为“不可见”的，表示这些部分属于内部变量，不应对仅仅期望使用其 API 的用户可见。使结构体“不可见”的方法是事先在 .h 文件中声明该结构体，但是不去实际定义它。sqlite3 的 handle 是本技巧的一个绝佳的例子。

A C++ class is laid out just like the struct above, and in fact, if it contains methods (member functions), these internally get called in exactly the same way:

C++ 中的类在布局上和上述结构体很相似，实际上，如果其包含方法（成员函数）的话，函数调用也是是完全一样的：

```cpp
class Circle
{
public:
	Circle(Canvas* canvas);  // "constructor"
	void position(int x, int y);
	void paint();
private:
	int d_x, d_y;
	int d_size;
	Canvas* d_canvas;
};

void Circle::paint()
{
	d_canvas->drawCircle(d_x, d_y, d_size);
}

```

If we look “under water” Circle::position(1, 2) is actually called as Circle::position(Circle* this, int x, int y). There is no more magic (or overhead) to it than that. In addition, the Circle::paint and Circle::position functions have d_x, d_y, d_size and d_canvas in scope.

如果我们透过现象看本质，`Circle::position(1, 2)` 实际上是调用了 `Circle::position(Circle* this, int x, int y)`，没啥特别的地方，也没什么额外的开销。另外，`d_x`, `d_y`, `d_size` 和 `d_canvas` 这些变量在 `Circle::paint` 和 `Circle::position` 的作用域中是可见的。


The one difference is that these ‘private member variables’ are not accessible from the outside. This may be useful for example when any change in x needs to be coordinated with the Canvas, and we don’t want users to change x without us knowing it. As noted, many C projects achieve the same opaqueness with tricks - this is just an easier way of doing it.

C++ 的类与 C 语言结构体不同的地方之一，是“私有成员变量”在类的外部无法访问。在一些场景下，这个功能是很有用的。例如，我们希望坐标 x 的改变要与画布同步，因此我们并不希望用户在我们不知情的情况下，从外部改变 x 坐标。正如上文提到的，很多 C 语言项目通过一些技巧实现了变量的私有 —— C++ 只是简化了这一操作罢了。

Up to this point, a class was nothing but syntactic sugar and some scoping rules. However..

从目前介绍的这些内容来看，C++ 的类其实就是一种语法糖以及一些作用域规则。但是。。。


## Resource Acquisition Is Initialization (RAII)
## 资源获取即初始化（ Resource Acquisition Is Initialization ）—— RAII

Most modern languages perform garbage collection because it is apparently too hard to keep track of memory. This leads to periodic GC runs which have the potential to ‘stop the world’. Even though the state of the art is improving, GC remains a fraught subject especially in a many-core world.

大多数的现代编程语言都会进行垃圾回收，因为追踪并管理内存显然非常困难。但这也使得周期性的垃圾回收具有“使程序停止”的功能。即便现如今的垃圾回收技术有了长足的进步，在多核领域，垃圾回收仍然是让人操心的话题。

Although C and C++ do not do garbage collection, it remains true that it is exceptionally hard to keep track of each and every memory allocation under all (error) conditions. C++ has sophisticated ways to help you and these are built on the primitives called Constructors and Destructors.

C 和 C++ 并不进行垃圾回收，在任何（或发生错误）的场景下，追踪管理每一块分配的内存是非常非常困难的。为了帮助你解决这一问题， C++ 提供了一套复杂又精密的机制 —— 构造函数和析构函数。


SmartFP is an example that we’ll beef up in following sections so it becomes actually useful and safe:
我们将使用 SmartFP （智能文件指针） 这一例子，并在后续的文章中逐步扩展它，使其变得功能强大且安全： 

```cpp
struct SmartFP
{
	SmartFP(const char* fname, const char* mode)
	{
		d_fp = fopen(fname, mode);
	}
	~SmartFP()
	{
		if(d_fp)
			fclose(d_fp);
	}
	FILE* d_fp;
};
```

Note: a struct is the same as a class, except everything is ‘public’.
注意：C++ 中的结构体和类是相似的，只不过它默认所有成员都是 public 类型的。

Typical use of SmartFP:
SmartFP 的一个典型应用：

```cpp
void func()
{
	SmartFP fp("/etc/passwd", "r");
	if(!fp.d_fp)
		// 异常处理

	char line[512];
	while(fgets(line, sizeof(line), fp.d_fp)) {
		// 处理每一行
	}	
	// 注意，文件没有关闭
}
```

As written like this, the actual call to fopen() happens when the SmartFP object is instantiated. This calls the constructor, which has the same name as the struct itself: SmartFP.

如果我们这样编写代码的话，当 SmartFP 类型的对象初始化时，`fopen()` 会自动被调用。这就是构造函数，构造函数和结构体同名：SmartFP。

We can then use the FILE* that is stored within the class as usual. Finally, when fp goes out of scope, its destructor SmartFP::~SmartFP() gets called, which will fclose() for us if d_fp was opened successfully in the constructor.

我们可以像平常一样，使用储存在类内部的 `FILE*`。最后，当 `fp` 的作用域结束时，它的析构函数 `SmartFP::~SmartFP()` 会被调用，这会间接调用 `fclose()` 函数，如果 `d_fp` 在之前的构造函数中正确的打开了文件，此处就会关闭它。

Written like this, the code has two huge advantages: 1) the FILE pointer will never leak 2) we know exactly when it will be closed. Languages with garbage collection also guarantee ‘1’, but struggle or require real work to deliver ‘2’.

这样编写代码有两个极大的好处：
1. FILE 指针永远不会泄露
2. 我们可以明确的知道文件何时被关闭。

具有垃圾回收机制的语言，同样可以保证第一点，但是会纠结于第二点，或者说为了做到第二点需要额外的工作。

This technique to use classes or structs with constructors and destructors to own resources is called Resource Acquisition Is Initialization or RAII, and it is used widely. It is quite common for even larger C++ projects to not contain a single call to new or delete (or malloc/free) outside of a constructor/destructor pair. Or at all, in fact.

通过构造函数和析构函数来管理我们的资源，这种使用类或者结构体的技术就叫做：资源获取即初始化（ Resource Acquisition Is Initialization ）或 简称为  RAII。这是一种被广泛使用的技术。对于大型 C++ 项目，使用这种方法可以保证不用单独调用 new 或者 delete (或 malloc/free)在构造和析构函数外申请和释放内存。

## Smart pointers
## 智能指针

Memory leaks are the bane of every project. Even with garbage collection it is possible to keep gigabytes of memory in use for a single window displaying chat messages.

对所有的项目来说，内存泄露都将是一场灾难。即使有了垃圾回收，对于一个对话框消息来说，也有可能占据大量的内存。

C++ offers a number of so called smart pointers that can help, each with its own (dis)advantages. The most “do what I want” smart pointer is std::shared_ptr and in its most basic form it can be used like this:

C++ 提供了一些被称作智能指针的对象来帮我们解决这个问题，每种智能指针都有其自己的优缺点。束缚最少的智能指针是 `std::shared_ptr` ，其最基本的用法如下：

```cpp
void func(Canvas* canvas)
{
	std::shared_ptr<Circle> ptr(new Circle(canvas));
	// 更好的做法 :
	auto ptr = std::make_shared<Circle>(canvas)
}
```

The first form shows the C++ way of doing malloc, in this case allocating memory for a Circle instance, and constructing it with the canvas parameter. As noted, most modern C++ projects rarely use “naked new” statements but mostly wrap them in infrastructure that takes care of (de)allocation.

第一种形式展示了 C++ 是如何进行 malloc 的，在这个例子中，首先给 Circle 实例分配了内存，并通过给它的构造函数传入 canvas 参数来对它进行构造。注意，大多数现代 C++ 项目很少使用单独的 new 语句，大多数情况下都会将其封装到用于管理内存申请释放的基础设施中。

The second way is not only less typing but is more efficient as well.

第二种形式不光可以少打一些字母，运行效率也更高。

std::shared_ptr however has more tricks up its sleeve:
然而，`std::shared_ptr` 还可以有很多花式玩儿法：

```cpp
// 创建一个容器，用于存放 Circle 实例的智能指针
std::vector<std::shared_ptr<Circle> > circles;

void func(Canvas* canvas)
{
	auto ptr = std::make_shared<Circle>(canvas)
	circles.push_back(ptr);
	ptr->draw();
}
```

This first defines a vector of std::shared_ptrs to Circle, then creates such a shared_ptr and stores it in the circles vector. When func returns, ptr goes out of scope, but since a copy of it is in the vector circles, the Circle object stays alive. std::shared_ptr is therefore a reference counting smart pointer.

首先我们创建一个容器，用于存放 `Circle` 实例的智能指针，然后我们创建一个 `shared_ptr` 并将其存放到容器中。当函数返回时，指针超过了它的作用域，但是因为它的一个拷贝还存放在容器中，`Circle` 对象仍然存在。`std::shared_ptr` 因此是一个引用计数智能指针。


std::shared_ptr has another neat feature which goes like this:

`std::shared_ptr` 还有一个简洁的特性，请看：

```cpp
void func()
{
        FILE *fp = fopen("/etc/passwd", "r");
        if(!fp)
          ; // 错误处理

        std::shared_ptr<FILE> ptr(fp, fclose);

        char buf[1024];
        fread(buf, sizeof(buf), 1, ptr.get());
}

```
Here we create a shared_ptr with a custom deleter called fclose. This means that ptr knows how to clean up after itself if needed, and with one line we’ve created a reference counted FILE handle.

这里我们创建了一个带有自定义删除器（deleter）`fclose` 的 `shared_ptr`。这表明该指针知道在必要时如何释放自己管理的资源，同时我们还创建了一个具有引用计数功能的 FILE 句柄（指针）。

And with this, we can now see why our earlier defined SmartFP is not very safe to use. It is possible to make a copy of it, and once that copy goes out of scope, it will ALSO close the same FILE*. std::shared_ptr saves us from having to think about thse things.

现在我们可以看到，为什么说之前我们定义的 `SmartFP` 指针并不安全。我们可以拷贝 `SmartFP` 指针，当它的任意拷贝超出作用域时，都会关闭 `FILE*`。`std::shared_ptr` 保证了我们不必担心这样的事情发生。

The downside of std::shared_ptr is that it uses memory for the actual reference count, which also has to be made safe for multi-threaded operations. It also has to store an optional custom deleter.

`std::shared_ptr` 的弊端是它需要占据部分内存来存放引用计数，在多线程条件下，我们需要确保该计数的安全。另外它也必须额外存放一个自定义的删除器。

C++ offers other smart pointers, the most relevant of which is std::unique_ptr. Frequently we do not actually need actual reference counting but only ‘clean up if we go out of scope’. This is what std::unique_ptr offers, with literally zero overhead. There are also facilities for ‘moving’ a std::unique_ptr into storage so it stays in scope. We will get back to this later.

C++ 还提供了其他的智能指针，和前文介绍的智能指针最相关的是 `std::unique_ptr`。通常我们并不需要引用计数器，我们仅仅是希望在变量超出作用域时释放内存。 `std::unique_ptr` 可以提供这种能力而且没有任何额外的开销。同时，我们可以转让 `std::unique_ptr` 的所有权，让它驻留在作用域中，这一点我们稍后会讨论。

## Threads, atomics
## 线程，原子操作

Every time I used to create a thread with pthread_create in C or older C++, I’d feel bad. Having to cram all the data to launch the thread through a void pointer felt silly and dangerous.

每次我通过 `pthread_create` 在 C 或者老版本 C++ 中创建线程的时候，我都感觉很不爽。把一堆数据通过一个 `void` 指针传入并启动线程，我觉得又傻又危险。

C++ offers a powerful layer on top of the native threading system to make this all easier and safer. In addition, it has ways of easily getting data back from a thread.

C++ 在原生的线程系统之上提供了一层强大的封装，使之变得既简单又安全。此外，也可以很方便地从线程获取返回的数据。

A small sample:

一个小例子：

```cpp
double factorial(unsigned int limit)
{
        double ret = 1;
        for(unsigned int n = 1 ; n <= limit ; ++n)
                ret *= n;
        return ret;
}


int main()
{
      auto future1 = std::async(factorial, 19);
      auto future2 = std::async(factorial, 12);      
      double result = future1.get() + future2.get();
      
      std::cout<<"Result is: " << result << std::endl;
}
```

If no return code is required, launching a thread is as easy as:
如果不需要返回值的话，创建线程是如此的简单：

```cpp
  std::thread t(factorial, 19);
	t.join(); // or t.detach()
```

Like C11, C++ offers atomic operations. These are as simple as defining std::atomic<uint64_t> packetcounter. Operations on packetcounter are then atomic, with a wide suite of ways of interrogating or updating packetcounter if specific modes are required to for example build lock free data structures.

和像 C11 一样，C++ 提供了原子操作。就像定义 `std::atomic<uint64_t> packetcounter` 一样简单，对 `packetcounter` 的查询和更新就变成了原子操作，如果我们需要创建一无锁数据结构的话，这样做很方便。

Note that as in C, declaring a counter to be used from multiple threads as volatile does nothing useful. Full atomics are required, or explicit locking.

注意，和 C 语言一样，在多线程中把一个计数器声明为 `volatile` 是没有任何作用的。需要完全原子的操作或者显式地加锁。

## Locking
## 锁


Much like keeping track of memory allocations, making sure to release locks on all codepaths is hard. As usual, RAII comes to the rescue:

就像追踪内存的申请和释放一样，确保锁的正确释放也是非常困难的。和之前一样，RAII 可以救我们于水火：

```cpp
std::mutex g_pages_mutex;
std::map<std::string, std::string> g_pages;

void func()
{
	std::lock_guard<std::mutex> guard(g_pages_mutex);
	g_pages[url] = result;
}
```

The guard object above will keep g_pages_mutex locked for a long as needed, but will always release it when func() is done, through an error or not.

上述 guard 对象会对 `g_pages_mutex` 进行加锁操作，但是当 func() 返回时，它一定会释放锁，不论函数成功或失败。


## Error handling
## 异常处理

To be honest, error handling is a poorly solved problem in any language. We can riddle our code with checks, and at each check I wonder “what should the program actually DO if this fails”. Options are rarely good - ignore, prompt user, restart program, or log a message in hopes that someone reads it.

说实话，在很多语言里面，都没有能够很好的解决异常处理这一问题。我们可以在代码中塞进各种各样的检查，每个检查处我都要思考“如果检查报错，程序应该怎么处理”。 还有一些可选的做法 —— 不处理、提示用户、重启程序或者记录日志（并期望有人会去读这些日志）。


C++ offers exceptions which in any case have some benefits over checking every return code. The good thing about an exception is that, unlike a return code, it is not ignored by default. First let us update SmartFP so it throws exceptions:

C++ 提供的异常机制，在很多情况下对于避免检查每处返回值还是有益处的。异常机制好的一面是，相对于 return，它不会默认不处理异常。首先，让我们升级一下我们的 `SmartFP` 类，使其能够抛出异常：

```cpp
std::string stringerror()
{
	return strerror(errno);
}

struct SmartFP
{
        SmartFP(const char* fname, const char* mode)
        {
                d_fp = fopen(fname, mode);
                if(!d_fp)
                    throw std::runtime_error("Can't open file: " + stringerror());
        }
        ~SmartFP()
        {
                fclose(d_fp);
        }
        FILE* d_fp;
};
```

If we now create a SmartFP and it does not throw an exception, we know it is good to use. And for error reporting, we can catch the exception:

如果我们此时创建 `SmartFP` 并且它没有抛出异常，我们就知道可以放心使用它了。如果需要错误报告，我们可以捕获异常：

```cpp
void func2()
{
        SmartFP fp("nosuchfile", "r");

        char line[512];
        while(fgets(line, sizeof(line), fp.d_fp)) {
                // do things with line
        }       
        // note, no fclose
}

void func()
{
    func2();
}

int main()
try {
    func();
} 
catch(std::exception& e) {
    std::cerr<< "Fatal error: " << e.what() << std::endl;
}
```

This shows an exception being thrown from SmartFP::SmartFP which then falls ‘through’ both func2() and func() to get caught in main(). The good thing about the fallthrough is that an error will always be noticed, unlike a simple return code which could be ignored. The downside however is that the exception may get ‘caught’ very far away from where it was thrown, which can lead to surprises. This does usually lead to good error logging though.

这里显示了一个被 `SmartFP::SmartFP` 抛出的异常，这个异常“穿越”了 `func2()` 和 `func()`，然后在 `main()` 中被捕获。这种不断上抛异常的特性，其好的一方面是所有错误最终都会被关注到，而不像 return 可能会导致异常没有被处理。然而，它不好的一方面是捕获它的地方与抛出它的地方相距甚远，这可能让人感到困惑。这通常需要做到很好的日志记录。

Combined with RAII, exceptions are a very powerful technique to safely acquire resources and also deal with errors.
结合 RAII ，异常机制可以成为非常强大的技术，用于安全的获取资源并处理错误。

Code that can throw exceptions is slightly slower than code that can’t but it barely shows up in profiles. Actually throwing an exception is rather heavy though, so only use it for error conditions.

具有异常处理机制的代码在执行速度上会稍慢一些，但是在性能分析中几乎是不可见的差异。实际上，抛出异常的确是一个很“重”的操作，所以请确保仅在异常情况下使用它。

Most debuggers can break on the throwing of an exception, which is a powerful debugging technique. In gdb this is done with catch throw.

大多数的调试器，可以打断异常的抛出，这是一个很强大的调试技术。在 gdb 中是通过捕获异常来实现的。

As noted, no error handling technique is perfect. One thing that seems promising is the std::expected work or boost::expected which creates functions that have both return codes or throw exceptions if you don’t look at them.

注意，没有什么异常处理技术是完美的。** `std::expected` 或 `boost::expected` 看上去很有前景，它们创建的函数可以返回错误信息，如果你不想查看错误信息，也可以直接抛出异常。**


## Summarising
## 总结

In part 2 of ‘C++ for C programmers’, we showed how classes are a concept that is actually well used in C already, except that C++ makes it easier. In addition, C++ classes (and structs) can have constructors and destructors and these are extremely useful to make sure resources are acquired and released when needed.

在本文中我们向你展示了，类其实是一个早在 C 语言中就有应用的概念，只不过 C++ 让类的使用变得更加简单了。此外，C++ 的类和结构体可以定义构造函数和析构函数，可以在必要时获取和释放资源。

Based on these primitives, C++ offers smart pointers of varying intelligence and overhead that cover most requirements.

基于这些基础功能，C++ 提供了多种智能指针，这些指针智能程度不同，开销也不同，可以满足大多数使用场景。

Furthermore, C++ offers good support for threads, atomics and locking. Finally, exceptions are a powerful way of (always) dealing with errors.

此外，C++ 对线程、原子操作、锁提供了很好的支持。最后，异常处理是一个处理错误的强大的特性。
