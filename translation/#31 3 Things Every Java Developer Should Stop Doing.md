## 3 Things Every Java Developer Should Stop Doing（Java 开发者应该停止的 3 种不良习惯）

> 转译自：https://dzone.com/articles/3-things-every-java-developer-should-stop-doing

> Looking for a few bad habits to drop? Let's take a look at null, functional programming, and getters and setters to see how you can improve your coding.

前言：想改掉一些坏习惯吗？让我们从 null、函数式编程以及 getter 和 setter 着手，看看如何改善代码。

From returning null values to overusing getters and setters, there are idioms that we as Java developers are accustom to making, even when unwarranted. While they may be appropriate in some occasions, they are usually forces of habit or fallbacks that we make to get the system working. In this article, we will go through three things that are common among Java developers, both novice and advanced, and explore how they can get us into trouble. It should be noted that these are not hard-and-fast rules that should always be adhered to, regardless of the circumstances. At times, there may be a good reason to use these patterns to solve a problem, but on the whole, they should be used a lot less than they are now. To start us off, we will begin with one of the most prolific, but double-edged keywords in Java: Null.

作为 Java 开发人员，我们会使用一些习惯用法，典型的例子，如：返回 null 值、滥用 getter 和 setter，即使在没有必要的情况下也是如此。虽然在某些情况下，这些用法可能是适当的，但通常是习惯使然，或者是我们为了让系统正常工作的权宜之计。在本文中，我们将讨论在 Java 初学者甚至高级开发人员中都常见的三种情况，并探究它们是如何给我们带来麻烦的。应该指出的是，文中总结的规则并不是无论何时都应该始终遵守的硬性要求。有时候，可能有一个很好的理由来使用这些模式解决问题，但是总的来说，还是应该相对的减少这些用法。首先，我们将从 Null 这个关键字开始讨论，它也是 Java 中使用最频繁、但也是最具两面性的关键字之一。

### 1. Returning Null（返回 Null）
Null has been the best friend and worst enemy of developers for decades and null in Java is no different. In high-performance applications, null can be a solid means of reducing the number of objects and signaling that a method does not have a value to return. In contrast to throwing an exception, which has to capture the entire stack trace when it is created, null serves as a quick and low-overhead way to signal clients that no value can be obtained.

null 一直是开发者最好的朋友，也是最大的敌人，这在 Java 中也不例外。在高性能应用中，使用 null 是一种减少对象数量的可靠方法，它表明方法没有要返回的值。与抛出异常不同，如果要通知客户端不能获取任何值，使用 null 是一种快速且低开销的方法，它不需要捕获整个堆栈跟踪。

Outside the context of high-performance systems, null can wreak havoc in an application by creating more tedious checks for null return values and causing NullPointerExceptions when dereferencing a null object. In most applications, nulls are returned for three primary reasons: (1) to denote no elements could be found for a list, (2) to signal that no valid value could be found, even if an error did not occur, or (3) to denote a special case return value.

在高性能系统的环境之外，null 的存在会导致创建更繁琐的 null 返回值检查，从而破坏应用程序，并在解引用空对象时导致 NullPointerExceptions。在大多数应用程序中，返回 null 有三个主要原因：（1）表示列表中找不到元素；（2）表示即使没有发生错误，也找不到有效值;（3）表示特殊情况下的返回值。

Barring any performance reasons, each of these cases has a much better solution which does not use null and force developers to handle null cases. Whatsmore, clients of these methods are not left scratching their heads wondering if the method will return a null in some edge case. In each case, we will devise a cleaner approach that does not involve returning a null value.

除非有任何性能方面的原因，否则以上每一种情况都有更好的解决方案，它们不使用 null，并且强制开发人员处理出现 null 的情况。更重要的是，这些方法的客户端不会为该方法是否会在某些边缘情况下返回 null 而伤脑筋。在每种情况下，我们将设计一种不返回 null 值的简洁方法。

#### No Elements（集合中没有元素的情况）
When returning lists or other collections, it can be common to see a null collection returned in order to signal that elements for that collection could not be found. For example, we could create a service that manages users in a database that resembles the following (some method and class definitions have been left out for brevity):

在返回列表或其他集合时，通常会看到返回空集合，以表明无法找到该集合的元素。例如，我们可以创建一个服务来管理数据库中的用户，该服务类似于以下内容（为了简洁起见，省略了一些方法和类定义）：

```Java
public class UserService {
    public List<User> getUsers() {
        User[] usersFromDb = getUsersFromDatabase();
        if (usersFromDb == null) {
            // No users found in database
            return null;
        }
        else {
            return Arrays.asList(usersFromDb);
        }
    }
}
UserServer service = new UserService();
List<Users> users = service.getUsers();
if (users != null) {
    for (User user: users) {
        System.out.println("User found: " + user.getName());
    }
}
```

