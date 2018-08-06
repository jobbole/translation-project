---
editor: yizheWork
published: true
title: Iteration Over Java Collections With High Performance
---
# Iteration Over Java Collections With High Performance
# 高效遍历 Java 容器

###### Learn more about the forEach loop in Java and how it compares to C style and Stream API in this article on dealing with collections in Java.

###### 通过本文，你可以更深入的学习 Java 语言中 forEach 语法的知识，以及它和 C 语言形式的 for 循环、 Steam API 的对比。

#### Introduction
Java developers usually deal with collections such as ArrayList and HashSet. Java 8 came with lambda and the streaming API that helps us to easily work with collections. In most cases, we work with a few thousands of items and performance isn't a concern. But, in some extreme situations, when we have to travel over a few millions of items several times, performance will become a pain.

#### 简介
Java 程序员经常使用容器，比如 ArrayList 和 HashSet。Java 8 中的 lambda 语法和 steaming API 可以让我们更方便的使用容器。大部分情况下，我们仅仅处理几千个元素，也不会去考虑性能问题。但是，在一些极端场景下，如果我们需要遍历上百万个元素，性能问题就凸显出来了。

I use JMH for checking the running time of each code snippet.

本文将采用 [JMH](http://openjdk.java.net/projects/code-tools/jmh/) 计算每块代码的运行时间。

#### forEach vs. C Style vs. Stream API
Iteration is a basic feature. All programming languages have simple syntax to allow programmers to run through collections. Stream API can iterate over Collections in a very straightforward manner.

遍历是一个基本的功能。所有编程语言都提供了简单的语法，让程序员去遍历容器。Steam API 以一种非常直接的形式来遍历容器。
```java
    public List<Integer> streamSingleThread(BenchMarkState state){
        List<Integer> result = new ArrayList<>(state.testData.size());
        state.testData.stream().forEach(item -> {
            result.add(item);
        });
        return result;
    }
    public List<Integer> streamMultiThread(BenchMarkState state){
        List<Integer> result = new ArrayList<>(state.testData.size());
        state.testData.stream().parallel().forEach(item -> {
            result.add(item);
        });
        return result;
    }
```

The forEach  loop is just as simple:

forEach 循环也很简单：
```java
    public List<Integer> forEach(BenchMarkState state){
      List<Integer> result = new ArrayList<>(state.testData.size());
      for(Integer item : state.testData){
        result.add(item);
      }
      return result;
    }
```

C style is more verbose, but still very compact:

C 语言形式的 for 循环啰嗦一些，不过依然很紧凑：
```java

    public List<Integer> forCStyle(BenchMarkState state){
      int size = state.testData.size();
      List<Integer> result = new ArrayList<>(size);
      for(int j = 0; j < size; j ++){
        result.add(state.testData.get(j));
      }
      return result;
    }
```

Then, the performance:

以下是性能报告：

    Benchmark                               Mode  Cnt   Score   Error  Units
    TestLoopPerformance.forCStyle           avgt  200  18.068 ± 0.074  ms/op
    TestLoopPerformance.forEach             avgt  200  30.566 ± 0.165  ms/op
    TestLoopPerformance.streamMultiThread   avgt  200  79.433 ± 0.747  ms/op
    TestLoopPerformance.streamSingleThread  avgt  200  37.779 ± 0.485  ms/op


With C style, JVM simply increases an integer, then reads the value directly from memory. This makes it very fast. But forEach is very different, according to this answer on StackOverFlow and document from Oracle, JVM has to convert forEach to an iterator and call hasNext() with every item. This is why forEach is slower than the C style.

使用 C 语言形式的 for 循环，JVM 每次仅仅增加一个数字，然后直接从内存里读出数据。这使得它非常迅速。但是 forEach 就大不一样，根据 [StackOverFlow 的这篇回答](https://stackoverflow.com/questions/85190/how-does-the-java-for-each-loop-work/85206#85206)，和 [Oracle 的文章](https://docs.oracle.com/javase/1.5.0/docs/guide/language/foreach.html)，JVM 需要把 forEach 转换成一个 iterator，然后每个元素都调用一次 hasNext() 方法。这就是 forEach 比 C 语言的形式慢一些的原因。

#### Which Is the High-Performance Way to Travelling Over Set?

#### 哪一个是遍历 Set 最高效的方法呢？

We define test data:

我们先定义测试数据集：
```java

    @State(Scope.Benchmark)
    public static class BenchMarkState {
        @Setup(Level.Trial)
        public void doSetup() {
            for(int i = 0; i < 500000; i++){
                testData.add(Integer.valueOf(i));
            }
        }
        @TearDown(Level.Trial)
        public void doTearDown() {
            testData = new HashSet<>(500000);
        }
        public Set<Integer> testData = new HashSet<>(500000);
    }
```

The Java Set also supports Stream API and forEach loop. According to the previous test, if we convert Set to ArrayList, then travel over ArrayList, maybe the performance improve?

Java 中的 Set 也支持 Steam API 和 forEach 循环。参考之前的测试，如果我们把 Set 转换成 ArrayList，然后遍历 ArrayList，或许性能会好一些？
```java

    public List<Integer> forCStyle(BenchMarkState state){
        int size = state.testData.size();
        List<Integer> result = new ArrayList<>(size);
        Integer[] temp = (Integer[]) state.testData.toArray(new Integer[size]);
        for(int j = 0; j < size; j ++){
            result.add(temp[j]);
        }
        return result;
    }
```

How about a combination of the iterator with the C style for loop?

如果把 iterator 和 C 语言形式结合起来呢？
```java

    public List<Integer> forCStyleWithIteration(BenchMarkState state){
        int size = state.testData.size();
        List<Integer> result = new ArrayList<>(size);
        Iterator<Integer> iteration = state.testData.iterator();
            for(int j = 0; j < size; j ++){
            	result.add(iteration.next());
            }
        return result;
    }

```
Or, what about simple travel?

或者，简单的遍历怎么样？
```java

    public List<Integer> forEach(BenchMarkState state){
        List<Integer> result = new ArrayList<>(state.testData.size());
        for(Integer item : state.testData) {
            result.add(item);
        }
        return result;
    }
```

This is a nice idea, but it doesn't work because initializing the new ArrayList also consumes resources.

这个主意不错，不过它的效率也不高，因为初始化一个新的 ArrayList 同样需要消耗资源。

    Benchmark                                   Mode  Cnt  Score   Error  Units
    TestLoopPerformance.forCStyle               avgt  200  6.013 ± 0.108  ms/op
    TestLoopPerformance.forCStyleWithIteration  avgt  200  4.281 ± 0.049  ms/op
    TestLoopPerformance.forEach                 avgt  200  4.498 ± 0.026  ms/op
    
HashMap (HashSet uses HashMap<E,Object>) isn't designed for iterating all items. The fastest way to iterate over
HashMap is a combination of Iterator and the C style for loop, because JVM doesn't have to call hasNext().

HashMap (使用 HashMap<E,Object> 的 HashSet) 不是为遍历所有元素设计的。遍历一个 HashMap 最快的方法是把 Iterator 和 C 语言形式结合起来，这样 JVM 就不会去调用 hasNext()。

#### Conclusion
#### 结论

Foreach and Stream API are convenient to work with Collections. You can write code faster. But, when your system is stable and performance is a major concern, you should think about rewriting your loop.

Foreach 和 Steam API 用来处理集合是很方便的。你可以更快的写代码。不过，如果你的系统很稳定，性能是一个主要的考量，你应该考虑一下重写你的循环。
