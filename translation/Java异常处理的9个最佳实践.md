---
translator: http://www.jobbole.com/members/Marticles/
reviewer: http://www.jobbole.com/members/hanxiaomax/
via: https://dzone.com/articles/9-best-practices-to-handle-exceptions-in-java
---

# 9 Best Practices to Handle Exceptions in Java
# Java异常处理的9个最佳实践

[原文链接](https://dzone.com/articles/9-best-practices-to-handle-exceptions-in-java)

> Whether you're brand new or an old pro, it's always good to brush up on exception handling practices to make sure you and your team can deal with problems.

> 无论你是新手还是资深程序员，复习下异常处理的实践总是一件好事，因为这能确保你与你的团队在遇到问题时能够处理得了它。

Exception handling in Java isn’t an easy topic. Beginners find it hard to understand and even experienced developers can spend hours discussing how and which exceptions should be thrown or handled.

在 Java 中处理异常并不是一件易事。新手觉得处理异常难以理解，甚至是资深开发者也会花上好几个小时来讨论是应该抛出抛异常还是处理异常。

That’s why most development teams have their own set of rules on how to use them. And if you’re new to a team, you might be surprised how different these rules can be to the ones you’ve used before.

这就是为何大多数开发团队都拥有一套自己的异常处理规范。如果你初进团队，你也许会发现这些规范和你曾使用的规范大相径庭。

Nevertheless, there are several best practices that are used by most teams. Here are the 9 most important ones that help you get started or improve your exception handling.

尽管如此，这里还是有一些被大多数团队所遵循的最佳实践准则。以下9个最重要的实践方法能帮助你开始进行异常处理，或提高你的异常处理水平。

## 1. Clean Up Resources in a Finally Block or Use a Try-With-Resource Statement

## 1.在 Finally 中清理资源或使用 Try-With-Resource 语句

It happens quite often that you use a resource in your try block, like an [InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html), which you need to close afterward. A common mistake in these situations is to close the resource at the end of the try block.

在实际开发中会经常遇到在 try 中使用资源的情况，比如一个[ InputStream ](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)，在使用后你需要关闭它。在这种情况下，一个常见的错误是在 try 的尾部关闭了资源。


```java
public void doNotCloseResourceInTry() {
    FileInputStream inputStream = null;
    try {
        File file = new File("./tmp.txt");
        inputStream = new FileInputStream(file);
        // use the inputStream to read a file
        // do NOT do this
        inputStream.close();
    } catch (FileNotFoundException e) {
        log.error(e);
    } catch (IOException e) {
        log.error(e);
    }
}
```

The problem is that this approach seems to work perfectly fine as long as no exception gets thrown. All statements within the try block will get executed, and the resource gets closed.

这种情况的问题是，只要异常没被抛出，程序就能很好地运行。所有在 try 中的代码都将被正常执行，资源也会被关闭。

But you added the try block for a reason. You call one or more methods which might throw an exception, or maybe you throw the exception yourself. That means you might not reach the end of the try block. And as a result, you will not close the resources.

但是，用 try 总是有原因的。当你调用一个或多个可能会抛出异常的方法或自己主动抛出异常时，程序可能会无法到达 try 的尾部。于是在最后，资源将不被关闭。

You should, therefore, put all your clean up code into the finally block or use a try-with-resource statement.

因为，你应该将所有清理资源的代码放进 finally 中，或使用 try-with-resource 语句。

## Use a Finally Block
## 使用 Finally

In contrast to the last few lines of your try block, the finally block gets always executed. That happens either after the successful execution of the try block or after you handled an exception in a catch block. Due to this, you can be sure that you clean up all the opened resources.

与 try 相比，无论是 try 中的代码被成功执行，还是在 catch 中处理了一个异常后，Finally 中的代码总会被执行。因此，你可以确保所有已打开的资源都将被关闭。


```java
public void closeResourceInFinally() {
    FileInputStream inputStream = null;
    try {
        File file = new File("./tmp.txt");
        inputStream = new FileInputStream(file);
        // use the inputStream to read a file
    } catch (FileNotFoundException e) {
        log.error(e);
    } finally {
        if (inputStream != null) {
            try {
                inputStream.close();
            } catch (IOException e) {
                log.error(e);
            }
        }
    }
}
```

## Java 7’s Try-With-Resource Statement
## Java 7 的 Try-With-Resource 语句

Another option is the try-with-resource statement which I explained in more detail in my [introduction to Java exception handling](https://stackify.com/specify-handle-exceptions-java/?utm_referrer=https%3A%2F%2Fdzone.com%2F#tryWithResource).

你还可以选择 try-with-resource 语句，在我的这篇[ Java 异常处理入门](https://stackify.com/specify-handle-exceptions-java/?utm_referrer=https%3A%2F%2Fdzone.com%2F#tryWithResource)中有更为详细的介绍。

You can use it if your resource implements the [AutoCloseable](https://docs.oracle.com/javase/8/docs/api/java/lang/AutoCloseable.html) interface. That’s what most Java standard resources do. When you open the resource in the try clause, it will get automatically closed after the try block got executed, or an exception handled.

如果你在资源中实现了[ AutoCloseable ](https://docs.oracle.com/javase/8/docs/api/java/lang/AutoCloseable.html)接口的话，就可以使用 try-with-resource 语句了，这也是大多数 Java 标准资源的做法。如果你在 try-with-resource 中打开了一个资源，在 try 中的代码被执行或异常处理后，这个资源将会被自动关闭。

```java
public void automaticallyCloseResource() {
    File file = new File("./tmp.txt");
    try (FileInputStream inputStream = new FileInputStream(file);) {
        // use the inputStream to read a file
    } catch (FileNotFoundException e) {
        log.error(e);
    } catch (IOException e) {
        log.error(e);
    }
}
```

## 2. Prefer Specific Exceptions
## 2. 抛出更具体的异常

The more specific the exception is that you throw, the better. Always keep in mind that a co-worker who doesn’t know your code, or maybe you in a few months, need to call your method and handle the exception.

你抛出的异常越具体、越明确越好。时刻牢记这点，特别是如果有一位并不了解你代码的同事，或几个月后的你需要调用自己的方法并处理异常时。

Therefore make sure to provide them as many information as possible. That makes your API easier to understand. And as a result, the caller of your method will be able to handle the exception better or [avoid it with an additional check](https://stackify.com/top-java-software-errors/?utm_referrer=https%3A%2F%2Fdzone.com%2F).

因此，你需要确保提供尽可能多的信息，这会使得你的 API 更易于理解。这样，调用你方法的人可以更好地处理异常，从而避免额外的诸如[此类的检查](https://stackify.com/top-java-software-errors/?utm_referrer=https%3A%2F%2Fdzone.com%2F)。

So, always try to find the class that fits best to your exceptional event, e.g. throw a [NumberFormatException](https://docs.oracle.com/javase/8/docs/api/java/lang/NumberFormatException.html) instead of an [IllegalArgumentException](https://docs.oracle.com/javase/8/docs/api/java/lang/IllegalArgumentException.html). And avoid throwing an unspecific Exception.

所以，应该找到与你的异常事件最符合的类，比如抛出一个[ NumberFormatException ](https://docs.oracle.com/javase/8/docs/api/java/lang/NumberFormatException.html) 而不是 [ IllegalArgumentException ](https://docs.oracle.com/javase/8/docs/api/java/lang/IllegalArgumentException.html)(注：例如将参数转换为数值出错时，应该抛出具体的 NumberFormatException ，而不是笼统的 IllegalArgumentException )。请避免抛出一个不具体的异常。

```java
public void doNotDoThis() throws Exception {
    ...
}
public void doThis() throws NumberFormatException {
    ...
}
```

## 3. Document the Exceptions You Specify
## 3. 为你的异常编写文档

Whenever you [specify an exception](https://stackify.com/specify-handle-exceptions-java/?utm_referrer=https%3A%2F%2Fdzone.com%2F#specify) in your method signature, you should also [document it in your Javadoc](http://blog.joda.org/2012/11/javadoc-coding-standards.html). That has the same goal as the previous best practice: Provide the caller as many information as possible so that he can avoid or handle the exception.

当你在方法签名中[指定一个异常](https://stackify.com/specify-handle-exceptions-java/?utm_referrer=https%3A%2F%2Fdzone.com%2F#specify)时，你也应该在[ Javadoc 中记录它](http://blog.joda.org/2012/11/javadoc-coding-standards.html)。

So, make sure to add a @throws declaration to your Javadoc and to describe the situations that can cause the exception.

所以，请确保在 Javadoc 中增加 @throws 声明，并描述可能会导致异常的情况。

```java
/**
 * This method does something extremely useful ...
 *
 * @param input
 * @throws MyBusinessException if ... happens
 */
public void doSomething(String input) throws MyBusinessException {
    ...
}
```

## 4. Throw Exceptions With Descriptive Messages
## 4. 将描述信息与异常一同抛出

The idea behind this best practice is similar to the two previous ones. But this time, you don’t provide the information to the caller of your method. The exception’s message gets read by everyone who has to understand what had happened when the exception was reported in the log file or your monitoring tool.

这个方法背后的思想和前两个是类似的。但这一次，你不必给你的方法调用者提供信息。对于任何遭遇异常错误并需要搞清楚错误原因的人来说，异常信息总是在异常出现的同时，被记录在了日志中，或打印在了屏幕上。

It should, therefore, describe the problem as precisely as possible and provide the most relevant information to understand the exceptional event.

因此，请尽可能精确地描所以，最好不要在 catch 中使用 Throwable ，除非你能确保自己处于一些特定情况下，比如你自己足以处理错误，又或被要求处理错误时。述异常事件，并提供最相关的信息以令其他人能够理解发生了什么异常时。

Don’t get me wrong; you shouldn’t write a paragraph of text. But you should explain the reason for the exception in 1-2 short sentences. That helps your operations team to understand the severity of the problem, and it also makes it easier for you to analyze any service incidents.

别误会我的意思了。你没必要去写上一大段的文字，但你应该用一两句简短的话来解释一下异常发生的原因。这能让你的开发团队明白问题的严重性，也能让你更容易地分析服务事故。

If you throw a specific exception, its class name will most likely already describe the kind of error. So, you don’t need to provide a lot of additional information. A good example for that is the NumberFormatException. It gets thrown by the constructor of the class java.lang.Long when you provide a String in a wrong format.

如果你抛出了一个特定的异常，它的类名很可能就已经描述了这是什么类型的错误了。所以，你不需要提供很多额外的描述信息。一个很好的例子是，当你提供了一个错误格式的 String 类型参数时，java.lang.Long 构造函数就会抛出 NumberFormatException 。

```java
try {
    new Long("xyz");
} catch (NumberFormatException e) {
    log.error(e);
}
```

The name of the NumberFormatException class already tells you the kind of problem. Its message only needs to provide the input string that caused the problem. If the name of the exception class isn’t that expressive, you need to provide the required information in the message.

NumberFormatException 的类名已经告诉了你问题的类型。所以异常信息只需要返回导致问题的输入字符串就行了。如果异常类的名字不能表明其含义，那么你还需要在异常信息中提供必要的解释信息。

```
17:17:26,386 ERROR TestExceptionHandling:52 - java.lang.NumberFormatException: For input string: "xyz"
```

## 5. Catch the Most Specific Exception First
## 5. 优先捕获具体的异常

Most IDEs help you with this best practice. They report an unreachable code block when you try to catch the less specific exception first.

大多数 IDE 都能帮你做到这点。当你尝试优先捕获不那么具体的异常时， IDE 会报告给你这是一个不能到达的代码块。

The problem is that only the first catch block that matches the exception gets executed. So, if you catch an IllegalArgumentException first, you will never reach the catch block that should handle the more specific NumberFormatException because it’s a subclass of the IllegalArgumentException.

这个问题的原因是只有第一个匹配到异常的 catch 块才会被执行。所以，如果你先 catch 了一个 IllegalArgumentException ，你将永远无法到达处理更具体异常 NumberFormatException 的 catch 块中，因为 NumberFormatException 是
 IllegalArgumentException 的子类。

Always catch the most specific exception class first and add the less specific catch blocks to the end of your list.

所以，请优先捕获更具体的异常，并把不那么具体的 catch 块放在后面。

You can see an example of such a try-catch statement in the following code snippet. The first catch block handles all NumberFormatExceptions and the second one all IllegalArgumentExceptions which are not a NumberFormatException.

在下面你可以看到这样的一个 try-catch 语句示例。第一个 catch 处理所有的 NumberFormatExceptions 异常，第二个 catch 处理 NumberFormatException 异常以外的 illegalargumentexception 异常。

```java
public void catchMostSpecificExceptionFirst() {
    try {
        doSomething("A message");
    } catch (NumberFormatException e) {
        log.error(e);
    } catch (IllegalArgumentException e) {
        log.error(e)
    }
}
```

## 6. Don’t Catch Throwable
## 6. 不要捕获 Throwable

[Throwable](https://docs.oracle.com/javase/8/docs/api/java/lang/Throwable.html) is the superclass of all exceptions and errors. You can use it in a catch clause, but you should never do it!

[Throwable ](https://docs.oracle.com/javase/8/docs/api/java/lang/Throwable.html)是所有 exceptions 和 errors 的父类。虽然你可以在 catch 子句中使用它，但你应该永远别这样做！

If you use Throwable in a catch clause, it will not only catch all exceptions; it will also catch all errors. Errors are thrown by the JVM to indicate serious problems that are not intended to be handled by an application. Typical examples for that are the [OutOfMemoryError](https://docs.oracle.com/javase/8/docs/api/java/lang/OutOfMemoryError.html) or the [StackOverflowError](https://docs.oracle.com/javase/8/docs/api/java/lang/StackOverflowError.html). Both are caused by situations that are outside of the control of the application and can’t be handled.

如果你在 catch 子句中使用了 Throwable ，它将不仅捕获所有异常，还会捕获所有错误。这些错误是由 JVM 抛出的，用来表明不打算由应用处理的严重错误。[ OutOfMemoryError ](https://docs.oracle.com/javase/8/docs/api/java/lang/OutOfMemoryError.html) 和 [ StackOverflowError ](https://docs.oracle.com/javase/8/docs/api/java/lang/StackOverflowError.html)就是典型的例子，这两种情况都是由一些超出应用控制范围的情况导致的，无法处理。

So, better don’t catch a Throwable unless you’re absolutely sure that you’re in an exceptional situation in which you’re able or required to handle an error.

所以，最好不要在 catch 中使用 Throwable ，除非你能确保自己处于一些特定情况下，比如你自己足以处理错误，又或被要求处理错误。

```java
public void doNotCatchThrowable() {
    try {
        // do something
    } catch (Throwable t) {
        // don't do this!
    }
}
```

## 7. Don’t Ignore Exceptions
## 7. 不要忽略异常

Have you ever analyzed a bug report where only the first part of your use case got executed?

你分析过只有用例的第一部分代码被执行的 bug 报告吗？

That’s often caused by an ignored exception. The developer was probably pretty sure that it would never be thrown and added a catch block that doesn’t handle or logs it. And when you find this block, you most likely even find one of the famous “This will never happen” comments.

这通常是由于忽略异常而导致的。开发者可能十分确定这个异常不会被抛出，然后添加了一个无法处理或无法记录这个异常的 catch 。当你找到这个 catch 时，你很可能会发现这么一句著名的注释： “This will never happen”。

```java
public void doNotIgnoreExceptions() {
    try {
        // do something
    } catch (NumberFormatException e) {
        // this will never happen
    }
}
```

Well, you might be analyzing a problem in which the impossible happened.

没错，你可能就是在分析一个永远也不会发生的问题。

So, please, never ignore an exception. You don’t know how the code will change in the future. Someone might remove the validation that prevented the exceptional event without recognizing that this creates a problem. Or the code that throws the exception gets changed and now throws multiple exceptions of the same class, and the calling code doesn’t prevent all of them.

所以，请你务必不要忽略异常。你不知道代码在将来会经历怎样的改动。有些人可能会误删异常事件的验证，而完全没意识到这会产出问题。或者抛出异常的代码被修改了，相同的类被抛出了多个异常，而调用它们的代码并不能阻止这些异常发生。

You should at least write a log message telling everyone that the unthinkable just had happened and that someone needs to check it.

你至少应该把日志信息打印出来，告诉那些无意识下错误操作的人需要检查这里。

```java
public void logAnException() {
    try {
        // do something
    } catch (NumberFormatException e) {
        log.error("This should never happen: " + e);
    }
}
```

## 8. Don’t Log and Throw
## 8. 不要同时打印并抛出异常

That is probably the most often ignored best practice in this list. You can find lots of code snippets and even libraries in which an exception gets caught, logged and rethrown.

这可能是本文中最常被忽略的一条实践准则了。你可以在许多代码片段甚至库中发现这个问题，异常被捕获，打印，再被重新抛出。

```java
try {
    new Long("xyz");
} catch (NumberFormatException e) {
    log.error(e);
    throw e;
}
```

It might feel intuitive to log an exception when it occurred and then rethrow it so that the caller can handle it appropriately. But it will write multiple error messages for the same exception.

这样也许会很直观地看到被打印的异常，异常再被重新抛出，调用者也能很好地处理它。但这样会使多个错误信息被同个异常给打印出来。

```
17:44:28,945 ERROR TestExceptionHandling:65 - java.lang.NumberFormatException: For input string: "xyz"
Exception in thread "main" java.lang.NumberFormatException: For input string: "xyz"
at java.lang.NumberFormatException.forInputString(NumberFormatException.java:65)
at java.lang.Long.parseLong(Long.java:589)
at java.lang.Long.(Long.java:965)
at com.stackify.example.TestExceptionHandling.logAndThrowException(TestExceptionHandling.java:63)
at com.stackify.example.TestExceptionHandling.main(TestExceptionHandling.java:58)
```

The additional messages also don’t add any information. As explained in best practice #4, the exception message should describe the exceptional event. And the stack trace tells you in which class, method, and line the exception was thrown.

额外的信息并不能提供更多的错误细节。如第4条准则中所述，异常信息应该准确描述异常事件。 Stack Trace (堆栈追踪)会告诉你异常在哪个类、哪个方法、哪个行中被抛出。

If you need to add additional information, you should catch the exception and wrap it in a custom one. But make sure to follow best practice number 9.

如果你需要添加额外的信息，你应该将异常捕获并包装在自定义的的异常中，但要确保遵循下面的第9条实践准则。

```java
public void wrapException(String input) throws MyBusinessException {
    try {
        // do something
    } catch (NumberFormatException e) {
        throw new MyBusinessException("A message that describes the error.", e);
    }
}
```

So, only catch an exception if you want to handle it. Otherwise, specify it in the method signature and let the caller take care of it.

所以，只有在你想要处理一个异常的时候才去捕获它。否则，在方法签名处指明这个异常让调用者关注就好了。

## 9. Wrap the Exception Without Consuming it
## 9. 包装异常但不要丢弃原始异常

It’s sometimes better to catch a standard exception and to wrap it into a custom one. A typical example for such an exception is an application or framework specific business exception. That allows you to add additional information and you can also implement a special handling for your exception class.
有时候将异常包装成一个自定义异常会比捕捉一个标准异常要更好。一个典型的例子是应用或框架的特定业务异常。这允许你添加额外的信息，也能为你的异常类实现一个特定的处理方法。

When you do that, make sure to set the original exception as the cause. The Exception class provides specific constructor methods that accept a Throwable as a parameter. Otherwise, you lose the stack trace and message of the original exception which will make it difficult to analyze the exceptional event that caused your exception.

当你这么做的时候，一定要确保原始的异常设为 cause 。 Exception 类提供了一系列的特定构造方法，这些方法可以接受 Throwable 作为参数(注：如`Exception(String message, Throwable cause)`)。否则，你将会丢失原始异常的 stack trace 与信息，这会使你分析导致异常的事件变得十分困难。

```java
public void wrapException(String input) throws MyBusinessException {
    try {
        // do something
    } catch (NumberFormatException e) {
        throw new MyBusinessException("A message that describes the error.", e);
    }
}
```

## Summary
## 总结

As you’ve seen, there are lots of different things you should consider when you throw or catch an exception. Most of them have the goal to improve the readability of your code or the usability of your API.

如你所见，当决定该抛出还是捕获异常时候，你需要去考虑很多方面。以上的大多数实践准则都是为了提高你代码和 API 的可读性与可用性。

Exceptions are most often an error handling mechanism and a communication medium at the same time. You should, therefore, make sure to discuss the best practices and rules you want to apply with your coworkers so that everyone understands the general concepts and uses them in the same way.

异常是不仅是一个错误处理机制，同时也是一个沟通媒介。因此，你应该与你的同事一起讨论哪些是你想要应用的最佳实践与准则，以便所有人都能理解相关的基本概念，并用同样的方式在实际中应用这些准则。