Since we have elected to return a null value in the case of no users, we are forcing our client to handle this case before iterating over the list of users. If instead, we returned an empty list to denote no users were found, the client can remove the null check entirely and loop through the users as normal. If there are no users, the loop will be skipped implicitly without having to manually handle that case; in essence, looping through the list of users functions as we intend for both an empty and populated list without having to manually handle one case or the other:

因为我们选择在没有用户的情况下返回 null 值，所以我们迫使客户端在遍历用户列表之前先处理这种情况。如果我们返回一个空列表来表示没有找到用户，那么客户端可以完全删除空检查并像往常一样遍历用户。如果没有用户，则隐式跳过循环，而不必手动处理这种情况；从本质上说，循环遍历用户列表的功能就像我们为空列表和填充列表所做的那样，而不需要手动处理任何一种情况：

```Java
public class UserService {
    public List<User> getUsers() {
        User[] usersFromDb = getUsersFromDatabase();
        if (usersFromDb == null) {
            // No users found in database
            return Collections.emptyList();
        }
        else {
            return Arrays.asList(usersFromDb);
        }
    }
}
UserServer service = new UserService();
List<Users> users = service.getUsers();
for (User user: users) {
    System.out.println("User found: " + user.getName());
}
```

In the case above, we have elected to return an immutable, empty list. This is an acceptable solution, so long as we document that the list is immutable and should not be modified (doing so may throw an exception). If the list must be mutable, we can return an empty, mutable list, as in the following example:

在上面的例子中，我们返回的是一个不可变的空列表。这是一个可接受的解决方案，只要我们记录该列表是不可变的并且不应该被修改（这样做可能会抛出异常）。如果列表必须是可变的，我们可以返回一个空的可变列表，如下例所示：

```Java
public List<User> getUsers() {
    User[] usersFromDb = getUsersFromDatabase();
    if (usersFromDb == null) {
        // No users found in database
        return new ArrayList<>();    // A mutable list
    }
    else {
        return Arrays.asList(usersFromDb);
    }
}
```

In general, the following rule should be adhered to when signaling that no elements could be found:

一般来说，当没有发现任何元素的时候，应遵守以下规则：

**Return an empty collection (or list, set, queue, etc.) to denote that no elements can be found**

返回一个空集合（或 list、set、queue 等等）表明找不到元素。

Doing so not only reduces the special-case handling that clients must perform, but it also reduces the inconsistencies in our interface (i.e. we return a list object sometimes and not others).

这样做不仅减少了客户端必须执行的特殊情况处理，而且还减少了接口中的不一致性（例如，我们常常返回一个 list 对象，而不是其他对象）。

#### Optional Value（可选值）
Many times, null values are returned when we wish to inform a client that an optional value is not present, but no error has occurred. For example, getting a parameter from a web address. In some cases, the parameter may be present, but in other cases, it may not. The lack of this parameter does not necessarily denote an error, but rather, it denotes that the user did not want the functionality that is included when the parameter is provided (such as sorting). We can handle this by returning null if no parameter is present or the value of the parameter if one is supplied (some methods have been removed for brevity):

很多时候，我们希望在没有发生错误时通知客户端不存在可选值，此时返回 null。例如，从 web 地址获取参数。在某些情况下，参数可能存在，但在其他情况下，它可能不存在。缺少此参数并不一定表示错误，而是表示用户不需要提供该参数时包含的功能（例如排序）。如果没有参数，则返回 null；如果提供了参数，则返回参数值（为了简洁起见，删除了一些方法）：

```Java
public class UserListUrl {
    private final String url;
    public UserListUrl(String url) {
        this.url = url;
    }
    public String getSortingValue() {
        if (urlContainsSortParameter(url)) {
            return extractSortParameter(url);
        }
        else {
            return null;
        }
    }
}
UserService userService = new UserService();
UserListUrl url = new UserListUrl("http://localhost/api/v2/users");
String sortingParam = url.getSortingValue();
if (sortingParam != null) {
    UserSorter sorter = UserSorter.fromParameter(sortingParam);
    return userService.getUsers(sorter);
}
else {
    return userService.getUsers();
}
```

When no parameter is supplied, a null is returned and a client must handle this case, but nowhere in the signature of the getSortingValue method does it state that the sorting value is optional. For us to know that this method is optional and may return a null if no parameter is present, we would have to read the documentation associated with the method (if any were provided).

当没有提供参数时，返回 null，客户端必须处理这种情况，但是在 getSortingValue 方法的签名中，没有任何地方声明排序值是可选的。如果方法的参数是可选的，并且在没有参数时，可能返回 null，要知道这个事实，我们必须阅读与该方法相关的文档（如果提供了文档）。

Instead, we can make the optionality explicit returning an Optional object. As we will see, the client still has to handle the case when no parameter is present, but now that requirement is made explicit. Whatsmore, the Optional class provides more mechanisms to handle a missing parameter than a simple null check. For example, we can simply check for the presence of the parameter using the query method (a state-testing method) provided by Optional:

相反，我们可以使可选性显式地返回一个 Optional 对象。正如我们将看到的，当没有参数存在时，客户端仍然需要处理这种情况，但是现在这个需求已经明确了。更重要的是，Optional 类提供了比简单的 null 检查更多的机制来处理丢失的参数。例如，我们可以使用 Optional 类提供的查询方法（一种状态测试方法）简单地检查参数是否存在:

```Java
public class UserListUrl {
    private final String url;
    public UserListUrl(String url) {
        this.url = url;
    }
    public Optional<String> getSortingValue() {
        if (urlContainsSortParameter(url)) {
            return Optional.of(extractSortParameter(url));
        }
        else {
            return Optional.empty();
        }
    }
}
UserService userService = new UserService();
UserListUrl url = new UserListUrl("http://localhost/api/v2/users");
Optional<String> sortingParam = url.getSortingValue();
if (sortingParam.isPresent()) {
    UserSorter sorter = UserSorter.fromParameter(sortingParam.get());
    return userService.getUsers(sorter);
}
else {
    return userService.getUsers();
}
```

This is nearly identical to that of the null-check case, but we have made the optionality of the parameter explicit (i.e. the client cannot access the parameter without calling get(), which will throw a NoSuchElementException if the optional is empty). If we were not interested in returning the list of users based on the optional parameter in the web address, but rather, consuming the parameter in some manner, we could use the ifPresentOrElse method to do so:

这与「空检查」的情况几乎相同，但是我们已经明确了参数的可选性（即客户机在不调用 `get()` 的情况下无法访问参数，如果可选参数为空，则会抛出NoSuchElementException）。如果我们不希望根据 web 地址中的可选参数返回用户列表，而是以某种方式使用该参数，我们可以使用 ifPresentOrElse 方法来这样做：

```Java
sortingParam.ifPresentOrElse(
    param -> System.out.println("Parameter is :" + param),
    () -> System.out.println("No parameter supplied.")
);
```

This greatly reduces the noise required for null checking. If we wished to disregard the parameter if no parameter is supplied, we could do so using the ifPresent method:

这极大降低了「空检查」的影响。如果我们希望在没有提供参数时忽略参数，可以使用 ifPresent 方法:

```Java
sortingParam.ifPresent(param -> System.out.println("Parameter is :" + param));
```

In either case, using an Optional object, rather than returning null, explicitly forces clients to handle the case that a return value may not be present and provides many more avenues for handling this optional value. Taking this into account, we can devise the following rule:

在这两种情况下，使用 Optional 对象要优于返回 null 以及显式地强制客户端处理返回值可能不存在的情况，为处理这个可选值提供了更多的途径。考虑到这一点，我们可以制定以下规则：

**If a return value is optional, ensure clients handle this case by returning an Optional that contains a value if one is found and is empty if no value can be found**

**如果返回值是可选的，则通过返回一个 Optional 来确保客户端处理这种情况，该可选的值在找到值时包含一个值，在找不到值时为空**

### Special-Case Value（特殊情况值）
The last common use case is that of a special case, where a normal value cannot be obtained and a client should handle a corner case different than the others. For example, suppose we have a command factory from which clients periodically request commands to complete. If no command is ready to be completed, the client should wait 1 second before asking again. We can accomplish this by returning a null command, which clients must handle, as illustrated in the example below (some methods are not shown for brevity):

最后一个常见用例是特殊用例，在这种情况下无法获得正常值，客户端应该处理与其他用例不同的极端情况。例如，假设我们有一个命令工厂，客户端定期从命令工厂请求命令。如果没有命令可以获得，客户端应该等待 1 秒钟再请求。我们可以通过返回一个空命令来实现这一点，客户端必须处理这个空命令，如下面的例子所示（为了简洁起见，没有显示一些方法）：

```Java
public interface Command {
    public void execute();
}
public class ReadCommand implements Command {
    @Override
    public void execute() {
        System.out.println("Read");
    }
}
public class WriteCommand implements Command {
    @Override
    public void execute() {
        System.out.println("Write");
    }
}
public class CommandFactory {
    public Command getCommand() {
        if (shouldRead()) {
            return new ReadCommand();
        }
        else if (shouldWrite()) {
            return new WriteCommand();
        }
        else {
            return null;
        }
    }
}
CommandFactory factory = new CommandFactory();
while (true) {
    Command command = factory.getCommand();
    if (command != null) {
        command.execute();
    }
    else {
        Thread.sleep(1000);
    }
}
```

Since the CommandFactory can return null commands, clients are obligated to check if the command received is null and if it is, sleep for 1 second. This creates a set of conditional logic that clients must handle on their own. We can reduce this overhead by creating a null-object (sometimes called a special-case object). A null-object encapsulates the logic that would have been executed in the null scenario (namely, sleeping for 1 second) into an object that is returned in the null case. For our command example, this means creating a SleepCommand that sleeps when executed:

由于 CommandFactory 可以返回空命令，客户端有义务检查接收到的命令是否为空，如果为空，则休眠1秒。这将创建一组必须由客户端自行处理的条件逻辑。我们可以通过创建一个「空对象」（有时称为特殊情况对象）来减少这种开销。「空对象」将在 null 场景中执行的逻辑（休眠 1 秒）封装到 null 情况下返回的对象中。对于我们的命令示例，这意味着创建一个在执行时休眠的 SleepCommand：

