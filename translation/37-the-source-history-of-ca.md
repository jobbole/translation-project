---
translator: http://www.jobbole.com/members/wx1905494155/
reviewer: http://www.jobbole.com/members/hanxiaomax/
via: https://twobithistory.org/2018/11/12/cat.html
---


# The Source History of Cat
# cat命令的源码进化史

I once had a debate with members of my extended family about whether a computer science degree is a degree worth pursuing. I was in college at the time and trying to decide whether I should major in computer science. My aunt and a cousin of mine believed that I shouldn’t. They conceded that knowing how to program is of course a useful and lucrative thing, but they argued that the field of computer science advances so quickly that everything I learned would almost immediately be outdated. Better to pick up programming on the side and instead major in a field like economics or physics where the basic principles would be applicable throughout my lifetime.

有一次，我跟我的亲戚有一场争论，是关于读一个计算机科学的学位是否值得。当时是我在大学里面临是否选择计算机科学专业的时候。我姑姑和一个表哥认为我不该选。他们觉得会编程当然是个既有用又合算的事情，但是他们也坚信，计算机科学更新太快了，当下学到的知识会很快被淘汰掉。所以最好是选一门编程的课程，然后主修经济或者物理这种基本知识一辈子都适用的专业。

I knew that my aunt and cousin were wrong and decided to major in computer science. (Sorry, aunt and cousin!) It is easy to see why the average person might believe that a field like computer science, or a profession like software engineering, completely reinvents itself every few years. We had personal computers, then the web, then phones, then machine learning… technology is always changing, so surely all the underlying principles and techniques change too. Of course, the amazing thing is how little actually changes. Most people, I’m sure, would be stunned to know just how old some of the important software on their computer really is. I’m not talking about flashy application software, admittedly—my copy of Firefox, the program I probably use the most on my computer, is not even two weeks old. But, if you pull up the manual page for something like grep, you will see that it has not been updated since 2010 (at least on MacOS). And the original version of `grep` was written in 1974, which in the computing world was back when dinosaurs roamed Silicon Valley. People (and programs) still depend on `grep` every day.

我并不相信他们的理论，并且选择了主修计算机专业（抱歉了姑姑和表哥！）其实不难看出，为什么常人会认为计算机科学，或者软件工程这样的专业，每几年就会更新换代。先是诞生了私人计算机，然后是网络，手机，机器学习……科技永远在变化，那么其潜在的技术原理当然也在变化了。当然，最让人惊讶的是，这些基础技术原理，其实基本没变。我相信大部分人要是知道他们计算机中重要软件到底有多老，肯定会震惊。我并不是说软件的表面，毕竟我自己用的最多的火狐浏览器，两周前才更新过。但是如果你打开帮助手册查看`grep`之类的工具，你会发现它的上一次更新还是在2010年（至少Mac系统是这样）。`grep`的初代诞生于1974年，那时候的计算机时代好比侏罗纪。现如今，人们（以及程序）在工作中仍然要依赖grep做很多事情

My aunt and cousin thought of computer technology as a series of increasingly elaborate sand castles supplanting one another after each high tide clears the beach. The reality, at least in many areas, is that we steadily accumulate programs that have solved problems. We might have to occasionally modify these programs to avoid software rot, but otherwise they can be left alone. grep is a simple program that solves a still-relevant problem, so it survives. Most application programming is done at a very high level, atop a pyramid of much older code solving much older problems. The ideas and concepts of 30 or 40 years ago, far from being obsolete today, have in many cases been embodied in software that you can still find installed on your laptop.

我姑姑和表哥把计算机科技想象成一系列沙滩上的城堡，涨潮时潮水抹去旧的城堡，更加华丽的新城堡又会被建成。其实在现实中的很多领域，我们都是不断地在现有的程序基础上进行迭代。我们也许会时不时的修改这些程序来避免软件崩溃，但是除此之外这些程序不需要额外的维护。`grep`是一个简单的程序，它所解决的问题现在也有意义，所以它至今还存在。很多应用程序的编写都起始于一个很高的角度，就像是在金字塔顶端的基础上构建，而金字塔本身是由曾经解决问题的答案所建成的。现在看来很陈旧的，三四十年前的想法与概念，在很多时候都融入到了你现在计算机上安装了的应用程序里。

