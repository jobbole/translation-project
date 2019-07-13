---
translator: http://www.jobbole.com/members/snowhere/
reviewer: http://www.jobbole.com/members/hanxiaomax/
via: https://dzone.com/articles/top-15-java-multithreading-concurrency-interview-q
---

# Java 面试：投行的 15 个多线程和并发面试题
# Top 15 Java Multithreading, Concurrency Interview Questions With Investment Banks

[原文](https://dzone.com/articles/top-15-java-multithreading-concurrency-interview-q)

Multithreading and concurrency questions are an essential part of any Java interview. If you are going for an interview with an investment bank, e.g. Barclays, Citibank, Morgan Stanley for an equities front office Java developer position, you can expect a lot of multithreading interview questions. Multithreading and concurrency are popular topics on investment banking interviews, especially on electronic trading development jobs where they grill candidates on the many tricky Java thread interview questions. They want to ensure that the candidate has a solid knowledge of multithreading and concurrent programming in Java, because most of them are in the business of performance which provides them a competitive advantage.

多线程和并发问题已成为各种 Java 面试中必不可少的一部分。如果你准备参加投行的 Java 开发岗位面试，比如巴克莱银行（Barclays）、花旗银行（Citibank）、摩根史坦利投资公司（Morgan Stanley），你会遇到很多有关多线程的面试题。多线程和并发是投行面试的热门知识点，尤其是在面试有关电子交易开发工作时，他们喜欢用棘手的 Java 线程面试题轰炸面试者。他们希望确保面试者对 Java 多线程和并发有扎实的知识基础，因为他们大多数关注高性能带来的竞争优势。

For example, high volume and low latency electronic trading systems, which are used for Direct to Market (DMA) trading, are usually concurrent in nature. Most of the time, they will focus on microsecond latency, which is why a good knowledge of how to effectively minimize latency and improve throughput is important.

举个例子，直接市场准入模式（Direct to Market，DMA）使用高容量低延迟的电子交易系统，通常来说是并发的。大多数时间他们致力于微秒级的延迟，所以掌握如何有效地降低延迟、提高吞吐量非常重要。

These are some of my favorite thread interview questions about Java. I am not providing an answer to these thread interview questions, but I will give you a hint whenever possible. I will update the post further with detailed answers, like I did for my recent post 10 Singleton interview questions in Java.

有一些 Java 线程面试题是我特别中意的。我并不会直接给你答案，而是尽可能给你指点。我会之后补充上详细答案，正如我在其他文章中那样。

After the introduction of the concurrency package in JDK 1.5, there were some questions on concurrent utility and concurrent collections, which were increased, e.g. ThreadLocal, BlockingQueue, Counting Semaphore and ConcurrentHashMap become popular.

JDK 1.5 中引入并发包之后，并发工具和并发集合备受欢迎，比如 ThreadLocal、 BlockingQueue、Counting Semaphore 和 ConcurrentHashMap，与这些工具相关的面试题也越来越多。

The same is true for Java 8 and Java 9. There were questions on lambda expressions, parallel streams, new fork-join pool, and CompletableFuture, which is on the rise in 2018 and will remain in 2019. Hence, you should be prepared for those topics.

Java 8 和 Java 9 也是这种情况。围绕 lambda 表达式、并行流（parallel streams）、新的 Fork/Join 线程池、CompletableFuture 的问题在 2018 年不断涌现，2019 年还将持续。今后你也应该对这些知识点有所准备。

## 15 Java Thread Interview Questions and answers
## 15 个 Java 线程面试题和答案

Anyway, without further ado, here is my list of some of the frequently asked Java multithreading and concurrency questions from Java developer interviews on investment banks, e.g. Barclays, Morgan Stanley, Citibank, etc.

总之不要考虑那么多，下面是各种投行，比如巴克莱银行（Barclays）、花旗银行（Citibank）、摩根史坦利投资公司（Morgan Stanley）等等，面试 Java 开发者时常问的 Java 多线程和并发问题。

1) You have thread T1, T2, and T3. How will you ensure that thread T2 is run after T1 and thread T3 after T2?

1) 现在有线程 T1、T2 和 T3。你如何确保 T2 线程在 T1 之后执行，并且 T3 线程在 T2 之后执行？