```Java
public class SleepCommand implements Command {
    @Override
    public void execute() {
        Thread.sleep(1000);
    }
}
public class CommandFactory {
    public Command getCommand() {
        if (shouldRead()) {
            return new ReadCommand();
        }
        else if (shouldWrite()) {
            return new WriteCommand();
        }
        else {
            return new SleepCommand();
        }
    }
}
CommandFactory factory = new CommandFactory();
while (true) {
    Command command = factory.getCommand();
    command.execute();
}
```

As with the case of returning empty collections, creating a null-object allows clients to implicitly handle special cases as if they were the normal case. This is not always possible, though; there may be instances where the decision for dealing with a special case must be made by the client. This can be handled by allowing the client to supply a default value, as is done with the Optional class. In the case of Optional, clients can obtain the contained value or a default using the orElse method:

与返回空集合的情况一样，创建「空对象」允许客户端隐式处理特殊情况，就像它们是正常情况一样。但这并不总是可行的；在某些情况下，处理特殊情况的决定必须由客户做出。这可以通过允许客户端提供默认值来处理，就像使用 Optional 类一样。在 Optional 的情况下，客户端可以使用 orElse 方法获取包含的值或默认值：

```Java
UserListUrl url = new UserListUrl("http://localhost/api/v2/users");
Optional<String> sortingParam = url.getSortingValue();
String sort = sortingParam.orElse("ASC");
```

If there is a supplied sorting parameter (i.e. if the Optional contains a value), this value will be returned. If no value exists, "ASC" will be returned by default. The Optional class also allows a client to create a default value when needed, in case the default creation process is expensive (i.e. the default will be created only when needed):

如果有一个提供的排序参数（例如，如果 Optional 包含一个值），这个值将被返回。如果不存在值，默认情况下将返回「ASC」。Optional 类还允许客户端在需要时创建默认值，以防默认创建过程开销较大（即只在需要时创建默认值）:

```Java
UserListUrl url = new UserListUrl("http://localhost/api/v2/users");
Optional<String> sortingParam = url.getSortingValue();
String sort = sortingParam.orElseGet(() -> {
    // Expensive computation
});
```

Using a combination of null-objects and default values, we can devise the following rule:

结合「空对象」和默认值的用法，我们可以设计以下规则：

**When possible, handle null cases with a null-object or allow clients to supply a default value**

如果可能，使用「空对象」处理使用 null 关键字的情况，或者允许客户端提供默认值

### 2. Defaulting to Functional Programming（默认使用函数式编程）
Since streams and lambdas were introduced in Java Development Kit (JDK) 8, there has been a push to migrate towards functional programming, and rightly so. Before lambdas and streams, performing simple functional tasks were cumbersome and resulted in severely unreadable code. For example, filtering a collection in the traditional style resulted in code that resembled the following:

自从在 JDK 8 中引入了 stream 和 lambda 表达式之后，就出现了向函数式编程迁移的趋势，这理当如此。在 lambda 表达式和 stream 出现之前，执行函数式任务是非常麻烦的，并且会导致代码可读性的严重下降。例如，如下代码用传统方式过滤一个集合：

```Java
public class Foo {
    private final int value;
    public Foo(int value) {
        this.value = value;
    }
    public int getValue() {
        return value;
    }
}
Iterator<Foo> iterator = foos.iterator();
while(iterator.hasNext()) {
    if (iterator.next().getValue() > 10) {
        iterator.remove();
    }
}
```

While this code is compact, it does not tell us in an obvious way that we are trying to remove elements of a collection if some criterion is satisfied. Instead, it tells us that we are iterating over a collection while there are more elements in the collection and removing each element if its value is greater than 10 (we can surmise that filtering is occurring, but it obscured in the verbosity of the code). We can shrink this logic down to one statement using functional programming:

虽然这段代码很紧凑，但它并没有以一种明显的方式告诉我们，当满足某个条件时，我们将尝试删除集合的元素。相反，它告诉我们，当集合中有更多的元素时将遍历集合，并将删除值大于 10 的元素（我们可以假设正在进行筛选，但是删除元素的部分被代码的冗长所掩盖）。我们可以使用函数式编程将这个逻辑压缩为一条语句：

```Java
foos.removeIf(foo -> foo.getValue() > 10);
```

Not only is this statement much more concise than its iterative alternative, it also tells us exactly what it is trying to do. We can even make it more readable if we name the predicate and pass it to the removeIf method:

这个语句不仅比迭代方式更简洁，而且准确的告诉我们它的行为。如果我们为 predicate 命名并将其传递给 removeIf 方法，甚至可以使其更具可读性：

```Java
Predicate<Foo> valueGreaterThan10 = foo -> foo.getValue() > 10;
foos.removeIf(valueGreaterThan10);
```

