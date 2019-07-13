---
translator: http://www.jobbole.com/members/pu_zhe/
reviewer: http://www.jobbole.com/members/hanxiaomax/
via: https://dzone.com/articles/java-code-bytes-be-resourceful-with-try-with-resou
---

# Java Code Bytes: Be Resourceful With Try-With-Resources
# Java 代码字节：足智多谋的 Try-With-Resources 

It is very common that, while implementing a business case in Java, we have to deal with resources. In this context, a resource (such as a file or socket handle) is encapsulated in an object that we must close after they are used in order to release the resource. Traditionally, the onus was on the developer to close all the resources they created to avoid dependency collisions, generally in the following finally block. Failing to do so is not a compilation error, but it can easily lead to a leakage of resource. Though modern static code analysis tools are smart enough to give you a hint, not everyone uses them, and also, those alerts can be easily overlooked.

当通过 Java 实现业务实例时，对资源进行处理是司空见惯的。一般情况下，资源（如文件或 socket 句柄）封装在对象中，使用后必须关闭才能释放资源。通常开发人员有责任关闭自己所创建的资源，以避免资源冲突，一般都会放在 finally 语句块中处理。不这样做其实也不会产生编译错误，但很容易导致资源泄露。虽然现在静态代码检查工具足够聪明，也可以做出提示。但不是每个人都使用工具，而且这些警告也容易被忽略。

try-with-resources was first introduced in Java 7 and is a new way to handle (closing of) resources; it makes it easier dealing with resources by automatically taking care of the closing of resources in the correct order, which was used within a try-catch block.

Java 7 中首次引入了一种新的处理（关闭）资源的方式——try-with-resources。它使得在 try-catch 语句块中的资源能按照正确顺序自动关闭，更加容易地处理资源。

Let's take a business case implementation where we need to fetch a given account's status code from a database. We will first see how it is done in the traditional way and, then, with more resourceful try-with-resources. Later, we will also see a more concise version of it, which was introduced in Java 9.

我们来一起看一个业务实例的实现，其需要从数据库中获取指定账户的状态码。首先可以看到它是如何以传统方式实现，紧接着是足智多谋的 try-with-resources 如何实现。最后，还将看到 Java 9 引入的更加简洁的版本。

## Resource Handling in the Traditional Way (pre-Java 7)  

## 传统的方式处理资源（Java 7 之前）

```java
// Code is simplified and kept relevant to focus on the topic in hand.
// 代码已简化，只保留跟眼下话题相关的内容。
public static int getAccountStatusCodeFromDataStore_traditional(String accountId) throws SQLException {
  String accountStatusCodeQuery = getAccountStatusCodeQuery(accountId);
  Statement statement = null;
  ResultSet resultSet = null;
  try {
    statement = createStatementFromConnection();
    resultSet = statement.executeQuery(accountStatusCodeQuery);
    return getAccountStatusCodeFromResultSet(resultSet);
  } finally {
    if (resultSet != null)
      resultSet.close();
    if (statement != null)
      statement.close();
  }
}
```

As shown above, we have to add a finally block to deal with the closing of resource. We have to explicitly check for null before we call the close operation. Also, we have to maintain the logical order for the closing of resources. The code here is verbose; and, I have seen many cases where developers tend to forget to add the finally block for closing resource, which will lead to resource leaks.

如上所示，我们必须增加 finally 语句块来处理资源关闭。在调用 close 方法之前，须显示地检查 null 值，并且同时要保证关闭资源的逻辑顺序。代码不但变得冗长，而且我们曾经遇到过许多开发人员会忘记编写 finally 语句块来关闭资源，导致资源泄露的情况。

As a side note, if exceptions are thrown here in both try block and finally block, the one thrown from finally block will suppress the other.

顺便提一下，假如 try 和 finally 语句块都抛出异常，finally 语句块抛出的异常会屏蔽对方。

## Resource Handling With try-with-resources in Java 7/8
## Java 7/8 中通过 try-with-resources 处理资源
The same block of code above is now implemented with try-with-resources, which will look like:

现通过 try-with-resources 实现与上面相同的代码块，如下所示：

```java
// Code is simplified and kept relevant to focus on the topic in hand.
// 代码已简化，只保留跟眼下话题相关的内容。
public static int getAccountStatusCodeFromDataStore_tryWithResourcesJava7(String accountId) throws SQLException {
  String accountStatusCodeQuery = getAccountStatusCodeQuery(accountId);
  try (Statement statement = createStatementFromConnection();
       ResultSet resultSet = statement.executeQuery(accountStatusCodeQuery)) {
    return getAccountStatusCodeFromResultSet(resultSet);
  }
}
```

In this example, you can see that the improved concisness of the code contributes to its overall readability. The resource management is done automatically here. We can have multiple resources in the try-with-resources statement. In that case, the resource declarations should be separated by a semicolon. These resources will be automatically closed, maintaining the logic order (the one declared last will be closed first etc.).

在本例中可以看到简洁的代码有助于提高整体可读性，资源管理也自动完成。try-with-resources 语句中可以包含多个资源，它们之间应通过分号隔开。资源会在保持逻辑顺序的前提下自动关闭（最后声明的将第一个关闭）。