This thread interview question is mostly asked in the first round or phone screening round of an interview and purpose of this multi-threading question is to check whether the candidate is familiar with the concept of "join" method or not. The answer to this multi-threading question is simple — it can be achieved by using the join method of Thread class.

这个线程面试题通常在第一轮面试或电话面试时被问到，这道多线程问题为了测试面试者是否熟悉 `join` 方法的概念。答案也非常简单——可以用 Thread 类的 `join` 方法实现这一效果。

2) What is the advantage of the new Lock interface over a synchronized block in Java? You need to implement a high-performance cache, which allows multiple readers, but how will you implement the single writer to keep the integrity?

2) Java 中新的 Lock 接口相对于同步代码块（synchronized block）有什么优势？如果让你实现一个高性能缓存，支持并发读取和单一写入，你如何保证数据完整性。

The major advantage of lock interfaces on multithreaded and concurrent programming is that they provide two separate locks for reading and writing, which enables you to write high-performance data structures, like ConcurrentHashMap and conditional blocking.

多线程和并发编程中使用 lock 接口的最大优势是它为读和写提供两个单独的锁，可以让你构建高性能数据结构，比如 `ConcurrentHashMap` 和条件阻塞。

This Java thread interview question is getting increasingly popular and more and more follow-up questions come based on the answer of the interviewee.

这道 Java 线程面试题越来越多见，而且随后的面试题都基于面试者对这道题的回答。

I would strongly suggest reading locks before appearing for any Java multithreading interview, because, nowadays, it's heavily used to build a cache for an electronic trading system on a client and exchange connectivity space.

我强烈建议在任何 Java 多线程面试前都要多看看有关锁的知识，因为如今电子交易系统的客户端和数据交互中，锁被频繁使用来构建缓存。

3) What are differences between wait and sleep method in Java?

3) Java 中 `wait` 和 `sleep` 方法有什么区别？

Let's take a look at another frequently-asked thread interview question in Java. This question will mostly appear in a phone interview. The only major difference is to wait to release the lock or monitor, while sleep doesn't release any lock or monitor while waiting. The wait is used for inter-thread communication, since sleep is used to introduce pause on execution. See my post wait vs sleep in Java for further information.

我们来看看另一个经常被问到的线程面试题。这道题常出现在电话面试中。两者主要的区别就是等待释放锁和监视器。`sleep` 方法在等待时不会释放任何锁或监视器。`wait` 方法多用于线程间通信，而 `sleep` 只是在执行时暂停。可以看我另一篇有关「[Java 中 wait 和 sleep](http://javarevisited.blogspot.sg/2011/12/difference-between-wait-sleep-yield.html)」的文章

![](https://2.bp.blogspot.com/-g1t_A_n7aSk/WpvPDbXs2bI/AAAAAAAAK8E/XOq6f_6bW9U25XM_ViX_ybOQ85y5tHhiACLcBGAs/s400/Sleep%2Bvs%2Bwait%2Bvs%2Byield%2Bmethod%2Bjava.gif)

4) Write code to implement blocking queue in Java?

4) 如何在 Java 中实现一个阻塞队列？

This is a relatively tough Java multithreading interview question that serves many purposes. It checks whether a candidate can actually write Java code using thread or not. It sees how good a candidate is on understanding concurrent scenarios, and you can ask a lot of follow-up question based upon his code. If he uses the wait() and notify() method to implement a blocking queue, once the candidate successfully writes it, you can ask him to write it again using new Java 5 concurrent classes, etc.

这是一道相对困难的 Java 多线程面试题，考察点很多。它考察了面试者是否真正写过 Java 多线程代码，考察了面试者对并发场景的理解。并且可以根据面试者的代码问很多后续问题，如果他用 `wait()` 和 `notify()` 方法成功实现了阻塞队列，可以让他用 Java 5 的并发类重新实现一次。

5) Write code to solve the produce consumer problem in Java? (solution)

