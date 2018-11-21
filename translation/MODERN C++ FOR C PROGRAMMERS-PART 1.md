# MODERN C++ FOR C PROGRAMMERS: PART 1

[原文链接](https://ds9a.nl/articles/posts/c++-1/)

NOTE: If you like this stuff, come work with me over at PowerDNS - [aspiring C++ programmers welcome!](https://www.powerdns.com/careers.html#securityDeveloper)

注意：如果你喜欢这篇文章，可以和我一起为 PowerDNS 工作 - [欢迎 C++ 程序员](https://www.powerdns.com/careers.html#securityDeveloper)

Welcome to part 1 of Modern C++ for C Programmers, please see the introduction for the goals and context of this series.

欢迎来到为 C 程序员准备的现代 C++ 的第一部分，请阅读对这个系列文章的目标和内容的介绍。

In this part we start with C++ features that you can use to spice up your code ‘line by line’, without immediately having to use all 1400 pages of ‘The C++ Programming Language’.

在这个部分我们从某些 C++ 特性开始介绍，这样我们就可以逐行的应用在我们的代码上，而不必等到读完厚厚的 1400 多行的《The C++ Programming Language》一书后，再去使用 C++ 的全部特性。

Various code samples discussed here can be found on [GitHub.](https://github.com/ahuPowerDNS/hello-cpp)

这里提到的各种代码样例都可以在 [GitHub](https://github.com/ahuPowerDNS/hello-cpp) 上找到。

## Relation between C and C++
## C 和 C++ 的关系

C and C++ are actually very close relatives, to the point that many compilers have unified infrastructure for both languages. In other words, your C code is already going through codepaths shared with C++ (and likely [written in C++](https://lwn.net/Articles/542457/)). In fact, when trivial C programs are compiled as C++ with g++, identically sized binaries come out. All example programs in our beloved [The C Programming Language](https://en.wikipedia.org/wiki/The_C_Programming_Language) compile as valid C++. Interestingly, the introduction of the 1988 edition of K&R notes Bjarne Stroustrup’s C++ “translator” was used extensively for local testing.

C 语言和 C++ 语言确实有很紧密的关系，实际上许多编译器都为这两种语言提供了统一的基础架构。换句话说，你的 C 代码已经通过编译器中的代码执行路径与 c++ 共享（并且可能是 [用 C++ 编写的](https://lwn.net/Articles/542457/)）。事实上，当简单的 C 程序被当做 C++ 语言被 g++ 编译时，编译出的二进制文件大小是相等的。我们钟爱的 [The C Programming Language](https://en.wikipedia.org/wiki/The_C_Programming_Language) 中的样例程序都可以被当做有效的 C++ 程序编译。有趣的是，1988 年出版的 K&R 中提到的 Bjarne Stroustrup 编写的 C++ 翻译器已经被广泛地用于本地测试。


The relation goes further - the entire C library is included in C++ ‘by reference’, and C++ knows how to call all C code. And conversely, it is entirely possible to call C++ functions from C.

当整个 C 语言的库都 “通过引用” 被包含在 C++ 库中时，这种关系就变得更加紧密。因此 C++ 知道怎样调用所有的 C 代码。反过来，在 C 程序中调用 C++ 函数也是完全有可能的。

C++ was explicitly designed to not present unavoidable overhead compared against C. To [quote from the ISO C++ website](https://isocpp.org/wiki/faq/big-picture#zero-overhead-principle):

与 C 相比，C++ 被明确设计为避免不必要的开销。引用自 [the ISO C++ website](https://isocpp.org/wiki/faq/big-picture#zero-overhead-principle)：

>The zero-overhead principle is a guiding principle for the design of C++. It states that: What you don’t use, you don’t pay for (in time or space) and further: What you do use, you couldn’t hand code any better.
>
>In other words, no feature should be added to C++ which would make any existing code (not using the new feature) larger or slower, nor should any feature be added for which the compiler would generate code that is not as good as a programmer would create without using the feature.

> 零开销原则是 C++ 设计的指导原则。它指出：你没使用的，你就不必承担它的开销（无论是时间上还是空间上），进一步讲：对于你使用了的功能，你无法手写出更好的代码。
>
> 换句话说，任何添加到 C++ 中的特性都不会导致已有的代码（不使用新特性的代码）占用更多的空间或是运行速度变慢，如果编译器产生的代码比程序员不使用这些特性手写的代码性能要差的话，就不应该添加这项特性。


These are big claims, and they do require some proof. For this to be true in 2018, we do have to be careful. Lots of code uses exceptions, and these do come with some overhead. However, it is also possible to declare that all or part of our code is exception free, which leads the compiler to remove that infrastructure.

要实现零开销原则可不容易。尤其是到了 2018 年，为了保证是零开销的，我们需要更加小心。许多的代码使用了异常处理，这的确带来了一些开销。然而，我们这里使用的所有代码都是没有异常处理的，这会导致编译器移除那些基础架构。

But, here is actual proof. Sorting 100 million integers using the C qsort() function, using std::sort() in C++ and using the C++-2017 parallel sort, we get the following timings:

但是，下面是确凿的证据。分别使用 C 语言的 qsort() 函数、C++ 语言的 std::sort() 函数和 C++-2017 中的并行排序函数对一亿个整数进行排序时，我们得到了下面的运行时间：

```c++
C qsort(): 13.4 seconds  (13.4 CPU)
C++ std::sort(): 8.0 seconds (8.0 CPU)
C++ parallel sort: 1.7 seconds (11.8 seconds of CPU time)
```

What is this magic? The C++ version is 40% faster than C? How is this possible?

这里用到的魔法是什么？ 为什么 C++ 版本比 C 版本的快了 40% ? 这怎么可能呢？

Here is the code:

下面是用到的代码：

```c++
int cmp(const void* a, const void* b)
{
  if(*(int*)a < *(int*)b)
    return -1;
  else if(*(int*)a > *(int*)b)
    return 1;
  else
    return 0;
}

int main(int argc, char**argv)
{
  auto lim = atoi(argv[1]);

  std::vector<int> vec;
  vec.reserve(lim);

  while(lim--)
    vec.push_back(random());

  if(*argv[2]=='q')
    qsort(&vec[0], vec.size(), sizeof(int), cmp);
  else if(*argv[2]=='p')
    std::sort(std::execution::par, vec.begin(), vec.end());
  else if(*argv[2]=='s')
    std::sort(vec.begin(), vec.end());
}
```

It is worth studying this a bit. The cmp() function is there for qsort(), and defines the sort order.

这值得研究一会。这里的 `cmp()` 函数是为 `qsort()` 函数准备的，同时也定义了排序的顺序。

Main is main as in C, but then we see the first oddity: auto. We’ll cover this later, but auto almost always does what you think it does: calculate the required type and use it.

C++ 和 C 中的主函数是一样的，都是 `main` 函数，下面我们看到了第一个奇怪的地方：auto。我们会在稍后详细介绍这一点，但 auto 的作用和我们想象的差不多：首先计算需要使用的类型，然后使用这个类型。

The next two lines define a vector containing integers, and reserve enough space in there for how many entries we want. This is an optional optimization. The while loop then fills the vector with ‘random’ numbers.

接下来的两行代码定义了一个容纳整数元素的 vector 容器，并且在容器中保留了足够的空间来放入我们想要的数据条数。这是一个可选的优化项。接下来使用 while 循环用’随机数‘填满这个容器。

Next up.. something magic happens. We call the C qsort() function, to operate on the C++ vector containing our numbers. How is this possible? It turns out std::vector is explicitly designed to be interoperable with raw pointer operations. It is meant to be able to be passed to C library or system calls. It stores its data in a consecutive slab of memory that can be changed at will.

接下来。。神奇的事情发生了。我们调用 C 语言的 `qsort()` 函数，来操纵容纳数字的 vector 容器。这是怎么办到的呢？实际上是这样：`std::vector` 容器被明确设计为可以通过原生指针进行交互操作。这意味着可以把它传递给 C 库或者系统调用。它把数据存储在可以随意更改的连续内存块中。

The next 4 lines use the C++ sorting functions. On some versions of G++, you may need this (non-standard) syntax to get the same result:

接下来的 4 行代码使用了 C++ 版本的排序函数。在某些版本的 G++ 中，你可能需要这个（不标准的）语法来得到相同的运行结果：

```c++
__gnu_parallel::sort(vec.begin(), vec.end()).
```

## So how come C++ std::sort is faster than qsort?
## 所以为什么 C++ 版本的 std::sort 比 qsort 快呢？

`qsort()` is a library function that accepts a comparison callback. The compiler (and its optimizer) can not look at the qsort() procedure as a whole therefore. In addition, there is function call overhead.

`qsort()` 是一个库函数，可以接收一个用于比较的回调函数。因此编译器（和它的优化器）无法把 `qsort()` 过程作为一个整体。此外，还有函数调用的开销。

The C++ std::sort version meanwhile is actually a ‘template’ which is able to inline the comparison predicate, which for ints defaults to the < operator.

C++ 版本中的 `std::sort` 函数事实上是一个 “模板”，它能够内联比较谓词，对于 int 类型来说默认比较谓词是 < 运算符。

To make sure we are being fair, since qsort() is using a custom comparator, and our std::sort is not, we can use:

因为 `qsort()` 使用了自定义的比较函数，但我们的 `std::sort` 函数没有，为了确保我们是公平的，因此我们可以使用下面的代码：


```C++
std::sort(vec.begin(), vec.end(),
          [](const auto& a, const auto& b) { return a < b; }
     );
```

When executed, this still takes the same amount of time. To sort in reverse order, we could change a < b to b < a. But what is this magic syntax? This is a C++ lambda expression, a way to define functions inline. This can be used for many things, and defining a sort operation this way is highly idiomatic.

在执行完之后，我们发现运行的时间是相同的。为了按照相反的顺序排序，我们可以把 `a < b` 改成 `b < a`。但是这个神奇的语法是什么呢？这是 C++ 的 lambda 表达式，定义内联函数的一种方式。这可以被用在许多事情上，而且用这种方式定义排序操作函数是非常常见的。

Finally, C++ 2017 comes with parallel versions of many core algorithms, and for our case, it appears the parallel sort is indeed delivering a 4.7-fold speedup on my 8 hyper-core machine.

最后，C++ 2017 版本附带了许多核心算法的并行版本，对于我们的例子，似乎并行排序函数在我的 8 核电脑上速度提高了 4.7 倍。

## Strings
## 字符串

It may be hard to believe, but for much of the time of C++’s original development, it did not have a string class. Writing such a class was somewhat of a rite of passage, and everyone made their own. The reason behind this was partially the prolonged attempt to make a class that was everything for everyone.

说起来可能很难相信，但在 C++ 最初开发的大部分时间里，确实没有字符串类。写这么一个字符串类有种仪式感，每个人都想写一个它们自己的版本。字符串类长时间没有被实现的原因，其背后的原因我们总想尝试写出一个满足所有人的功能强大的字符串类。

The `std::string` C++ ended up with in 1998 interoperates well with C code:

1998 年完成的 C++ 中的 std::string 可以很好地和 C 程序交互：

```c++
std::string dir("/etc/"), fname;
fname = dir + "hosts";
FILE* fp = fopen(fname.c_str(), "r");
```

[std::string](http://en.cppreference.com/w/cpp/string/basic_string) offers most functionality you’d expect, like concatenation (as shown above). Some further code:

[std::string](http://en.cppreference.com/w/cpp/string/basic_string) 提供了大多数你想到的功能，像是字符串连接 (正如上面展示的)。更多的代码：

```c++
auto pos = fname.find('/');
if(pos != string::npos)
	cout << "First / is at" << pos << "\n";

pos = fname.find("host");
if(pos != string::npos)
	cout << "Found host at" << pos << "\n";

std::string newname = fname;
newname += ".backup";

unlink(newname.c_str());
```

`std::string` provides unsafe and unchecked access to its characters with the `[]` operator, so newname[0] == '/', but wise people use [newname.at(0)](http://en.cppreference.com/w/cpp/string/basic_string/at) which performs bounds checking.

`std::string` 提供了一种不安全、没有安全检查的 `[]` 运算符来访问字符串中的字符，所以可以这样访问字符串 `newname[0] == '/'`, 但明智的人都使用 [newname.at(0)](http://en.cppreference.com/w/cpp/string/basic_string/at) 来访问字符串中的字符，这种方式是有边界检查。

The post-2011 design of std::string is pretty interesting. The storage of basic string implementation could look like this:

2011 年的 `std::string` 设计文章非常有趣。基本字符串存储的实现看起来像是下面这样：

```c++
struct mystring
{
	char* data;
	size_t len;
	size_t capacity; // how much we've allocated already
};
```

On a modern system, this is 24 bytes of data. The capacity field is used to store how much memory has been allocated so mystring knows when it needs to reallocate. Not reallocating every time a character is added to a string is a pretty big win.

在现代操作系统中，上面的结构体占 24 个字节。`capacity` 字段通常用来记录已分配了多少内存，因此 `mystring` 结构体知道什么时候需要重新分配内存。不必每添加一个字符就重新分配一次内存，这是一个巨大的胜利。

Frequently however, the things we store in strings are a lot shorter than 24 bytes. For this reason, modern C++ std::string implementations implement Small String Optimization, which allows them to store 16 or even 21 bytes of characters within their own storage, without using `malloc()`, which is a speedup.

然而，我们经常要在字符串中存储的内容要比 24 字节小很多。因此，现代 C++ 中 `std::string` 类的实现中对小字符串的存储进行了优化，允许它们在自己的存储空间中存 16 甚至 21 个字节的字符串，而不必使用 `malloc()` 函数，这样提高了运行速度。


Another benefit of preventing needless calls to malloc() is that an array of strings is now stored in contiguous memory, which is great for memory cache hitrates, which often delivers whole factors of speedup.

防止不必要的 `malloc()` 函数调用的另一个好处是，字符串数组会存储在连续的内存中，这对于内存缓冲机制非常重要，这通常是提高运行速度的全部原因。

After years of design, std::string may not be everything to everyone, but consistent with the ‘zero overhead’ principle, it beats what you would have quickly written by hand.

经过多年的设计之后，`std::string` 可能还不能让所有人都满意，但是因为坚持了‘零开销’原则，所以这要优于你在短时间内手写出的 `string` 类。

## Summarising
## 总结

In part 1 of this series, I hope to have shown you some interesting bits of C++ you could start using right away - gaining you a lot of new power without immediately filling your code with complicated stuff.

在这个系列的第一部分，我希望向你展示一些有趣的、你可以立即上手使用的 C++ 代码 - 让你获得许多的新能力而不会立刻让你的代码充满复杂的内容。

Part 2 can be found [here](https://ds9a.nl/articles/posts/cpp-2/).

第二部分可以在 [这里](https://ds9a.nl/articles/posts/cpp-2/) 找到。



