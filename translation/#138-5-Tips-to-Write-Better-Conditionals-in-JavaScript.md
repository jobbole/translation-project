## 5 Tips to Write Better Conditionals in JavaScript（优化 JavaScript 条件语句的5个技巧）

> 转译自：https://scotch.io/tutorials/5-tips-to-write-better-conditionals-in-javascript

When working with JavaScript, we deal a lot with conditionals, here are the 5 tips for you to write better / cleaner conditionals.

在使用 JavaScript 时，我们会处理很多条件语句，这里有 5 个技巧可以帮助您编写更好、更简洁的条件语句。

### 1、Use Array.includes for Multiple Criteria（对多个条件使用 Array.includes）

Let's take a look at the example below:

让我们看看下面的例子：

```
// condition
function test(fruit) {
  if (fruit == 'apple' || fruit == 'strawberry') {
    console.log('red');
  }
}
```

At first glance, the above example looks good. However, what if we get more red fruits, say cherry and cranberries? Are we going to extend the statement with more || ?

乍一看，上面的例子看起来不错。然而，如果还有更多红颜色的水果需要判断呢，比如樱桃和小红莓，我们要用更多的 || 来扩展这个表述吗？

We can rewrite the conditional above by using Array.includes (Array.includes)(https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/includes)

我们可以用 Array.includes 重写上面的条件

```
function test(fruit) {
  // extract conditions to array
  const redFruits = ['apple', 'strawberry', 'cherry', 'cranberries'];

  if (redFruits.includes(fruit)) {
    console.log('red');
  }
}
```

We extract the red fruits (conditions) to an array. By doing this, the code looks tidier.

我们将红色水果（条件）提取到一个数组中。这样做之后，代码看起来更整洁。

### 2、Less Nesting, Return Early（更少的嵌套，尽早返回）

Let's expand the previous example to include two more conditions:

让我们扩展前面的示例，以包含另外两个条件：

- if no fruit provided, throw error

如果没有提供水果（名称），抛出错误。

- accept and print the fruit quantity if exceed 10.

如果（红色水果）数量超过 10 个，接受并打印。

```
function test(fruit, quantity) {
  const redFruits = ['apple', 'strawberry', 'cherry', 'cranberries'];

  // condition 1: fruit must has value
  if (fruit) {
    // condition 2: must be red
    if (redFruits.includes(fruit)) {
      console.log('red');

      // condition 3: must be big quantity
      if (quantity > 10) {
        console.log('big quantity');
      }
    }
  } else {
    throw new Error('No fruit!');
  }
}

// test results
test(null); // error: No fruits
test('apple'); // print: red
test('apple', 20); // print: red, big quantity
```

Look at the code above, we have:

看看上面的代码，我们有：

- 1 if/else statement that filter out invalid condition

1 组过滤无效条件的 if/else 语句

- 3 levels of nested if statement (condition 1, 2 & 3)

3 层的 if 嵌套语句（条件 1、2 和 3）

A general rule I personally follow is **return early when invalid conditions** found.

我个人遵循的一般规则是，**当发现无效条件时，提前返回。**

```
/_ return early when invalid conditions found _/

function test(fruit, quantity) {
  const redFruits = ['apple', 'strawberry', 'cherry', 'cranberries'];

  // condition 1: throw error early
  if (!fruit) throw new Error('No fruit!');

  // condition 2: must be red
  if (redFruits.includes(fruit)) {
    console.log('red');

    // condition 3: must be big quantity
    if (quantity > 10) {
      console.log('big quantity');
    }
  }
}
```

By doing this, we have one less level of nested statement. This coding style is good especially when you have long if statement (imagine you need to scroll to the very bottom to know there is an else statement, not cool).

这样，我们就少了一层嵌套。这种编码风格很好，尤其是当你有很长的 if 语句时（想象一下，你需要滚动到最底部才能知道还有一个 else 语句，这并不酷）。

We can further reduce the nesting if, by inverting the conditions & return early. Look at condition 2 below to see how we do it:

通过反转条件和提早返回，我们可以进一步减少嵌套。看看下面的条件 2，我们是怎么做的：

