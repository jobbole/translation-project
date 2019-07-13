In this probably final part 5, we’ll be going over some of the most powerful stuff in modern C++: “perfect” reference counting and the concept of std::move. Note that this installment introduces some pretty unfamiliar concepts, so it may be heavier reading than earlier parts.  
在最后的第五部分里，我们会介绍 C++ 中一些非常有用的东西：“完美的”引用统计和 `std::move` 的概念。注意这部分的内容介绍了一些不太常见的概念，因此可能比起以前的部分来说读起来比较困难。  

## Memory management 
## 内存管理

Memory is frequently the most important factor determining a program’s speed and reliability. CPUs these days tend to be tremendously faster than their attached RAM, so preventing needless copies and fragmented memory access may deliver whole orders of magnitude improvements in speed.   
内存管理通常来说是决定一个程序运行速度和可靠性的重要因素。目前的 CPU 比起与它们相连的 RAM 速度快的多得多，因此如果能够防止不必要的拷贝和内存碎片访问，程序的运行速度将会有巨大的提升。  

The authors of C++ were well aware of this and have delivered functionality that makes it possible to pass around or construct objects “in place”, thus saving a lot of memory bandwidth.  
C++ 的作者意识到了这一点，并且提交了一些功能，这些功能可以使得 C++ 可以“原地”传递和创建对象，从而节省大量的内存带宽。  

Most of these techniques require some thinking, but we’re going to start with one that is nearly invisible, and explains why some C code becomes faster simply by being recompiled as C++.   
大多数这种技术需要很复杂的思考，因此我们现在从一个几乎不被人注意的技术开始说起，并解释为什么一些 C 代码只是被当做 C++ 重新编译了一下，运行速度就会变得更快。

## Copy elision or Return Value Optimization  
## 复制省略或者返回值优化

Ponder the following code:   
仔细思考下面的代码：   

```c
struct Object
{
	// many fields
};

Object getObject(size_t i)
{
	Object obj;
	// retrieve object #i
	return obj;
}

int main()
{
	Object o = getObject(271828);
}
```

Seasoned C programmers will have been exhorted to never do this, starting from gloried pages of K&R. “Passing structs over the stack leads to needless copying”. Instead, we’d be passing a pointer to an Object, meticulously reset it to its default state and then fill it out.    
老道的 C 程序员会劝你不要这样做。在 K&R 书中有几页是这么说的：“通过堆栈传递结构体将导致不必要的复制”。相反，我们会传递一个指向对象的指针，我们会很小心地把它设置成默认状态，然后为它赋值。  


In C, the compiler is not allowed to optimize the code as written above, and the struct Object gets copied on the return from getObject. In C++ however, not only is the compiler allowed to optimize, all of them actually do it. In effect, Object o gets constructed on the caller’s stack and filled out there, with no copying going on.   
在 C 语言中，不允许编译器对上面的代码进行优化，因此从 `getObject` 函数返回值的时候， struct 结构体会被复制。然而在 C++ 语言中，不仅允许编译器对上面的代码进行优化，而且它们也确实进行了优化。实际上，结构体 `o` 在调用函数的堆栈里被创建后，在进行完赋值操作之后，没有任何的复制操作。   


This enables code like this to be efficient:   
这就使得像下面这样的代码效率很高： 

```c++
Vector<Object> getAll(); // "Vector" from part 3
..
auto all = getAll(); // returns millions of Objects
```

Later we will see how C++ offers explicit opportunities to transfer ownership without copying.   
之后我们会看看 C++ 是提供了怎样的机制来传递所有权而不必复制。  

## Smart Pointers  
## 智能指针 