I thought it would be interesting to take a look at one such old program and see how much it had changed since it was first written. cat is maybe the simplest of all the Unix utilities, so I’m going to use it as my example. Ken Thompson wrote the original implementation of cat in 1969. If I were to tell somebody that I have a program on my computer from 1969, would that be accurate? How much has cat really evolved over the decades? How old is the software on our computers?

我想仔细研究一个这样的老程序，看看它从诞生到现在到底被修改了多少次，这肯定很有趣。我想用`cat`这个最简单的Unix工具来作为例子。Ken Thompson在1969年开发了初代`cat`。如果我跟别人说我计算机里有个1969年的程序，这准确吗？`cat`在这几十年里到底经历了几次迭代？我们计算机里的程序到底有多古老？

Thanks to repositories like this one, we can see exactly how cat has evolved since 1969. I’m going to focus on implementations of cat that are ancestors of the implementation I have on my Macbook. You will see, as we trace cat from the first versions of Unix down to the cat in MacOS today, that the program has been rewritten more times than you might expect—but it ultimately works more or less the same way it did fifty years ago.

幸好有[这个](https://github.com/dspinellis/unix-history-repo)代码仓库，我们可以清晰的了解到从1969年以来，`cat`是如何进化的。我接下来会主要聚焦于我自己Macbook上`cat`程序的历史实现方式。你会看到，`cat`历史从最初的Unix版本，到现在的Mac版本，这个程序被重写了比你预想的还要多的次数-但是最终它所实现的功能几乎跟五十年前一模一样。

## Research Unix
## Unix实验版本

Ken Thompson and Dennis Ritchie began writing Unix on a PDP 7. This was in 1969, before C, so all of the early Unix software was written in PDP 7 assembly. The exact flavor of assembly they used was unique to Unix, since Ken Thompson wrote his own assembler that added some features on top of the assembler provided by DEC, the PDP 7’s manufacturer. Thompson’s changes are all documented in the original Unix Programmer’s Manual under the entry for as, the assembler.

1969年，Ken Thompson和Dennis Ritchie开始在PDP 7上开发Unix。这是在C语言出现之前，所以早期的Unix程序都是用PDP 7上的汇编语言开发的。他们使用了专门针对于Unix的汇编版本，因为Ken Thompson开发了自己的汇编编译器，他在PDP 7出厂商DEC提供的编译器基础上添加了新的功能。Thompson的改进文档在初始[Unix编程手册](https://www.bell-labs.com/usr/dmr/www/man11.pdf)中有收录，在`as`, 编译器条目下面。

The first implementation of cat is thus in PDP 7 assembly. I’ve added comments that try to explain what each instruction is doing, but the program is still difficult to follow unless you understand some of the extensions Thompson made while writing his assembler. There are two important ones. First, the ;character can be used to separate multiple statements on the same line. It appears that this was used most often to put system call arguments on the same line as the sys instruction. Second, Thompson added support for “temporary labels” using the digits 0 through 9. These are labels that can be reused throughout a program, thus being, according to the Unix Programmer’s Manual, “less taxing both on the imagination of the programmer and on the symbol space of the assembler.” From any given instruction, you can refer to the next or most recent temporary label n using nf and nb respectively. For example, if you have some code in a block labeled 1:, you can jump back to that block from further down by using the instruction jmp 1b. (But you cannot jump forward to that block from above without using jmp 1f instead.)

`cat`的初代实现使用了PDP 7汇编语言。我有添加一些注释来解释每行命令，但是除非你明白Thompson编写汇编编译器的一些扩展，不然这个程序还是很难理解。这里有两个重要的点。第一，字符`;`可以被用于分隔同一行的声明语句。根据sys指令的描述，`;`通常被用于在同一行使用系统调用参数。第二，Thompson添加了数字0-9用于支持“暂存标记”。这些标记可以被整个程序重用，这就像Unix编程手册所描述的，“对于程序员思维和汇编语言字符空间的缩减优化”。从手册中，你可以使用`nf`来表示下一个标记`n`;用`nb`来表示上一个标记`n`。举个例子，如果你有个标记为`1:`的代码块，你可以从相距很远的下方代码中使用`jmp 1b`来往上跳回标记代码。(但是你不能往下跳到标记代码，除非你使用`jmp 1f`。)

The most interesting thing about this first version of `cat` is that it contains two names we should recognize. There is a block of instructions labeled `getc`and a block of instructions labeled `putc`, demonstrating that these names are older than the C standard library. The first version of `cat` actually contained implementations of both functions. The implementations buffered input so that reads and writes were not done a character at a time.

关于初代`cat`最有意思的是，它包含了两个我们熟知的名字，分别是一个标记为是一个标记为`getc`，和一个标记为`putc`的代码块，这表示这俩名字要比标准C语言库都要历史久远。初代`cat`实际上包含了这两个方法的实现。这样的实现方式使得输入字符可以被写入缓冲区，也就是说，读和写不需要以单个字符为单位完成。

The first version of `cat` did not last long. Ken Thompson and Dennis Ritchie were able to persuade Bell Labs to buy them a PDP 11 so that they could continue to expand and improve Unix. The PDP 11 had a different instruction set, so `cat` had to be rewritten. I’ve marked up this second version of `cat`with comments as well. It uses new assembler mnemonics for the new instruction set and takes advantage of the PDP 11’s various addressing modes. (If you are confused by the parentheses and dollar signs in the source code, those are used to indicate different addressing modes.) But it also leverages the `;` character and temporary labels just like the first version of `cat`, meaning that these features must have been retained when `as` was adapted for the PDP 11.

[初代`cat`](https://gist.github.com/sinclairtarget/47143ba52b9d9e360d8db3762ee0cbf5#file-1-cat-pdp7-s)并没有存在很久。Ken Thompson和Dennis Ritchie成功的劝说了贝尔实验室帮他们购入了一台PDP11，以便于他们对Unix系统进行扩展与提高。PDP 11使用的是一种不同的指令集，因此他们不得不重写`cat`。对于[第二代`cat`](https://gist.github.com/sinclairtarget/47143ba52b9d9e360d8db3762ee0cbf5#file-2-cat-pdp11-s)代码我也加了注释。第二代使用了针对于新指令集的新版汇编助记符，也利用了PDP 11中不同的[地址模式](https://en.wikipedia.org/wiki/PDP-11_architecture#Addressing_modes)。（那些源代码中的括号和$符号，是被用来指代不同的地址模式的。）但是`cat`第二代中也同样使用了初代中的`;`和暂存标记，这些功能一定是在PDP 11中移植`as`时，被保留了下来。

The second version of `cat` is significantly simpler than the first. It is also more “Unix-y” in that it doesn’t just expect a list of filename arguments—it will, when given no arguments, read from `stdin`, which is what `cat` still does today. You can also give this version of `cat` an argument of `-` to indicate that it should read from `stdin`.

`cat`的第二代源代码远比初代要简洁很多。第二代也更加的”Unix-y”，因为它不再需要一串文件名作为命令参数，而是与如今的`cat`一样，在没有参数的情况下，从`stdin`读取输入。对于二代`cat`，你也可以使用参数`-`来指定从`stdin`读取输入数据。

In 1973, in preparation for the release of the Fourth Edition of Unix, much of Unix was rewritten in C. But `cat` does not seem to have been rewritten in C until a while after that. The first C implementation of `cat` only shows up in the Seventh Edition of Unix. This implementation is really fun to look through because it is so simple. Of all the implementations to follow, this one most resembles the idealized `cat` used as a pedagogic demonstration in K&R C. The heart of the program is the classic two-liner:

1973年，为了准备发布第四版Unix，很大一部分Unix系统都用C语言重写了一遍。但是C语言版本的`cat`在Unix发布后过了一段时间才出现。[第一个C语言版本](https://gist.github.com/sinclairtarget/47143ba52b9d9e360d8db3762ee0cbf5#file-3-cat-v7-c)的`cat`只出现在第七版Unix系统中。这个实现方法非常值得一读，因为它非常简单明了。与其他版本比较，这一版最能作为代表`cat`的K&R C语言教育演示版本。这段程序的核心就是如下两行：
```
while ((c = getc(fi)) != EOF)
    putchar(c);
```

There is of course quite a bit more code than that, but the extra code is mostly there to ensure that you aren’t reading and writing to the same file. The other interesting thing to note is that this implementation of `cat` only recognized one flag, `-u`. The `-u` flag could be used to avoid buffering input and output, which `cat` would otherwise do in blocks of 512 bytes.

当然还有更多的代码，但是除了这两行以外，剩下的逻辑更多的是在确保用户不会同时读写同一个文件。另一个有意思的地方是，这个版本的`cat`只认得一个标记，`-u`。这个`-u`标记可以被用于关闭输入输出缓冲区，不然`cat`会默认缓存512字节。

## BSD
## 伯克利软件套件/BSD

After the Seventh Edition, Unix spawned all sorts of derivatives and offshoots. MacOS is built on top of Darwin, which in turn is derived from the Berkeley Software Distribution (BSD), so BSD is the Unix offshoot we are most interested in. BSD was originally just a collection of useful programs and add-ons for Unix, but it eventually became a complete operating system. BSD seems to have relied on the original `cat` implementation up until the fourth BSD release, known as 4BSD, when support was added for a whole slew of new flags. The 4BSD implementation of `cat` is clearly derived from the original implementation, though it adds a new function to implement the behavior triggered by the new flags. The naming conventions already used in the file were adhered to—the `fflg` variable, used to mark whether input was being read from `stdin` or a file, was joined by `nflg`, `bflg`, `vflg`, `sflg`, `eflg`, and `tflg`, all there to record whether or not each new flag was supplied in the invocation of the program. These were the last command-line flags added to `cat`; the man page for `cat` today lists these flags and no others, at least on Mac OS. 4BSD was released in 1980, so this set of flags is 38 years old.

在第七版之后，Unix催生了各种各样的衍生品。MacOS是基于Darwin系统的，而Darwin是基于伯克利软件套件（BSD），因此BSD是我们最感兴趣的Unix分支。BSD最初是作为Unix附加功能的软件合集，但是它最终成为了一个完整的操作系统。BSD似乎一直在用`cat`的初代版本，一直到第四版BSD发布为止。第四版BSD也就是4BSD，它添加了对于新标记的支持。[4BSD版本的`cat`](https://gist.github.com/sinclairtarget/47143ba52b9d9e360d8db3762ee0cbf5#file-4-cat-bsd4-c)能明显的看出是初代的衍生品，不过它添加了一些新的函数用来实现用新标记触发的功能。4BSD文件系统的命名方法是基于`fflg`这个变量的，`fflg`用于标记指令的输入是从文件，还是`stdin`读取的。继`fflg`之后，`nflg`，`bflg`，`vflg`，`sflg`，`eflg`和`tflg`也被用于记录程序中的标记是否被用到。这些命令行标记是`cat`添加的最后一批标记；如今至少在Mac系统中的`cat`命令行手册有列出来这些标记。4BSD是在1980年发布的，所以这一系列的标记有38岁了。

`cat` would be entirely rewritten a final time for BSD Net/2, which was, among other things, an attempt to avoid licensing issues by replacing all AT&T Unix-derived code with new code. BSD Net/2 was released in 1991. This final rewrite of `cat` was done by Kevin Fall, who graduated from Berkeley in 1988 and spent the next year working as a staff member at the Computer Systems Research Group (CSRG). Fall told me that a list of Unix utilities still implemented using AT&T code was put up on a wall at CSRG and staff were told to pick the utilities they wanted to reimplement. Fall picked `cat` and `mknod`. The `cat` implementation bundled with MacOS today is built from a source file that still bears his name at the very top. His version of `cat`, even though it is a relatively trivial program, is today used by millions.

`cat`最后一次被重写是为了BSD Net/2，这主要是为了避免软件许可证问题，因此所有AT&T Unix衍生代码都被替换为了新代码。BSD Net/2在1991年发布。最后一次重写是由Kevin Fall完成的，Kevin Fall于1988年毕业于伯克利，之后他花了一年的时间在计算机系统研究院(CSRG)工作了一年。Fall告诉我，用AT&T代码写的Unix工具集列表被挂在了CSRG的一面墙上，员工们被告知可以选择感兴趣的工具重写。Fall选择了`cat`和`mknod`。在如今Mac系统的默认`cat`版本中，Fall的名字排在开发者名单前列。他所编写的`cat`，虽然是个很简单的程序，但是直到今年还有数百万的用户在使用。

Fall’s original implementation of `cat` is much longer than anything we have seen so far. Other than support for a `-?` help flag, it adds nothing in the way of new functionality. Conceptually, it is very similar to the 4BSD implementation. It is only longer because Fall separates the implementation into a “raw” mode and a “cooked” mode. The “raw” mode is `cat` classic; it prints a file character for character. The “cooked” mode is `cat` with all the 4BSD command-line options. The distinction makes sense but it also pads out the implementation so that it seems more complex at first glance than it actually is. There is also a fancy error handling function at the end of the file that further adds to its length.

[Fall所写的`cat`源代码](https://gist.github.com/sinclairtarget/47143ba52b9d9e360d8db3762ee0cbf5#file-5-cat-net2-c)比我们之前看到的版本要长许多。除了支持`-?`帮助标记，这一版并没有添加新的功能。理论上来说，这一版代码与4BSD版本非常相似。代码之所以长，是因为Fall分开了“旧版”和“新版”的逻辑。“旧版”是典型的`cat`；它一个字符一个字符的输出。“新版”的`cat`包括了4BSD命令行选项。这样的分割很有道理，但是使得代码在第一眼看上去比实际复杂很多。代码的最后有个华丽的错误处理方程，这也增加了代码长度。

## MacOS
## MacOS

In 2001, Apple launched Mac OS X. The launch was an important one for Apple, because Apple had spent many years trying and failing to replace its existing operating system (classic Mac OS), which had long been showing its age. There were two previous attempts to create a new operating system internally, but both went nowhere; in the end, Apple bought NeXT, Steve Jobs’ company, which had developed an operating system and object-oriented programming framework called NeXTSTEP. Apple took NeXTSTEP and used it as a basis for Mac OS X. NeXTSTEP was in part built on BSD, so using NeXTSTEP as a starting point for Mac OS X brought BSD-derived code right into the center of the Apple universe.

2001年，苹果公司发布了Mac OS X系统。这次发布对于苹果公司来说非常重要，因为他们花了很多年，走了不少弯路，为了研发能够取代存在了很多年的旧版Mac OS系统。苹果公司内部曾经有过两次研发新系统的尝试，但是最终都没能成功；后来，苹果收购了史蒂夫·乔布斯的公司NeXT，他们公司开发了一款名为NeXTSTEP的，基于面向对象编程框架的操作系统。苹果决定使用NeXTSTEP作为Mac OS X的基础。NeXTSTEP的一部分是基于BSD开发的，所以用NeXTSTEP作为Mac OS X的基础，同时也给苹果系统带来了BSD代码风格。

The very first release of Mac OS X thus includes an implementation of `cat` pulled from the NetBSD project. NetBSD, which remains in development today, began as a fork of 386BSD, which in turn was based directly on BSD Net/2. So the first Mac OS X implementation of `cat` is Kevin Fall’s `cat`. The only thing that had changed over the intervening decade was that Fall’s error-handling function `err()` was removed and the `err()` function made available by `err.h` was used in its place. `err.h` is a BSD extension to the C standard library.

新发布的第一版Mac OS X中包含了来自NetBSD项目的[`cat`代码实现](https://gist.github.com/sinclairtarget/47143ba52b9d9e360d8db3762ee0cbf5#file-6-cat-macosx-c)。NetBSD项目如今仍在不断开发中，它最初是来自386BSD的分支。而386BSD是直接基于BSD Net/2的。所以Mac OS X上的`cat`就是Kevin Fall所写的`cat`。唯一变化的是，Kevin Fall写的错误处理函数`err()`被替换成了`err.h`中的`err()`。`err.h`是BSD基于C语言标准库的扩展。

The NetBSD implementation of `cat` was later swapped out for FreeBSD’s implementation of `cat`. According to Wikipedia, Apple began using FreeBSD instead of NetBSD in Mac OS X 10.3 (Panther). But the Mac OS X implementation of `cat`, according to Apple’s own open source releases, was not replaced until Mac OS X 10.5 (Leopard) was released in 2007. The FreeBSD implementation that Apple swapped in for the Leopard release is the same implementation on Apple computers today. As of 2018, the implementation has not been updated or changed at all since 2007.

NetBSD版本的`cat`在不久之后被FreeBSD版本取代了，根据[维基百科](https://en.wikipedia.org/wiki/Darwin_(operating_system))，苹果从Mac OS X 10.3 (Panther)开始，使用FreeBSD来取代NetBSD。但是Mac OS X版本的`cat`，根据苹果的开软发布记录，一直到2007年发布Mac OS X 10.5 (Leopard)才被取代。苹果为了发布Leopard而引进的[FreeBSD的实现版本](https://gist.github.com/sinclairtarget/47143ba52b9d9e360d8db3762ee0cbf5#file-7-cat-macos-10-13-c)一直被沿用到了今天。从2007一直到2018年，这一版没有做过任何升级或者改变。

So the Mac OS `cat` is old. As it happens, it is actually two years older than its 2007 appearance in MacOS X would suggest. This 2005 change, which is visible in FreeBSD’s Github mirror, was the last change made to FreeBSD’s `cat` before Apple pulled it into Mac OS X. So the Mac OS X `cat`implementation, which has not been kept in sync with FreeBSD’s `cat`implementation, is officially 13 years old. There’s a larger debate to be had about how much software can change before it really counts as the same software; in this case, the source file has not changed at all since 2005.

所以说Mac OS中的`cat`是古老的。实际上`cat`的出现，比2007年的正式发布时间还早两年。[2005年的改动](https://github.com/freebsd/freebsd/commit/a76898b84970888a6fd015e15721f65815ea119a#diff-6e405d5ab5b47ca2a131ac7955e5a16b)，在FreeBSD的Github镜像中可以看到，是`cat`被移植到Mac OS X之前FreeBSD版的最后一次更新。所以Mac OS X中`cat`实际上有13年的历史了，它并没有与FreeBSD的`cat`进行同步更新。这里有过一个辩论，软件到底被改动过几次才算是一个新的软件呢；就`cat`这个个例来看，它的源代码从2005年开始就完全没有改变过了。

The `cat` implementation used by Mac OS today is not that different from the implementation that Fall wrote for the 1991 BSD Net/2 release. The biggest difference is that a whole new function was added to provide Unix domain socket support. At some point, a FreeBSD developer also seems to have decided that Fall’s `raw_args()` function and `cook_args()` should be combined into a single function called `scanfiles()`. Otherwise, the heart of the program is still Fall’s code.

如今Mac OS系统中的`cat`与Fall在1991年为BSD Net/2所写的版本并没有太多不同。最大的不同是添加了一个新的函数用来支持Unix上的套接字。一个FreeBSD的开发者认为Fall所写的`raw_args()`函数应该与`cook_args()`合并为一个函数`scanfiles()`。除此之外，最核心的部分还是Fall的代码。

I asked Fall how he felt about having written the `cat` implementation now used by millions of Apple users, either directly or indirectly through some program that relies on `cat` being present. Fall, who is now a consultant and a co-author of the most recent editions of TCP/IP Illustrated, says that he is surprised when people get such a thrill out of learning about his work on `cat`. Fall has had a long career in computing and has worked on many high-profile projects, but it seems that many people still get most excited about the six months of work he put into rewriting `cat` in 1989。

我问过Fall，有几百万苹果用户在使用你所写的`cat`，还有很多程序直接或者间接依赖`cat`，对此你有什么感想。如今已经是顾问兼最新版TCP/IP协议的合作者的Fall表示，人们对他开发`cat`的经历如此的感兴趣，让他觉得非常惊讶。Fall曾经在计算领域工作过很久，并且有过很多有影响力的项目经历。但是似乎人们对于他在1989年开发`cat`的那六个月更加感兴趣。

## The Hundred-Year-Old Program
## 百岁程序

In the grand scheme of things, computers are not an old invention. We’re used to hundred-year-old photographs or even hundred-year-old camera footage. But computer programs are in a different category—they’re high-tech and new. At least, they are now. As the computing industry matures, will we someday find ourselves using programs that approach the hundred-year-old mark?

纵观历史上各种伟大的发明，计算机的历史并没有很久。我们仍然在使用有着百年历史的照片和胶卷。但是计算机软件是另外一个类别——目前仍属于高新科技。至少现在的软件是这样。随着计算机产业日渐成熟，我们会不会有一天发现，我们在使用有着百年历史的软件呢？

Computer hardware will presumably change enough that we won’t be able to take an executable compiled today and run it on hardware a century from now. Perhaps advances in programming language design will also mean that nobody will understand C in the future and `cat` will have long since been rewritten in another language. (Though C has already been around for fifty years, and it doesn’t look like it is about to be replaced any time soon.) But barring all that, why not just keep using the `cat` we have forever?

计算机硬件最终也会更新换代，现在的软件想必是没法跑在一个世纪以后的硬件上。也许高级语言设计的进步，也会导致在将来没有人会使用C语言，而`cat`也会被其他的语言重写。（不过C语言已经存在了五十年了，估计短期内也不会被取代。）不考虑以上这些的话，不如我们就一直用现在这版`cat`吧。

I think the history of `cat` shows that some ideas in computer science are in fact very durable. Indeed, with `cat`, both the idea and the program itself are old. It may not be accurate to say that the `cat` on my computer is from 1969. But I could make a case for saying that the `cat` on my computer is from 1989, when Fall wrote his implementation of `cat`. Lots of other software is just as ancient. So maybe we shouldn’t think of computer science and software development primarily as fields that disrupt the status quo and invent new things. Our computer systems are built out of historical artifacts. At some point, we may all spend more time trying to understand and maintain those historical artifacts than we spend writing new code.

我认为，`cat`的历史告诉我们，在计算机科学领域有一些思想是非常耐用的。实际上，对于`cat`，它的代码和思想都是很多年前出现的。要说我计算机中的`cat`是1969年的其实并不准确。但如果说我计算机中的`cat`是1989年Fall开发的，就准确多了。很多软件都很古老。也许我们不能单纯的认为计算机科学和软件开发是不断更新换代的领域。我们所开发的系统都是基于历史基础的。在某些时候，我们在开发新代码的同时，也需要去花时间去理解和维护历史代码。