The final line of this snippet reads like a sentence in English, informing us exactly of what the statement is doing. With code that looks so compact and readable, it is tempting to try and use functional programming in every situation where iteration is required, but this is a naive philosophy. Not every situation lends itself to functional programming. For example, if we tried to print the cross product of the set of suits and ranks in a deck of cards (every combination of suits and ranks), we could create the following (see Effective Java, 3rd Edition for a more detailed listing of this example):

这段代码的最后一行读起来像一个英语句子，准确地告诉我们语句在做什么。对于看起来如此紧凑和极具可读性的代码，在任何需要迭代的情况下尝试使用函数式编程是很让人向往的，但这是一种天真的想法。并不是每种情况都适合函数式编程。例如，如果我们尝试在一副牌中打印一组花色和牌面大小的排列组合（花色和牌面大小的每一种组合），我们可以创建以下内容（参见《Effective Java, 3rd Edition》获得这个示例的详细内容）：

```Java
public static enum Suit {
    CLUB, DIAMOND, HEART, SPADE;
}
public static enum Rank {
    ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING;
}
Collection<Suit> suits = EnumSet.allOf(Suit.class);
Collection<Rank> ranks = EnumSet.allOf(Rank.class);
suits.stream()
    .forEach(suit -> {
        ranks.stream().forEach(rank -> System.out.println("Suit: " + suit + ", rank: " + rank));
    });
```

While this is not over-complicated to read, it is not the most straightforward implementation we could devise. It is pretty clear that we are trying to force streams into a realm where traditional iteration is much more favorable. If we used traditional iteration, we could have simplified the cross product of suits and ranks to the following:

虽然读起来并不复杂，但这种实现并不是最简单的。很明显，我们正试图强行使用 stream，而此时使用传统迭代明显更有利。如果我们使用传统的迭代方法，我们可以将 花色和等级的排列组合简化为：

```Java
for (Suit suit: suits) {
    for (Rank rank: ranks) {
        System.out.println("Suit: " + suit + ", rank: " + rank);
    }
}
```

This style, although much less flashy, is much more straightforward. We can quickly see that we are attempting to iterate over each suit and rank and pair each rank with each suit. The tediousness of functional programming becomes much more acute the larger the stream expression becomes. Take for example the following code snippet created by Joshua Bloch in Effective Java, 3rd Edition (pp. 205, Item 45) to find all the anagrams over a specified length contained in a dictionary at the path supplied by the user:

这种风格虽然不那么浮华，但却直截了当得多。我们可以很快地理解，我们试图遍历每个花色和等级，并将每个等级与每个花色配对。stream 表达式越大，函数式编程的乏味性就越明显。以 Joshua Bloch 在《Effective Java, 3rd Edition》第 205 页，第 45 项中创建的以下代码片段为例，在用户提供的路径上查找字典中包含的指定长度内的所有词组：

```js
public class Anagrams {
    public static void main(String[] args) throws IOException {
        Path dictionary = Paths.get(args[0]);
        int minGroupSize = Integer.parseInt(args[1]);
        try (Stream<String> words = Files.lines(dictionary)) {
            words.collect(
                groupingBy(word -> word.chars().sorted()
                           .collect(StringBuilder::new,
                               (sb, c) -> sb.append((char) c),
                               StringBuilder::append).toString()))
                .values().stream()
                    .filter(group -> group.size() >= minGroupSize)
                    .map(group -> group.size() + ": " + group)
                    .forEach(System.out::println);
        }
    }
}
```

Even the most seasoned stream adherents would probably balk at this implementation. It is unclear as to the intention of the code and would take a decent amount of thinking to uncover what the above stream manipulations are trying to accomplish. This does not mean that streams are complicated or that they are too wordy, but they are not always the best choice. As we saw above, using the removeIf reduced a complicated group of statements into a single, easily-comprehensible statement. Therefore, we should not try to replace every instance of traditional iteration with streams or even lambdas. Instead, we should abide by the following rule when deciding whether to functional programming or use the traditional route:

即使是经验最丰富的 stream 使用者也可能会对这个实现感到迷茫。短时间内很难理解代码的意图，需要大量的思考才能发现上面的 stream 操作试图实现什么。这并不意味着 stream 一定很复杂或太冗长，只是因为它们不总是最好的选择。正如我们在上面看到的，使用 removeIf 可以将一组复杂的语句简化为一个易于理解的语句。因此，我们不应该试图用 stream 甚至 lambda 表达式替换传统迭代的每个使用场景。相反，在决定是使用函数式编程还是使用传统方式时，我们应该遵循以下规则：

**Functional programming and traditional iteration both have their benefits and disadvantages: Use whichever results in the simplest and most readable code**

**函数式编程和传统的迭代都有其优点和缺点：应该以简易性和可读性为准来选择**

Although it may be tempting to use the flashiest, most up-to-date features of Java in every possible scenario, this is not always the best route. Sometimes, the old-school features work best.

尽管在每个可能的场景中使用 Java 最炫、最新的特性可能很让人向往，但这并不总是最好的方法。有时候，老式的功能效果反而最好。