If exceptions are thrown here, in both the try-with-resources block and try block, the one thrown from try block will suppress the other. If required, we can retrieve the suppressed exceptions by calling the Throwable.getSuppressed method from the exception thrown by the try block.

如果在 try-with-resources 和 try 语句块中抛出异常，从 try 中抛出的异常将会屏蔽对方。假如有需要，可从 try 语句块抛出的异常中，通过调用  Throwable.getSuppressed 方法找回屏蔽的异常。


Also, a try-with-resources statement can have catch and finally blocks. Any catch or finally block is run after the resources declared have been closed.

try-with-resources 语句中也可以写 catch 和 finally 语句块。任何 catch 和 finally 语句块会在声明的资源关闭后运行。

## Resource Handling With try-with-resources in Java 9 
## Java 9 中通过 try-with-resources 处理资源

A more concise version is introduced in Java 9. If we already have a resource declared as a final or effective final, we can use them in try-with-resources without creating any new variables. This allows us to take advantage of automatic resource management. The same block of code above, now implemented with more concise try-with-resources, will look like: 

Java 9 中引入了更加简练的版本。如果已经把资源声明为 final 或 effective final，则在 try-with-resources 中无需创建任何新的变量，可直接使用。这使得能够利用自动资源管理。现通过更简洁的 try-with-resources 语句来实现与上面相同的代码块，如下所示：

```java
// Code is simplified and kept relevant to focus on the topic in hand.
// 代码已简化，只保留跟眼下话题相关的内容。
public static int getAccountStatusCodeFromDataStore_tryWithResourcesJava9(String accountId) throws SQLException {
  String accountStatusCodeQuery = getAccountStatusCodeQuery(accountId);
  // declared explicitly final
  // 显示地声明 final 
  final Statement statement = createStatementFromConnection();
  // effective final
  ResultSet resultSet = statement.executeQuery(accountStatusCodeQuery);
  try (statement; resultSet) {
    return getAccountStatusCodeFromResultSet(resultSet);
  }
}
```  

## How It Works Behind the Scenes

## 幕后如何运行
The AutoCloseable interface was introduced with Java 7, and it was specifically designed to work with try-with-resources statements. The Closeable interface was introduced earlier with Java 5 and was modified to extend to the AutoCloseable. They both have this abstract method close, which the resource should implement and provide a valid implementation. We can use try-with-resources to close any resource that implements either AutoCloseable or Closeable. All of the JDK resource-based classes and interfaces are modified to extend either of these interfaces, making them compatible with try-with-resources out of the box.

Java 7 引入了专门设计用于 try-with-resources 语句的 AutoCloseable 接口。Java 5 引入的 Closeable 接口也修改为继承 AutoCloseable 接口。这两个接口都拥有抽象的 close 方法，资源应该实现它并提供有效的方法。任何实现 AutoCloseable 和 Closeable 接口的资源都可以通过 try-with-resources 来关闭。所有基于 JDK 资源的类和接口都已修改成继承这两个接口其中之一，使之能与现有的 try-with-resources 语句兼容。

However, if we are dealing with a resource that doesn't implement either of AutoCloseable or Closeable, we have to follow the traditional approach for closing the resource. 

然而，若处理的资源没有实现 AutoCloseable 或 Closeable 接口，则必须使用传统的方法来关闭。

## Key Takeaways

## 关键要点
try-with-resources facilitates automatic resource management with no need to write an explicit finally block to deal with closing of resources. Here is the summary of the key takeaways about try-with-resources.   

try-with-resources 有助于自动资源管理，不需要编写显示的 finally 语句块来处理关闭资源。下面是对 try-with-resources 关键点的总结：

- It helps in achieving more concise and legible code.

- 有助于实现简练清晰的代码。

- We can deal with multiple resources in the try-with-resources statement.

- 可以在 try-with-resources 语句中同时处理多个资源。

- In Java 7/8, these resources must be declared in try-with-resources statement. The resources declared this way are implicitly final.

- 在 Java 7/8 ，try-with-resources 语句中必须声明要关闭的资源。通过这种方式声明的资源属于隐式 final。

- In Java 9, we can even use pre-created resources, given that the resources referenced are declared as a final or are effective final.

- Java 9 中甚至能使用预先创建的资源，只要所引用的资源声明为 final 或者是 effective final。

- AutoCloseable or Closeable interfaces do behind the scenes magic — they work in tandem with try-with-resources statements.

- 在幕后施展魔法的是 AutoCloseable 或者 Closeable 接口，它们与 try-with-resources 语句协同工作。

- Most of the resource-based classes and interfaces in JDK are modified to implement either AutoCloseable or Closeable, making them compatible with try-with-resources out of the box.

- JDK 中大多数基于资源的类和接口已修改成实现 AutoCloseable 或 Closeable 接口，使它们能与现有的 try-with-resources 兼容。

- We can have our custom resources implement either of AutoCloseable or Closeable and make them work with try-with-resources statements.

- 可以使自定义的资源实现 AutoCloseable 或 Closeable 接口，以便能够在 try-with-resources 语句中使用。