```
/_ return early when invalid conditions found _/

function test(fruit, quantity) {
  const redFruits = ['apple', 'strawberry', 'cherry', 'cranberries'];

  if (!fruit) throw new Error('No fruit!'); // condition 1: throw error early
  if (!redFruits.includes(fruit)) return; // condition 2: stop when fruit is not red

  console.log('red');

  // condition 3: must be big quantity
  if (quantity > 10) {
    console.log('big quantity');
  }
}
```

By inverting the conditions of condition 2, our code is now free of a nested statement. This technique is useful when we have long logic to go and we want to stop further process when a condition is not fulfilled.

通过反转条件 2 的条件，我们的代码现在没有嵌套语句。当我们有很长的逻辑要处理时，这种技术是有用的，当一个条件没有满足时，我们想要停止进一步的处理。

However, that's no **hard rule** for doing this. Ask yourself, is this version (without nesting) better / more readable than the previous one (condition 2 with nested)?

然而，这并不是**严格的规则**。问问自己，这个版本（没有嵌套）是否比前一个版本（嵌套的条件 2）更好、更易读？

For me, I would just leave it as the previous version (condition 2 with nested). It is because:

对于我来说，我将把它保留为以前的版本（条件 2 和嵌套）。这是因为：

- the code is short and straight forward, it is clearer with nested if

代码简短而直接，如果嵌套，代码就更清晰了

- inverting condition may incur more thinking process (increase cognitive load)

反转条件可能会导致更多的思考过程（增加认知负担）

Therefore, always aims for Less Nesting and Return Early but don't overdo it. There is an article & StackOverflow discussion that talks further on this topic if you interested:

因此，总是以更少的嵌套及尽早返回为目标，但不要过度。如果你感兴趣的话，StackOverflow 有一篇相关的文章讨论了这个话题：