In part 2 we touched on smart pointers. We also noted that memory leaks are the bane of every project, and probably the most vexing thing about writing in pure C. Every C (and C++) programmer I know has lost at least one solid week on chasing an obscure memory leak.   
在[第二部分](https://ds9a.nl/articles/posts/cpp-2)我们接触到了智能指针。我们也注意到内存泄露是所有项目的灾难，这大概也是用纯 C 语言编写代码最让人头疼的事情。我认识的 C （和 C++) 程序员都曾在解决隐蔽的内存泄露的问题上花过至少一个周的痛苦时间。  

These problems are so large that most modern programming languages decided to incur a significant amount of overhead to implement garbage collection (GC). GC is amazing when it works, and especially lately, the overhead is now at least manageable. But as of 2018, all environments still struggle with hick-ups caused by GC runs, which always tend to happen exactly when you don’t want them to. And to be fair, this is a very difficult problem to solve, especially when many threads are involved.   
这些问题太严重了以至于现代编程语言决定以牺牲大量开销为代价来实现垃圾回收（GC)。GC 在开始使用的时候非常神奇的，特别是刚刚应用的那段时间，开销还处于可控状态。但是在 2018 年，所有环境都在和 GC 运行造成的混乱做斗争，这种情况通常会在你想不到的时候发生。公平来说，这是个非常难解决的问题，特别是当涉及多线程的时候。  

