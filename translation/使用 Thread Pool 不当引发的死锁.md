---
translator: http://www.jobbole.com/members/snowhere/
reviewer: http://www.jobbole.com/members/hanxiaomax/
via: https://dzone.com/articles/thread-pool-self-induced-deadlocks
---
# Thread Pool Self-Induced Deadlocks
# 使用 Thread Pool 不当引发的死锁

## Introduction
## 简介

* Deadlocks are caused by many threads locking the same resources
* Deadlocks can also occur if thread pool is used inside a task running in that pool
* Modern libraries like RxJava/Reactor are also susceptible

* 多线程锁定同一资源会造成死锁
* 线程池中的任务使用当前线程池也可能出现死锁
* RxJava 或 Reactor 等现代流行库也可能出现死锁

A deadlock is a situation where two or more threads are waiting for resources acquired by each other. For example thread A waits for lock1  locked by thread B, whereas thread B waits for  lock2, locked by thread A. In worst case scenario, the application freezes for an indefinite amount of time. Let me show you a concrete example. Imagine there is a Lumberjack class that holds references to two accessory locks:

死锁是两个或多个线程互相等待对方所拥有的资源的情形。举个例子，线程 A 等待 lock1，lock1 当前由线程 B 锁住，然而线程 B 也在等待由线程 A 锁住的 lock2。最坏情况下，应用程序将无限期冻结。让我给你看个具体例子。假设这里有个 `Lumberjack`（伐木工） 类，包含了两个装备的锁：

```
import com.google.common.collect.ImmutableList;
import lombok.RequiredArgsConstructor;
import java.util.concurrent.locks.Lock;
@RequiredArgsConstructor
class Lumberjack {
    private final String name;
    private final Lock accessoryOne;
    private final Lock accessoryTwo;
    void cut(Runnable work) {
        try {
            accessoryOne.lock();
            try {
                accessoryTwo.lock();
                work.run();
            } finally {
                accessoryTwo.unlock();
            }
        } finally {
            accessoryOne.unlock();
        }
    }
}
```

Every Lumberjack needs two accessories: a helmet and a chainsaw. Before he approaches any work, he must hold the exclusive lock to both of these. We create lumberjacks as follows:

每个 `Lumberjack`（伐木工）需要两件装备：`helmet`（安全帽） 和 `chainsaw`（电锯）。在他开始工作前，他必须拥有全部两件装备。我们通过如下方式创建伐木工们：

```
import lombok.RequiredArgsConstructor;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
@RequiredArgsConstructor
class Logging {
    private final Names names;
    private final Lock helmet = new ReentrantLock();
    private final Lock chainsaw = new ReentrantLock();
    Lumberjack careful() {
        return new Lumberjack(names.getRandomName(), helmet, chainsaw);
    }
    Lumberjack yolo() {
        return new Lumberjack(names.getRandomName(), chainsaw, helmet);
    }
}
```

As you can see, there are two kinds of lumberjacks: those who first take a helmet and then a chainsaw and vice versa. Careful lumberjacks try to obtain a helmet first and then wait for a chainsaw. A YOLO-type of lumberjack first takes a chainsaw and then looks for a helmet. Let’s generate some Lumberjacks and run them concurrently:

可以看到，有两种伐木工：先戴好安全帽然后再拿电锯的，另一种则相反。谨慎派（`careful()`）伐木工先戴好安全帽，然后去拿电锯。狂野派伐木工（`yolo()`）先拿电锯，然后找安全帽。让我们并发生成一些伐木工：

```
private List<Lumberjack> generate(int count, Supplier<Lumberjack> factory) {
    return IntStream
            .range(0, count)
            .mapToObj(x -> factory.get())
            .collect(toList());
}
```

generate() is a simple method that creates a collection of lumberjacks of a  given type. Then, we generate a bunch of careful and YOLO:

`generate()`方法可以创建指定类型伐木工的集合。我们来生成一些谨慎派伐木工和狂野派伐木工。

```
private final Logging logging;
//...
List<Lumberjack> lumberjacks = new CopyOnWriteArrayList<>();
lumberjacks.addAll(generate(carefulLumberjacks, logging::careful));
lumberjacks.addAll(generate(yoloLumberjacks, logging::yolo));
```

Finally, let’s put these Lumberjacks to work:

最后，我们让这些伐木工开始工作：

```
IntStream
        .range(0, howManyTrees)
        .forEach(x -> {
            Lumberjack roundRobinJack = lumberjacks.get(x % lumberjacks.size());
            pool.submit(() -> {
                log.debug("{} cuts down tree, {} left", roundRobinJack, latch.getCount());
                roundRobinJack.cut(/* ... */);
            });
        });
```