### 3. Creating Indiscriminate Getters and Setters（滥用 getter 和 setter）
One of the first things that novice programmers are taught is to encapsulate the data associated with a class in private fields and expose them through public methods. In practice, this results in creating getters to access the private data of a class and setters to modify the private data of a class:

新手程序员学到的第一件事是将与类相关的数据封装在私有字段中，并通过公共方法暴露它们。在实际使用时，通过创建 getter 来访问类的私有数据，创建 setter 来修改类的私有数据：

```Java
public class Foo {
    private int value;
    public void setValue(int value) {
        this.value = value;
    }
    public int getValue() {
        return value;
    }
}
```

While this is a great practice for newer programmers to learn, it is not a practice that should go unrefined into intermediate or advanced programming. What normally occurs in practice is that every private field is given a pair of getters and setters, exposing the internals of the class to external entities. This can cause some serious issues, especially if the private fields are mutable. This is not only a problem with setters but even when only a getter is present. Take for example the following class, which exposes its only field using a getter:

虽然这对于新程序员来说是一个很好的学习实践，但这种做法不能未经思索就应用在中级或高级编程。在实际中通常发生的情况是，每个私有字段都有一对 getter 和 setter 将类的内部内容暴露给外部实体。这会导致一些严重的问题，特别是在私有字段是可变的情况下。这不仅是 setter 的问题，甚至在只有 getter 时也是如此。以下面的类为例，该类使用 getter 公开其唯一的字段：

```Java
public class Bar {
    private Foo foo;
    public Bar(Foo foo) {
        this.foo = foo;
    }
    public Foo getFoo() {
        return foo;
    }
}
```

This exposure may seem innocuous since we have wisely restricted removed a setter method, but it is far from it. Suppose that another class accesses an object of type Bar and changes the underlying value of Foo without the Bar object knowing:

由于我们删除了 setter 方法，这么做可能看起来明智且无害，但并非如此。假设另一个类访问 Bar 类型的对象，并在 Bar 对象不知道的情况下更改 Foo 的底层值：

```Java
Foo foo = new Foo();
Bar bar = new Bar(foo);
// Another place in the code
bar.getFoo().setValue(-1);
```

In this case, we have changed the underlying value of the Foo object without informing the Bar object. This can cause some serious problems if the value that we provided the Foo object breaks an invariant of the Bar object. For example, if we had an invariant that stated the value of Foo could not be negative, then the above snippet silently breaks this invariant without notifying the Bar object. When the Bar object goes to use the value of its Foo object, things may go south very quickly, especially if the Bar object assumed that the invariant held since it did not expose a setter to directly reassign the Foo object it held. This can even cause failure to a system if data is severely altered, as in the following example of an array being inadvertently exposed:

在本例中，我们更改了 Foo 对象的底层值，而没有通知 Bar 对象。如果我们提供的 Foo 对象的值破坏了 Bar 对象的一个不变量，这可能会导致一些严重的问题。举个例子，如果我们有一个不变量，它表示 Foo 的值不可能是负的，那么上面的代码片段将在不通知 Bar 对象的情况下静默修改这个不变量。当 Bar 对象使用它的 Foo 对象值时，事情可能会迅速向不好的方向发展，尤其是如果 Bar 对象假设这是不变的，因为它没有暴露 setter 直接重新分配它所保存的 Foo 对象。如果数据被严重更改，这甚至会导致系统失败，如下面例子所示，数组的底层数据在无意中暴露：

```Java
public class ArrayReader {
    private String[] array;
    public String[] getArray() {
        return array;
    }
    public void setArray(String[] array) {
        this.array = array;
    }
    public void read() {
        for (String e: array) {
            System.out.println(e);
        }
    }
}

public class Reader {
    private ArrayReader arrayReader;
    public Reader(ArrayReader arrayReader) {
        this.arrayReader = arrayReader;
    }
    public ArrayReader getArrayReader() {
        return arrayReader;
    }
    public void read() {
        arrayReader.read();
    }
}

ArrayReader arrayReader = new ArrayReader();
arrayReader.setArray(new String[] {"hello", "world"});
Reader reader = new Reader(arrayReader);
reader.getArrayReader().setArray(null);
reader.read();
```

Executing this code would cause a NullPointerException because the array associated with the ArrayReader object is null when it tries to iterate over the array. What is disturbing about this NullPointerException is that it can occur long after the change to the ArrayReader was made and maybe even in an entirely different context (such as in a different part of the code or maybe even in a different thread), making the task of tracking down the problem very difficult.

执行此代码将导致 NullPointerException，因为当 ArrayReader 的实例对象试图遍历数组时，与该对象关联的数组为 null。这个 NullPointerException 的令人不安之处在于，它可能在对 ArrayReader 进行更改很久之后才发生，甚至可能发生在完全不同的场景中（例如在代码的不同部分中，甚至在不同的线程中），这使得调试变得非常困难。

