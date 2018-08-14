---
translator: http://www.jobbole.com/members/yizhe/
reviewer: http://www.jobbole.com/members/hanxiaomax/
via: https://dzone.com/articles/leveraging-lambda-expressions-for-lazy-evaluation
---


# Leveraging Lambda Expressions for Lazy Evaluation in Java

# 利用 Lambda 表达式实现 Java 中的惰性求值

In Java, the potential of lazy evaluation is quite neglected (actually, at the language level, it's pretty much limited to the implementation of minimal evaluation). Advanced languages, like Scala, for example, differentiate between call-by-value and call-by-name calls or introduce dedicated keywords like lazy.

 Java 中惰性求值的潜能，完全被忽视了（在语言层面上，它仅被用来实现[ 短路求值 ](https://en.wikipedia.org/wiki/Short-circuit_evaluation)）。更先进的语言，如 Scala，区分了传值调用与传名调用，或者引入了 lazy 这样的关键字。



Although Java 8 brought an improvement on that field by providing the implementation of the lazy sequence concept (we all know it as java.util.stream.Stream), today, we'll skip that and focus on how the introduction of lambda expressions brought us a new lightweight method of leveraging delayed evaluation.

尽管 Java 8 通过延迟队列的实现（java.util.stream.Stream）在惰性求值的方面有些改进，但是我们会先跳过 Stream，而把重点放在如何使用 lambda 表达式实现一个轻量级的惰性求值。

## Lambda-Backed Lazy Evaluation

## 基于 lambda 的惰性求值

### Scala

### Scala

Whenever we want to lazily evaluate method parameters in Scala, we can do it the "call-by-name" way.

当我们想对 Scala 中的方法参数进行惰性求值时，我们用“传名调用”来实现。

Let's create a simple foo  method that accepts a String  instance and returns it:

让我们创建一个简单的 foo 方法，它接受一个 String 示例，然后返回这个 String：

```scala
def foo(b: String): String = b
```

Everything is eager, just like in Java Now, if we wanted to make b computed lazily, we could leverage the call-by-name syntax and simply add two signs to the b 's type declaration, and voilà:

一切都是马上返回的，跟 Java 中的一样。如果我们想让 b 的计算延迟，可以使用传名调用的语法，只要在 b 的类型声明上加两个符号，来看：

```scala
def foo(b: => String): String = b
```

If we try to javap reverse-engineer the generated  *.class file , we'd see:

如果用 javap 反编译上面生成的 `*.class` 文件，可以看到:

```java
Compiled from "LazyFoo.scala"

public final class LazyFoo {

    public static java.lang.String foo(scala.Function0<java.lang.String>);

    Code:   

    0: getstatic #17 // Field LazyFoo.MODULE:LLazyFoo$;

    3: aload_0

    4: invokevirtual #19 // Method LazyFoo$.foo:(Lscala/Function0;)Ljava/lang/String;

    7: areturn

}
```



It turns out that the parameter passed to our method is no longer a _String_ , but a _Function0<String>_ instead, which makes it possible to evaluate the expression lazily — as long as we don't call it, the computation isn't triggered. It is as simple as that.

看起来传给这个函数的参数不再是一个 _String_ 了，而是变成了一个 _Function0<String>_，这使得对这个表达式进行延迟计算变得可能 —— 只要我们不去调用他，计算就不会被触发。Scala 中的惰性求值就是这么简单。 

### In Java

### 使用 Java

Now, whenever we need to lazily evaluate a computation returning T, **we can reuse the above idea and simply wrap the computation into a Java Function0 equivalent to the Supplier<T>  instance:**

现在，如果我们需要延迟触发一个返回 _T_ 的计算，**我们可以复用上面的思路，将计算包装为一个返回 _Supplier<T>_ 实例的 Java Function0 ：**

```java
Integer v1 = 42; // eager

Supplier<Integer> v2 = () -> 42; // lazy
```

That would prove to be much more practical if we needed to obtain a result of some long-lasting method instead:

如果需要花费较长时间才能从函数中获得结果，上面这个方法会更加实用：

```java
Integer v1 = compute(); //eager

Supplier<Integer> value = () -> compute(); // lazy
```

And, again, this time as a method param:

同样的，这次传入一个方法作为参数：

```java
private static int computeLazily(Supplier<Integer> value) {
    // ...
}
```



If you look closely at the APIs introduced in Java 8, you will notice that this pattern is used quite often. One of the most evident examples would be Optional#orElseGet, which is a lazy equivalent of Optional#orElse.

如果仔细观察 Java 8 中新增的 API，你会注意到这种模式使用得特别频繁。一个最显著的例子就是  [Optional#orElseGet ](https://docs.oracle.com/javase/8/docs/api/java/util/Optional.html#orElseGet-java.util.function.Supplier)，[Optional#orElse](https://docs.oracle.com/javase/8/docs/api/java/util/Optional.html#orElse-T-) 的惰性求值版本。

If not this pattern, it'd make the  Optional 's usefulness...  questionable. Naturally, we're not limited to suppliers only. We can reuse all functional interfaces in a similar manner.

如果不使用这种模式的话，那么 Optional 就没什么用处了... 或许吧。当然，我们不会满足于 suppliers 。我们可以用同样的方法复用所有 functional 接口。

### Thread-Safety and Memoization

### 线程安全和缓存

Unfortunately, that simple approach is flawed. The computation will be triggered for every function call. This applies not only to multithreaded environments but also when a Supplier is called consecutive times by the same thread. And, it's fine as long as we're aware of the fact and applying the technique reasonably.

不幸的是，上面这个简单的方法是有缺陷的：每次调用都会触发一次计算。不仅多线程的调用有这个缺陷，同一个线程连续调用多次也有这个缺陷。不过，如果我们清楚这个缺陷，并且合理的使用这个技术，那就没什么问题。

## Lazy Evaluation with Memoization

## 使用缓存的惰性求值

As mentioned already, the lambda-based approach can be perceived as flawed in certain contexts because of the fact that the value never gets memorized. In order to fix that, we'd need to construct a dedicated tool, let's say Lazy:

刚才已经提到，基于 lambda 表达式的方法在一些情况下是有缺陷的，因为返回值没有保存起来。为了修复这个缺陷，我们需要构造一个专用的工具，让我们叫它 Lazy ：

```java
public class Lazy<T> { ... }
```


That one would need to hold both a Supplier<T> and the value T itself:

这个工具需要自身同时保存 _Supplier<T>_ 和 返回值 _T_。

```java
@RequiredArgsConstructor
public class NaiveLazy<T> { 

    private final Supplier<T> supplier;

    private T value;

    public T get() {

        if (value == null) {

            value = supplier.get();

         }

        return value;

    }

}
```

It is as simple as that. Keep in mind that the above implementation serves as a PoC and is not thread-safe, yet.

就是这么简单。注意上面的代码仅仅是一个概念模型，暂时还不是线程安全的。

Luckily, making it thread-safe involves, pretty much, just making sure that multiple threads do not trigger the same computation when trying to obtain the value. This can be easily achieved by utilizing the double-checked locking pattern (we could've simply synchronized on the get()  method, but that would introduce unwanted contention):

幸运的是，如果想让它变得线程安全，只需要保证不同的线程在获取返回值的时候不会触发同样的计算。这可以简单的通过双重检查锁定机制来实现（我们不能直接在 get() 方法上加锁，这会引入不必要的竞争）：

```java
@RequiredArgsConstructor

public class Lazy<T> {

    private final Supplier<T> supplier;

    private volatile T value;

    public T get() {
        if (value == null) {
            synchronized (this) {
                if (value == null) {
                    value = supplier.get();
                }
            }
        }
       return value;
    }
}
```

And, now, we have a fully functional implementation of the lazy evaluation pattern in Java. Since it's not implemented at the language level, additional costs associated with creating a new object need to be paid.

现在，我们有了一个完整的 Java 惰性求值的函数化实现。由于它不是在语言的层面实现的，需要付出创建一个新对象的代价。

## Further Development

## 更深入的讨论

Of course, we don't need to stop here, and can further improve the tool itself. For example, by adding a lazy filter()/flatMap()/map() methods that would enable a more fluent interaction and composability:

当然，我们不会就此打住，我们可以进一步的优化这个工具。比如，通过引入一个惰性的 _filter()/flatMap()/map()_ 方法，可以让它使用起来更加流畅，并且组合性更强：

```java
public <R> Lazy<R> map(Function<T, R> mapper) {
    return new Lazy<>(() -> mapper.apply(this.get()));
}

public <R> Lazy<R> flatMap(Function<T, Lazy<R>> mapper) {
    return new Lazy<>(() -> mapper.apply(this.get()).get());
}

public Lazy<Optional<T>> filter(Predicate<T> predicate) {
    return new Lazy<>(() -> Optional.of(get()).filter(predicate));
}
```

Sky's the limit.

优化永无止境。

Let's also throw in a handy factory method:

我们也可以暴露一个方便的工厂方法：

```java
public static <T> Lazy<T> of(Supplier<T> supplier) {
    return new Lazy<>(supplier);
}
```

And in action:

实际使用上：

```java
Lazy.of(() -> compute(42))
  .map(s -> compute(13))
  .flatMap(s -> lazyCompute(15))
  .filter(v -> v > 0);
```

As you can see, as long as #get isn't called at the end of the chain, nothing gets computed.

你可以看到，只要作为调用链底层的 #get 方法没有被调用，那么什么计算也不会触发。

## Nulls

## Null 的处理

In some situations, null can be a valid value, but it won't work properly with our implementation - a valid null value gets treated just like an uninitialized value, which is not ideal.

某些情况下，null 会被当做有意义的值。不过它与我们的实现有冲突 —— 一个有意义的 null 值被当做一个未初始化的值，这不太合适。

The way to go around it would be simply to be explicit about the optional result by... returning it wrapped in an Optional instance.

解决方法也很简单，直接把这种可能的结果包装到一个 Optional 实例里返回。

Other than that, it'd be a good idea to explicitly forbid null values, for example, by doing:

除此之外，明确禁止 null 作为返回值也是一个好办法，比如：

```java
value = Objects.requireNonNull(supplier.get());
```

## GCing an Unused Supplier

## 回收不再使用的 Supplier

As some of you have probably already noticed, after the value gets evaluated, a supplier will never be used again, but it still occupies some resources.

有些读者可能已经注意到了，结果计算完毕之后，supplier 就不再使用了，但是它仍然占据一些资源。

The way to handle that would be to make the Supplier non-final and free it by setting it to a null after our value gets evaluated.

解决办法就是把 Supplier 标记为非 final 的，一旦结果计算完毕，就把它置为 null。

## A Complete Example

## 完整的例子

```java
public class Lazy<T> {
    private transient Supplier<T> supplier;
    private volatile T value;
    public Lazy(Supplier<T> supplier) {
        this.supplier = Objects.requireNonNull(supplier);
    }
    public T get() {
        if (value == null) {
            synchronized (this) {
                if (value == null) {
                    value = Objects.requireNonNull(supplier.get());
                    supplier = null;
                }
            }
        }
        return value;
    }
    public <R> Lazy<R> map(Function<T, R> mapper) {
        return new Lazy<>(() -> mapper.apply(this.get()));
    }
    public <R> Lazy<R> flatMap(Function<T, Lazy<R>> mapper) {
        return new Lazy<>(() -> mapper.apply(this.get()).get());
    }
    public Lazy<Optional<T>> filter(Predicate<T> predicate) {
        return new Lazy<>(() -> Optional.of(get()).filter(predicate));
    }
    public static <T> Lazy<T> of(Supplier<T> supplier) {
        return new Lazy<>(supplier);
    }
}
```

The above code can be also found on GitHub.

以上的代码也可以在 [ GitHub ](https://github.com/pivovarit/articles/tree/master/java-lazy-initialization) 上找到。