This loop takes Lumberjacks — one after another — in a round-robin fashion and asks them to cut a tree. Essentially, we are submitting the howManyTrees number of tasks to a thread pool ( ExecutorService). In order to figure out when the job was done, we use a  CountDownLatch:

这个循环让所有伐木工一个接一个（轮询方式）去砍树。实质上，我们向线程池（`ExecutorService`）提交了和树木数量（`howManyTrees`）相同个数的任务，并使用 `CountDownLatch` 来记录工作是否完成。

```
CountDownLatch latch = new CountDownLatch(howManyTrees);
IntStream
        .range(0, howManyTrees)
        .forEach(x -> {
            pool.submit(() -> {
                //...
                roundRobinJack.cut(latch::countDown);
            });
        });
if (!latch.await(10, TimeUnit.SECONDS)) {
    throw new TimeoutException("Cutting forest for too long");
}
```

The idea is simple. We will let a bunch of Lumberjacks compete over a helmet and a chainsaw across multiple threads. The complete source code is as follows:

其实想法很简单。我们让多个伐木工（`Lumberjacks`）通过多线程方式去竞争一个安全帽和一把电锯。完整代码如下：

```
import lombok.RequiredArgsConstructor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.TimeoutException;
import java.util.function.Supplier;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
@RequiredArgsConstructor
class Forest implements AutoCloseable {
    private static final Logger log = LoggerFactory.getLogger(Forest.class);
    private final ExecutorService pool;
    private final Logging logging;
    void cutTrees(int howManyTrees, int carefulLumberjacks, int yoloLumberjacks) throws InterruptedException, TimeoutException {
        CountDownLatch latch = new CountDownLatch(howManyTrees);
        List<Lumberjack> lumberjacks = new ArrayList<>();
        lumberjacks.addAll(generate(carefulLumberjacks, logging::careful));
        lumberjacks.addAll(generate(yoloLumberjacks, logging::yolo));
        IntStream
                .range(0, howManyTrees)
                .forEach(x -> {
                    Lumberjack roundRobinJack = lumberjacks.get(x % lumberjacks.size());
                    pool.submit(() -> {
                        log.debug("{} cuts down tree, {} left", roundRobinJack, latch.getCount());
                        roundRobinJack.cut(latch::countDown);
                    });
                });
        if (!latch.await(10, TimeUnit.SECONDS)) {
            throw new TimeoutException("Cutting forest for too long");
        }
        log.debug("Cut all trees");
    }
    private List<Lumberjack> generate(int count, Supplier<Lumberjack> factory) {
        return IntStream
                .range(0, count)
                .mapToObj(x -> factory.get())
                .collect(Collectors.toList());
    }
    @Override
    public void close() {
        pool.shutdownNow();
    }
}

```

Now, let's take a look at the interesting part. If you only create careful  Lumberjacks , the application completes almost immediately, for example:

现在，让我们来看有趣的部分。如果我们只创建谨慎派伐木工（`careful Lumberjacks`），应用程序几乎瞬间运行完成，举个例子：

```
ExecutorService pool = Executors.newFixedThreadPool(10);
Logging logging = new Logging(new Names());
try (Forest forest = new Forest(pool, logging)) {
    forest.cutTrees(10000, 10, 0);
} catch (TimeoutException e) {
    log.warn("Working for too long", e);
}
```

However, if you play a bit with the number of Lumberjacks, e.g. 10 careful  and one yolo, the system quite often fails. What happened? Everyone in the careful  team tries to pick up a helmet first. If one of the Lumberjacks picked up a helmet, everyone else just waits. Then, the lucky guy picks up a chainsaw, which must be available. Why? Everyone else is waiting for the helmet before they pick up a chainsaw. So far, so good. But, what if there is one yolo   Lumberjack in the team? While everyone competes for a helmet, he sneakily grabs a chainsaw. But, there’s a problem. One of the careful  Lumberjacks gets his safety helmet. However, he can’t pick up a chainsaw, because it’s already taken by someone else. To make matters worse, the current owner of the chainsaw (the yolo guy) will not release his chainsaw until he gets a helmet. There are no timeouts here. The careful guy waits infinitely with his helmet, unable to get a chainsaw. The yolo guy sits idle forever, because he can not obtain a helmet — a deadlock.