The astute reader may also notice that we could have made the private ArrayReader field final since we did not expose a way to reassign it after it has been set through the constructor. Although it might seem that this would make the ArrayReader constant, ensuring that the ArrayReader object we return cannot be changed, this is not the case. Instead, adding final to a field only ensures that the field itself is not reassigned (i.e. we cannot create a setter for that field). It does not stop the state of the object itself from being changed. If we tried to add final to the getter method, this is futile as well, since final modifier on a method only means that the method cannot be overridden by subclasses.

读者如果仔细考虑，可能还会注意到，我们可以将私有的 ArrayReader 字段设置为 final，因为我们在通过构造函数赋值之后，没有对它重新赋值的方法。虽然这看起来会使 ArrayReader 成为常量，确保我们返回的 ArrayReader 对象不会被更改，但事实并非如此。如果将 final 添加到字段中只能确保字段本身没有重新赋值（即，不能为该字段创建 setter）而不会阻止对象本身的状态被更改。或者我们试图将 final 添加到 getter 方法中，这也是徒劳的，因为方法上的 final 修饰符只意味着该方法不能被子类重写。

We can even go one step further and defensively copy the ArrayReader object in the constructor of Reader, ensuring that the object that was passed into the object cannot be tampered with after it has been supplied to the Reader object. For example, the following cannot happen:

我们甚至可以更进一步考虑，在 Reader 的构造函数中防御性地复制 ArrayReader 对象，确保在将对象提供给 Reader 对象之后，传入该对象的对象不会被篡改。例如，应避免以下情况发生：

```Java
ArrayReader arrayReader = new ArrayReader();
arrayReader.setArray(new String[] {"hello", "world"});
Reader reader = new Reader(arrayReader);
arrayReader.setArray(null);    // Change arrayReader after supplying it to Reader
reader.read();    // NullPointerException thrown
```

Even with these three changes (the final modifier on the field, the final modifier on the getter, and the defensive copy of the ArrayReader supplied to the constructor), we still have not solved the problem. The problem is not found in how we are exposing the underlying data of our class, but in the fact that we are doing it in the first place. For us to solve this issue, we have to stop exposing the internal data of our class and instead provide a method to change the underlying data, while still adhering to the class invariants. The following code solves this problem, while at the same time introducing a defensive copy of the supplied ArrayReader and marking the ArrayReader field final, as should be the case since there is no setter:

即使有了这三个更改（字段上增加 final 修饰符、getter 上增加 final 修饰符以及提供给构造函数的 ArrayReader 的防御性副本），我们仍然没有解决问题。问题不在于我们暴露底层数据的方式，而是因为我们是在一开始就是错的。要解决这个问题，我们必须停止公开类的内部数据，而是提供一种方法来更改底层数据，同时仍然遵循类不变量。下面的代码解决了这个问题，同时引入了提供的 ArrayReader 的防御性副本，并将 ArrayReader 字段标记为 final，因为没有 setter，所以应该是这样：

**译注：原文的如下代码有一处错误，Reader 类中的 setArrayReaderArray 方法返回值类型应为 void，该方法是为了取代 setter，不应产生返回值。**

```Java
public class ArrayReader {
    public static ArrayReader copy(ArrayReader other) {
        ArrayReader copy = new ArrayReader();
        String[] originalArray = other.getArray();
        copy.setArray(Arrays.copyOf(originalArray, originalArray.length));
        return copy;
    }
    // ... Existing class ...
}

public class Reader {
    private final ArrayReader arrayReader;
    public Reader(ArrayReader arrayReader) {
        this.arrayReader = ArrayReader.copy(arrayReader);
    }
    public ArrayReader setArrayReaderArray(String[] array) {
        arrayReader.setArray(Objects.requireNonNull(array));
    }
    public void read() {
        arrayReader.read();
    }
}

ArrayReader arrayReader = new ArrayReader();
arrayReader.setArray(new String[] {"hello", "world"});
Reader reader = new Reader(arrayReader);
reader.read();
Reader flawedReader = new Reader(arrayReader);
flawedReader.setArrayReaderArray(null);    // NullPointerException thrown
```

If we look at the flawed reader, a NullPointerException is still thrown, but it is thrown immediately when the invariant (that a non-null array is used when reading) is broken, not at some later time. This ensures that the invariant fails-fast, which makes debugging and finding the root of the problem much easier.

如果我们查看这个有缺陷的读取器，它仍然会抛出 NullPointerException，但在不变量（读取时使用非空数组）被破坏时，会立即抛出该异常，而不是在稍后的某个时间。这确保了不变量的快速失效，这使得调试和找到问题的根源变得容易得多。

We can take this principle one step further and state that it is a good idea to make the fields of a class completely inaccessible if there is no pressing need to allow for the state of a class to be changed. For example, we could make the Reader class fully encapsulated by removing any methods that modify its state after creation:

我们可以进一步利用这一原则。如果不迫切需要更改类的状态，那么让类的字段完全不可访问是一个好主意。例如，我们可以删除所有能够修改 Reader 类实例对象状态的方法，实现 Reader 类的完全封装：

