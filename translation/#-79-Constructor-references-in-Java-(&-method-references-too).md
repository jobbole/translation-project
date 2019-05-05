---
translator: http://www.jobbole.com/members/wx3433627156/
reviewer: http://www.jobbole.com/members/hanxiaomax/
via: https://jaxenter.com/constructor-references-java-148670.html
---

## Constructor references in Java (& method references too)（Java 中的构造函数引用和方法引用）

> 转译自：https://jaxenter.com/constructor-references-java-148670.html

JDK 8 saw the advent of a special feature: constructor references and method references. In this article, Adrian D. Finlay explores how developers can unlock the true potential of constructor references.

JDK 8 见证了一个特殊特性的出现：构造函数引用和方法引用。在本文中， Adrian D. Finlay 探讨了开发人员如何释放构造函数引用的真正潜力。

### Some background on method references（方法引用的一些背景）

If you didn’t already know, Java Constructors are, themselves, special methods. As such, it will benefit the reader to see a basic example of a method reference, and through understanding this, understand what Constructor References are.

如果你还不知道 Java 构造函数本身就是特殊的方法，那么阅读方法引用的基本示例将对读者有所帮助，通过了解这些内容，可以了解构造函数引用是什么。

“Method references provide easy-to-read lambda expressions for methods that already have a name.”

「方法引用为已经有名称的方法提供易读的 lambda 表达式。」

“They provide an easy way to refer to a method without executing it.” ( Java, The Complete Reference 9th Ed, by Herbert Schildt)

「它们提供了一种无需执行就可以引用方法的简单方式。」

>以上引自《Java 8 编程参考官方教程（第 9 版）》，作者：Herbert Schildt

译注：该书的第 8 版中文译本名称为：《Java 完全参考手册（第 8 版）》，第 9 版中文译本名称为：《Java 8 编程参考官方教程（第 9 版）》

Method references can refer to both static and instance methods and can be generic. Method References are instances of a functional interface. While Lambda Expressions allow you to create method implementations on the fly, often times one ends up calling another method inside the lambda expression to fulfill what we want done. A more direct way to do this is to use a method reference. This is useful in circumstances where you already have a method that fulfills the implementation of the Functional Interface.

方法引用可以引用静态方法和实例方法，两者是通用的。方法引用是函数式接口的实例。虽然 Lambda 表达式允许你动态创建方法实现，但通常情况下，一个方法最终会调用 Lambda 表达式中的另一个方法来完成我们想要完成的工作。更直接的方法是使用方法引用。当你已经有一个方法来实现这个函数式接口时，这是非常有用的。

Let’s look at an example with static & instance methods.

让我们看一个使用静态方法及实例方法的示例。

```java
//step #1 - Create a funnctional interface.
interface FuncInt {
    //contains one and only abstract method
    String answer(String x, boolean y);
}

//step #2 - Class providing method(s)that match FuncInt.answer()'s definition.
class Answer {
    static String ans_math_static(String x, Boolean y) {
        return "\"" + x + "\"" + "\t = \t" + y.toString().toUpperCase();
    }

    String ans_math_inst(String x, Boolean y) {
        return "\"" + x + "\"" + "\t = \t" + y.toString().toUpperCase();
    }
}
```

译注：以上代码的测试用例如下，因静态方法与实例方法结果相同，仅以静态方法为例。

```
Answer.ans_math_static("9 > 11 ?", false);
Answer.ans_math_static("987.6 < 1.1 ?", false);
Answer.ans_math_static("1 > 0.9 ?", true);
Answer.ans_math_static("T/F: Is Chengdu in Sichuan?", true);
Answer.ans_math_static("-1 % 0.2=0 ?", false);
Answer.ans_math_static("T/F: Does Dwyne Wade play for the Knicks?", false);
```

得到与原文举例相同的输出结果：

```
"9 > 11 ?"	 = 	FALSE
"987.6 < 1.1 ?"	 = 	FALSE
"1 > 0.9 ?"	 = 	TRUE
"T/F: Is Chengdu in Sichuan?"	 = 	TRUE
"-1 % 0.2=0 ?"	 = 	FALSE
"T/F: Does Dwyne Wade play for the Knicks?"	 = 	FALSE
```