5) 如何在 Java 中编写代码解决生产者消费者问题？「[答案](http://www.java67.com/2015/12/producer-consumer-solution-using-blocking-queue-java.html)」

Similar to the above questions on the thread, this question is more classic in nature, but sometimes an interviewer will ask follow up questions, like "How do you solve the producer consumer problem in Java?" Well, it can be solved in multiple ways. I have shared one way to solve the producer-consumer problem using BlockingQueue in Java, so be prepared for a few surprises. Sometimes, they even ask you to implement a solution of dining the philosopher problem, as well.

和上面有关线程的问题相似，这个问题在工作中很典型，但有时面试官会问这类问题，比如“在 Java 中如何解决生产者消费者问题？”其实，有很多解决方式。我分享过用 Java 中 BlockingQueue 的解决方案。有时他们甚至会让你给出哲学家进餐问题的解决方案。

6) Write a program that will result in a deadlock. How will you fix deadlock in Java?

6) 写一段死锁代码。你在 Java 中如何解决死锁？

This is my favorite Java thread interview question, because, even though deadlock is quite common while writing a multithreaded concurrent program, many candidates are not able to write deadlock-free code, and they simply struggle.

这是我最喜欢的 Java 多线程面试题，因为即使死锁在多线程并发编程中十分常见，许多面试者仍然抓耳挠腮，不能写出无死锁的代码。

Just ask them if you have N resources and N threads to complete an operation; then, you require all resources.

只需要问他们如果有 N 个资源和 N 个线程去执行某个操作，然后请求所有资源。

Here N can be replaced with two for the simplest case and higher numbers to make the question more intimidating. See How to avoid deadlock in Java for more information on the deadlock.

这里的 N 可以是 2 作为最简单的情况，也可以是个很大的数字让问题变复杂。有关死锁的更多信息可以看这篇文章「[Java 中如何避免死锁](http://javarevisited.blogspot.com/2010/10/what-is-deadlock-in-java-how-to-fix-it.html)」

![](https://1.bp.blogspot.com/-HCcRwM1YX58/WpvPZJQ0vBI/AAAAAAAAK8I/2L7IldmbVcc5DkZm6uuLTNDoir8Hky6YACLcBGAs/s400/how%2Bto%2Bavoid%2Bdeadlock%2Bin%2BJava.png)

7) What is an atomic operation? What are atomic operations in Java?

7) 什么是原子操作？Java 中有哪些原子操作？

This is a simple Java thread interview question. Another follow-up question would be: do you need to synchronize an atomic operation? You can read more about Java synchronization here.

这是个简单的 Java 线程面试题。另一个紧随其后的问题将是：你需要同步原子操作吗？你可以看这篇文章了解更多「[Java 同步](http://javarevisited.blogspot.com/2011/04/synchronization-in-java-synchronized.html)」

8) What is a volatile keyword in Java? How do you use it? How is it different from the synchronized method in Java?

8) Java 中 `volatile` 关键字是什么？你如何使用它？它和 Java 中的同步方法有什么区别？

Thread questions based on a volatile keyword in Java has become more popular after changes made on it for Java 5 and the Java memory model. It's good to prepare for how volatile variables ensures visibility, ordering, and consistency in a concurrent environment.

自从 Java 5 中调整 `volatile` 关键字和 Java 内存模型后，有关 `volatile` 关键字的线程问题越来越常见。掌握 `volatile` 变量在并发环境中如何确保可见性、有序性和一致性非常重要。

9) What is a race condition? How will you find and solve race condition?

9) 什么是竞态条件？你如何发现并解决竞态条件？

Another multithreading question in Java appears mostly on senior-level interviews. Most interviewers ask about a recent race condition that you have faced, how to solve it, and sometimes they will write sample code and ask you to detect the race condition. See my post on the race condition in Java for more information. In my opinion, this is one of the best Java thread interview questions and can really test the candidate's experience on solving race conditions or writing code that is free of data race or any other race condition. The best book about topic is "Concurrency practices in Java.'"

这个 Java 多线程问题一般出现在高级面试。多数面试官会问你最近一次遇到的竞态条件，如何解决的，有时他们也会写点简单代码让你发现竞态条件。可以看看我的这篇文章「[Java 中的竞态条件](http://javarevisited.blogspot.sg/2012/02/what-is-race-condition-in.html)」。我认为，这是最棒的 Java 线程面试问题之一，而且可以测试出面试者解决竞态条件的经验，或是编写无数据竞争、无其竞态条件的代码经验。

10) How will you take thread dump in Java? How will you analyze Thread dump?