但是，如果你对伐木工（`Lumberjacks`）的数量做些修改，比如，10 个谨慎派（`careful`）伐木工和 1 个狂野派（`yolo`）伐木工，系统就会经常运行失败。怎么回事？谨慎派（`careful`）团队里每个人都首先尝试获取安全帽。如果其中一个伐木工取到了安全帽，其他人会等待。然后那个幸运儿肯定能拿到电锯。原因就是其他人在等待安全帽，还没到获取电锯的阶段。目前为止很完美。但是如果团队里有一个狂野派（`yolo`）伐木工呢？当所有人竞争安全帽时，他偷偷把电锯拿走了。这就出现问题了。某个谨慎派（`careful`）伐木工牢牢握着安全帽，但他拿不到电锯，因为被其他某人拿走了。更糟糕的是电锯所有者（那个狂野派伐木工）在拿到安全帽之前不会放弃电锯。这里并没有一个超时设定。那个谨慎派（`careful`）伐木工拿着安全帽无限等待电锯，那个狂野派（`yolo`）伐木工因为拿不到安全帽也将永远发呆，这就是死锁。

Now, what would happen if all the Lumberjacks were yolo, i.e., they all tried to pick the chainsaw first? It turns out that the easiest way to avoid deadlocks is to obtain and release locks always in the same order. For example, you can sort your resources based on some arbitrary criteria. If one thread obtains lock A followed by B, whereas the second thread obtains B first, it’s a recipe for a deadlock.

如果所有伐木工都是狂野派（`yolo`）会怎样，也就是说，所有人都首先去尝试拿电锯会怎样？事实证明避免死锁最简单的方式就是以相同的顺序获取和释放各个锁，也就是说，你可以对你的资源按照某个标准来排序。如果一个线程先获取 A 锁，然后是 B 锁，但第二个线程先获取 B 锁，会引发死锁。

## Thread Pool Self-Induced Deadlocks
## 线程池自己引发的死锁

This was an example of a deadlock, rather than a simple one. But, it turns out that a single thread pool can cause a deadlock when used incorrectly. Imagine you have an ExecutorService, just like in the previous example, that you use, as shown below:

这里有个与上面不同的死锁例子，它证明了单个线程池使用不当时也会引发死锁。假设你有一个 `ExecutorService`，和之前一样，按照下面的方式运行。

```
ExecutorService pool = Executors.newFixedThreadPool(10);
pool.submit(() -> {
    try {
        log.info("First");
        pool.submit(() -> log.info("Second")).get();
        log.info("Third");
    } catch (InterruptedException | ExecutionException e) {
        log.error("Error", e);
    }
});
```

This looks fine — all messages appear on the screen as expected:

看起来没什么问题 —— 所有信息按照预期的样子呈现在屏幕上：

```
INFO [pool-1-thread-1]: First
INFO [pool-1-thread-2]: Second
INFO [pool-1-thread-1]: Third
```

Notice that we block, see  get(), waiting for the inner Runnable to complete before we display "Third." It’s a trap! Waiting for the inner task to complete means it must acquire a thread from a thread pool in order to proceed. However, we already acquired one thread, therefore, the inner will be blocked until it can get the second. Our thread pool is large enough at the moment, so it works fine. Let’s change our code a little bit, shrinking the thread pool to just one thread. Also, we’ll remove  get(), which is crucial:

注意我们用 `get()` 阻塞线程，在显示“`Third`”之前必须等待内部线程（`Runnable`）运行完成。这是个大坑！等待内部任务完成意味着需要从线程池额外获取一个线程来执行任务。然而，我们已经使用到了一个线程，所以内部任务在获取到第二个线程前将一直阻塞。当前我们的线程池足够大，运行没问题。让我们稍微改变一下代码，将线程池缩减到只有一个线程，另外关键的一点是我们移除 `get()` 方法：

```
ExecutorService pool = Executors.newSingleThreadExecutor();
pool.submit(() -> {
    log.info("First");
    pool.submit(() -> log.info("Second"));
    log.info("Third");
});
```

This code works fine, but with a twist:

代码正常运行，只是有些乱：

```
INFO [pool-1-thread-1]: First
INFO [pool-1-thread-1]: Third
INFO [pool-1-thread-1]: Second
```

Two things to notice:

两点需要注意：

* Everything runs in a single thread (unsurprisingly)
* The "Third" message appears before "Second"

* 所有代码运行在单个线程上（毫无疑问）
* “`Third`”信息显示在“`Second`”之前

The change of order is entirely predictable and does not come from some race condition between threads (in fact, we have just one). Watch closely what happens: we submit a new task to a thread pool (the one printing "Second"). However, this time we don’t wait for the completion of that task. Great, because the very single thread in a thread pool is already occupied by the task printing "First"  and "Third". Therefore, the outer task continues, printing  "Second."  When this task finishes, it releases the single thread back to a thread pool. The inner task can finally begin execution, printing "Second."   Now, where’s the deadlock? Try adding blocking get()to inner task:

顺序的改变完全在预料之内，没有涉及线程间的竞态条件（事实上我们只有一个线程）。仔细分析一下发生了什么：我们向线程池提交了一个新任务（打印“`Second`”的任务），但这次我们不需要等待这个任务完成。因为线程池中唯一的线程被打印“`First`”和“`Third`”的任务占用，所以这个外层任务继续执行，并打印“`Third`”。当这个任务完成时，将单个线程释放回线程池，内部任务最终开始执行，并打印“`Second`”。那么死锁在哪里？来试试在内部任务里加上 `get()` 方法：

```
ExecutorService pool = Executors.newSingleThreadExecutor();
pool.submit(() -> {
    try {
        log.info("First");
        pool.submit(() -> log.info("Second")).get();
        log.info("Third");
    } catch (InterruptedException | ExecutionException e) {
        log.error("Error", e);
    }
});
```

Deadlock! Step-by-step:

死锁出现了！我们来一步一步分析：

* Task printing "First" is submitted to an idle single-threaded pool
* This task begins execution and prints "First"
* We submit an inner task printing "Second" to a thread pool
* The inner task lands in a pending task queue. No threads are available since the only one is currently being occupied
* We block waiting for the result of the inner task. Unfortunately, while waiting for the inner task, we hold the only available thread
* get() will wait forever, unable to acquire thread
* deadlock

* 打印“First”的任务被提交到只有一个线程的线程池
* 任务开始执行并打印“First”
* 我们向线程池提交了一个内部任务，来打印“Second”
* 内部任务进入等待任务队列。没有可用线程因为唯一的线程正在被占用
* 我们阻塞住并等待内部任务执行结果。不幸的是，我们等待内部任务的同时也在占用着唯一的可用线程
* `get()` 方法无限等待，无法获取线程
* 死锁

Does it mean having a single-thread pool is bad? Not really. The same problem could occur with a thread pool of any size. But, in that case, a deadlock may occur only under high load, which is much worse from a maintenance perspective. You could technically have an unbounded thread pool, but that’s even worse.

这是否意味单线程的线程池是不好的？并不是，相同的问题会在任意大小的线程池中出现，只不过是在高负载情况下才会出现，这维护起来更加困难。你在技术层面上可以使用一个无界线程池，但这样太糟糕了。

## Reactor/RxJava
## Reactor/RxJava

Notice that this problem can occur with higher-level libraries, like Reactor:

请注意，这类问题也会出现在上层库，比如 `Reactor`：

```
 Scheduler pool = Schedulers.fromExecutor(Executors.newFixedThreadPool(10));
Mono
    .fromRunnable(() -> {
        log.info("First");
        Mono
                .fromRunnable(() -> log.info("Second"))
                .subscribeOn(pool)
                .block();  //VERY, VERY BAD!
        log.info("Third");
    })
    .subscribeOn(pool);
```

Once you subscribe, this seems to work, but it is terribly non-idiomatic. The basic problem is the same. Outer Runnable  acquires one thread from a  pool ,  subscribeOn() in the last line, and at the same time, inner Runnable  tries to obtain a thread as well. You need to replace the underlying thread pool with a single-thread pool, and this produces a deadlock. At least with RxJava/Reactor, the cure is simple — just compose asynchronous operations rather than blocking inside each other:

当你部署代码，它似乎可以正常工作，但很不符合编程习惯。根源的问题是相通的，最后一行的 `subscribeOn()` 表示外层任务（`Runnable`）请求了线程池(`pool`)中一个线程，同时，内部任务（`Runnable`）也试图获取一个线程。如果把基础的线程池换成只包含单个线程的线程池，会发生死锁。对于 RxJava/Reactor 来说，解决方案很简单——用异步操作替代阻塞操作。

```
Mono
    .fromRunnable(() -> {
        log.info("First");
        log.info("Third");
    })
    .then(Mono
            .fromRunnable(() -> log.info("Second"))
            .subscribeOn(pool))
    .subscribeOn(pool)
```

## Prevention
## 防患于未然

There is no 100 percent sure way of preventing deadlocks. One technique is to avoid situations that may lead to deadlocks, like sharing resources or locking exclusively. If that’s not possible (or deadlocks are not obvious, like with thread pools), consider proper code hygiene. Monitor thread pools and avoid blocking indefinitely. I can hardly imagine a situation when you are willing to wait an indefinite amount of time for a completion. And, that’s how get() or block() without timeout are working.

并没有彻底避免死锁的方法。试图解决问题的技术手段往往会带来死锁风险，比如共享资源和排它锁。如果无法根治死锁（或死锁并不明显，比如使用线程池），还是试着保证代码质量、监控线程池和避免无限阻塞。我很难想象你情愿无限等待程序运行完成，如同 `get()` 方法和 `block()` 方法在没有设定超时时间的情况下执行。

Thanks for reading!

感谢阅读！