- [Avoid Else, Return Early](http://blog.timoxley.com/post/47041269194/avoid-else-return-early) by Tim Oxley

Tim Oxley 的文章，避免 Else，尽早返回

- [StackOverflow discussion](https://softwareengineering.stackexchange.com/questions/18454/should-i-return-from-a-function-early-or-use-an-if-statement) on if/else coding style

StackOverflow 基于 if/else 编码风格的讨论

### 3、Use Default Function Parameters and Destructuring（使用默认的函数参数和解构）

I guess the code below might look familiar to you, we always need to check for null / undefined value and assign default value when working with JavaScript:

我想下面的代码对您来说可能很熟悉，我们在使用 JavaScript 时总是需要检查 null 或 undefined 值并分配默认值:

```
function test(fruit, quantity) {
  if (!fruit) return;
  const q = quantity || 1; // if quantity not provided, default to one

  console.log(`We have ${q} ${fruit}!`);
}

//test results
test('banana'); // We have 1 banana!
test('apple', 2); // We have 2 apple!
```

In fact, we can eliminate the variable `q` by assigning default function parameters.

事实上，我们可以通过指定默认的函数参数来消除变量 `q`。

```
function test(fruit, quantity = 1) { // if quantity not provided, default to one
  if (!fruit) return;
  console.log(`We have ${quantity} ${fruit}!`);
}

//test results
test('banana'); // We have 1 banana!
test('apple', 2); // We have 2 apple!
```

Much easier & intuitive isn't it? Please note that each parameter can has it own [default function parameter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters). For example, we can assign default value to `fruit` too: `function test(fruit = 'unknown', quantity = 1)`.

更简单和直观，不是吗？请注意，每个参数都可以有自己的默认函数参数。例如，我们也可以为 `fruit` 赋值：`function test(fruit = 'unknown'， quantity = 1)`。

What if our `fruit` is an object? Can we assign default parameter?

如果我们的 `fruit` 是一个对象呢？我们可以指定默认参数吗？

```
function test(fruit) {
  // printing fruit name if value provided
  if (fruit && fruit.name)  {
    console.log (fruit.name);
  } else {
    console.log('unknown');
  }
}

//test results
test(undefined); // unknown
test({ }); // unknown
test({ name: 'apple', color: 'red' }); // apple
```

Look at the example above, we want to print the fruit name if it's available or we will print unknown. We can avoid the conditional fruit && fruit.name checking with default function parameter & destructing.

请看上面的示例，如果 `fruit.name` 是可用的，我们将打印该水果名称，否则我们将打印 `unknown`。我们可以避免使用与默认函数参数和解构对条件 `fruit && fruit.name` 进行检查。

```
// destructing - get name property only
// assign default empty object {}
function test({name} = {}) {
  console.log (name || 'unknown');
}

//test results
test(undefined); // unknown
test({ }); // unknown
test({ name: 'apple', color: 'red' }); // apple
```

Since we only need property `name` from fruit, we can destructure the parameter using `{name}`, then we can use `name` as variable in our code instead of `fruit.name`.

因为我们只需要水果中的属性 `name`，所以我们可以使用 `{name}` 来解构，然后我们可以在代码中使用 `name` 作为变量，而不是 `fruit.name`。

We also assign empty object `{}` as default value. If we do not do so, you will get error when executing the line `test(undefined)` - Cannot destructure property name of `undefined` or `null`. because there is no `name` property in undefined.

我们还将空对象 `{}` 指定为默认值。如果我们不这样做，当执行 `test(undefined)`，不能解构 `undefined` 或 `null` 的属性名时，您将会得到错误。因为在 undefined中没有 `name` 属性。

If you don't mind using 3rd party libraries, there are a few ways to cut down null checking:

如果您不介意使用第三方库，有一些方法可以减少 null 检查：

- use [Lodash get](https://lodash.com/docs/4.17.10#get) function

使用 Lodash 的 get 函数

- use Facebook open source's [idx](https://github.com/facebookincubator/idx) library (with Babeljs)

使用 Facebook 的开源库 idx（以及 Babeljs）

Here is an example of using Lodash:

这是使用 Lodash 的例子：

```
// Include lodash library, you will get _
function test(fruit) {
  console.log(__.get(fruit, 'name', 'unknown'); // get property name, if not available, assign default value 'unknown'
}

//test results
test(undefined); // unknown
test({ }); // unknown
test({ name: 'apple', color: 'red' }); // apple
```

You may run the demo code [here](https://jsbin.com/bopovajiye/edit?js,console). Besides, if you are a fan of Functional Programming (FP), you may opt to use [Lodash fp](https://github.com/lodash/lodash/wiki/FP-Guide), the functional version of Lodash (method changed to `get` or `getOr`).

您可以在 [这里](https://jsbin.com/bopovajiye/edit?js,console) 运行演示代码。此外，如果你喜欢函数式编程（FP），你可以选择使用 Lodash fp, 即 Lodash 的函数式版本（方法改为 `get` 或 `getOr`）。

### 4、Favor Map / Object Literal than Switch Statement（选择 Map 或对象字面量，而不是 Switch 语句）

Let's look at the example below, we want to print fruits based on color:

让我们看看下面的例子，我们想要基于颜色打印水果名称：

```
function test(color) {
  // use switch case to find fruits in color
  switch (color) {
    case 'red':
      return ['apple', 'strawberry'];
    case 'yellow':
      return ['banana', 'pineapple'];
    case 'purple':
      return ['grape', 'plum'];
    default:
      return [];
  }
}

//test results
test(null); // []
test('yellow'); // ['banana', 'pineapple']
```

The above code seems nothing wrong, but I find it quite verbose. The same result can be achieve with object literal with cleaner syntax:

上面的代码似乎没有什么问题，但我发现它相当冗长。同样的结果可以通过对象字面量和更简洁的语法来实现：

```
// use object literal to find fruits in color
  const fruitColor = {
    red: ['apple', 'strawberry'],
    yellow: ['banana', 'pineapple'],
    purple: ['grape', 'plum']
  };

function test(color) {
  return fruitColor[color] || [];
}
```

Alternatively, you may use Map to achieve the same result:

或者，可以使用 [Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) 来实现相同的结果：

```
// use Map to find fruits in color
  const fruitColor = new Map()
    .set('red', ['apple', 'strawberry'])
    .set('yellow', ['banana', 'pineapple'])
    .set('purple', ['grape', 'plum']);

function test(color) {
  return fruitColor.get(color) || [];
}
```

Map is the object type available since ES2015, allow you to store key value pair.

Map 是 ES2015 以后可用的对象类型，允许您存储键值对。

Should we ban the usage of switch statement? Do not limit yourself to that. Personally, I use object literal whenever possible, but I wouldn't set hard rule to block that, use whichever make sense for your scenario.

我们应该禁止使用 switch 语句吗？不要把自己局限于此。就我个人而言，我尽可能地使用对象字面量，但是我不会设置严格的规则来阻止它，使用对您的场景有意义的任何一个。

Todd Motto has an article that dig deeper on switch statement vs object literal, you may read here.

Todd Motto 有一篇文章深入讨论 switch 语句与对象字面量，你可以在 [这里](https://toddmotto.com/deprecating-the-switch-statement-for-object-literals/) 阅读。

### TL;DR; Refactor the syntax（重构的语法）

For the example above, we can actually refactor our code to achieve the same result with `Array.filter`.

对于上面的示例，我们实际上可以重构代码，以使用 `Array.filter` 获得相同的结果。

```
const fruits = [
   { name: 'apple', color: 'red' },
   { name: 'strawberry', color: 'red' },
   { name: 'banana', color: 'yellow' },
   { name: 'pineapple', color: 'yellow' },
   { name: 'grape', color: 'purple' },
   { name: 'plum', color: 'purple' }
];

function test(color) {
 // use Array filter to find fruits in color

 return fruits.filter(f => f.color == color);
}
```

There's always more than 1 way to achieve the same result. We have shown 4 with the same example. Coding is fun!

总有不止一种方法可以达到同样的效果。我们展示了 4 个相同效果的例子。编码是有趣的！

### 5、Use Array.every & Array.some for All / Partial Criteria（所有或部分使用 Array.every & Array.some 的条件）

This last tip is more about utilizing new (but not so new) Javascript Array function to reduce the lines of code. Look at the code below, we want to check if all fruits are in red color:

最后一个技巧是关于使用新的（但不是很新）Javascript 数组函数来减少代码行。看看下面的代码，我们想检查所有的水果是否都是红色的:

```
const fruits = [
    { name: 'apple', color: 'red' },
    { name: 'banana', color: 'yellow' },
    { name: 'grape', color: 'purple' }
  ];

function test() {
  let isAllRed = true;

  // condition: all fruits must be red
  for (let f of fruits) {
    if (!isAllRed) break;
    isAllRed = (f.color == 'red');
  }

  console.log(isAllRed); // false
}
```

The code is so long! We can reduce the number of lines with `Array.every`:

代码太长了！我们可以用 `Array.every` 来减少行数：

```
const fruits = [
    { name: 'apple', color: 'red' },
    { name: 'banana', color: 'yellow' },
    { name: 'grape', color: 'purple' }
  ];

function test() {
  // condition: short way, all fruits must be red
  const isAllRed = fruits.every(f => f.color == 'red');

  console.log(isAllRed); // false
}
```

Much cleaner now right? In a similar way, if we want to test if any of the fruit is red, we can use `Array.some` to achieve it in one line.

现在干净多了，对吧？类似地，如果我们想用一行代码来判断任何一个水果是否为红色，我们可以使用 `Array.some`。

```
const fruits = [
    { name: 'apple', color: 'red' },
    { name: 'banana', color: 'yellow' },
    { name: 'grape', color: 'purple' }
];

function test() {
  // condition: if any fruit is red
  const isAnyRed = fruits.some(f => f.color == 'red');

  console.log(isAnyRed); // true
}
```

### Summary

Let's produce more readable code together. I hope you learn something new in this article.

让我们一起生成更多可读的代码。我希望你能从这篇文章中学到一些新的东西。

That's all. Happy coding!

这是所有。编码快乐!