SEE ALSO: All about var: How Local-Variable Type Inference can clear up Java verbosity

另请参阅：[All about var: How Local-Variable Type Inference can clear up Java verbosity（关于var的所有内容：局部变量类型推断如何清除Java代码冗余）](https://jaxenter.com/java-10-local-var-type-inference-148390.html)

The steps for making use of method references are essentially:

使用方法引用的主要步骤有：

1. Define a Functional Interface

定义一个函数式接口

2. Define a method that meets the requirements of the Functional Interface’s abstract method

定义一个满足函数式接口抽象方法要求的方法

3. Instantiate an instance of the Functional Interface with a method reference to the method defined in step 2. (x :: y )

使用对步骤2中定义的方法的方法引用实例化函数式接口的实例。

译注：静态方法的方法引用格式为 `类名 :: 方法名` ；实例方法的方法引用格式为 `对象实例名 :: 方法名` 。

4. Use Functional Interface instance: Instance.AbstractMethod();

使用函数式接口实例调用方法： `Instance.AbstractMethod();`

This gives a way to create plug-able instances of methods. Lambda Expression and Method References bring a Functional Aspect to Java Programming.

这提供了一种创建方法实现的可插拔方式。Lambda 表达式和方法引用为 Java 编程带来了一个功能方面的提升。

SEE ALSO: How well do you actually understand annotations in Java?

另请参阅：[How well do you actually understand annotations in Java?（你到底有多了解Java的注释?）](https://jaxenter.com/understand-annotations-java-148001.html)

### Constructor method references（构造函数的方法引用）

Let’s get down to the meat and potatoes.

让我们开始详细讨论吧。

Constructors are methods just like any other. Right? Wrong. They’re a bit special — they’re object initialization methods. Nevertheless, they are a still a method, and there is nothing stopping us from making Constructor Method References like any other method reference.

构造函数和其他方法一样是方法。对吗？错。它们有点特殊，它们是对象初始化方法。尽管如此，它们仍然是一个方法，没有什么能阻止我们像其他方法引用一样创建构造函数的方法引用。

```java
//step #1 - Create a funnctional interface.
interface FuncInt {
    //contains one and only abstract method
    Automobile auto(String make, String model, short year);
}

//step #2 - Class providing method(s)that match FuncInt.answer()'s definition.
class Automobile {

    //Trunk Member Variables
    private String make;
    private String model;
    private short year;

    //Automobile Constructor
    public Automobile(String make, String model, short year) {
        this.make = make;
        this.model = model;
        this.year = year;
    }

    protected void what() {
        System.out.println("This Automobile is a" + year + " " + make + " " + model + ".");
    }
}

//Step #3 - Class making use of method reference
public class ConstrRef {

    static void createInstance() {
    }

    public static void main(String[] args) {
        System.out.println();

        //Remember, a Method Reference is an instance of a Functional Interface. Therefore....
        FuncInt auto = Automobile::new;//We really don't gain much from this example

        //Example #1
        Automobile honda = auto.auto("honda", "Accord", (short) 2006);
        honda.what();

        //Example #1
        Automobile bmw = auto.auto("BMW", "530i", (short) 2006);
        bmw.what();

        System.out.println();
    }
}
```

输出结果

```
This Automobile is a2006 honda Accord.
This Automobile is a2006 BMW 530i.
```

### Explanation（说明）

The first thing that should be obvious to the user is that this basic example is not that useful. It is a rather roundabout way to create an instance of an object. Practically speaking, you almost certainly wouldn’t go through all this trouble to create an instance of an Automobile, but for conceptual completeness, it is included here.

用户应该清楚的第一件事是这个基本示例没有那么实用。这是一种相当迂回的创建对象实例的方式。实际上，几乎可以肯定，你不会经历所有这些麻烦来创建一个Automobile实例，但是为了概念的完整性，还是要提及。

The steps for making use of constructor method references are essentially:

使用构造函数的方法引用的主要步骤有：

1. Define a Functional Interface with an abstract method whose return type is the same as the Object with which you intend to make a Constructor Reference

定义一个只有抽象方法的函数式接口，该方法的返回类型与你打算使用该对象进行构造函数引用的对象相同

2. Create a class with a constructor that matches the Functional Interface’s abstract method

创建一个类，该类的构造函数与函数式接口的抽象方法匹配

3. Instantiate an instance of the Functional Interface with a method reference to the constructor defined in step #2. (x :: y )

使用对步骤 #2 中定义的构造函数的方法引用，实例化函数式接口的实例。

译注：构造函数的方法引用格式为 `类名 :: new`

4. Instantiate an instance of the class in step#2 using the constructor reference such that MyClass x = ConstructorReference.AbstractMethod (x, y, z…)

在步骤 #2 中使用构造函数引用实例化类的实例，例如 `MyClass x = ConstructorReference.AbstractMethod (x, y, z…)`

> Where Constructor References become useful is when they are used in tandem with Generics. By using a generic factory method one can create various types of objects.

> 构造函数引用与泛型一起使用的时候变得更有用。通过使用泛型工厂方法，可以创建各种类型的对象。

Let’s have a peek.

让我们看一看。

```java
//step #1 - Create a funnctional interface.
interface FuncInt<Ob, X, Y, Z> {
    //contains one and only abstract method
    Ob func(X make, Y model, Z year);
}

//step #2 - Create a Generic class providing a constructor compatible with FunInt.func()'s definition
class Automobile<X, Y, Z> {

    //Automobile Member Variables
    private X make;
    private Y model;
    private Z year;

    //Automobile Constructor
    public Automobile(X make, Y model, Z year) {
        this.make = make;
        this.model = model;
        this.year = year;
    }

    protected void what() {
        System.out.println("This Automobile is a " + year + " " + make + " " + model + ".");
    }
}

//step #3 - Create a Non-Generic class providing a constructor compatible with FunInt.func()'s definition
class Plane {

    //Automobile Member Variables
    private String make;
    private String model;
    private int year;

    //Plane Constructor
    public Plane(String make, String model, int year) {
        this.make = make;
        this.model = model;
        this.year = year;//Automatic unboxing
    }

    protected void what() {
        System.out.println("This Plane is a " + year + " " + make + " " + model + ".");
    }
}

//Step #3 - Class making use of method reference with generics
public class ConstrRefGen {

    //Here is where the magic happens
    static <Ob, X, Y, Z> Ob factory(FuncInt<Ob, X, Y, Z> obj, X p1, Y p2, Z p3) {
        return obj.func(p1, p2, p3);
    }

    public static void main(String[] args) {
        System.out.println();

        //Example #1
        FuncInt<Automobile<String, String, Integer>, String, String, Integer> auto_cons = Automobile<String, String, Integer>::new;
        Automobile<String, String, Integer> honda = factory(auto_cons, "Honda", "Accord", 2006);
        honda.what();

        //Example #2
        FuncInt<Plane, String, String, Integer> plane_cons = Plane::new;
        Plane cessna = factory(plane_cons, "Cessna", "Skyhawk", 172);
        cessna.what();

        System.out.println();
    }
}
```

输出结果

```
This Automobile is a 2006 Honda Accord.
This Plane is a 172 Cessna Skyhawk.
```

SEE ALSO: Structs in Java: How to handle them like a pro

另请参阅：[Structs in Java: How to handle them like a pro（Java中的结构：如何像专业人士一样处理它们）](https://jaxenter.com/java-struct-benefits-145396.html)

### Explanation（说明）

Now, there is a lot to digest here. In fact, the code may appear rather obscure at first glance, if you have never dived into Generics before. Let’s break it down.

这里有很多东西需要消化。事实上，如果你以前从未深入研究过泛型，那么这些代码看上去可能相当晦涩。让我们分解一下。

The first thing we do is create a generic functional interface. Pay attention to the details. We have four generic type parameters — Ob, X,Y,Z.

我们做的第一件事是创建一个通用的函数式接口。注意细节。我们有四个泛型类型参数：Ob、X、Y、Z。

Ob — The Class whose constructor we want to reference

Ob代表要引用其构造函数的类。

X,Y,Z — The arguments to the constructor of said class.

X,Y,Z代表该类的构造函数的参数。

If we substitute the generic method placeholders, the Abstract method could look like this: SomeClass func (String make, String model, int year). Notice that because we made the interface generic, we can specify any return type or type of class we desire. This allows to unlock the true potential of constructor references.

如果我们替换泛型方法占位符，抽象方法可能是这样的: `SomeClass func (String make, String model, int year)`。注意，由于我们使接口具有了泛型，所以可以指定任何返回类型或我们希望返回的类实例。这释放了构造函数引用的真正潜力。

The next two portions are relatively straightforward — We essentially create what is the same class, one generic, and one non-generic to demonstrate their interoperability with the factory method we will later define in the public class. Notice that the Constructors of these classes are compatible with the method signature of FuncInt.func().

接下来的两个部分相对简单，我们创建了相同的类，一个泛型类和一个非泛型类，以演示它们与在公共类中定义的工厂方法的互操作性。注意，这些类的构造函数与 `FuncInt.func()` 的方法签名是兼容的。

Enter into the public class of the file. This method is where the magic happens.

进入公共类的文件。这个方法就是奇迹发生的地方。

```java
//Here is where the magic happens
static <Ob, X, Y, Z> Ob factory(FuncInt<Ob, X, Y, Z> obj, X p1, Y p2, Z p3) {
    return obj.func(p1, p2, p3);
}
```

We label the method as static, so we can do without an instance of ConstRefGen and, after all, it’s a factory method. Notice that the factory method has the same generic type parameters as the functional interface. Notice that the return type of the method is Ob which will be whichever class we decide. X,Y,Z , are, of course, the method arguments of a method in Ob. Notice that the function takes an instance of the FuncInt as an argument (with the Class Type and the method arguments as type paramaters) as well as the arguments of the method of the class of type Ob.

我们将该方法标记为静态的，所以我们可以不使用 ConstRefGen 实例，毕竟它是一个工厂方法。注意，factory 方法具有与函数式接口相同的泛型类型参数。注意，方法的返回类型是 Ob，它可以是由我们决定的任何类。当然，X、Y、Z是 Ob 中方法的方法参数。请注意，该函数以 FuncInt 的一个实例作为参数（类类型和方法参数作为类型参数），同时也接受 Ob 类型的类作为方法的参数。

SEE ALSO: Reactor.js: A lightweight library for reactive programming

另请参阅：[Reactor.js: A lightweight library for reactive programming（Reactor.js：用于响应式编程的轻量级库）](https://jaxenter.com/reactor-js-library-reactive-programming-148585.html)

Inside the body of the method it calls the method reference and feeds it the arguments passed in factory().

在方法体中，它调用方法引用并将在 `factory()` 中传递的参数提供给它。

Our first task — create a method reference that complies with FuncInt<>

我们的第一个任务是创建一个符合 `FuncInt<>` 的方法引用

Here we refer to the constructors of Automobile and Plane respectively.

这里我们分别引用 Automobile 类和 Plane 类的构造函数。

Our next task — Create an object with a method reference.

我们的下一个任务是创建一个带有方法引用的对象。

To do this, we call factory() and we feed it the Constructor Reference it needs as well as the arguments for the constructor in question as defined by factory ().

为此，我们调用 `factory()` 并将它需要的构造函数引用以及 `factory()` 定义的有关构造函数的参数提供给它。

factory() can agnostically create constructor references to various methods because it is generic. Because the Plane & Automobile constructors match the method signature of FuncInt.func() they will work with as a method reference with FuncInt.func(). factory() returns an instance of the class in question by calling obj.func(x,y,z) which is a constructor method reference that when evaluated will give you an instance of the class that was specified as an argument to it.

`factory()` 可以灵活地创建对各种方法的构造函数引用，因为它是通用的。因为 Plane 类和 Automobile 类的构造函数匹配 `FuncInt.func()` 的方法签名，所以它们可作为 `FuncInt.func()` 的方法引用使用。`factory()` 通过调用 `obj.func(x,y,z)` 返回类的一个实例，这是一个构造函数方法引用，当求值时，它将为你提供指定为其参数的类的一个实例。

Wrestle with this one for a while — It’s a VERY useful addition to Java ;)

斟酌这个问题一段时间，会发现它是Java的一个非常有用的补充