10) 在 Java 中你如何转储线程（thread dump）？如何分析它？

In UNIX, you can use kill -3 and then the thread dump will print the log on windows that you can use "CTRL+Break." While this is a rather simple thread interview question, it can get tricky if they ask you how to analyze it. A thread dump can be useful to analyze deadlock situations, as well.

在 UNIX 中，你可以使用 `kill -3` 然后线程转储日志会打印在屏幕上，可以使用 `CTRL+Break` 查看。这只是一个较简单的线程面试题，狡猾一点的话他们会问你如何分析转储日志。线程转储日志对于分析死锁情况非常有用。

11) Why do we call start() method which in turns calls run() method, why not we directly call run() method?

11) 既然 `start()` 方法会调用 `run()` 方法，为什么我们调用 `start()` 方法，而不直接调用 `run()` 方法？

This is another classic Java multithreading interview question. Originally, I had some doubt when I started programming in the thread. Nowadays, I am mostly asked in phone interviews or the first round of interview questions at mid and junior-level Java interviews.

这是一个基本的 Java 多线程面试题。最初，我刚开始多线程编程时对此还有些困惑。如今我一般在 Java 中级面试的电话面试或一轮面试中遇到。

Here is the answer to this question. When you call the start() method, it creates a new thread and executes code declared in the run()  while directly calling the run() method. This doesn't create any new threads and executes code on the same calling thread. Read my post Difference Between Start and Run Method in Thread for more details.

这道问题的答案是这样的。当你调用 `start()` 方法时，它会新建一个线程然后执行 `run()` 方法中的代码。如果直接调用 `run()` 方法，并不会创建新线程，方法中的代码会在当前调用者的线程中执行。可以看这篇文章了解更多「[线程中 Start 和 Run 方法的区别](http://javarevisited.blogspot.sg/2012/03/difference-between-start-and-run-method.html)」

![](https://4.bp.blogspot.com/-lEawyydE9Og/WpvQ1uPbYlI/AAAAAAAAK8k/zsl3LNJTvVItGXOBEHQYCXTocRzhQfJ0QCLcBGAs/s400/Difference%2Bbetween%2BStart%2Band%2BRun%2Bmethod%2Bin%2BJava.png)

12) How will you awake a blocked thread in Java?

12) Java 中你如何唤醒阻塞线程？

This is a tricky question on threading. Blocking can result in many ways — if the thread is blocked on IO, then, I don't think there is a way to interrupt the thread. Let me know if there is any. On the other hand, if a thread is blocked due to the result of calling the  wait() ,  sleep() , or join()   method, you can interrupt the thread, and it will awake by throwing  InterruptedException. See my post called How to Deal With Blocking Methods in Java for more information on handling blocked thread.

这是有关线程的一个很狡猾的问题。有很多原因会导致阻塞，如果是 IO 阻塞，我认为没有方式可以中断线程（如果有的话请告诉我）。另一方面，如果线程阻塞是由于调用了 `wait()`，`sleep()` 或 `join()` 方法，你可以中断线程，通过抛出 `InterruptedException` 异常来唤醒该线程。可以看这篇文章了解有关处理阻塞线程的知识「[Java 中如何处理阻塞方法](http://javarevisited.blogspot.sg/2012/02/what-is-blocking-methods-in-java-and.html)」

13) What is the difference between CyclicBarriar and CountdownLatch in Java? ( answer)

13) Java 中 `CyclicBarriar` 和 `CountdownLatch` 有什么区别？

New Java thread interview questions mostly check your familiarity with JDK 5 concurrent packages. One difference is that you can reuse the CyclicBarrier once the barrier is broken, but you can not reuse  CountDownLatch. If you want to learn more, check out the Multithreading and Parallel Computing in Java course on Udemy.

