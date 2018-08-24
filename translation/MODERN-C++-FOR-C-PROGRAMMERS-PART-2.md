---
editor: hanxiaomax
published: false
title: MODERN C++ FOR C PROGRAMMERS-PART-2
---
## Namespaces
## 命名空间

Namespaces allow things with identical names to live side by side. This is of immediate relevance to us since C++ defines a lot of functions and classes that might collide with names you are already using in C. Because of this, the C++ libraries live in the std:: namespace, making it far easier to compile your C code as C++.

命名空间保证变量可以拥有唯一到变量名。这和我们嘻嘻相关因为 C++ 定义了很多函数和类，以至于可能会有和 C 语言同名函数产生命名冲突的可能。因此 C++ 标准库被定义在`std::`命名空间中，这使得将你的 C 语言代码看作 C++ 进行编译变得更加简单。

To save a lot of typing, it is possible to import the entire std:: namespace with using namespace std, or to select individual names: using std::thread.

为了减少繁琐的输入，我们可以使用 `using namespace std` 直接将 `std::`，或者可以使用单独的名字 `using std::thread`。

C++ does have some keywords itself like this, class, throw, catch and reinterpret_cast that could collide with existing C code.

C++ 也有一些自己的关键字，例如`this`,`class`,`throw`,`catch`和`reinterpret_cast`，这些也可以和已经存在的 C 代码产生冲突。


## Classes
## 类

An older name of C++ was ‘C with classes’, and consisted of a translator that converted this new C++ into plain C. Interestingly enough this translator itself was written in ‘C with classes’.

C++ 有个曾用名，叫做“有类的C语言” （C with classes），同时它包含一个可以将 C++ 翻译为 C 的翻译器。有意思的是，这个翻译器就是使用“有类的C语言”编写的。

Most advanced C projects already use classes almost exactly like C++. In its simplest form, a class is nothing more than a struct with some calling conventions. (Inheritance & virtual functions complicate the picture, and these optional techniques will be discussed in part 3).

很多高级的 C 语言项目都已经在使用类了，几乎和 C++ 完全一样。对于一个类来讲，其最简单的形式其实就是一个结构体外加一些调用的规则（继承和虚函数使其变得更加复杂，这些非必须的技术我们会在第三篇文章中讨论）。

Typical modern C code will define a struct that describes something and then have a bunch of functions that accept a pointer to that struct as the first parameter:

一个典型的现代 C 语言代码会定一个一个结构体来描述一个对象，并且定义一系列的函数，其第一个参数的类型就是该结构体的指针类型。

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

A C++ class is laid out just like the struct above, and in fact, if it contains methods (member functions), these internally get called in exactly the same way:

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

The one difference is that these ‘private member variables’ are not accessible from the outside. This may be useful for example when any change in x needs to be coordinated with the Canvas, and we don’t want users to change x without us knowing it. As noted, many C projects achieve the same opaqueness with tricks - this is just an easier way of doing it.

Up to this point, a class was nothing but syntactic sugar and some scoping rules. However..

## Resource Acquisition Is Initialization (RAII)
Most modern languages perform garbage collection because it is apparently too hard to keep track of memory. This leads to periodic GC runs which have the potential to ‘stop the world’. Even though the state of the art is improving, GC remains a fraught subject especially in a many-core world.

Although C and C++ do not do garbage collection, it remains true that it is exceptionally hard to keep track of each and every memory allocation under all (error) conditions. C++ has sophisticated ways to help you and these are built on the primitives called Constructors and Destructors.

SmartFP is an example that we’ll beef up in following sections so it becomes actually useful and safe:

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

Typical use of SmartFP:

```cpp
void func()
{
	SmartFP fp("/etc/passwd", "r");
	if(!fp.d_fp)
		// do error things

	char line[512];
	while(fgets(line, sizeof(line), fp.d_fp)) {
		// do things with line
	}	
	// note, no fclose
}
```
As written like this, the actual call to fopen() happens when the SmartFP object is instantiated. This calls the constructor, which has the same name as the struct itself: SmartFP.

We can then use the FILE* that is stored within the class as usual. Finally, when fp goes out of scope, its destructor SmartFP::~SmartFP() gets called, which will fclose() for us if d_fp was opened successfully in the constructor.

Written like this, the code has two huge advantages: 1) the FILE pointer will never leak 2) we know exactly when it will be closed. Languages with garbage collection also guarantee ‘1’, but struggle or require real work to deliver ‘2’.

This technique to use classes or structs with constructors and destructors to own resources is called Resource Acquisition Is Initialization or RAII, and it is used widely. It is quite common for even larger C++ projects to not contain a single call to new or delete (or malloc/free) outside of a constructor/destructor pair. Or at all, in fact.

## Smart pointers
Memory leaks are the bane of every project. Even with garbage collection it is possible to keep gigabytes of memory in use for a single window displaying chat messages.

C++ offers a number of so called smart pointers that can help, each with its own (dis)advantages. The most “do what I want” smart pointer is std::shared_ptr and in its most basic form it can be used like this:

```cpp
void func(Canvas* canvas)
{
	std::shared_ptr<Circle> ptr(new Circle(canvas));
	// or better:
	auto ptr = std::make_shared<Circle>(canvas)
}
```

The first form shows the C++ way of doing malloc, in this case allocating memory for a Circle instance, and constructing it with the canvas parameter. As noted, most modern C++ projects rarely use “naked new” statements but mostly wrap them in infrastructure that takes care of (de)allocation.

The second way is not only less typing but is more efficient as well.

std::shared_ptr however has more tricks up its sleeve:

```cpp
// make a vector of shared pointers to Circle instances
std::vector<std::shared_ptr<Circle> > circles;

void func(Canvas* canvas)
{
	auto ptr = std::make_shared<Circle>(canvas)
	circles.push_back(ptr);
	ptr->draw();
}
```

This first defines a vector of std::shared_ptrs to Circle, then creates such a shared_ptr and stores it in the circles vector. When func returns, ptr goes out of scope, but since a copy of it is in the vector circles, the Circle object stays alive. std::shared_ptr is therefore a reference counting smart pointer.

std::shared_ptr has another neat feature which goes like this:



```cpp
void func()
{
        FILE *fp = fopen("/etc/passwd", "r");
        if(!fp)
          ; // do error things

        std::shared_ptr<FILE> ptr(fp, fclose);

        char buf[1024];
        fread(buf, sizeof(buf), 1, ptr.get());
}

```
Here we create a shared_ptr with a custom deleter called fclose. This means that ptr knows how to clean up after itself if needed, and with one line we’ve created a reference counted FILE handle.

And with this, we can now see why our earlier defined SmartFP is not very safe to use. It is possible to make a copy of it, and once that copy goes out of scope, it will ALSO close the same FILE*. std::shared_ptr saves us from having to think about thse things.

The downside of std::shared_ptr is that it uses memory for the actual reference count, which also has to be made safe for multi-threaded operations. It also has to store an optional custom deleter.

C++ offers other smart pointers, the most relevant of which is std::unique_ptr. Frequently we do not actually need actual reference counting but only ‘clean up if we go out of scope’. This is what std::unique_ptr offers, with literally zero overhead. There are also facilities for ‘moving’ a std::unique_ptr into storage so it stays in scope. We will get back to this later.


## Threads, atomics
Every time I used to create a thread with pthread_create in C or older C++, I’d feel bad. Having to cram all the data to launch the thread through a void pointer felt silly and dangerous.

C++ offers a powerful layer on top of the native threading system to make this all easier and safer. In addition, it has ways of easily getting data back from a thread.

A small sample:

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

```cpp
  std::thread t(factorial, 19);
	t.join(); // or t.detach()
```

Like C11, C++ offers atomic operations. These are as simple as defining std::atomic<uint64_t> packetcounter. Operations on packetcounter are then atomic, with a wide suite of ways of interrogating or updating packetcounter if specific modes are required to for example build lock free data structures.

Note that as in C, declaring a counter to be used from multiple threads as volatile does nothing useful. Full atomics are required, or explicit locking.


## Locking
Much like keeping track of memory allocations, making sure to release locks on all codepaths is hard. As usual, RAII comes to the rescue:

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




## Error handling
To be honest, error handling is a poorly solved problem in any language. We can riddle our code with checks, and at each check I wonder “what should the program actually DO if this fails”. Options are rarely good - ignore, prompt user, restart program, or log a message in hopes that someone reads it.

C++ offers exceptions which in any case have some benefits over checking every return code. The good thing about an exception is that, unlike a return code, it is not ignored by default. First let us update SmartFP so it throws exceptions:

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

Combined with RAII, exceptions are a very powerful technique to safely acquire resources and also deal with errors.

Code that can throw exceptions is slightly slower than code that can’t but it barely shows up in profiles. Actually throwing an exception is rather heavy though, so only use it for error conditions.

Most debuggers can break on the throwing of an exception, which is a powerful debugging technique. In gdb this is done with catch throw.

As noted, no error handling technique is perfect. One thing that seems promising is the std::expected work or boost::expected which creates functions that have both return codes or throw exceptions if you don’t look at them.

## Summarising
In part 2 of ‘C++ for C programmers’, we showed how classes are a concept that is actually well used in C already, except that C++ makes it easier. In addition, C++ classes (and structs) can have constructors and destructors and these are extremely useful to make sure resources are acquired and released when needed.

Based on these primitives, C++ offers smart pointers of varying intelligence and overhead that cover most requirements.

Furthermore, C++ offers good support for threads, atomics and locking. Finally, exceptions are a powerful way of (always) dealing with errors.

If you have any favorite things you’d like to see discussed or questions, please hit me up on @PowerDNS_Bert or bert.hubert@powerdns.com

Part 3 is now available.

NOTE: If you like this stuff, come work with me over at PowerDNS - aspiring C++ programmers welcome!