```Java
public class Reader {
    private final ArrayReader arrayReader;
    public Reader(ArrayReader arrayReader) {
        this.arrayReader = ArrayReader.copy(arrayReader);
    }
    public void read() {
        arrayReader.read();
    }
}

ArrayReader arrayReader = new ArrayReader();
arrayReader.setArray(new String[] {"hello", "world"});
Reader reader = new Reader(arrayReader);
// No changes can be made to the Reader after instantiation
reader.read();
```

Taking this concept to its logical conclusion, it is a good idea to make a class immutable if it is possible. Thus, the state of the object never changes after the object has been instantiated. For example, we can create an immutable Car object as follows:

从逻辑上总结这个概念，如果可能的话，让类不可变是一个好主意。因此，在实例化对象之后，对象的状态永远不会改变。例如，我们可以创建一个不可变的 Car 对象如下：

```Java
public class Car {
    private final String make;
    private final String model;
    public Car(String make, String model) {
        this.make = make;
        this.model = model;
    }
    public String getMake() {
        return make;
    }
    public String getModel() {
        return model;
    }
}
```

It is important to note that if the fields of the class are non-primitive, a client can modify the underlying object as we saw above. Thus, immutable objects should return defensive copies of these objects, disallowing clients to modify the internal state of the immutable object. Note, though, that defensive copying can reduce performance since a new object is created each time the getter is called. This issue should not be prematurely optimized (disregarding immutability for the promise of possible performance increases), but it should be noted. The following snippet provides an example of defensive copying for method return values:

需要注意的是，如果类的字段不是基本数据类型，客户端可以如前所述那样修改底层对象。因此，不可变对象应该返回这些对象的防御性副本，不允许客户端修改不可变对象的内部状态。但是请注意，防御性复制会降低性能，因为每次调用 getter 时都会创建一个新对象。对于这个缺陷，不应该过早地进行优化（忽视不可变性，以保证可能的性能提高），但是应该注意到这一点。下面的代码片段提供了一个方法返回值的防御性复制示例：

```Java
public class Transmission {
    private String type;
    public static Transmission copy(Transmission other) {
        Transmission copy = new Transmission();
        copy.setType(other.getType);
        return copy;
    }
    public String setType(String type) {
        this.type = type;
    }
    public String getType() {
        return type;
    }
}
public class Car {
    private final String make;
    private final String model;
    private final Transmission transmission;
    public Car(String make, String model, Transmission transmission) {
        this.make = make;
        this.model = model;
        this.transmission = Transmission.copy(transmission);
    }
    public String getMake() {
        return make;
    }
    public String getModel() {
        return model;
    }
    public Transmission getTransmission() {
        return Transmission.copy(transmission);
    }
}
```

This leaves us with the following principle:

这给我们提示了以下原则：

**Make classes immutable, unless there is a pressing need to change the state of a class. All fields of an immutable class should be marked as private and final to ensure that no reassignments are performed on the fields and no indirect access should be provided to the internal state of the fields**

**使类不可变，除非迫切需要更改类的状态。不可变类的所有字段都应该标记为 private 和 final，以确保不会对字段执行重新赋值，也不会对字段的内部状态提供间接访问**

Immutability also brings with it some very important advantages, such as the ability of the class to be easily used in a multi-threaded context (i.e. two threads can share the object without fear that one thread will alter the state of the object while the other thread is accessing that state). In general, there are many more instances that we can create immutable classes than we realize at first: Many times, we add getters or setters out of habit.

不变性还带来了一些非常重要的优点，例如类能够在多线程上下文中轻松使用（即两个线程可以共享对象，而不用担心一个线程会在另一个线程访问该状态时更改该对象的状态）。总的来说，在很多实际情况下我们可以创建不可变的类，要比我们意识到的要多很多，只是我们习惯了添加了 getter 或 setter。

### Conclusion（结论）
Many of the applications we create end up working, but in a large number of them, we introduce sneaky problems that tend to creep up at the worst possible times. In some of those cases, we do things out of convenience, or even out of habit, and pay little mind to whether these idioms are practical (or safe) in the context we use them. In this article, we delved into three of the most common of these practices, such null return values, affinity for functional programming, and careless getters and setters, along with some pragmatic alternatives. While the rules in this article should not be taken as absolute, they do provide some insight into the uncommon dangers of common practices and may help in fending off laborious errors in the future.

我们创建的许多应用程序最终都能正常工作，但是在大量应用程序中，我们无意引入的一些问题可能只会在最极端的情况下出现。在某些情况下，我们做事情是出于方便，甚至是出于习惯，而很少注意这些习惯在我们使用的场景中是否实用（或安全）。在本文中，我们深入研究了在实际应用中最常见的三种问题，如：空返回值、函数式编程的魅力、草率的 getter 和 setter，以及一些实用的替代方法。虽然本文中的规则不是绝对的，但是它们确实为一些在实际应用中遇到的罕见问题提供了见解，并可能有助于在今后避开一些费劲的问题。