最近的 Java 线程面试题多数在测试你对 JDK 5 并发包的掌握程度。两者区别之一就是 `CyclicBarrier` 在屏障打开之后（所有线程到达屏障点），可以重复使用。而 `CountDownLatch` 不行。想了解更多可以参与课程「[Java 中的多线程和并行计算](https://click.linksynergy.com/fs-bin/click?id=JVFxdTr9V80&subid=0&offerid=323058.1&type=10&tmpid=14538&RD_PARM1=https%3A%2F%2Fwww.udemy.com%2Fmultithreading-and-parallel-computing-in-java%2F)」

14) What is an immutable object? How does it help in writing a concurrent application?

14) 什么是不可变类？它对于编写并发应用有何帮助？

While this interview question does not directly relate to the thread, it indirectly helps a lot. This interview question can become more tricky if they ask you to write an immutable class or ask you Why String is Immutable in Java as a follow-up.

尽管这道面试题和线程没有直接关系，但间接影响也很大。如果面试官随后让你写一个不可变类，或问你「[为什么 Java 中的 String 是不可变的](http://javarevisited.blogspot.com/2010/10/why-string-is-immutable-in-java.html)」，会让面试题变得更加复杂。

15) What are some common problems you have faced in multi-threading environment? How did you resolve it?

15) 你在多线程环境中遇到的最多的问题是什么？你如何解决的？

Memory-interference, race conditions, deadlock, livelock, and starvation are an example of some problems that come with multithreading and concurrent programming. There is no end of a problem; if you get it wrong, they will be hard to detect and debug.

内存干扰、竞态条件、死锁、活锁、线程饥饿是多线程和并发编程中比较有代表性的问题。这类问题无休无止，而且难于定位和调试。

This is mostly an experience-based interview question about Java. You can see Java Concurrency in Practice Course by Heinz Kabutz for some real-world problems faced in actual high-performance multithreaded applications.

这是基于经验给出的 Java 面试题。你可以看看「[Java 并发实战课程](https://learning.javaspecialists.eu/courses/concurrency-in-practice-bundle?affcode=92815_johrd7r8) 」来了解现实生活中高性能多线程应用所面临的问题。

These were some of my favorite Java thread interview questions and commonly-asked questions by investment banks. This list is by no means complete, so please comment below some of the interesting Java thread questions that you have faced during an interview. This article collects and shares great interview questions on the multithreading concept, which not only helps in the interview but opens the door for learning a new threading concept.

上面所说的是我喜欢的，也是投行最常问的 Java 线程面试题。这个清单并不完整，所以可以在下方评论出你在面试中遇到的有意思的 Java 线程题目。这篇文章收集并分享与多线程概念有关的面试题，不仅仅有助于面试，还为大家打开多线程概念的大门。

One of the Java-revisited readers, Hemant, has contributed some more thread interview questions in Java. Here are those additional questions:
1) Difference between green thread and native thread in Java?
2) Difference between thread and process? (answer)
3) What is context switching in multi-threading?
4) Difference between deadlock and livelock, deadlock and starvation?
5) What thread-scheduling algorithm is used in Java?
6) What is thread-scheduler in Java?
7) How do you handle an unhandled exception in the thread?
8) What is thread-group, why its advised not to use thread-group in Java?
9) Why is the Executor framework better than creating and managing threads via the application?
10) Difference between Executor and Executors in Java? (answer)
11) How to find which thread is taking maximum CPU in windows and Linux server?

有位读者提供了一些 Java 线程面试题。补充在下面：
1) Java 中绿色线程和本地线程的区别？
2) 线程和进程的区别？「[答案](http://javarevisited.blogspot.sg/2015/12/difference-between-thread-and-process.html)」
3) 多线程的上下文切换是什么？
4) 死锁和活锁的区别？死锁和饥饿的区别？
5) Java 中使用什么线程调度算法？
6) Java 中线程调度是什么？
7) 线程中如何处理某个未处理异常？
8) 什么是线程组？为什么 Java 中不建议使用线程组？
9) 为什么使用 `Executor` 框架比直接创建线程要好？
10) Java 中 `Executor` 和 `Executors` 的区别？「[答案](http://javarevisited.blogspot.sg/2017/02/difference-between-executor-executorservice-and-executors-in-java.html)」
11) 在 windows 和 linux 系统上分别如何找到占用 CPU 最多的线程？
