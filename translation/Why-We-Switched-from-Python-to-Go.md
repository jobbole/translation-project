# GetStream.io: Why We Switched from Python to Go
# GetStream.io：我们用 Go 替换 Python 的原因


![](https://cdn-images-1.medium.com/max/1600/1*NRRnK49Q9HuOh9r9G4L-pg.png)


Switching to a new language is always a big step, especially when only one of your team members has prior experience with that language. Early this year, we switched [Stream’s](https://getstream.io/) primary programming language from Python to Go. This post will explain some of the reasons why we decided to leave Python behind and make the switch to Go.

切换到新的编程语言始终是一件大事，尤其是在严峻的情况下：团队成员中仅有一人具备该种语言的使用经验。今年年初，我们将 [Stream’s](https://getstream.io/) 的主要编程语言从 Python 切换到了 Go。 这篇文章将给出一些理由以说明两个问题：为什么我们决定舍弃 Python？又是为什么选择了 Go？


## Reasons to Use Go

## 为什么使用 Go？

### Reason 1 — Performance

### 原因 1 - 性能

Go is extremely fast. The performance is similar to that of Java or C++. For our use case, Go is typically 30 times faster than Python. Here’s a small benchmark game comparing [Go vs Java](https://benchmarksgame.alioth.debian.org/u64q/go.html).

Go 的运行速度非常快。性能类似于 Java 或者 C++。对于我们的使用情况来说，Go 一般比 Python 快 30 倍。这里有个小型的测试游戏 [Go vs Java](https://benchmarksgame.alioth.debian.org/u64q/go.html)。

### Reason 2 — Language Performance Matters

### 原因 2 - 语言的性能很重要

For many applications, the programming language is simply the glue between the app and the database. The performance of the language itself usually doesn’t matter much.

对于很多应用来说，编程语言只是应用程序和数据库之间的粘合剂。语言本身的性能通常无关紧要。

Stream, however, is an API provider powering the feed infrastructure for 500 companies and more than 200 million end users. We’ve been optimizing Cassandra, PostgreSQL, Redis, etc. for years, but eventually, you reach the limits of the language you’re using.

然而，Stream 是一家 API 提供商，其为 500 家公司和 2 亿多终端用户提供信息流基础设施。我们一直在优化 Cassandra、PostgreSQL 和 Redis 等工具。这持续了好几年，但是最终，我们还是到达了所用语言的瓶颈。

Python is a great language but its performance is pretty sluggish for use cases such as serialization/deserialization, ranking and aggregation. We frequently ran into performance issues where Cassandra would take 1ms to retrieve the data and Python would spend the next 10ms turning it into objects.

Python 是一门很棒的语言，但是在诸如序列化/反序列化、排序以及聚合之类的场景上，它的性能相当差。我们常常遇到性能上的问题：花 1ms 的时间拿到 Cassandra 中的数据，Python 接下来还需要花 10ms 的时间将拿到的数据转换成对象。

### Reason 3 — Developer Productivity & Not Getting Too Creative

### 原因 3 - 开发人员的开发效率 & 拒绝太富有创造性

Have a look at this little snippet of Go code from the [How I Start Go tutorial](http://howistart.org/posts/go/1/). (This is a great tutorial and a good starting point to pick up a bit of Go.)

看看这些来自于 [How I Start Go tutorial](http://howistart.org/posts/go/1/) 的 Go 的代码片段。（这是一个很棒的教程，也是一个很好的学习 Go 语言的起点。）

If you’re new to Go, there’s not much that will surprise you when reading that little code snippet. It showcases multiple assignments, data structures, pointers, formatting and a built-in HTTP library.

如果你是 Go 语言的新手，在阅读那些代码片段时，没有什么会让你大吃一惊。它只是多个赋值、数据结构、指针、格式化和内置的 HTTP 库。

When I first started programming I always loved using Python’s more advanced features. Python allows you to get pretty creative with the code you’re writing. For instance, you can:

当我第一次开始编程时，我总是喜欢用 Python 比较高级的特性。Python 允许你更有“创意”的写代码。比如，你能够做如下的事：

- Use MetaClasses to self-register classes upon code initialization

- 在代码初始化时使用元类自行注册类

- Swap out True and False

- 关键字 True 和 False 的值可以互换

- Add functions to the list of built-in functions

- 编写自己的函数，并且使其成为内建函数。

- Overload operators via magic methods

- 通过魔法方法重载运算符


These features are fun to play around with but, as most programmers will agree, they often make the code harder to understand when reading someone else’s work.

这些特性很有趣，但是，正如大多数程序员都同意的那样，在阅读别人的代码时，它们的存在使得代码更难理解。

Go forces you to stick to the basics. This makes it very easy to read anyone’s code and immediately understand what’s going on.

Go 迫使你回归基础。这决定了 Go 代码是容易阅读和理解的。

Note: How “easy” it is really depends on your use case, of course. If you want to create a basic CRUD API I’d still recommend Django + [DRF](http://www.django-rest-framework.org/), or Rails.

说明：当然，“容易”的程度需要视情况而定。如果你想要创建一个基本的增删改查接口，我仍然推荐你使用 Django + [DRF](http://www.django-rest-framework.org/)，或者用 Rails。


### Reason 4 — Concurrency & Channels

### 原因 4 - 并发 & 管道

As a language, Go tries to keep things simple. It doesn’t introduce many new concepts. The focus is on creating a simple language that is incredibly fast and easy to work with. The only area where it does get innovative is goroutines and channels. (To be 100% correct the concept of [CSP](https://en.wikipedia.org/wiki/Communicating_sequential_processes) started in 1977, so this innovation is more of a new approach to an old idea.) Goroutines are Go’s lightweight approach to threading, and channels are the preferred way to communicate between goroutines.

作为一门编程语言，Go 试图让事情变得简单。它没有引入很多的新概念。重点是创造的这门编程语言的性能要难以置信的快，并且容易上手。goroutines 和管道是 Go 仅有的创新点。（如果要让 [CSP](https://en.wikipedia.org/wiki/Communicating_sequential_processes) 这个1977年提出来的概念完全准确，那不得不说，这个创新更像是一种对旧概念的新的实现方案。）Goroutines 是 Go 对线程的轻量级实现，而管道是让 goroutines 之间相互通信的绝佳的方式。

Goroutines are very cheap to create and only take a few KBs of additional memory. Because Goroutines are so light, it is possible to have hundreds or even thousands of them running at the same time.

Goroutines 占用的资源非常少，只需要几 KBs 的额外内存。因为 Goroutines 非常轻量，所以同时运行数百甚至数千个也不在话下。

You can communicate between goroutines using channels. The Go runtime handles all the complexity. The goroutines and channel-based approach to concurrency makes it very easy to use all available CPU cores and handle concurrent IO — all without complicating development. Compared to Python/Java, running a function on a goroutine requires minimal boilerplate code. You simply prepend the function call with the keyword “go”:

你可以使用管道在 goroutines 之间通信。Go 运行时会处理所有的复杂事物。goroutines 的存在以及基于管道的并发方法，使得程序可以充分利用 CPU 资源、处理并发 IO -- 所有这些都没有增加开发的复杂性。与 Python/Java 相比，在 goroutine 上运行一个函数只需要非常少的样板代码。您只需在函数调用前加上关键字“go”：

[https://tour.golang.org/concurrency/1](https://tour.golang.org/concurrency/1)

Go’s approach to concurrency is very easy to work with. It’s an interesting approach compared to Node where the developer has to pay close attention to how asynchronous code is handled.

Go 的并发方法非常容易使用。和 Node 相比，这是一个有意思的方法。如果使用 Node 写并发方法，开发者必须密切关注异步代码的处理方式。

Another great aspect of concurrency in Go is the [race detector](https://blog.golang.org/race-detector). This makes it easy to figure out if there are any race conditions within your asynchronous code.

Go 自带[竞争检测器](https://blog.golang.org/race-detector)，这是用 Go 写并发程序另一个好的方面。如果异步代码中出现条件竞争的情况，检测器能帮你轻松地找到问题。

Here are a few good resources to get started with Go and channels:

如果要学习 Go 和管道的话，下面是一些不错的资料：

- [https://blog.golang.org/race-detector](https://blog.golang.org/race-detector)

- [https://tour.golang.org/concurrency/2](https://tour.golang.org/concurrency/2)

- [http://guzalexander.com/2013/12/06/golang-channels-tutorial.html](http://guzalexander.com/2013/12/06/golang-channels-tutorial.html)

- [https://www.golang-book.com/books/intro/10](https://www.golang-book.com/books/intro/10)

- [https://www.goinggo.net/2014/02/the-nature-of-channels-in-go.html](https://www.goinggo.net/2014/02/the-nature-of-channels-in-go.html)

- [Goroutines vs Green threads](https://softwareengineering.stackexchange.com/questions/222642/are-go-langs-goroutine-pools-just-green-threads)

### Reason 5 — Fast Compile Time

### 原因 5 - 编译时间短

Our largest micro service written in Go currently takes 6 seconds to compile. Go’s fast compile times are a major productivity win compared to languages like Java and C++ which are famous for sluggish compilation speed. I like sword fighting, but it’s even nicer to get things done while I still remember what the code is supposed to do:

目前，我们使用 Go 编写的最大微服务只需 6 秒钟就能完成编译。与 Java 和 C++ 这样以低速编译速度著称的语言相比，Go 的快速编译能力是一场生产力上的大胜。我喜欢击剑（下图指利用编译的时间暂时脱离工作，从事自己的爱好，暗示编译时间慢），但是，当我还记得代码是做什么事情的时候，代码就已经完成编译了，那自然是最好的事了：

![](https://cdn-images-1.medium.com/max/1600/1*N5NJvvxy-D9TrSwXGaMsCQ.png)

### Reason 6 — The Ability to Build a Team

### 原因 6 - 创建一个团队的能力

First of all, let’s start with the obvious: there are not as many Go developers compared to older languages like C++ and Java. According to [StackOverflow](https://insights.stackoverflow.com/survey/2017), 38% of developers know Java, 19.3% know C++ and only 4.6% know Go. [GitHub data](https://madnight.github.io/githut/) shows a [similar trend](http://githut.info/): Go is more widely used than languages such as Erlang, Scala and Elixir, but less popular than Java and C++.

首先，让我们认清一个现实：与旧式的像 C++ 和 Java 这样的编程语言相比，Go 开发人员的数量是不占上风的。根据 [StackOverflow](https://insights.stackoverflow.com/survey/2017) 的数据，38% 的开发人员熟悉 Java，19.3% 的开发人员熟悉 C++，仅仅 4.6% 的开发人员熟悉 Go。[GitHub 上的数据](https://madnight.github.io/githut/)显示一个[相似的趋势](https://madnight.github.io/githut/)： Go 用得比 Erlang、Scala 以及 Elixir 广泛，但是不及 Java 和 C++。

Fortunately, Go is a very simple and easy to learn language. It provides the basic features you need and nothing else. The new concepts it introduces are the “[defer](https://blog.golang.org/defer-panic-and-recover)” statement and built-in management of concurrency with “go routines” and channels. (For the purists: Go isn’t the first language to implement these concepts, just the first to make them popular.) Any Python, Elixir, C++, Scala or Java dev that joins a team can be effective at Go within a month because of its simplicity.

幸运的是，Go 很简单，而且易于学习。它提供了你所需要的基本的特性，一点不多，一点不少。它引入了 2 个新的概念：“[defer](https://blog.golang.org/defer-panic-and-recover)”声明、“go routines” 和管道内建的并发管理。（对于纯粹主义者来说：Go 并不是第一种实现这些概念的语言，而是第一种使它们受欢迎的语言。）团队中任何地 Python、Elixir、C++、Scala 或 Java 开发人员都可以在一个月内有效地掌握 Go，因为它非常简单。

We’ve found it easier to build a team of Go developers compared to many other languages. If you’re hiring people in competitive ecosystems like [Boulder and Amsterdam](http://angel.co/stream/jobs) this is an important benefit.

我们发现，和很多其他的编程语言相比，创建一个 Go 开发团队更容易。如果你在竞争激烈的环境（如 [Boulder、Amsterdam](http://angel.co/stream/jobs)）雇佣人员，这是一大优点。

### Reason 7 — Strong Ecosystem

### 原因 7 - 强大的生态系统

For a team of our size (~20 people) the ecosystem matters. You simply can’t create value for your customers if you have to reinvent every little piece of functionality. Go has great support for the tools we use. Solid libraries were already available for Redis, RabbitMQ, PostgreSQL, Template parsing, Task scheduling, Expression parsing and RocksDB.

对于我们一个大约 20 个人的团队来说，生态系统很重要。如果你不得不重新发明每一部分的功能，你根本不可能为你的客户创造价值。Go 对我们使用的工具提供了很大的支持。比如这些可靠的库：Redis、RabbitMQ、PostgreSQL、模板解析、任务调度、表达式解析和 RocksDB。

Go’s ecosystem is a major win compared to other newer languages like Rust or Elixir. It’s of course not as good as languages like Java, Python or Node, but it’s solid and for many basic needs you’ll find high-quality packages already available.

与 Rust 或 Elixir 等其他新语言相比，Go 的生态系统是一项重大胜利。当然，Go 并不像 Java、Python 或者 Node 那样出色。但是它非常的可靠，并且对于一些基本的需求，你都可以找到高质量的包。

### Reason 8 — Gofmt, Enforced Code Formatting

### 原因 8 - Gofmt：强制代码格式化

Let’s start with what is Gofmt? And no, it’s not a swear word. Gofmt is an awesome command line utility, built into the Go compiler for formatting your code. In terms of functionality it’s very similar to Python’s autopep8. While the show Silicon Valley portrays otherwise, most of us don’t really like to argue about tabs vs spaces. It’s important that formatting is consistent, but the actual formatting standard doesn’t really matter all that much. Gofmt avoids all of this discussion by having one official way to format your code.

那么什么是 Gofmt 呢？注意，它并不是脏话。Gofmt 是一个极棒的命令行工具集，已集成到了 Go 编译器，用于格式化代码。从功能上来讲，它有点像 Python 中的 autopep8。除非是在《硅谷》电视剧中，不然大多数人并不真的喜欢争论该用 tabs 还是 spaces。格式的一致性是非常重要的，但是实际的格式标准并不是那么重要。Gofmt 提供官方的标准来格式化你的代码，从而避免了不必要的争论。

### Reason 9 — gRPC and Protocol Buffers

### 原因 9 - gRPC 与 Protocol Buffers

Go has first-class support for protocol buffers and gRPC. These two tools work very well together for building microservices which need to communicate via RPC. You only need to write a manifest where you define the RPC calls that can be made and what arguments they take. Both server and client code are then automatically generated from this manifest. This resulting code is both fast, has a very small network footprint and is easy to use.

Go 对 protocol buffers 和 gRPC 有着一流的支持。在构建需要通过 RPC 进行通信的微服务时，这两个工具可以很好地协同工作。你只需编写一个说明文件，里面只需定义可以进行的 RPC 调用以及它们采用的参数。根据这份说明文件，服务器和客户端代码就会自动生成。由此产生的代码运行快速，网络占用空间小，易于使用。

From the same manifest, you can generate client code for many different languages even, such as C++, Java, Python and Ruby. So, no more ambiguous REST endpoints for internal traffic, that you have to write almost the same client and server code for every time. 

根据相同的说明文件，甚至可以生成很多不同编程语言的客户端代码，比如 C++、Java、Python 和 Ruby。因此，内部流量不再有模糊的 REST 终端，因为你不必每次都写一遍几乎相同的客户端和服务器端代码。

## Disadvantages of Using Golang

## 使用 Golang 的缺点

### Disadvantage 1 — Lack of Frameworks

### 缺点 1 - 缺少框架

Go doesn’t have a single dominant framework like Rails for Ruby, Django for Python or Laravel for PHP. This is a topic of heated debate within the Go community, as many people advocate that you shouldn’t use a framework to begin with. I totally agree that this is true for some use cases. However, if someone wants to build a simple CRUD API they will have a much easier time with Django/DJRF, Rails Laravel or [Phoenix](http://phoenixframework.org/).

Go 没有一个具有代表性的框架，像 Ruby 有 Rails、Python 有 Django 或者 PHP 有 Laravel。在 Go 社区中，这是一个争论激烈的话题，很多人提倡不应该一开始就使用框架。某些使用案例，我完全同意这样的观点。然而，如果只是想要创建一个增删改查的接口，使用 Django/DJRF、Rails Laravel 或者 [Phoenix](http://phoenixframework.org/) 是一个更好的选择。

### Disadvantage 2 — Error Handling

### 缺点 2 - 错误处理机制

Go handles errors by simply returning an error from a function and expecting your calling code to handle the error (or to return it up the calling stack). While this approach works, it’s easy to lose scope of what went wrong to ensure you can provide a meaningful error to your users. The [errors package](https://github.com/pkg/errors) solves this problem by allowing you to add context and a stack trace to your errors.

Go 处理错误的过程如下：简单地从函数中返回错误，并且期望你调用代码来处理该错误（或者将它返回到调用堆栈之上）。虽然这种方法有效，但很容易丢失出错的范围，导致无法为用户提供有意义的错误。 [errors ](https://github.com/pkg/errors)包通过允许你为错误添加上下文和堆栈来跟踪问题。

Another issue is that it’s easy to forget to handle an error by accident. Static analysis tools like errcheck and megacheck are handy to avoid making these mistakes.

另一个问题是很容易忘记处理错误。像 errcheck 和 megacheck 这样的静态分析工具可以方便地规避这些错误。

While these workarounds work well it doesn’t feel quite right. You’d expect proper error handling to be supported by the language.

虽然这些解决方法很有效，但总感觉哪里不太对劲。 你肯定希望语言本身就支持一定的错误处理的功能。

### Disadvantage 3 — Package Management

### 缺点 3 - 包管理

Go’s package management is by no means perfect. By default, it doesn’t have a way to specify a specific version of a dependency and there’s no way to create reproducible builds. Python, Node and Ruby all have better systems for package management. However, with the right tools, Go’s package management works quite well.

Go 的包管理肯定不是完美的。默认情况下，它没有办法指定依赖项的特定版本，也没有办法创建[可重现的构建](https://en.wikipedia.org/wiki/Reproducible_builds)。 Python、Node 和 Ruby 都有更好的包管理系统。然而，通过合适的工具，Go 的包管理表现的很好。

You can use [Dep](https://github.com/golang/dep) to manage your dependencies to allow specifying and pinning versions. Apart from that, we’ve contributed an open-source tool called [VirtualGo](https://github.com/getstream/vg) which makes it easier to work on multiple projects written in Go.

你可以使用 [Dep](https://github.com/golang/dep) 来管理依赖项以允许指定和固定版本。 除此之外，我们还提供了一个叫做 [VirtualGo](https://github.com/getstream/vg) 的开源工具，它可以更轻松地处理用 Go 编写的多个项目。

![](https://cdn-images-1.medium.com/max/1600/1*OVIzfruxudBtFpzISIEriA.png)

## Python vs Go

## Python vs Go

One interesting experiment we conducted was taking our [ranked feed](https://getstream.io/docs/#custom_ranking) functionality in Python and rewriting it in Go. Have a look at this example of a ranking method:

我们之前做过一个有趣的实验：选择我们的 [ranked feed](https://getstream.io/docs/#custom_ranking) 功能，用 Go 语言将它重写。简单看下这个排名方法的例子：

Both the Python and Go code need to do the following to support this ranking method:

为了使这个排名方法成立，Python 和 Go 都需要遵循下面的事：

1.Parse the expression for the score. In this case, we want to turn this string “simple_gauss(time)*popularity” into a function that takes an activity as input and returns a score as output.

1.解析表达式以便打分。在这种情况下，我们希望将“simple_gauss（time）* popular”这个字符串转换成一个函数：函数以一个活动作为输入，然后返回一个分数作为输出。

2.Create partial functions based on the JSON config. For example, we want “simple_gauss” to call “decay_gauss” with a scale of 5 days, offset of 1 day and a decay factor of 0.3.

2.基于 JSON 配置创建偏函数。比如：我们想要“simple_gauss”调用“decay_gauss”，并传递规模为 5 天，偏差为 1 天，衰减系数为 0.3 这些参数。

3.Parse the “defaults” configuration so you have a fallback if a certain field is not defined on an activity.

3.解析“默认值”配置，以便在活动中出现未定义字段时可以进行回退。

4.Use the function from step 1 to score all activities in the feed.

4.使用步骤 1 中的函数给流中的所有活动打分。

Developing the Python version of the ranking code took roughly 3 days. That includes writing the code, unit tests and documentation. Next, we’ve spent approximately 2 weeks optimizing the code. One of the optimizations was translating the score expression (simple_gauss(time)*popularity) into an [abstract syntax tree](https://docs.python.org/3/library/ast.html). We also implemented caching logic which pre-computed the score for certain times in the future.

开发 Python 版本的排名代码大约需要 3 天。这包括编写代码、单元测试和文档书写。接下来，我们花了大约 2 周时间来优化代码。其中一个优化是将评分表达式（simple_gauss(time)*popularity）转换为抽象[语法树](https://docs.python.org/3/library/ast.html)。我们还实现了缓存逻辑，该逻辑在将来的某些时间预先计算得分。

In contrast, developing the Go version of this code took roughly 4 days. The performance didn’t require any further optimization. So while the initial bit of development was faster in Python, the Go based version ultimately required substantially less work from our team. As an added benefit, the Go code performed roughly 40 times faster than our highly-optimized Python code.

相比之下，开发该代码的 Go 版本大约需要 4 天时间。性能不需要任何进一步的优化。因此，虽然 Python 初始的开发速度更快些，但如果基于 Go 的版本，最终，我们团队的工作量大大减少。作为额外的优点，Go 代码的执行速度比我们高度优化的 Python 代码快大约 40 倍。

Now, this is just a single example of the performance gains we’ve experienced by switching to Go. It is, of course, comparing apples to oranges:

这只是一个简单的说明性能提升的例子：仅仅用 Go 替换 Python。 当然，它们没有可比性：

- The ranking code was my first project in Go

- 排名代码是我第一个用 Go 写的项目

- The Go code was built after the Python code, so the use case was better understood

- Go 代码是在 Python 代码之后构建的，因此我可以更好地理解用例

- The Go library for expression parsing was of exceptional quality

- 用于表达式解析的 Go 库是非常高质量的

Your mileage will vary. Some other components of our system took substantially more time to build in Go compared to Python. As a general trend, we see that developing Go code takes slightly more effort. However, we spend much less time optimizing the code for performance.

具体细节需要视情况而定。和 Python 相比，用 Go 构建一些我们系统中其他的组件，需要花费更多的时间。一般情况下，我们发现用 Go 开发代码更费些劲。然而，在性能方面，我们花费更少的时间来优化代码。

## Elixir vs Go — The Runner Up

## Elixir vs Go — 亚军

Another language we evaluated is [Elixir](https://elixir-lang.org/). Elixir is built on top of the Erlang virtual machine. It’s a fascinating language and we considered it since one of our team members has a ton of experience with Erlang.

我们评估了另一种语言：[Elixir](https://elixir-lang.org/)。Elixir 构建于 Erlang 虚拟机之上。这是一种引人入胜的语言。我们考虑过它，因为我们团队成员中有一个人拥有大量的 Erlang 经验。

For our use cases, we noticed that Go’s raw performance is much better. Both Go and Elixir will do a great job serving thousands of concurrent requests. However, if you look at individual request performance, Go is substantially faster for our use case. Another reason why we chose Go over Elixir was the ecosystem. For the components we required, Go had more mature libraries whereas, in many cases, the Elixir libraries weren’t ready for production usage. It’s also harder to train/find developers to work with Elixir.

对于我们的用例，我们注意到 Go 的原始性能要好得多。Go 和 Elixir 都可以很好地为数千个并发请求提供服务。但是，如果你查看单个请求的性能，Go 对我们的用例来说要快得多。生态系统是另一个我们选择 Go 而不选择 Elixir 的原因。对于我们需要的组件，Go 有更多成熟的库，而在许多情况下，Elixir 库还没有为生产使用做好准备。培训/招聘用 Elixir 的开发人员也更难。

These reasons tipped the balance in favor of Go. The Phoenix framework for Elixir looks awesome though and is definitely worth a look.

这些原因让我们选择了 Go。虽然 Elixir 的 Phoenix 框架看起来非常棒，并且也绝对值得一看。

## Conclusion

## 总结

Go is a very performant language with great support for concurrency. It is almost as fast as languages like C++ and Java. While it does take a bit more time to build things using Go compared to Python or Ruby, you’ll save a ton of time spent on optimizing the code.

Go 是一种非常高效的语言，且对并发性有很大的支持。它的性能几乎与 C++ 和 Java 等语言一样快。虽然和 Python 或 Ruby 相比，使用 Go 构建内容需要花费更多时间，但你将节省大量时间来优化代码。

We have a small development team at [Stream](https://getstream.io/team/) powering the feeds for over 200 million end users. Go’s combination of a great ecosystem, easy onboarding for new developers, fast performance, solid support for concurrency and a productive programming environment make it a great choice.

我们在 [Stream](https://getstream.io/team/) 有一个小型的开发团队，为超过2亿的终端用户提供信息流。拥有一个伟大的生态系统、新开发人员容易上手、快速的性能、对并发性的可靠支持以及高效的编程环境，使 Go 成为一个很好的选择。

Stream still leverages Python for our dashboard, site and machine learning for [personalized feeds](https://getstream.io/personalization). We won’t be saying goodbye to Python anytime soon, but going forward all performance-intensive code will be written in Go.

Stream 仍然利用 Python 为我们的控制面板、站点和机器学习提供[个性化的流](https://getstream.io/personalization)。 我们不会很快告别 Python，但是所有性能密集型代码都将用 Go 编写。

If you want to learn more about Go check out the blog posts listed below. To learn more about Stream, [this interactive tutorial](https://getstream.io/get_started/) is a great starting point.

如果你想要了解更多有关 Go，查看下面列出的博客文章。如果你想要了解 Stream，[这个互动教程](https://getstream.io/get_started/)是一个好的起点。

## More Reading about Switching to Golang

## 关于切换到 Golang 的更多阅读

- [https://movio.co/en/blog/migrate-Scala-to-Go/](https://movio.co/en/blog/migrate-Scala-to-Go/)

- [https://hackernoon.com/why-i-love-golang-90085898b4f7](https://hackernoon.com/why-i-love-golang-90085898b4f7)

- [https://sendgrid.com/blog/convince-company-go-golang/](https://sendgrid.com/blog/convince-company-go-golang/)

- [https://dave.cheney.net/2017/03/20/why-go](https://dave.cheney.net/2017/03/20/why-go)

## Learning Go

## 学习 Go

- [https://learnxinyminutes.com/docs/go/](https://learnxinyminutes.com/docs/go/)

- [https://tour.golang.org/](https://tour.golang.org/)

- [http://howistart.org/posts/go/1/](http://howistart.org/posts/go/1/)

- [https://getstream.io/blog/building-a-performant-api-using-go-and-cassandra/](https://getstream.io/blog/building-a-performant-api-using-go-and-cassandra/)

- [https://www.amazon.com/gp/product/0134190440](https://www.amazon.com/gp/product/0134190440)

> This post was originally written by Thierry Schellenbach, CEO at [GetStream.io](https://getstream.io/). The original blog post can be found at [https://getstream.io/blog/switched-python-go/](https://getstream.io/blog/switched-python-go/).

> 这篇文章最初由 Thierry Schellenbach 撰写，[GetStream.io](https://getstream.io/) 的 CEO。原始博文的地址是[https://getstream.io/blog/switched-python-go/](https://getstream.io/blog/switched-python-go/)。