C++ has therefore not implemented garbage collection. Instead, there is a judicious [selection of smart pointers](https://en.cppreference.com/w/cpp/memory) that perform their own cleanup. In [part 2](https://ds9a.nl/articles/posts/cpp-2) we described std::shared_ptr as “the most do what I mean” smart pointer available, and this is true.   
因此 C++ 目前为止并没有实现垃圾回收。相反，它明智地选择了[一种智能指针](https://en.cppreference.com/w/cpp/memory)，这种指针可以完成它们自己的清理工作。在[第二部分](https://ds9a.nl/articles/posts/cpp-2)中我们把 `std::shared_ptr` 描述为“最合心意”的智能指针，这是完全正确的。   

Such magic does not come for free however. If we look ‘inside’ a std::shared_ptr, it turns out it carries a lot of administration. First there is of course the actual pointer to the object contained. Then there is the reference count, which needs to be updated and checked atomically at all times. Next up, there may also be a custom deleter. For good reasons, this metadata is itself allocated dynamically (on the heap). So while the sizeof of a std::shared_ptr may only be 16 bytes (on a 64 bit system), effectively it uses much more memory. [In one specific test](https://github.com/ahupowerdns/hello-cpp/blob/master/move.cc), a std::shared_ptr<uint32_t> ended up using 47 bytes of memory on average.   
然而这种技术并不是白白得来的。如果我们深入 `std::shared_ptr` 内部，结果就是这个指针包含了大量的管理机制。首先这个指针内部一定会有一个指向被包含对象的普通指针。其次还有引用计数器，需要随时进行自动更新和检查。接下来，可能还有一个自定义的删除函数。出于充分的理由，这些元数据本身是位于动态分配的内存中（位于堆中）。因此当 `std::shared_ptr` 的大小可能只是 16 字节的时候（在 64 位的系统上），实际这占用了更多的内存。[在一个特定测试中](https://github.com/ahupowerdns/hello-cpp/blob/master/move.cc)，`std::shared_ptr<uint32_t>` 平均占用 47 字节内存。

The question of course is: can we do better?  
显而易见的问题是： 我们还能继续优化吗？

## Introducing: std::unique_ptr  
## 简介：std::unique_ptr  

The overhead of generic reference counted pointer was well known when C++ took its initial standardized form. Back then, a quirky smart pointer called [std::auto_ptr](https://en.cppreference.com/w/cpp/memory/auto_ptr) was defined, but it turned out that within the C++ of 1998 it was not possible to create something useful. Making “the perfect smart pointer” required features that only became available in C++ 2011.   
当 C++ 采用最初的标准化形式时，普通的引用计数指针的开销是非常出名的。那时，一个叫做 [`std::auto_ptr`](https://en.cppreference.com/w/cpp/memory/auto_ptr) 的古怪的智能指针被定义出来，但结果就是在 C++(98)中，我们根本不可能利用它创造出有用的东西。创造“完美的智能指针”所需要的特性直到 2011 年 C++ 才能提供。

First, let us try some simple things [(source on GitHub)](https://github.com/ahupowerdns/hello-cpp/blob/master/move.cc):  
首先，让我们尝试一些简单的东西 [（Github 上的源代码）](https://github.com/ahupowerdns/hello-cpp/blob/master/move.cc)：  

```c++
  std::unique_ptr<uint32_t> testUnique;
  uint32_t* testRaw;
  std::shared_ptr<uint32_t> testShared;

  cout << "sizeof(testUnique):\t" << sizeof(testUnique) << endl;
  cout << "sizeof(testRaw):\t" << sizeof(testRaw) << endl;
  cout << "sizeof(testShared):\t" << sizeof(testShared) << endl;
```

Rather amazingly this outputs:    
输出非常神奇：   


```c++
sizeof(testUnique): 8
sizeof(testRaw):    8
sizeof(testShared): 16
```

You saw that right. A std::unique_ptr has no overhead over a ‘raw’ pointer. And in fact, with some judicious casting, you can find out it in contains nothing other than the pointer you put in there. That’s zero overhead.   
你看到的没错。`std::unique_ptr` 比起“普通”的指针来说没有任何额外的开销。事实上，通过一些机智的类型转换，你就会发现它内部只包含一个你放入的指针。因此这是零开销的。 

Here’s how to use it:  
下面是怎样使用它：  

```c++
void function()
{
  auto uptr = std::make_unique<uint32_t>(42);

  cout << *uptr << endl;
} // uptr contents get freed here   
```

The first line is a shorter (and better) way to achieve:  
第一行的使用方式更短（并且更好）：  

```c++
std::unique_ptr<uint32_t> uptr = std::unique_ptr<uint32_t>(new uint32_t(42));
```  

>In general, always prefer the std::make_* form for smart pointers. For std::shared_ptr it turns two allocations into one, which is a huge win both in CPU cycles and memory consumed.   
>通常来说，我偏爱使用 `std::make_*` 这种形式来使用智能指针。对于 `std::shared_ptr` 来说，它把两次内存分配变成了一次，这在 CPU 周期和内存消耗上是一个巨大的胜利。  

It should be noted that std::unique_ptr may be a smart pointer, but it is not a generic reference counted pointer. Or, to put it more precisely, there is always exactly one place that owns a std::unique_ptr. This is the magic of why there is no overhead: there is no reference count to store, it is always ‘1’.    
应该指出的是 `std::unique_ptr` 可能也是一个智能指针，但它不是一个普通的引用计数指针。或者，更准确的说，总有一个指针指向 `std::unique_ptr` 。 这就是为什么没有额外开销的原因：不需要保存引用计数器，因为引用计数永远是 ‘1’。  

std::unique_ptr cleans up only when it goes out of scope, or when it is reset or replaced.  
`std::unique_ptr` 只有在超出作用域或是重置，或是被替换的时候，才进行清理工作。

To access the contents of a smart pointer, either deference it (with * or ->), or use the get() method if you need the actual pointer inside. Smart pointers can also be unset, and in that case evaluate as ‘false’:   
访问智能指针的内容，既不需要解引用 （使用（ * 或者 ->）,也不需要使用 `get()` 函数来访问内部普通的指针。智能指针可以不被初始化，在这种情况下它相当于 ‘false’：  

```c++
  std::unique_ptr<int> iptr;

  auto p = [](const auto& a) {
    cout << "pointer is " << (a ? "" : "not ") << "set\n";
  };

  p(iptr);
  cout << (void*) iptr.get() << endl;  

  iptr = std::make_unique<int>(12);
  p(iptr);

  iptr.reset();
  p(iptr);
```

This prints:  
输出结果是：   

```c++
pointer is not set
0
pointer is set
pointer is not set  
``` 

If we attempt to copy a std::unique_ptr, the compiler stops us. It does allow us however to ‘move’ it:   
如果我们尝试复制 `std::unique_ptr` ,编译器会阻止我们。然而它允许我们 ‘移动’（move） 它：  


```c++
  std::unique_ptr<uint32_t> uptr2;

  uptr2 = uptr; // error about 'deleted constructor'

  uptr2 = std::move(uptr); // works
```

The reason a simple copy is not allowed is that this would lead to a non-unique pointer: both uptr and uptr2 would refer to the same uint32_t instance.   
不允许简单复制的原因是这会产生不唯一的指针：`uptr` 和 `uptr2` 都指向相同的 `uint32_t` 实例。 

So what is this std::move thing, and why does that work?   
所以 `std::move` 到底是什么呢？为什么它是有效的呢？  

## std::move    

In [part 2](https://ds9a.nl/articles/posts/cpp-2) we defined a SmartFP class as an example of Resource Acquisition Is Initialization (RAII). It’s intended to be used like this:    
在[第二部分](https://ds9a.nl/articles/posts/cpp-2)我们定义了一个 `SmartFP` 类，作为资源获取就是初始化（ RAII ）的一个例子。使用方法见下面：  

```c++
int main()
try
{
	string line;
	SmartFP sfp("/etc/passwd", r");
	stringfgets(line, sfp.d_fp); // simple wrapper
	// do stuff
}
catch(std::exception& e) 
{
	cerr << "Fatal error: " << e.what() << endl;
}  
```

SmartFP underneath is nothing but a wrapper for fopen and fclose. It also turns fopen errors into an explanatory exception. The nice thing about RAII that it guarantees the filedescriptor won’t ever leak, even in the face of error conditions.   
`SmartFP` 内部只是对 `fopen` 和 `fclose` 进行了包装。它也把 `fopen` 的错误信息转换成了解释性的说明。RAII 的好处就是它保证了文件描述符永远不会泄露，即使出现错误条件也不会泄露。  

In [part 2](https://ds9a.nl/articles/posts/cpp-2) we also noted that as defined, SmartFP had a problem. It performs an fclose when it goes out of scope, but what if someone copied our SmartFP instance? We would then close the same FILE pointer twice, which is very bad. Enter the move constructor:     
在[第二部分](https://ds9a.nl/articles/posts/cpp-2)我们指出定义的 `SmartFP` 有一个问题。它在超出作用域的时候调用 `fclose` 函数，但是如果有人复制了我们的 `SmartFP` 对象呢？我们会对同一个文件指针执行两次关闭操作，这是非常严重的错误。因此引进了移动构造函数：  

```c++
struct SmartFP
{
  SmartFP(const char* fname, const char* mode)
  {
    d_fp = fopen(fname, mode);
    if(!d_fp)
      throw std::runtime_error("Can't open file: " + stringerror());
  }

  SmartFP(SmartFP&& src) // move constructor. Note "&&"
  {
    d_fp = src.d_fp;
    src.d_fp = 0;
  }

  ~SmartFP()
  {
    if(d_fp)
      fclose(d_fp);
  }
  FILE* d_fp{0};
};
```

The move constructor is the important bit. Its presence tells C++ that this class can not be copied, only moved. The semantics of a move are a true transfer of ownership.  
移动构造函数非常重要。在这里它通知 C++ 这个类不能被复制，只能被移动。移动语法实际上就是转让对象的所有权。   

The following may help:    
接下里的例子可能对你有帮助：  

```c++
SmartFP sfp("/etc/passwd", "ro");
cout << (void*) sfp.d_fp << endl;  // prints a pointer 

SmartFP sfp2 = sfp;                // error
SmartFP sfp2 = std::move(sfp);     // transfer!

cout << (void*) sfp.d_fp << endl;  // prints 0
cout << (void*) sfp2.d_fp << endl; // prints same pointer
```

When this code runs, the FILE pointer we created on the first line gets fclosed exactly once. This is because during the move, the ‘donor’ FILE* was set to zero, and in the destructor we make sure not to fclose a 0.    
当代码运行的时候，我们在第一行创建的文件指针事实上只被 `fclose` 了一次。这是因为在‘移动’过程中，‘donor’ 文件指针被设置为 0，因此我们确保了在析构函数中不会 `fclose` 一个 0。

This move is performed automatically on return:  
移动语法在返回的时候自动调用：  

```c++
SmartFP getTmpFP()
{
	// get tmp name
	return SmartFP(tmp, "w");
}

...

SmartFP fp = getTmpFP();
```

Additionally, the C++ standard containers are all move aware, with a special syntax to construct elements ‘in place’:   
此外，C++ 标准容器都是支持移动语义的，有一个特殊的语法来”原地“创建元素：  

```c++
  vector<SmartFP> vec;
  vec.emplace_back("move.cc", "r");
```

All the parameters to emplace_back get forwarded to the SmartFP constructor, which constructs the instance straight into the std::vector - all without a single copy. When filling large containers, this can make a huge difference.    
所有传入 `emplace_back` 的变量都被传递到 `SmartFP` 构造函数内，构造函数构造完对象之后直接放入 `std::vector` 内 - 完全没有额外的复制。当填充大的容器的时候，情况可能有所不同。

Note that if we want to, a class can have both move constructors and regular constructors. A good example of this are all the C++ standard containers, including std::string. This gives you a choice between making a real copy or transferring ownership.   
注意如果我们想的话，一个类可以既有移动构造函数，也可以有普通的构造函数。所有的 C++ 标准容器都是这样，包括 `std::string` 。这样你就可以选择是进行复制还是传递所有权。   

## Smart pointers and polymorphism  
## 智能指针和多态

A main reason we store things as pointers is to benefit from polymorphism. The downside of pointers is of course memory management, so it would be great if smart pointers were to interoperate with base and derived classes. The wonderful news is that they do.   
我们把对象存储为指针的一个主要原因得益于多态。指针的缺点当然是内存管理，因此如果智能指针还能够和基类、派生类进行交互的，那就再好不过了。好消息是它们的确能够做到。  

Based on our Event class from [part 3](https://ds9a.nl/articles/posts/cpp-3):  
基于[第三部分](https://ds9a.nl/articles/posts/cpp-3)的 `Event` 类：   

```c++
  std::deque<std::unique_ptr<Event>> eventQueue;

  eventQueue.push_back(std::make_unique<PortScanEvent>("1.2.3.4"));
  eventQueue.push_back(std::make_unique<ICMPEvent>());

  for(const auto& e : eventQueue) {
    cout << e->getDescription() << endl;
  }
```

This all works as expected, and the contents of eventQueue get cleaned up when the container goes out of scope.  
它们的输出结果和期待的一样，并且 `eventQueue` 的内容在容器超出作用域之后会进行自动清理。

>When using polymorphic classes, make sure there either is no ~destructor, or that it is declared as virtual. Otherwise std::unique_ptr will call the base class destructor. See [part 3](https://ds9a.nl/articles/posts/cpp-3) for more details, plus this [stackoverflow post](https://stackoverflow.com/questions/461203/when-to-use-virtual-destructors)   

>当使用多态类的时候，一定要确保类中没有析构函数（析构函数命名以 `~` 开头），也没有被声明为虚拟类。否则 `std::unique_ptr` 会调用基类的构造函数。详情请[看第三部分](https://ds9a.nl/articles/posts/cpp-3/)，参考 [stackoverflow 上的这篇文章](https://stackoverflow.com/questions/461203/when-to-use-virtual-destructors)   

## Placement new  
## Placement new 运算符 

As noted earlier, C makes it possible to ‘live on the edge’, or as some of the Node.JS people said, to [‘be close to the metal’](https://twitter.com/shit_hn_says/status/234856345579446272). The good thing is that C++ offers you that same ability, should you need it, and more.   
正如前面提到的, C 使得接近底层编程成为了可能，或者像一些 Node.JS 用户说的，非常接近底层 ([be close to the metal](https://twitter.com/shit_hn_says/status/234856345579446272))（这里是想说明 C 语言比较接近底层）。好消息是 C++ 不仅提供了与 C 语言相同的能力，而且在我们需要的功能之上又添加了新的功能。    

When we do the following:  
当我们运行下面代码的时候：  

```c++
auto ptr = new SmartFP("/etc/passwd", "ro");
```

This does two things:    
这行代码一共做了两件事：   

1. Allocate memory to store a SmartFP instance 
2. Call the SmartFP constructor using that memory  

3. 分配内存来存储一个 `SmartFP` 对象
4. 调用 `SmartFP` 构造函数使用这段内存

Generally this is what we need. However, sometimes our memory arrives from elsewhere but we’d still like to construct objects on there. Enter placement new.  
通常来说这就是我们想要的结果。然而，有时候我们的内存是来自于别处的，但是我们想在这段内存中创建对象。这时就引入了 `placement new` 运算符。  

Here is an actual usecase from the PowerDNS dumresp utility:
这里有一个来自 PowerDNS dumresp 软件中的使用实例：  

```c++
std::atomic<uint64_t>* g_counter;

  auto ptr = mmap(NULL, sizeof(std::atomic<uint64_t>), PROT_READ | PROT_WRITE,
		  MAP_SHARED | MAP_ANONYMOUS, -1, 0);

  g_counter = new(ptr) std::atomic<uint64_t>();
  
  for(int i = 1; i < atoi(argv[3]); ++i) {
    if(!fork())
      break;
  }
```

This uses mmap to allocate memory that will be shared with any child processes, and then uses fancy placement new syntax to construct a std::atomic<uint64_t> instance in that shared memory.    
上面的代码使用了 `mmap` 函数来分配内存，这些内存会和任何子进程进行共享，然后使用有趣的 `placemeng new` 语法在这些共享内存中创建一个 `std::atomic<uint64_t>` 对象。

The code then forks the number of processed described in argv[3]. Within all these processes, a simple ++(*g_counter) works, and all update the same counter.  
接下来将 `argv[3]` 参数处理为整数，然后调用这个整数次 `fork` 函数。所有的这些进程, `++(*g_counter)` 都是有效的，都对同一个计数器进行修改。  


Based on techniques like these, it is possible to create highly efficient and easy to use interprocess communications libraries, like for example [Boost Interprocess](https://www.boost.org/doc/libs/1_67_0/doc/html/interprocess/quick_guide.html).   
基于这些技术，可以创建更高效、更易于使用的进程间通信库，例如 [Boost Interprocess](https://www.boost.org/doc/libs/1_67_0/doc/html/interprocess/quick_guide.html) 。

## Some general advice  
## 一些常规性的建议 

Many modern C++ projects will only have a handful of explicit calls to new or delete (or malloc/free). It is easy to audit those few calls. Restrict manual memory allocation to the cases where you really have to.  
许多现代 C++ 工程只在很少的情况下直接调用 `new` 或者 `delete` (或者 `malloc`/`free`)。检查这些调用非常简单。只有在你不得不手动分配内存的时候，才那样去做。

For the rest, use std::unique_ptr if you can get away with it, and std::shared_ptr when you can’t. Note that you can convert a std::unique_ptr into a std::shared_ptr efficiently, so you can change your mind:     
至于其他的，尽量使用 `std::unique_ptr` ,如果不行就使用 `std::shared_ptr` 。注意你可以非常高效地把 `std::unique_ptr` 转换成 `std::shared_ptr` ，因此你可以随时改变主意。


```c++
auto unique = std::make_unique<std::string>("test");
std::shared_ptr<std::string> shared = std::move(unique);
```

In addition, a std::unique_ptr can also release() the pointer it owns, which means it will not get deleted automatically.   
此外，`std::unique_ptr` 也可以 `release()` （释放）它拥有的指针，这意味它拥有的指针不会被自动删除。  

The easy ability to cheaply convert a std::unique_ptr into a std::shared_ptr or a raw pointer means that functions can return a std::unique_ptr and keep everyone happy.  
把 `std::unique_ptr` 转换成 `std::shared_ptr` 或者普通指针的简单能力意味着函数可以返回一个 `std::unique_ptr` ，并且满足所有人的要求（因为可以进行类型转换）。  

On the move constructor, it pays to understand this somewhat unfamiliar construct. Classes that represent resources (like sockets, file descriptors, database connections) are naturals for having a move constructor, since this makes their semantics closely match how these resources work: should be opened and closed exactly once, and exactly when we want them to.  
对于移动构造函数，理解这个有点陌生的语法是值得的。代表资源的类（像是套接字，文件描述符，数据库连接）本身就有一个移动构造函数，因为这种语法和这些资源的工作方式紧密相关：打开资源和关闭资源只应该进行一次，并且是在我们需要的时候。

## Summarising  
## 总结

Memory allocation is hard and various smart pointers provided by C++ make it easier. std::unique_ptr  is luxurious but comes with baggage, std::unique_ptr is frequently good enough and carries no overhead at all.    
内存分配很困难，但 C++ 提供了各种智能指针来简化它。`std::unique_ptr` 非常好用但是有额外的开销，`std::unique_ptr` 通常来说不仅足够好，而且没有额外的开销。  


C++ tries hard to prevent needless copying of objects and adding a move constructor makes this explicit. By using std::move it is possible to store std::unique_ptr instances in containers, which is both safe and fast.  
C++ 尽力避免不必要的对象复制，并且添加移动构造函数来明确这一点。通过使用 `std::move` ,我们可以在容器中存储 `std::unique_ptr`,这不仅安全，而且运行速度很快。  

