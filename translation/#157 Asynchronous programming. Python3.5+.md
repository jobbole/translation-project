# Asynchronous programming. Python3.5+

# 【python异步编程系列4】基于python3.5+的异步编程

![](https://luminousmen.com/media/asynchronous-programming-python3.5.jpg)

This is a practical post of the series of asynchronous programming.

这篇文章是Python异步编程系列文章中的一篇

Whole series:

整个系列如下：

- [Asynchronous programming. Blocking I/O and non-blocking I/O](https://luminousmen.com/post/asynchronous-programming-blocking-and-non-blocking)
- [Asynchronous programming. Cooperative multitasking](https://luminousmen.com/post/asynchronous-programming-cooperative-multitasking)
- [Asynchronous programming. Await the Future](https://luminousmen.com/post/asynchronous-programming-await-the-future)
- [Asynchronous programming. Python3.5+](https://luminousmen.com/post/asynchronous-programming-python3.5)

- [异步编程，I/O阻塞和I/O非阻塞](https://luminousmen.com/post/asynchronous-programming-blocking-and-non-blocking)
- [异步编程，多任务合作](https://luminousmen.com/post/asynchronous-programming-cooperative-multitasking)
- [异步编程，Await和Future](https://luminousmen.com/post/asynchronous-programming-await-the-future)
- [异步编程，Python3.5+](https://luminousmen.com/post/asynchronous-programming-python3.5)

In this post we will be talking about the Python stack on the concepts we talked so far: from the simplest like threads, processes to the asyncio library.

在这篇文章中我们将讨论到目前为止我们谈到的Python栈的概念：从最简单的线程、进程，到asyncio库。

Asynchronous programming in Python has become more and more popular lately. There are many different libraries in python for doing asynchronous programming. One of those libraries is asyncio, which is a python standard library added in Python 3.4. In Python 3.5 we got an async/await syntax. Asyncio is part of the reason asynchronous programming is becoming more popular in Python. This article will explain what asynchronous programming is and compare some of these libraries.

异步编程最近在Python中越来越流行。在Python中有很多做异步编程的库。其中一个库asyncio已经被收录到了Python3.4的官方库中。在Python3.5中我们有了async/await语法。异步编程在Python中越来越流行的部分原因就是Asyncio。这篇文章将解释什么是异步编程，并且对其中的一些库进行比较。

-------------------------------------------------------------------------------

## Quick Recap
## 导读

What we have realized so far from the previous posts:

- **Sync:** Blocking operations.

- **Async:** Non-blocking operations.

- **Concurrency:** Making progress together.

- **Parallelism:** Making progress in parallel.

- **Parallelism implies Concurrency**. But Concurrency doesn’t always mean Parallelism.

我们从之前的文章中所讲的了解到：

- **同步**: 阻塞操作。

- **异步**: 非阻塞操作。

- **并发**: 使程序同时被运行

- **并行**: 使程序并行被执行

- **并行意味着并发**，但[并发并不一定意味着并行](https://luminousmen.com/post/concurrency-and-parallelism-are-different)

-------------------------------------------------------------------------------

Python code can now be mainly executed in one of two worlds, synchronous or asynchronous. You should think of them as separate worlds with different libraries and styles of calls, but sharing variables and syntax.

Python现在主要运行方式有两种，同步和异步。**你需要把他们当成两个分开的方式，他们的库和调用方式不一样**，但是变量和语法是相同的。

In the synchronous Python world, which has existed for several decades, you call functions directly, and everything is processed sequentially, exactly as you wrote your code. There are options to run the code concurrently.

Python的同步方式已经存在了几十年，你直接调用函数，所有的程序都按照你写的代码按顺序处理。这里有几种方式可以并行的运行代码。

## Synchronous world
## 同步的世界

In this post we will be comparing different implementations of the same code. We will try to execute two functions. First one is calculating the power of number:

在这篇文章中我们将比较同样代码的不同实现方式。我们会尝试执行两个函数，第一个是对数字进行幂运算：

```
def cpu_bound(a, b):
    return a ** b
```

We will do it N times:

我们将对这个方法调用N次：

```
def simple_1(N, a, b):
    for i in range(N):
        cpu_bound(a, b)
```
And the second one is downloading data from the web:

第二个是在网上下载数据：

```
def io_bound(urls):
    data = []
    for url in urls:
        data.append(urlopen(url).read())
    return data

def simple_2(N, urls):
    for i in range(N):
        io_bound(urls)
```
To compare how much time function works we implement simple decorator/context manager:

为了比较函数的运行时间，我们实现了简单的装饰器/上下文管理器：

```
import time
from contextlib import ContextDecorator

class timeit(object):
    def __call__(self, f):
        @functools.wraps(f)
        def decorated(*args, **kwds):
            with self:
                return f(*args, **kwds)
        return decorated

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, *args, **kw):
        elapsed = time.time() - self.start_time
        print("{:.3} sec".format(elapsed))
```
Now let's put it all together and run, to understand how much time my machine will be executing this code:

现在让我们将所有代码放在一起运行一下，来看看你的机器执行这些代码需要多长时间：

```
import time
import functools
from urllib.request import urlopen
from contextlib import ContextDecorator


class timeit(object):
    def __call__(self, f):
        @functools.wraps(f)
        def decorated(*args, **kwds):
            with self:
                return f(*args, **kwds)
        return decorated

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, *args, **kw):
        elapsed = time.time() - self.start_time
        print("{:.3} sec".format(elapsed))


def cpu_bound(a, b):
    return a ** b


def io_bound(urls):
    data = []
    for url in urls:
        data.append(urlopen(url).read())
    return data


@timeit()
def simple_1(N, a, b):
    for i in range(N):
        cpu_bound(a, b)


@timeit()
def simple_2(N, urls):
    for i in range(N):
        io_bound(urls)


if __name__ == '__main__':
    a = 7777
    b = 200000
    urls = [
        "http://google.com",
        "http://yahoo.com",
        "http://linkedin.com",
        "http://facebook.com"
    ]
    simple_1(10, a, b)
    simple_2(10, urls)
```

We implemented execution of the same functions N times sequentially.

我们将这些函数同时运行了N次。

On my hardware, cpu_bound function took 2.18 sec, io_bound — 31.4 sec.

在我的硬件条件上，计算密集型函数花了2.18秒，I/O密集型用了31.4秒。

So, we get our basic performance. Let's move on to threads.

所以，我们得到了基本的性能标准。我们现在来了解一下线程。

## Threads
## 线程

![](https://luminousmen.com/media/asynchronous-programming-python3.5-1.jpg)

A thread is the smallest unit of processing that can be performed in an OS.

线程是操作系统中能够进行运算调度的最小单元。

Threads of a process can share the memory of global variables. If a global variable is changed in one thread, this change is valid for all threads.

一个进程中的线程可以共享内存中的全局变量。如果全局变量在一个线程中被修改，这个修改在所有线程中都有效。

In simple words, a thread is a sequence of such operations within a program that can be executed independently of other code.

简单来说，**线程**是在程序中一系列操作，可以独立于其他代码运行。

Threads executing concurrently but can be executing in parallel — it depends on the system on which they are running.

线程是并发执行的，也可以并行执行，这就依赖于在什么系统上运行。

Python threads are implemented using OS threads in all implementations I know (CPython, PyPy and Jython). For each Python thread, there is an underlying OS thread.

Python线程是通过系统线程实现的，我知道的Python线程实现的解释器（CPython， PyPy和Jython）。对于每个Python线程，都有一个系统线程。

One thread is executed on one processor core per unit of time. It works until it consumes its time slice (default is 100 ms) or until it gives up control to the next thread by making a system call.

每单位时间在一个处理器核心上执行一个线程。它一直工作，直到分给它的时间用完（默认为100毫秒），或直到因为系统调用放弃对下一个线程的控制。

Let's try to implement our example functionality using threads:

我们试着通过线程来实现示例：

```
from threading import Thread

@timeit()
def threaded(n_threads, func, *args):
    jobs = []
    for i in range(n_threads):
        thread = Thread(target=func, args=args)
        jobs.append(thread) 

    # start the threads
    for j in jobs:
        j.start() 

    # ensure all of the threads have finished
    for j in jobs:
        j.join()

if __name__ == '__main__':
    ...
    threaded(10, cpu_bound, a, b)
    threaded(10, io_bound, urls)
```

On my hardware, cpu_bound took 2.47 sec, io_bound — 7.9 sec.

在我的硬件上，计算密集型函数花了2.47秒，I/O密集型用了7.9秒。

The I/O-bound function executed more than 5 times faster because we download the data in parallel on separate threads. But why CPU-bound operation goes slower?

I/O密集型函数执行时间快了5倍，因为我们在不同的线程上并行下载数据。但是为什么计算密集型运行更慢了呢？

In the reference implementation of Python — CPython there is the infamous GIL (Global Interpreter Lock). And we slowly go to its section...

这里实现Python的解析器用的是CPython，它有一个臭名昭著的GIL（Global Interpreter Lock）。我们先来了解一下GIL。。。

## Global Interpreter Lock (GIL)

## 全局解释器锁（GIL）

First of all, GIL is a lock that must be taken before any access to Python (and this is not only the execution of Python code but also calls to the Python C API). In essence, GIL is a global semaphore that does not allow more than one thread to work simultaneously within an interpreter.

首先，GIL是一个锁，在访问Python之前必须带GIL（且不仅仅是执行Python代码，调用Python API时也是）。本质上，GIL是一个全局信号量，GIL不允许多个线程在一个解释器中同时工作。

Strictly speaking, the only calls available after running the interpreter with an uncaptured GIL are its capture. Violation of the rule leads to an instant crash (the best option) or delayed crash of the program (much worse and harder to debug).

严格地说，在使用未捕获的GIL运行解释器之后，唯一可用的调用是它的捕获。违反规则会导致即时崩溃（最好的情况）或程序延迟崩溃（更糟糕且更难调试）。

*How it works?*

*它是怎么工作的呢？*

When the thread starts, it performs a GIL capture. After a while, the process scheduler decides that the current thread has done enough and give control to the next thread. Thread #2 sees that GIL is captured so that it does not continue to work, but plunges itself into sleep, yielding the processor to thread #1.

当线程开启时，会执行一个GIL捕获。一段时间后，进程调度程序认为当前线程已经做完了，然后将控制权给下一个线程。线程#2看到GIL已经被捕获就不会继续工作，而是进入休眠，把进程让给线程#1.

But the thread cannot hold GIL indefinitely. Prior to Python 3.3, GIL switched every 100 machine code instructions. In later versions of GIL, a thread can be held no longer than 5 ms. GIL is also released if the thread makes a system call, works with a disk or network(I/O-bound operation).

但是线程不能一直占着GIL。在Python 3.3之前，每100个机器代码指令GIL切换一次。在后面的GIL版本，一个线程不能超过5毫秒。如果线程进行系统调用，或使用磁盘或网络（I​​/O绑定操作），也会释放GIL。

In fact, GIL in python makes the idea of ​​using threads for parallelism in computational problems(CPU-bound operations) useless. They will work sequentially even on a multiprocessor system. On CPU-bound tasks, the program will not accelerate, but only slow down, because now the threads will have to halve the processor time. At the same time, the GIL I/O operation will not slow down, since before the system call the thread releases the GIL.

事实上，Python中通过使用线程解决计算机（CPU-绑定操作）并行的问题的想法，因为 GIL 的存在而失效了。即使在多线程系统也是同步运行。在计算密集型任务中，程序运行不会加快，反而会变慢，因为线程减半了进程的时间，同时，I/O操作不会变慢，因为系统调用线程释放了GIL。

It is clear that GIL slows down the execution of our program due to the additional work of creating and communicating threads, capturing and releasing the semaphore itself and preserving the context. But it needs to be mentioned that GIL does not limit parallel execution.

很明显，GIL让我们的程序执行速度变慢的原因是，由于创建和传递线程，捕获和释放信号以及保留上下文这些额外的工作。但是需要提到的是，GIL名没有限制并行执行。

GIL is not part of the language and does not exist in all language implementations, but only in the above mentioned CPython.

GIL不是一种Python语言的一部分，不是每种实现都存在该问题。只是在 CPython 中被用到。


*So why the heck does he even exist?*

*所以它为什么会存在呢？*

**GIL protects operating data structures from concurrent access problems.** For example, it prevents the race condition when the object's reference count value changes. GIL makes it easy to integrate non-thread safe libraries on C. Thanks to GIL, we have so many fast modules and binders for almost everything.

**GIL保护数据结构操作免受并发访问问题的影响。**比如，当对象的引用计算的数值发生改变是，它可以防止竞争条件。GIL使得可以很容易地在C上集成非线程安全库。感谢有GIL，我们可以有那么多的快速模块和绑定器。

There are exceptions, for example, the GIL control mechanism is available to C libraries. For example, NumPy releases it on long operations. Or, when using the numba package, the programmer can control the semaphore disabling itself.

也有例外，GIL控制器可以直接用于C库。例如，NumPy在整型操作中可以释放GIL。或者，当使用numba包时，程序可以控制关掉信号。

On this sad note, you can come to the conclusion that threads will be enough for parallelizing tasks that are tied to I/O. But computing tasks should be run in separate processes.

在这段悲伤的说明中，你可以得出结论是，线程适用于在I/O密集型中处理并行任务。但是计算任务应该被放在不同的进程中执行。

## Processes

## 进程

From the OS point of view, a process is a data structure that holds a memory area and some other resources, for example, files opened by it. Often the process has one thread, called main, but the program can create any number of threads. At the start, the thread is not allocated individual resources, instead, it uses the memory and resources of the process that spawned it. Due to this, the threads can quickly start and stop.

从系统角度来看，进程是一个数据结构有一个内存空间和一些资源，比如，需要一个进程打开文件。通常一个进程有一个线程，称为主线程，不过程序可以创建任意数目的线程。在一开始，线程是不可分配的独立资源，它会用进程的内存和资源。因为这个原因，线程可以很快的开始和结束。

Multitasking is handled by the scheduler — part of the OS kernel, which in turn loads the execution threads into the central processor.

多任务由调度程序控制，调度程序是操作系统内核之一，会将执行线程加载到中央处理器中。

Like threads, processes are always executed concurrently, but they can also be executed in parallel, depending on the presence of the hardware component.

像线程一样，进程通常也是并发执行，且也可以并行，这取决于当前的硬件条件。

```
from multiprocessing import Process

@timeit()
def multiprocessed(n_threads, func, *args):
    processes = []
    for i in range(n_threads):
        p = Process(target=func, args=args)
        processes.append(p)

    # start the processes
    for p in processes:
        p.start()

    # ensure all processes have finished execution
    for p in processes:
        p.join()

if __name__ == '__main__':
    ...
    multiprocessed(10, cpu_bound, a, b)
    multiprocessed(10, io_bound, urls)
```
On my hardware, cpu_bound took 1.12 sec, io_bound — 7.22 sec.

在我的硬件中，计算密集型花费1.12秒，I/O密集型花费7.22秒。

So, the calculation operation executed faster than threaded implementation because now we are not stuck in capturing GIL, but the I/O bound function took slightly more time because processes are more heavyweight than threads.

因此，计算操作比线程实现执行得更快，因为现在我们并没有停留在捕获GIL，但是I/O密集型函数花费的时间更多，因为进程比线程更重。

## Asynchronous world

## 异步的世界

![](https://luminousmen.com/media/asynchronous-programming.jpg)

In an asynchronous world, everything changes a bit. Everything works in a central event-processing loop, which is a small code that allows you to run several coroutines (an important term, in simple terms it is not OS-managed threads, except they are co-operatively multitasking, and hence not truly concurrent) at the same time. Coroutines work synchronously until the expected result is reached, and then they stop, transfer control to the event loop, and something else can happen.

在异步的世界，所有的事情都发生了一些改变。所有的任务都在一个中央事件处理环中，事件循环是一段很小的代码，它允许你同时做几个协程（这是一个重要的术语，简单的来说这不是系统管理线程，它们是多任务合作，但并不是真正的并发）。协程工作是同步运行的，直到得到期望的结果，然后工作结束，控制权转给了事件循环，接着再做其他的事。

### Green threads
### 绿色线程

![](https://luminousmen.com/media/asynchronous-programming-python3.5-2.jpg)

Green threads are a primitive level of asynchronous programming. A green thread is a regular thread, except that switching between threads is done in the application code(on the user level), and not in the processor(OS level). The core of it is non-blocking operations. Switching between threads occurs only on I/O. Non-I/O threads will take control forever.

[绿色线程](https://luminousmen.com/post/asynchronous-programming-await-the-future)是异步编程的基础层。绿色线程与常规线程一样，除了它的线程切换实现是在应用程序中（用户层），而不是处理器（操作系统层）。它的核心是[非阻塞操作](https://luminousmen.com/post/asynchronous-programming-blocking-and-non-blocking)。线程之间的切换仅在I/O上发生。非I/O线程将一直享有控制权。

Gevent is a well-known Python library for using green threads. Gevent is a green thread and non-blocking I/O. gevent.monkey modifies the behavior of standard Python libraries so that they allow non-blocking I/O operations to be performed.

[Gevent](http://www.gevent.org/)是一个目前非常广泛的绿色线程以及非阻塞的Python包。gevent.monkey方法改变了标准Python包，使得其可以允许非阻塞操作。

Other libraries:

其他的库：

- [eventlet](http://eventlet.net/)
- [Tornado](https://www.tornadoweb.org/en/stable/)
- [Twisted](https://twistedmatrix.com/)
- [Stackless Python](https://en.wikipedia.org/wiki/Stackless_Python)

Let's see how performance changes if we start using green threads using gevent library in Python:

让我们来看看在Python中通过使用gevent来使用绿色线程的效果是怎么样的吧：

```
import gevent.monkey

# patch any other imported module that has a blocking code in it 
# to make it asynchronous.
gevent.monkey.patch_all()

@timeit()
def green_threaded(n_threads, func, *args):
    jobs = []
    for i in range(n_threads):
        jobs.append(gevent.spawn(func, *args))
    # ensure all jobs have finished execution
    gevent.wait(jobs)

if __name__ == '__main__:
    ...
    green_threaded(10, cpu_bound, a, b)
    green_threaded(10, io_bound, urls)
```

Results are: cpu_bound — 2.23 sec, io_bound — 6.85 sec.

结果：计算密集型 - 2.23秒，I/O密集型 - 6.85秒

Slower for CPU-bound function, and faster for I/O-bound function. As expected.

如期望中的一样，计算密集型更慢了，I/O密集型更快了。

## Asyncio

## Asyncio

The asyncio package is described in the Python documentation as a library for writing parallel code. However, asyncio is not multithreaded and is not multiprocessing. It is not built on top of one of them.

Asyncio在Python中是用来编写[并行代码的库](https://docs.python.org/3/library/asyncio.html)。然而，Asyncio并不是多线程和多进程的。它不是为了多线程和多进程而设计的。

While Gevent and Twisted aim to be higher level frameworks, asyncio aims to be a lower-level implementation of an asynchronous event loop, with the intention that higher level frameworks like Twisted, Gevent or Tornado, will build on top of it. However, by itself, it makes a suitable framework on its own.

Gevent和Twisted的目标是作为高层级的框架。而Asyncio的目的是异步事件循环的低层级实现，从而让其他高层级框架（Twisted, Gevent和Tornado等）可以基于它而构建。
然而，就Asyncio本身而言，它就是一个很好的框架。

In fact, asyncio is a single-threaded, single-process project: it uses cooperative multitasking. asyncio allows us to write asynchronous concurrent programs running in the same thread, using an event loop for scheduling tasks and multiplexing I/O through sockets (and other resources).

事实上，Asyncio是一个[处理多任务](https://luminousmen.com/post/asynchronous-programming-cooperative-multitasking)的单线程和单进程项目。Asyncio可以让我们在同一个线程上运行异步并发程序，通过事件循环来处理任务，通过sockets（或其他的资源）来多路复用I/O.

asyncio provides us an event loop along with other good stuff. The event loop tracks different I/O events and switches to tasks which are ready and pauses the ones which are waiting on I/O. Thus we don’t waste time on tasks which are not ready to run right now.
 
Asyncio提供很多有用的API，包括事件循环。事件循环追踪不同的I/O事件，让那些已经准备好的任务开始执行，而将还在I/O上等待的任务暂停。

## How it works

## 怎么工作的呢？

Synchronous and asynchronous functions/callables are different types — you can't just mix them. If you block a coroutine synchronously — maybe you use time.sleep(10) rather than await asyncio.sleep(10) — you don't return control to the event loop — the entire process will block.

同步和异步的方法或调用是不同的，你能不将他们混为一谈。如果你要阻塞了一个同步的协程，你要用time.sleep(10)而不是await asyncio.sleep(10)，你不需要将控制返回给事件循环，全部的进程都会被阻塞。

You should think of your codebase as comprised of pieces of either sync code or async code — anything inside an async def is async code, anything else (including the main body of a Python file or class) is synchronous code.

你要考虑你的代码既有同步代码也有异步代码，任何在异步方法中的代码都是异步的，其他（包括Python文件或者类的主函数）是同步代码。

![](https://luminousmen.com/media/asynchronous-programming-await-the-future-4.jpg)

The idea is very simple. There’s an event loop. And we have an asynchronous function (coroutine) in Python, you declare it with async def, which changes how its call behaves. In particular, **calling it will immediately return a coroutine object**, which basically says "I can run the coroutine and return a result when you await me".

这样想比较简单。这有一个事件循环。然后我们将Python中的一个异步方法（协程）声明为一个async def，函数的调用方式就发生了改变。特别是，**调用这个函数会很快返回一个协程对象**，它的意思是说“我可以运行协程，当你await的时候返回一个结果”。

We give those functions to the event loop and ask it to run them for us. The event loop gives us back a Future object, it’s like a promise that we will get something back in the future. We hold on to the promise, time to time check if it has a value (when we feel impatient) and finally when the future has a value, we use it in some other operations.

我们将这些方法交给事件循环，让它帮我们去运行这些函数。事件循环会给我们返回一个Future对象，这就像一个保证告诉我们未来会把结果返回给我们。我们拿着这个保证，一次一次的去查看它有没有返回的结果（当我们失去耐心时），终于返回值来了，我们可以用返回的结果再进行其他的操作。

When you call await, the function gets suspended while whatever you asked to wait on happens, and then when it's finished, the event loop will wake the function up again and resume it from the await call, passing any result out. 

当你调用await时，当前方法执行会暂停下来，等待你要等的东西，当等待结束后，事件循环将再次唤醒函数从await调用中恢复，并将await到的结果返回。

Example:
示例：

```
import asyncio

async def say(what, when):
    await asyncio.sleep(when)
    print(what)

loop = asyncio.get_event_loop()
loop.run_until_complete(say('hello world', 1))
loop.close()
```

In the example here, the say() function pauses and gives back control to the event loop, which sees that sleep needs to run, calls it, and then that calls await and gets suspended with a marker to resume it one second. Once it resumes, say completes, returns a result, and then that makes main ready to run again and the event loop resumes it with the returned value.

在这个例子中，say()方法暂停运行并把控制交给事件循环，事件循环看到要运行**sleep**方法并调用它，然后整个调用进入等待，并且标记在一秒钟后恢复。一旦恢复，会通知事件循环完成并返回结果，然后让主程序准备继续运行，事件循环恢复了主程序并返回结果。

This is how async code can have so many things happening at once - anything that's blocking calls await, and gets put onto the event loop's list of paused coroutines so something else can run. Everything that's paused has an associated callback that will wake it up again — some are time-based, some are I/O-based, and most of them are like the example above and waiting for a result from another coroutine.

这就是异步代码为什么可以同时发生那么多事情的原因——任何方法阻塞当前调用使其进入等待，然后被放入事件循环的暂停协程列表，这样其他的程序就能够运行。每个被暂停的程序都有一个相关的回调，用于未来将它唤醒，而这些程序被暂停有的是因为运行时间，有些是因为I/O操作，且大多数都像上面的例子一样，需要等待另一个协程的结果。

Let's return to our example. We have two blocking functions cpu_bound and io_bound. As I said, we cannot mix synchronous and asynchronous operations — we must make all of them asynchronous. Naturally, not for everything there are asynchronous libraries. Some code remains blocking, and it must somehow be run so that it does not block our event loop. For this, there is a good run_in_executor() method, which runs what we passed to it in one of the threads of the built-in pool, without blocking the main thread with the event loop. We will use this functionality for our CPU-bound function. We will rewrite the I/O-bound function completely to await those moments when we are waiting for an event.

让我们回到刚刚的例子。我们有两个阻塞的函数，计算密集型和I/O密集型。就像我说的那样，我们不能把同步和异步操作混在一起用——**而是必须把所有操作都变成异步的**。当然，不是所有东西都有异步库。**有些代码仍然是[阻塞](https://luminousmen.com/post/asynchronous-programming-blocking-and-non-blocking)的**，必须以某种方式让它运行，不然会阻塞事件循环。这个问题的解决方法是，使用事件循环对象的 run_in_executor()方法，它会在线程池中新建一个线程来运行，而不会阻塞事件循环中的主线程。我们将在计算密集型方法中使用这个功能。我们也会完全重写I/O密集型方法，使其await那些我们需要等待的事件。

```
import asyncio
import aiohttp

async def async_func(N, func, *args):
    coros = [func(*args) for _ in range(N)]
    # run awaitable objects concurrently
    await asyncio.gather(*coros)


async def a_cpu_bound(a, b):
    result = await loop.run_in_executor(None, cpu_bound, a, b)
    return result


async def a_io_bound(urls):
    # create a coroutine function where we will download from individual url
    async def download_coroutine(session, url):
        async with session.get(url, timeout=10) as response:
            await response.text()

    # set an aiohttp session and download all our urls
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            await download_coroutine(session, url)


if __name__ == '__main__':
    ...
    loop = asyncio.get_event_loop()
    with timeit():
        loop.run_until_complete(async_func(10, a_cpu_bound, a, b))

    with timeit():
        loop.run_until_complete(async_func(10, a_io_bound, urls))
```

Results are: cpu_bound — 2.23 sec, io_bound — 4.37 sec.

结果：计算密集型 - 2.23秒，I/O密集型 - 4.37秒。

Slower for CPU-bound function, and almost twice as fast as the threaded example for I/O-bound function.

计算密集型慢了，而I/O密集型比线程的例子快了近两倍。

## Making the Right Choice
## 做一个正确的选择

- CPU-bound -> multiprocessing
- I/O-bound, fast I/O, Limited Number of Connections -> multithreading
- I/O-bound, slow I/O, many connections -> asyncio

- 计算密集型 -> 多进程 
- I/O密集型，I/O比较快，连接数有限制 -> 多线程
- I/O密集型，I/O比较慢，连接数比较多 -> 异步

## Conclusion

## 结论

Threads will be easier if you have a typical web application that does not depend on external services, and relatively finite amount users for whom the response time will be predictably short.

如果是一个不依赖于外部服务的典型的Web应用，并且相关的有限数量的用户的响应时间可以预见是比较短的，那么使用线程会比较容易。

async is suitable if the application spends most of the time reading/writing data, rather than processing it. For example, you have a lot of slow requests — websockets, long polling, or there are slow external synchronous backends, requests for which are unknown when they end.

异步适用于需要花大部分时间进行数据读写而不是处理的操作的应用，比如，你有大量慢请求 - websockets，长轮询，或者是一些比较慢的外部后端同步操作，那些不知道什么时候结束的请求。

Synchronous programming is what most often begins the development of applications in which sequential execution of commands is performed.

同步编程是那些连续执行的命令的应用的开发中最常用的。

Even with conditional branching, loops, and function calls, we think about code in terms of performing one step at a time. After the completion of the current step, it proceeds to the next.

即使在条件分支，循环，和函数调用中，我们也会考虑一次执行一个步骤，完成当前步骤后再进入下一步。

An asynchronous application behaves differently. It still running one step at a time, but the difference is that the system moving forward, it's not waiting for the completion of the current execution step. As a result, we are going to the event-driven programming.

异步应用的表现是不一样的。它仍然是一次执行一个步骤，不同的地方在于系统会继续向前运行，不会等待当前执行结束。结果就是，我们将进行[事件驱动的编程](https://en.wikipedia.org/wiki/Event-driven_programming)。

asyncio is a great library and it's cool that it was included into Python standard library. asyncio has already begun to build an ecosystem (aiohttp, asyncpg, etc.) for application development. There are other event loop implementations (uvloop, dabeaz/curio, python-trio/trio), and I think the asyncio will evolve in even more powerful tool.

asyncio是一个很好用的库，已经被放进Python的标准库里了。asyncio已经开始为应用开发建造一个系统了（aiohttp，asyncpg，等）。这里也有一些其他的事件循环的实现（[uvloop](https://github.com/MagicStack/uvloop)，[dabeaz/curio](https://github.com/dabeaz/curio)，[python-trio/trio](https://github.com/python-trio/trio)）。我认为asyncio将会发展成一个很厉害的工具。

## Links

## 链接

- [PEP 342](https://www.python.org/dev/peps/pep-0342/)
- [PEP 492](https://www.python.org/dev/peps/pep-0492/)
- Check the old [guido's presentation](https://www.dropbox.com/s/essjj4qmmtrhys4/SFMeetup2013.pdf) of the asyncio approach.
- Interesting talk of Robert Smallshire ["Get to grips with asyncio in Python3"](https://youtu.be/M-UcUs7IMIM)
- [David Beazley's Curio library](https://curio.readthedocs.io/en/latest/)
- [Trio project](https://trio.readthedocs.io/en/latest/)
- [David Beazley talk](https://youtu.be/ZzfHjytDceU) about getting rid of asyncio
- [uvloop - faster event-loop for asyncio](https://magic.io/blog/uvloop-blazing-fast-python-networking/)
- [Some thoughts on asynchronous API design in a post-async/await world](https://vorpus.org/blog/some-thoughts-on-asynchronous-api-design-in-a-post-asyncawait-world/)