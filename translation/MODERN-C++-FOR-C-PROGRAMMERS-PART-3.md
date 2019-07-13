# MODERN C++ FOR C PROGRAMMERS: PART 3
[原文链接](https://ds9a.nl/articles/posts/cpp-3/)   

NOTE: If you like this stuff, come work with me over at PowerDNS - aspiring C++ programmers welcome!
注意：如果你喜欢这篇文章，可以和我一起为 PowerDNS 工作 - [欢迎 C++ 程序员](https://www.powerdns.com/careers.html#securityDeveloper)      


Welcome back! In part 2 I discussed basic classes, threading, atomic operations, smart pointers, resource acquisition and (very briefly) namespaces.  
欢迎回来！在第二部分我们讨论了基本的类、线程、原子操作、智能指针、资源请求和（非常简单的）命名空间。

In this part we continue with further C++ features that you can use to spice up your code ‘line by line’, without immediately having to use all 1400 pages of ‘The C++ Programming Language’.  
在这个部分我们继续深入那些你可以一点点用在你代码上的 C++ 特性，而不必等到读完厚厚的 1400 多行的《The C++ Programming Language》一书后，再去使用。

Various code samples discussed here can be found on GitHub. 
文章中讨论的所有样例代码都可以在 [Github](https://github.com/ahuPowerDNS/hello-cpp) 上找到。



## Inheritance & polymorphism 
## 继承和多态
These are features that are sometimes useful, but by no means the first things to reach for. It is entirely possible to write C++ that never uses any kind of inheritance. In other words, there is no pressure or need to be “all object oriented”.   
有时候许多很有用的特性我们不会第一时间接触到。在我们用 C++ 的时候不使用任何继承完全是有可能的。换句话说，我们没必要让所有程序都 “面向对象”。  


But, it does have its uses. For example, an event-processing library may have to deal with arbitrary kinds of events, all of which have to pass through a single API. It works like this:   
但是，继承确实有它的用处。例如，事件处理库可能需要处理各种随机事件，这些随机事件都必须通过一个单独的 API 传入。这就像是下面这样工作：   

```c++
class Event
{
public:
	std::string getType();
	struct timeval getTime();
	virtual std::string getDescription()=0;

private:
	std::string m_type;
	struct timeval m_time;
};
```

This is the base class called `Event`. It has three methods, two of which are normal member functions: `getType()` and `getTime()`. These return data from the two member variables that every Event shares.   
这是一个基类叫做 `Event` 。它有三个方法，其中两个是正常的成员函数： `getType()` 和 `getTime()` 。这两个函数返回两个成员变量的数据，这两个成员变量是每个 Event 实例都有的。

The third one `getDescription()` is `virtual` which means it is different in derived classes. In addition, we have set the function to zero which means that every derived class will have to define this function. In other words, you can’t do this:  
第三个函数 `getDescription()` 是 `virtual` （虚函数），这意味着这个函数因派生类而不同。顺便说一句，我们把这个函数设置成了 0 ，所以每个派生的子类都必须定义这个函数。换句话说，你不能像下面这样做：   

`Event e; // will error on 'pure virtual getDescription'  `

To make an actual Event that works, we do:   
为了构造一个能够正常运行的 Event 实例，我们可以这样做：     

```c++

class PortScanEvent : public Event
{
public:
	virtual std::string getDescription() override
	{
		return "Port scan from "+m_fromIP;
	}	
private:
	std::string m_fromIP;
};
```

This defines a derived class that inherits from `Event`, which is its ‘base class’. Note how we define `getDescription` here, and that it is flagged with `override` which means the compiler will error out unless we are actually overriding a base class method.    
上面的代码定义了一个继承自 `Event` 类的派生类，其中 `Event` 是基类。 注意我们这里是怎样定义 `getDescription` 函数的，并对这个函数使用 `override` 标记，这个标记的含义是如果你不重写基类中的方法，编译器就会报错。   

Let’s assume we’ve also created an `ICMPEvent`, we could now write:    
现在假设我们已经创建了一个 `ICMPEvent` 类，我们现在可以这样写： 

```c++
  PortScanEvent pse;
  cout << pse.getType() << endl; // "Portscan"

  ICMPEvent ice;
  cout << ice.getType() << endl; // "ICMP"

```

This is all entirely conventional, and does not do any magic, except that we are using an object that is partially defined in its base class.   
这非常方便，没有什么神奇的东西，除了我们正在使用的这个函数一部分是定义在它的基类里面的。   

However, we can also do:   
我们也可以这样做：   

```c++
  Event* e = &ice;
  cout << e->getDescription() << endl; // "ICMP of type 7"

  e = &pse;
  cout << e->getDescription() << endl; // "Portscan from 1.2.3.4"
```

This defines a pointer to an `Event`, in which we first store a pointer to an `ICMPEvent`. And lo, it continues to function as an `ICMPEvent`, even when stored in an `Event` pointer. The next two lines demonstrate how this also works for a `PortScanEvent`.   
上面的代码定义了一个指向 `Event` 类的指针，并给它赋值一个指向 `ICMPEvent` 类的指针。 虽然这个指针（指向 `ICMPEvent` 的指针）被存储在一个 `Event` 类型的指针，但是它和 `ICMPEvent` 功能是一样的，接下来的两行中演示了这种方法也适用于 `PortScanEvent` 类。


`Event` contains metadata which lets us know at runtime what type it `really` holds, and this metadata is consulted before doing any call that needs to know the actual class in there. This represents overhead, but is is the same kind of overhead generated if classes are simulated, as many C projects end up doing.  
`Event` 包含了一些元数据，这些数据让我们知道在运行的时候这个指针到底是什么类型，并且在进行一些调用，这些调用需要知道真正类型的时候，这些元数据已经提前计算出来了。这会产生一些开销，但这些开销和许多 C 项目中模拟类产生的是同一种开销。  

Interestingly enough, in the case above, compilers are sometimes able to ‘[devirtualise](http://hubicka.blogspot.com/2014/01/devirtualization-in-c-part-1.html)‘ calls since from the control flow, they know at compile time what the actual type of `Event` will be - an optimization not typically implemented in simulated classes in C.   
有趣的是，在上面的例子中，编译器有时能够‘[去虚拟化](http://hubicka.blogspot.com/2014/01/devirtualization-in-c-part-1.html)’，因为从上面的控制流程中，编译器在编译的时候知道到底是哪种 `Event` 类 - 这个优化通常来说在 C 语言中的模拟类中没有实现。   

Finally, if you ever need to know, you can find out what the real type of an `Event` is like this:  
最后，如果你需要知道类的真正类型的话，你可以像下面这样找出 `Event` 的真实类型：  

```c++
  auto ptr = dynamic_cast<PortScanEvent*>(e);
  if(ptr) {
    cout << "This is a PortScanEvent" << endl;
  }
```

If you got it wrong, `ptr` will be 0 (or `nullptr` in modern C++ lingo).  
如果第一行代码发生错误的话， `ptr` 就会变成 0 (或是现代 C++ 术语中的 `空指针`).     


I personally rarely use `runtime polymorphism` in a project, and then almost exclusively for APIs that need to receive/respond with records or events of different types. It is of great use whenever you have a collection of different ‘things’ that need to be stored in a single data structure.   
我个人很少在工程中使用 `运行时多态` ，除了需要发送/接受不同类型的记录或者事件的时候。无论何时你有大量不同的事务需要存储在唯一一个数据结构中，这都将非常有用。  

Of special note, the moment you find yourself writing functions that start with a `switch` statement depending on the type of your struct, you are likely better off using actual C++ inheritance.    
特别说明，当你发现你自己写的函数中的 `switch` 流程取决于你数据结构的类型的时候，你最好使用 C++ 继承。 

## A brief note on references  
## 对于引用的简单介绍  

```c++
void f(int& x) 
{
	x=0;
}

...

int i = 0;
int& j = i; 
j = 2;
cout << i << endl; // prints 2

f(i); // both i and j are now 0
```

Up to now, I have neglected to describe references, which made it to two examples in parts 1 and 2 of this series. Technically, a reference is nothing other than a pointer. There is no overhead. They are so much the same one may wonder why C++ bothered to provide this alternate syntax. Pointers already provided for pass by reference semantics.    
现在，我不会详细讲解引用，这个部分放在这个系列的第一部分和第二部分中的两个例子。技术上来说，引用就是一个指针。这里没有额外的开销。引用和指针非常相像，有人可能会好奇为什么 C++ 会特意提供这个可替代的语法。指针已经提供了传递引用的语法。

There are some finer points to be made, but references do save some typing. Functions can now return things ‘by reference’ and not force you to add `*` or `->` to every use for example.   
引用确实比指针有一些优点，引用可以省去一些打字的麻烦。函数现在可以‘通过引用’返回值，并且不强制你每次使用的时候都添加 `*` 和 `->` 运算符。   


This makes it possible for containers to implement: `v[12]=4` for example, which underneath is `value_type& operator[](size_t offset)`. If this returned a `value_type*` we’d have to type `*(v[12])=12` everywhere.    
这为容器的实现提供了可能性： 例如 `v[12]=4` ,在底层中使用了 `value_type& operator[](size_t offset)` 。如果它返回一个 `value_type*` （指针类型），我们就必须全部都用 `*(v[12])=12` 。

Some discussion on pointers versus references can be found [here](http://hubicka.blogspot.com/2014/01/devirtualization-in-c-part-1.html) and [here](https://stackoverflow.com/questions/8007832/could-operator-overloading-have-worked-without-references) on Stackoverflow.    
关于指针和引用比较的一些讨论可以在[这里](http://hubicka.blogspot.com/2014/01/devirtualization-in-c-part-1.html)和 [Stackover](https://stackoverflow.com/questions/8007832/could-operator-overloading-have-worked-without-references) 上找到。  

## Templates 
## 模板   
As noted in [part 1](https://ds9a.nl/articles/posts/c++-1), C++ was designed with the “Zero Overhead” principle in mind, which in its second part states “[no] feature [should] be added for which the compiler would generate code that is not as good as a programmer would create without using the feature”. This is a bold statement.    
正如 [第一部分](https://ds9a.nl/articles/posts/c++-1) 所说，C++ 是以 “零开销” 为原则设计的，在第二部分提到过 “任何添加到 C++ 中的特性都不会导致已有的代码（不使用新特性的代码）占用更多的空间或是运行速度变慢，如果编译器产生的代码比程序员不使用这些特性手写的代码性能要差的话，就不应该添加这项特性”。这是一个大胆的声明。  

Most programming languages called “Object Oriented” have made all objects descend (or inherit) from a magic Object base class. This means that to write a container in such a language means writing a data structure that hosts `Object` instances. If we store an `ICMPEvent` in there, we do so as an `Object`.  
大多数声称面向对象的编程语言都让所有对象从一个魔术基类派生（或者继承）。在这种语言中写一个容器意味着写一个能够容纳 `Object` 实例的数据结构。如果我们在其中存储一个 `ICMPEvent` 实例，我们也可以存储一个 `Object` 实例。  

A problem with this technique is that for C++, it violates the “Zero Overhead” principle. Storing a billion 32 bit numbers in C uses 4GB of memory. Storing a billion `Object` instances will use no less than 16GB - and likely more.  
这种技术有一个问题那就是对于 C++ 来说，它违背了 “零开销” 原则。在 C 语言中存储 10 亿 32 位整数使用了 4GB 内存。存储 10 亿 `Object` 实例需要使用多达 16GB 内存 - 甚至更多。

To adhere to its “Zero Overhead” promise, C++ implemented ‘templates’. Templates are like macros on steroids and come with tremendous power and, it has to be said, complication. They are worth it however, as they enable the library to provide generic containers that are as good and likely better than what you could write - and leave open the possibility of creating better versions too.    
为了遵守“零开销”原则，C++ 实现了 ‘模板’。模板就像是宏的升级版一样，非常有用，但不得不说，它很复杂。然而这种复杂相对于它的能力来说是值得的，因为它们能使库提供通用的容器，这些容器可能和你写出的一样甚至更好 - 并且提供了创造更棒版本的可能。   


As a brief example:  
一个简单的例子：   
```c++
template<typename T>
struct Vector
{
  void push_back(const T& t)
  {
    if(size + 1 > capacity) {
      if(capacity == 0) 
        capacity = 1;
      auto newcontents = new T[capacity *= 2];
      for(size_t a = 0 ; a < size ; ++a)
        newcontents[a]=contents[a];
      delete[] contents;
      contents=newcontents;
    }
    contents[size++] = t;
  }
  T& operator[](size_t pos)
  {
    return contents[pos];
  }       

  ~Vector()
  {
    delete[] contents;
  }

  size_t size{0}, capacity{0};
  T* contents{nullptr};
};

```

This implements a simplistic auto-growing vector of arbitrary type. It is used like this:   
这实现了一个简单的能够自动扩大容量，并且能容纳任意类型的 vector 容器。它可以这样使用：   

```c++
  Vector<uint32_t> v;
  for(unsigned int n = 0 ; n < 1000000000; ++n) {
    v.push_back(n);
  }
```

When the compiler encounters the first line, it triggers the instantiation of the `Vector` with `T` replaced by `uint32_t`. This delivers the exact same code as if you had written it by hand. There is no overhead.    
当编译器遇到第一行代码时，它会使用 `uint32_t` 替换 `T` 来生成一个 `Vector` 实例。这和你手写的代码完全一样。没有额外的开销。  

Similarly, functions can be templatized, for example:    
同样的，函数也可以模板化，例如：  

```c++
struct User
{
	std::string name;
	int uid;
};

Vector<User> users;
// fill users

if(users.isSorted([](const auto& a, const auto& b) {
	return a.uid < b.uid;}) 
{
	// do things
}
```  

This code compiles down to be as efficient as if you had written `a.uid < b.uid` in there yourself. Incidentally, because templates are incredibly generic, you could also pass function pointers or whole object to `isSorted`, as long as it is something the compiler can call. Incidentally, as shown in [part 1](https://ds9a.nl/articles/posts/c++-1/), passing a “predicate” like this is also what makes `std::sort` faster than C `qsort`.     
这些代码和你自己写 `a.uid < b.uid` 编译出来的运行效率使一样的。顺便说一下，因为模板适用范围很广，所以你也可以传递函数指针或者整个对象给 `isSorted` 函数，只要是编译器能够调用的，就可以传递给函数。另外，正如[第一部分](https://ds9a.nl/articles/posts/c++-1/)展示的，像这样传递一个 “谓语” 同样也可以让 `std::sort` 比 C语言的 `qsort` 速度快。  


Based on these templates, C++ offers an [array of powerful containers](https://en.cppreference.com/w/cpp/container) to store data in. Each of these containers comes with an API but also with a performance (scaling) guarantee. This in turn makes sure that implementors have to use state of the art algorithms - and they do.   
基于这些模板， C++ 提供 [有效容器的集合](https://en.cppreference.com/w/cpp/container) 来存储数据。每一个容器都有一个保证性能指标的的 API 。这反过来有确保了实现者必须使用高效的算法 - 他们也确实是这样做的。 

**Note:** This also means none of the sample code above should ever see production - [`std::vector`](https://en.cppreference.com/w/cpp/container/vector) and the associated [`std::is_sorted`](https://en.cppreference.com/w/cpp/algorithm/is_sorted) are already there and do a far better job.  
** 注意：** 这也意味着上面样例代码没有一个应该出现在实际产品中 - [`std::vector`](https://en.cppreference.com/w/cpp/container/vector) 和相关的 [`std::is_sorted`](https://en.cppreference.com/w/cpp/algorithm/is_sorted) 都已经实现了，并且性能比我们手写的更好。  

You may find yourself using a lot of these templated containers and associated algorithms, but very rarely writing any templated functions yourself. And this is pretty good news in two ways - first, writing templated code is harder than you’d think, and it has some surprising syntactical inconveniences. But secondly, almost everything you’d want to write a template for has been written already, so there rarely is a need.    
你可能发现你用了很多这些模板容器和相关的算法，几乎没有手写过任何模板函数。这在两个方面上来说是好消息 - 首先，写模板代码比你想象的难，并且它有一些令人吃惊的不便之处。但其次，几乎所有你想写的模板都已经存在了，所以几乎没有手写模板函数的必要。   

## A worked example
## 一个处理过的样例
Our hallowed “The C Programming Language” contains example code to count the use of C keywords in C programs. The good book rightfully spends a lot of time creating the relevant data structures from scratch.  
我们钟爱的 “The C Programming Language” 包含了这样一个样例代码，用来统计 C 程序中 C 关键词的使用。这本超棒的书花了大量的时间来从头开始创建相关的数据结构。  

Within our C++ environment however, we know our journey starts with very capable data structures already, so let’s not only count words in code, let’s also index everything. What follows is a 100 line example that indexes the entire Linux kernel source code (692MB) in 10 seconds, and performs instant lookups.    
然而在我们的 C++ 运行环境中，我们是从非常高效的数据结构开始的，所以我们现在不仅仅要统计代码中的关键词，还要给它们建立索引。接下来是一个 100 行的样例代码，在 10s 内给整个 Linux 内核代码（692MB） 建立索引，并且实现即时查询。   

First, let’s read which files to index:   
首先，让我们读入需要建立索引的文件：   

```c++
int main(int argc, char** argv)
{
	vector<string> filenames;

	ifstream ifs(argv[1]);
	std::string line;

	while(getline(ifs, line))
		filenames.push_back(line);

	cout<<"Have "<<filenames.size()<<" files"<<endl;
}
```

We read a file with filenames to index into a `std::vector`. Earlier I noted the C++ `iostreams` are in no way mandatory and that you can continue to use C `stdio`, but in this case `iostreams` are a convenient way to read lines of text of arbitrary length.     
我们通过文件名把文件读入到一个 `std::vector` 容器内。早前我注意到 C++ 中的 `iostreams` 不是强制的，你仍然可以使用 C 语言中的 `stdio` ,但 `iostream` 比起 `stdio` 来说可以很方便地读入任意长度的文本。

Next up, we read and index each file in turn:    
接下来，我们读入文件，依次给每个文件建立索引：  

```c++
unsigned int fileno=0;
	std::string word;

	for(const auto& fname : filenames) {   // "range-based for"
		size_t offset=0;
    		SmartFP sfp(fname.c_str(), "r");
		while(getWord(sfp.d_fp, word, offset)) {
			allWords[word].push_back({fileno, offset});
    		}
		++fileno;
  	}
```

This special form of `for` loop iterates over the contents of the `std::vector filenames`. This syntax works on all standard C++ containers, and will work on yours too if you [adhere to some simple rules](https://www.cprogramming.com/c++11/c++11-ranged-for-loop.html).    
这种特别形式的 `for` 循环遍历 `std::vector filenames` 中的内容。这个语法在所有标准 C++ 容器中都有效，如果你手写容器的时候[遵守了一些简单的规则](https://www.cprogramming.com/c++11/c++11-ranged-for-loop.html)，这个语法在你的容器也有效。  

In the next line we use `SmartFP` as defined in [part 2](https://ds9a.nl/articles/posts/cpp-2/) of this series. `SmartFP` internally carries a C `FILE*`, which means we get the raw speed of C `stdio`.     
接下来的一行中，我们使用这个系列 [第二部分的](https://ds9a.nl/articles/posts/cpp-2/) 中定义的 `SmartFP` 。 `SmartFP` 底层包含了一个 C `FILE*` ,这意味着我们获得了 C 相当于 `stdio` 的速度。    

`getWord` can be found in our sample code [GitHub](https://github.com/ahupowerdns/hello-cpp/blob/master/windex.cc), the only special thing to note there is that `std::string word` gets passed as a reference. This means we can keep reusing the same string instance, which saves a ton of malloc traffic. It also passes `offset` by reference, and this gets updated to the offset where this word was found in the file.  
`getWord` 可以在我们的样例代码 [GitHub](https://github.com/ahupowerdns/hello-cpp/blob/master/windex.cc) 中找到,需要特别指出的一点是 `std::string word` 是以引用的方式传入的。这意味这我们可以反复使用同一个 string 实例，这样可以节省大量 malloc 分配内存的开销。另外 `offset` 也是通过引用方式传入的， `offset` 会被赋值为文件中单词找到的位置。   


The `allWords` line is where the action happens. allWords is defined like this:  
`allWords` 行是所有行为发生的地方。`allWords` 是像下面这样定义：   

```c++
struct Location
{
	unsigned int fileno;
	size_t offset;
};

std::unordered_map<string, vector<Location>> allWords;
```

What this does is create an unordered associative container, keyed on a `string`. Per entry it contains a vector of Location objects, each of which represents a place where this word was found.   
这一行所做的是创建一个无序的关联型容器，键是 `string` 。每一项中都包含一个容纳位置对象的 vector 容器，每一个位置对象都代表着一个单词被找到的位置。 


Internally, the `unordered` containers are based on the hash of the key and by default C++ knows how to hash most primitive data types already. Compared to an `std::map`, which is ordered, the unordered variant is twice as fast for this usecase.     
在内部， `unordered` （无序)容器是基于键值的哈希值，并且默许 C++ 已经知道怎样对大多数简单的数据类型求哈希值。与 `std::map` 比起来，这个容器是有序的，无序的容器比我们样例快两倍。  


To actually look something up, we do:   
为了进行查找，我们这样做：  

```c++
while(getline(cin, line)) {
	auto iter = allWords.find(line);

	if(iter == allWords.end()) {
		cout<<"Word '"<<line<<"' was not found"<<endl;
		continue;
	}

	cout<<"Word '"<<line<<"' occurred "<<iter->second.size()<<" times: "<<endl;

	for(const auto& l : iter->second) {
		cout<<"\tFile "<<filenames[l.fileno]<<", offset "<<l.offset<<endl;
	}
}
```

This introduces the concept of an iterator. Sometimes an iterator is nothing more than a pointer, sometimes it is more complex, but it always denotes a ‘place’ within a container. There are two magic places, one `begin()`, one `end()`. To denote that nothing was found, the `end()` iterator is returned, and this is what we check against in the next line.   
这里引入了一个迭代器的概念。有时迭代器就是一个指针，有时它会更复杂一些，但它通常会标识容器中的位置。有两个神奇的位置，一个是 `begin()` ，另一个是 `end()` 。为了表示什么都没找到，它会返回一个 `end()` 迭代器，在上面的代码中我们在查找下面进行检查。  


If we have found something, we use iterator syntax to print how many hits we found: `iter->second.size()`. For an associative container, an iterator has two parts, conveniently called `first` and `second`. The first one has the key of the item, the other one provides access to the value found there (or, the actual item).   
如果找到了这个单词，我们就使用迭代器语法来输出我们找到了多少项： `iter->second.size()` 。对于一个关联型容器来说，一个迭代器有两个部分，简单地来说叫做 `first` 和 `second` 。第一个包含某项的键值，另一个提供对找到的值（或者说是真正的项）的访问权。  

In the final three lines, we again use range-based for syntax to loop over all the `Locations` for the word we searched for, and print the details.  
在最后三行里面，我们再次使用 range-based 形式的 for 语法来遍历所有的 `locations` 对象来寻找我们要的单词，然后输出详细内容。 

Now, to calibrate, we spent less than 50 unique lines on this using only default functionality, is this any good?  
现在，为了测试，我们使用 50 行互不相同的文本来测试这个功能，这有什么优点呢？

```shell
$ find ~/linux-4.13 -name "*.c" -o -name "*.h" > linux
$ /usr/bin/time ./windex linux < /dev/null
Have 45000 files
...
45000/45000 /home/ahu/linux-4.13/tools/usb/ffs-test.c, 103302249 words, 607209 different
Read 692542148 bytes
Done indexing
9.62user 1.09system 0:10.73elapsed 99%CPU (0avgtext+0avgdata 2047712maxresident)k
```

This represents an indexing speed of around 65MB/s, covering 692MB of data. Lookups are instantaneous. Memory usage, at 2GB is around 20 bytes per word which is not too shabby, since this includes storage of the word itself. If we add `__attribute__((packed))` or the equivalent to our `struct Location`, storage requirements decrease to 1.4GB or 15 bytes per word - close to the theoretical minimum of 12.    
这代表对 692 MB 数据建立索引的速度大约是 65MB/s。查找在一瞬间就完成了。在每个单词大约 20 bytes 的时候内存占用 2GB，这并不是很 low ,因为这 2GB 包含了单词本身占用的存储空间。如果我们添加 `__attribute__((packed))` 或者等价的 `struct Location` ,存储所需会降低到 1.4GB 或者每个单词 15 bytes - 几乎达到了理论上的最小值 12 bytes 。

On [GitHub](https://github.com/ahupowerdns/hello-cpp/blob/master/windex.cc) you can find the source code of the indexer - with the additional functionality that it can do prefix searches as well.  
在 [GitHub](https://github.com/ahupowerdns/hello-cpp/blob/master/windex.cc) 上你可以找到这个索引器的源代码 - 附带了额外的功能，还可以做前缀搜索。

## Summarising 
## 总结
C++ offers inheritance and polymorphic classes, and these are sometimes useful, definitely better than the hand-coded equivalent, but absolutely not mandatory to use. As an alternative to deriving everything from `Object`, as some languages do, C++ offers templates, which provide generic code that works on arbitrary types. This is what enables `std::sort` to be faster than `qsort` in C.    
C++ 提供了继承和多态类，有时候确实很有用，比起同样的手写代码肯定好地多，但这对我们来说并不是绝对强制使用的。作为替代从 `Object` 派生一切事物的方法，就像一些编程语言所做的，C++ 提供了模板，这提供了适用于各种类型的通用代码。这就是使得 `std::sort` 比 C 语言中 `qsort` 快的原因。

Templates are very powerful, and underlie the useful array of C++ standard containers like `std::map`, `std::unordered_map`, `std::vector`. Using range-based for loops and iterators, containers can be interrogated and modified.  
模板非常有效，并且组成了非常高效的 C++ 标准容器合集，像是 `std::map` ， `std::unordered_map` ， `std::vector` 。可以使用 range-based 形式的 for 循环和迭代器对容器进行查找和修改。

In [part 4](https://ds9a.nl/articles/posts/cpp-4) we continue to explore C++ and containers, and if you have any favorite things you’d like to see discussed or questions, please do hit me up on [@PowerDNS_Bert](https://twitter.com/PowerDNS_Bert) or bert.hubert@powerdns.com.   
在[第四部分](https://ds9a.nl/articles/posts/cpp-4) 我们将继续探索 C++ 和容器，如果你有任何你想讨论的喜欢的事情或者问题的话，请联系我 [@PowerDNS_Bert](https://twitter.com/PowerDNS_Bert) 或者使用邮箱 bert.hubert@powerdns.com 。 

NOTE: If you like this stuff, come work with me over at PowerDNS - aspiring C++ programmers welcome!   
注意：如果你喜欢这篇文章，可以和我一起为 PowerDNS 工作 - [欢迎 C++ 程序员](https://www.powerdns.com/careers.html#securityDeveloper)    

