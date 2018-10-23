---
translator: http://www.jobbole.com/members/wx1763043264/
reviewer: http://www.jobbole.com/members/hanxiaomax/
via: https://twobithistory.org/2018/08/05/where-vim-came-from.html
---

# Where Vim Came From

# Vim 的起源

I recently stumbled across a file format known as Intel HEX. As far as I can gather, Intel HEX files (which use the `.hex` extension) are meant to make binary images less opaque by encoding them as lines of hexadecimal digits. Apparently they are used by people who program microcontrollers or need to burn data into ROM. In any case, when I opened up a HEX file in Vim for the first time, I discovered something shocking. Here was this file format that, at least to me, was deeply esoteric, but Vim already knew all about it. Each line of a HEX file is a record divided into different fields—Vim had gone ahead and colored each of the fields a different color. `set ft?` I asked, in awe.`filetype=hex`, Vim answered, triumphant.



我最近偶然发现了一种名为 Intel HEX 的文件格式。据我所知，Intel HEX 文件（使用` .hex` 扩展名）通过将二进制图像编码成十六进制数字行，使二进制图像不那么晦涩难懂。显然，当人们需要对微控制器进行编程或者将数据烧录进 ROM 时会用到这种文件。无论如何，当我第一次在 Vim 中打开一个 HEX 文件时，我发现了一些震惊的东西。至少对我来说，这种文件格式是非常深奥难懂的，但 Vim 已经掌握了它。HEX 文件的每一行都是一条被划分为不同字段的记录—— Vim 已经预先将每个字段显示成不同的颜色。`set ft` 吗? 我充满敬畏地发问。`filetype=hex`，Vim 得意地回答。

Vim is everywhere. It is used by so many people that something like HEX file support shouldn’t be a surprise. Vim comes pre-installed on Mac OS and has a large constituency in the Linux world. It is familiar even to people that hate it, because enough popular command line tools will throw users into Vim by default that the uninitiated getting trapped in Vim has become [a meme](https://stackoverflow.blog/wp-content/uploads/2017/05/meme.jpeg). There are major websites, including Facebook, that will scroll down when you press the `j` key and up when you press the `k` key—the unlikely high-water mark of Vim’s spread through digital culture.

Vim 无所不在且受众极其广泛，以至于其支持 HEX 文件也应该在预料之中。Mac OS 中预装了 Vim，同时，Linux 世界中也有很多 Vim 的支持者。即使那些讨厌 Vim 的人也对它很熟悉，因为太多的流行命令行工具默认使用 Vim，不熟悉 Vim 的用户往往身陷其中，这已经变成了一个[meme](https://stackoverflow.blog/wp-content/uploads/2017/05/meme.jpeg)。包括 Facebook 在内的一些大型网站，当你按下` j `键时，会向下滚动，而当你按下` k `键时，会向上滚动——这意味着 Vim 通过数字文化传播达到了难以想象的高水准。

And yet Vim is also a mystery. Unlike React, for example, which everyone knows is developed and maintained by Facebook, Vim has no obvious sponsor. Despite its ubiquity and importance, there doesn’t seem to be any kind of committee or organization that makes decisions about Vim. You could spend several minutes poking around the [Vim website](https://www.vim.org/) without getting a better idea of who created Vim or why. If you launch Vim without giving it a file argument, then you will see Vim’s startup message, which says that Vim is developed by “Bram Moolenaar et al.” But that doesn’t tell you much. Who is Bram Moolenaar and who are his shadowy confederates?

然而，Vim 也是谜一般的存在。例如，与人尽皆知的由 Facebook 开发和维护的 React 不同，Vim没有明显的发起人。尽管它如此常见和重要，但是似乎没有任何委员会或组织为 Vim 做出决策。你可以花几分钟去任意浏览 [Vim 网站](https://www.vim.org/)，但却无法得知是谁创建了 Vim 或者为什么创建。如果只启动 Vim 不打开任何文件，你会看到 Vim 的启动消息，表明 Vim 是由”Bram Moolenaar 等人“开发的。但这并不能说明什么，Bram Moolenaar 到底是谁，他的神秘同伙又是谁？

Perhaps more importantly, while we’re asking questions, why does exiting Vim involve typing `:wq`? Sure, it’s a “write” operation followed by a “quit” operation, but that is not a particularly intuitive convention. Who decided that copying text should instead be called “yanking”? Why is `:%s/foo/bar/gc` short for “find and replace”? Vim’s idiosyncrasies seem too arbitrary to have been made up, but then where did they come from?

当我们求索上述问题的时候，也许更重要的是，为什么退出 Vim 需要输入`：wq`？当然，这是一个“写”操作，然后是一个“退出”操作，但这不是一个特别容易直观理解的约定。谁决定了复制文本应该被称为“ yanking ”？为什么`：%s/foo/bar/gc`是“查找和替换”的缩写？Vim 的特性如此武断，不可能是被编造出来的，那么它们又从何而来呢？

The answer, as is so often the case, begins with that ancient crucible of computing, Bell Labs. In some sense, Vim is only the latest iteration of a piece of software—call it the “wq text editor”—that has been continuously developed and improved since the dawn of the Unix epoch.

就像众多情况一样，答案是从那个古老的计算机熔炉——贝尔实验室开始。从某种意义上说，Vim 只是一款被称为“ wq 文本编辑器”软件的最新版本。自 Unix 时代诞生以来，这个软件一直在不断地被开发和改进。

## Ken Thompson Writes a Line Editor

## Ken Thompson 创建了行编辑器

In 1966, Bell Labs hired Ken Thompson. Thompson had just completed a Master’s degree in Electrical Engineering and Computer Science at the University of California, Berkeley. While there, he had used a text editor called QED, written for the Berkeley Timesharing System between 1965 and 1966.<sup>1</sup> One of the first things Thompson did after arriving at Bell Labs was rewrite QED for the MIT Compatible Time-Sharing System. He would later write another version of QED for the Multics project. Along the way, he expanded the program so that users could search for lines in a file and make substitutions using regular expressions.<sup>2</sup>

1966 年，贝尔实验室聘用了 Ken Thompson 。Thompson 刚刚在加州大学伯克利分校完成了电气工程和计算机科学的硕士学位。在伯克利他使用一个名为 QED 的文本编辑器，该编辑器在 1965 到 1966 年间被开发用于伯克利分时系统。<sup>1 </sup>Thompson 到达贝尔实验室后做的第一件事就是为麻省理工学院兼容分时系统重写 QED。他后来又为 Multics 项目写了另一个版本的QED。在重写过程中，他对程序进行了扩展，以便用户可以在文件中搜索某一行，并使用正则表达式进行替换。<sup>2</sup>



The Multics project, which like the Berkeley Timesharing System sought to create a commercially viable time-sharing operating system, was a partnership between MIT, General Electric, and Bell Labs. AT&T eventually decided the project was going nowhere and pulled out. Thompson and fellow Bell Labs researcher Dennis Ritchie, now without access to a time-sharing system and missing the “feel of interactive computing” that such systems offered, set about creating their own version, which would eventually be known as Unix.<sup>3 </sup>In August 1969, while his wife and young son were away on vacation in California, Thompson put together the basic components of the new system, allocating “a week each to the operating system, the shell, the editor, and the assembler.”<sup>4</sup>

与伯克利的分时系统一样，由麻省理工学院、通用电气和贝尔实验室合作的 Multics 项目试图创建一个可行的商业分时操作系统。最终，AT&T 认为这个项目毫无进展并退出。在没有分时系统的情况下，Thompson 和贝尔实验室资深研究员 Dennis Ritchie，开始怀念分时系统所提供的“交互式计算的感觉”，并着手创建他们自己的版本，该版本最终发展成为 Unix。<sup>3</sup> 1969 年 8 月，在妻子和幼子外出去加州度假时，Thompson “给操作系统、shell、编辑器和汇编程序分别分配了一个星期”，将新系统的基本组件组合在一起。<sup>4</sup>

The editor would be called `ed`. It was based on QED but was not an exact re-implementation. Thompson decided to ditch certain QED features. Regular expression support was pared back so that only relatively simple regular expressions would be understood. QED allowed users to edit several files at once by opening multiple buffers, but `ed` would only work with one buffer at a time. And whereas QED could execute a buffer containing commands, `ed`would do no such thing. These simplifications may have been called for. Dennis Ritchie has said that going without QED’s advanced regular expressions was “not much of a loss.”<sup>5</sup>

这个编辑器被称为 `ed` 。它是基于 QED 的，但并不完全是 QED 的复现。 Thompson 决定放弃某些 QED 的功能，弱化了对常规的表达式的支持，因此 ed 只能理解相对简单的正则表达式。QED 允许用户打开多个缓冲区同时编辑多个文件，但是 `ed` 一次只使用一个缓冲区。QED 可以执行包含命令的缓冲区，而 `ed` 则不能。这些简化可能是必要的。Dennis Ritchie 曾说过，去掉 QED 的高级正则表达式是“并不大的损失”。<sup>5</sup>

`ed` is now a part of the POSIX specification, so if you have a POSIX-compliant system, you will have it installed on your computer. It’s worth playing around with, because many of the `ed` commands are today a part of Vim. In order to write a buffer to disk, for example, you have to use the `w` command. In order to quit the editor, you have to use the `q` command. These two commands can be specified on the same line at once—hence, `wq`. Like Vim, `ed` is a modal editor; to enter input mode from command mode you would use the insert command (`i`), the append command (`a`), or the change command (`c`), depending on how you are trying to transform your text. `ed` also introduced the `s/foo/bar/g` syntax for finding and replacing, or “substituting,” text.

 `ed` 现在是 POSIX 规范的一部分，所以如果你有一个符合 POSIX 的系统，你的电脑上就安装了 `ed` 。现在，许多 `ed` 命令都是 Vim 的一部分，因此，这就值得摆弄一番了。例如，你必须使用 `w` 命令来写入磁盘缓冲区，必须使用 `q` 命令来退出编辑器。这两个命令可以写在同一行命令中，也就是 `wq`。`ed` 与 Vim 一样，是一个模态编辑器；若要从命令模式进入输入模式，取决于你试图如何转换文本，需使用 insert 命令（`i`）、append 命令（`a`）或 change 命令（`c`）。`ed` 还引入了`s/foo/bar/g`语法来查找和替换或“替换”文本。

Given all these similarities, you might expect the average Vim user to have no trouble using `ed`. But `ed` is not at all like Vim in another important respect. `ed` is a true line editor. It was written and widely used in the days of the teletype printer. When Ken Thompson and Dennis Ritchie were hacking away at Unix, they looked like this:

考虑到所有这些相似之处，你可能会认为大部分 Vim 用户可以流畅地使用 `ed`。但 `ed` 在另一个重要方面，和 Vim 一点也不相似。`ed` 是一个真正的行编辑。它被广泛应用于电传打字机时代。当 Ken Thompson 和 Dennis Ritchie 在 Unix 上调试程序时看起来是这样的：

![Ken Thompson interacting with a PDP-11 via teletype.](https://upload.wikimedia.org/wikipedia/commons/8/8f/Ken_Thompson_%28sitting%29_and_Dennis_Ritchie_at_PDP-11_%282876612463%29.jpg)

`ed` doesn’t allow you to edit lines in place among the other lines of the open buffer, or move a cursor around, because `ed` would have to reprint the entire file every time you made a change to it. There was no mechanism in 1969 for`ed` to “clear” the contents of the screen, because the screen was just a sheet of paper and everything that had already been output had been output in ink. When necessary, you can ask `ed` to print out a range of lines for you using the list command (`l`), but most of the time you are operating on text that you can’t see. Using `ed` is thus a little trying to find your way around a dark house with an underpowered flashlight. You can only see so much at once, so you have to try your best to remember where everything is.

 `ed` 不允许你编辑开放缓冲区中那些被其他行围绕的行，也不允许移动光标，因为 `ed`  在每次修改的时候都必须重新打印整个文件。在1969年，  `ed` 没有任何机制来“清除”屏幕上的内容，因为”屏幕“就是一张纸，所有已经输出的东西都像是已经用墨水打印出来了。在必要的时候，你可以使用列表命令（`l`）要求  `ed` 打印出一系列的行，但是大多数时候，你都是在你看不到的文本上操作。因此，使用 `ed`  就像是尝试用一个低电量的手电筒在黑暗房间中摸索。每次你只能看到那么一点儿，所以必须尽最大努力去记住每件东西的位置。

Here’s an example of an `ed` session. I’ve added comments (after the `#`character) explaining the purpose of each line, though if these were actually entered `ed` wouldn’t recognize them as comments and would complain:

下面有一个 `ed` 会话的例子。我添加了注释（在字符 `# `之后）来解释了每一行，不过如果这些注释真的被输入，`ed` 并不会把它们当作注释并且会报错：

```
[sinclairtarget 09:49 ~]$ ed
i                           # Enter input mode
Hello world!

Isn't it a nice day?
.                           # Finish input
1,2l                        # List lines 1 to 2
Hello world!$
$
2d                          # Delete line 2
,l                          # List entire buffer
Hello world!$
Isn't it a nice day?$
s/nice/terrible/g           # Substitute globally
,l
Hello world!$
Isn't it a terrible day?$
w foo.txt                   # Write to foo.txt
38                          # (bytes written)
q                           # Quit
[sinclairtarget 10:50 ~]$ cat foo.txt
Hello world!
Isn't it a terrible day?
```





As you can see, `ed` is not an especially talkative program.

正如你所看到的，`ed` 并不是一个特别友好的程序。

## Bill Joy Writes a Text Editor

## Bill Joy 创建了文本编辑器

`ed` worked well enough for Thompson and Ritchie. Others found it difficult to use and it acquired a reputation for being a particularly egregious example of Unix’s hostility toward the novice.<sup>6 </sup>In 1975, a man named George Coulouris developed an improved version of `ed` on the Unix system installed at Queen Mary’s College, London. Coulouris wrote his editor to take advantage of the video displays that he had available at Queen Mary’s. Unlike `ed`, Coulouris’ program allowed users to edit a single line in place on screen, navigating through the line keystroke by keystroke (imagine using Vim on one line at a time). Coulouris called his program `em`, or “editor for mortals,” which he had supposedly been inspired to do after Thompson paid a visit to Queen Mary’s, saw the program Coulouris had built, and dismissed it, saying that he had no need to see the state of a file while editing it.<sup>7</sup>

对 Thompson 和 Ritchie 说， `ed` 已经足够好了。但是其他人则认为它很难用，而且它作为一个淋漓尽致地表现 Unix 对新手敌意的例子而臭名昭著。<sup>6</sup>在 1975 年，一个名叫 George Coulouris 的人在伦敦玛丽皇后学院的 Unix 系统上开发了一个改进版 `ed` 。Coulouris 利用他在玛丽女王学院的视频显示器开发他的编辑器。与 `ed` 不同的是，Coulouris 的程序允许用户编辑在屏幕中的一行代码，通过一次次击键的方式来操作行（想象一下在 Vim 中每次编辑一行）。 Thompson 拜访玛丽女王学院时，看到 Coulouris 已经建好的程序，驳斥道他不需要在编辑文件的时候看到它的状态。受此启发，Coulouris 将他的程序命名为 `em`，或者“为凡人而生的编辑器”。<sup>7</sup>

In 1976, Coulouris brought `em` with him to UC Berkeley, where he spent the summer as a visitor to the CS department. This was exactly ten years after Ken Thompson had left Berkeley to work at Bell Labs. At Berkeley, Coulouris met Bill Joy, a graduate student working on the Berkeley Software Distribution (BSD). Coulouris showed `em` to Joy, who, starting with Coulouris’ source code, built out an improved version of `ed` called `ex`, for “extended `ed`.” Version 1.1 of `ex` was bundled with the first release of BSD Unix in 1978. `ex` was largely compatible with `ed`, but it added two more modes: an “open” mode, which enabled single-line editing like had been possible with `em`, and a “visual” mode, which took over the whole screen and enabled live editing of an entire file like we are used to today.

1976年，Coulouris 把 `em` 引入了加州大学伯克利分校，在那里他用了一个夏天的时间在 CS 系访学。这是 Ken Thompson 离开伯克利去贝尔实验室工作十年之后的事了。在伯克利，Coulouris 遇到了 Bill Joy，一名伯克利软件发行公司（BSD）的研究生。Coulouris 斯向乔伊展示了 `em`， Joy 以 Coulouris 的源代码为基础，为扩展 `ed` 建立了一个名为 `ex` 的改进版 `ed`。1978年，1.1 版本的 `ex` 与第 1 个版本的 BSD Unix 捆绑在一起。`ex` 在很大程度上与 `ed` 兼容，但它增加了两种模式：一种“开放”模式，这种模式可以使 `em` 单行编辑成为可能，还有一种“可见”模式，这种模式会占据整个屏幕，并且可以像我们今天所习惯的那样，对整个文件进行实时编辑。

For the second release of BSD in 1979, an executable named `vi` was introduced that did little more than open `ex` in visual mode.<sup>8</sup>

1979 年的第 2 版 BSD 引入了一个名为 `vi` 的可执行文件，它只在可视模式下打开 `ex` 。<sup>8</sup>

`ex`/`vi` (henceforth `vi`) established most of the conventions we now associate with Vim that weren’t already a part of `ed`. The video terminal that Joy was using was a Lear Siegler ADM-3A, which had a keyboard with no cursor keys. Instead, arrows were painted on the `h`, `j`, `k`, and `l` keys, which is why Joy used those keys for cursor movement in `vi`. The escape key on the ADM-3A keyboard was also where today we would find the tab key, which explains how such a hard-to-reach key was ever assigned an operation as common as exiting a mode. The `:` character that prefixes commands also comes from `vi`, which in regular mode (i.e. the mode entered by running `ex`) used `:` as a prompt. This addressed a long-standing complaint about `ed`, which, once launched, greets users with utter silence. In visual mode, saving and quitting now involved typing the classic `:wq`. “Yanking” and “putting,” marks, and the `set` command for setting options were all part of the original `vi`. The features we use in the course of basic text editing today in Vim are largely `vi` features.

`ex`/`vi` （后来称为 `vi`）建立了我们现在使用的 Vim 中大多数的约定，但这些约定当时并不是 `ed` 的一部分。Joy 使用的视频终端是 Lear Siegler ADM-3A，它的键盘没有光标键。而是，`h`、`j`、`k`和`l`键上绘制光标键，所以 Joy 在`vi` 中就使用这些键来进行光标移动。ADM-3A 键盘上 escape 键位置是今天我们所使用的键盘上的 tab 键，这也就解释了为什么这样一个难以够着的键会被用来实现像退出当前模式这么常见的操作。前缀命令的`:`字符同样也来自 `i`，它在常规模式下（即运行 `ex` 进入的模式）使用 `:` 作为提示。这解决了一个 `ed` 中被长期诟病的问题，也就是一旦启动之后，没有任何反馈信息向用户致以问候。在可见模式下，保存和退出需要使用现在仍在使用的经典 `wq`。“Yanking”和“puttng”、标记、以及用于设置选项的 `set` 命令都是原始 `vi` 的一部分。我们今天在 Vim 中使用的的基本文本编辑过程，都是 `vi`  中使用的特性。

![A Lear Siegler ADM-3A keyboard.](https://vintagecomputer.ca/wp-content/uploads/2015/01/LSI-ADM3A-full-keyboard.jpg)

`vi` was the only text editor bundled with BSD Unix other than `ed`. At the time, Emacs could cost hundreds of dollars (this was before GNU Emacs), so `vi` became enormously popular. But `vi` was a direct descendant of `ed`, which meant that the source code could not be modified without an AT&T source license. This motivated several people to create open-source versions of `vi`. STEVIE (ST Editor for VI Enthusiasts) appeared in 1987, Elvis appeared in 1990, and `nvi` appeared in 1994. Some of these clones added extra features like syntax highlighting and split windows. Elvis in particular saw many of its features incorporated into Vim, since so many Elvis users pushed for their inclusion.<sup>9</sup>

`vi` 是除 `ed`之外唯一与 BSD Unix 捆绑的文本编辑器。在那个时候，Emacs 可能会花费数百美元（这是在 GNU Emacs 之前），所以 `vi` 变得非常流行。但是 `vi` 是 `ed` 的直接衍生版本，这意味着如果没有 AT&T 的源代码，源代码就不能被修改。这促使一些人创建了 `vi` 的开源版本。 STEVIE （专门为 VI 爱好者的 ST 编辑器）出现于1987年，Elvis 出现于 1990 年，`nvi` 出现于 1994 年。其中一些克隆版本添加了额外的功能，如语法高亮和窗口分离。尤其是 Elvis ，它的许多功能被整合到 Vim 中，因为许多 Elvis 用户推动了这些功能的加入。<sup>9)</sup>

## Bram Moolenaar Writes Vim

## Bram Moolenaar 创建了 Vim

“Vim”, which now abbreviates “Vi Improved”, originally stood for “Vi Imitation.” Like many of the other `vi` clones, Vim began as an attempt to replicate `vi` on a platform where it was not available. Bram Moolenaar, a Dutch software engineer working for a photocopier company in Venlo, the Netherlands, wanted something like `vi` for his brand-new Amiga 2000. Moolenaar had grown used to using `vi` on the Unix systems at his university and it was now “in his fingers.”<sup>10</sup>So in 1988, using the existing STEVIE `vi`clone as a starting point, Moolenaar began work on Vim.

“Vim”现在是“改进版 Vi”的缩写，而最初代表的是“模拟版 Vi”。和其他许多“vi克隆版本”一样，Vim 始于在一个无法使用 `vi` 的平台上复现 `vi` 的一个尝试。在荷兰 Venlo 一家影印公司工作的软件工程师 Bram Moolenaar 想要为他全新的 Amiga 2000 准备一款类似于 `vi` 的编辑器。Moolenaar 已经习惯了在大学时使用的 Unix 系统上的 `vi` ，当时他 已经对` vi `了如指掌。<sup>10 </sup>所以在 1988 年，Moolenaar 使用当时的 STEVIE ` vi `克隆版本开始在 Vim 上工作。

Moolenaar had access to STEVIE because STEVIE had previously appeared on something called a Fred Fish disk. Fred Fish was an American programmer that mailed out a floppy disk every month with a curated selection of the best open-source software available for the Amiga platform. Anyone could request a disk for nothing more than the price of postage. Several versions of STEVIE were released on Fred Fish disks. The version that Moolenaar used had been released on Fred Fish disk 256.<sup>11</sup>(Disappointingly, Fred Fish disks seem to have nothing to do with [Freddi Fish](https://en.wikipedia.org/wiki/Freddi_Fish).)

Moolenaar 接触到 STEVIE 缘于其曾经出现在一个叫 Fred Fish 的磁盘上。Fred Fish 是一名美国程序员，每个月都会寄出一张软盘，内含为 Amiga 平台提供的精选可用开源软件。任何人只要支付邮费就可以得到一张这样的磁盘。有若干版本的 STEVIE 曾在 Fred Fish 磁盘上发布。Moolenaar  使用的 STEVIE 版本在 Fred Fish 256 号磁盘上发布。<sup>11</sup>（令人失望的是，Fred Fish 磁盘似乎与 [Freddi Fish](https://en.wikipedia.org/wiki/Freddi_Fish) 没有任何关系。）

Moolenaar liked STEVIE but quickly noticed that there were many `vi`commands missing.<sup>12 </sup>So, for the first release of Vim, Moolenaar made `vi`compatibility his priority. Someone else had written a series of `vi` macros that, when run through a properly `vi`-compatible editor, could solve a [randomly generated maze](https://github.com/isaacs/.vim/tree/master/macros/maze). Moolenaar was able to get these macros working in Vim. In 1991, Vim was released for the first time on Fred Fish disk 591 as “Vi Imitation”.<sup>13</sup> Moolenaar had added some features (including multi-level undo and a “quickfix” mode for compiler errors) that meant that Vim had surpassed `vi`. But Vim would remain “Vi Imitation” until Vim 2.0, released in 1993 via FTP.

Moolenaar  喜欢 STEVIE，但很快就注意到其缺失了很多 `vi` 命令。<sup>12 </sup>因此，在第一次发布 Vim 时，Moolenaar 优先考虑了 `vi` 的兼容性。当时已经有其他人编写了一系列的 `vi` 宏，当运行一个合适的 `vi` 兼容编辑器时，可以求解一个[随机生成的迷宫](https://github.com/isaacs/.vim/tree/master/macros/maze)。Moolenaar 能够让这些宏在 Vim 中运行。1991年，Vim  以 `Vi模拟`为名第一次发布于 Fred Fish 591 号磁盘。<sup>13 </sup>Moolenaar 添加了一些特性（包括多级撤销和解决编译器错误的“quickfix”模式），这意味着 Vim 已经完成了对 `Vi` 的超越。在 1993 年通过 FTP 发布 Vim 2.0 之前，Vim 都仍以 `Vi模拟` 的身份存在。

Moolenaar, with the occasional help of various internet collaborators, added features to Vim at a steady clip. Vim 2.0 introduced support for the `wrap`option and for horizontal scrolling through long lines of text. Vim 3.0 added support for split windows and buffers, a feature inspired by the `vi` clone `nvi`. Vim also now saved each buffer to a swap file, so that edited text could survive a crash. Vimscript made its first appearance in Vim 5.0, along with support for syntax highlighting. All the while, Vim’s popularity was growing. It was ported to MS-DOS, to Windows, to Mac, and even to Unix, where it competed with the original `vi`.

在众多互联网合作者的帮助下，Moolenaar 稳健地在 Vim 中加入了一些功能。Vim 2.0 引入了对` wrap `选项的支持，以及对长行文本进行水平滚动的支持。受到了` vi `克隆` nvi `的启发，Vim 3.0 增加了对分割窗口和缓冲区的支持。Vim 现在还将每个缓冲区保存到交换文件中以避免程序崩溃造成文件丢失。Vimscript 支持语法高亮显示，第一次出现是在 Vim 5.0 中。与此同时，Vim 的受欢迎程度也在不断增长。它被移植到 MS-DOS、 Windows、Mac，甚至被移植到 Unix 与原来的` vi `竞争。

In 2006, Vim was voted the most popular editor among *Linux Journal* readers.<sup>14 </sup>Today, according to Stack Overflow’s 2018 Developer Survey, Vim is the most popular text-mode (i.e. terminal emulator) editor, used by 25.8% of all software developers (and 40% of Sysadmin/DevOps people).<sup>15 </sup>For a while, during the late 1980s and throughout the 1990s, programmers waged the “Editor Wars,” which pitted Emacs users against `vi` (and eventually Vim) users. While Emacs certainly still has a following, some people think that the Editor Wars are over and that Vim won.<sup>16</sup>The 2018 Stack Overflow Developer Survey suggests that this is true; only 4.1% of respondents used Emacs.

2006 年，Vim 被 *Linux Journal* 读者评为最受欢迎的编辑器。<sup>14 </sup>如今，根据 2018 年 Stack Overflow 的开发者调查，Vim 是最受欢迎的文本模式（即终端模拟器）编辑器，受用于 25.8% 的软件开发人员(和 40% 的 Sysadmin / DevOps 人员)。<sup>15</sup> 在 1980 年代末和整个 1990 年代，程序员一度发起了“编辑器战争”，将 Emacs 用户与 `vi` （即最终的 Vim ）用户进行了对比。虽然 Emacs 肯定仍有一些追随者，但有些人认为编辑器战争已经以 Vim 获胜而结束。<sup>16 </sup>2018年 Stack Overflow 的开发者调查显示只有 4.1% 的受访者使用 Emacs，也验证了这个事实。

How did Vim become so successful? Obviously people like the features that Vim has to offer. But I would argue that the long history behind Vim illustrates that it had more advantages than just its feature set. Vim’s codebase dates back only to 1988, when Moolenaar began working on it. The “wq text editor,” on the other hand—the broader vision of how a Unix-y text editor should work—goes back a half-century. The “wq text editor” had a few different concrete expressions, but thanks in part to the unusual attention paid to backward compatibility by both Bill Joy and Bram Moolenaar, good ideas accumulated gradually over time. The “wq text editor,” in that sense, is one of the longest-running and most successful open-source projects, having enjoyed contributions from some of the greatest minds in the computing world. I don’t think the “startup-company-throws-away all-precedents-and-creates-disruptive-new-software” approach to development is necessarily bad, but Vim is a reminder that the collaborative and incremental approach can also yield wonders.

Vim 是如何变得如此成功的？显然，人们喜欢 Vim 所提供的特性。但我认为，Vim 背后的悠久历史表明了它的优势远不仅仅体现在其功能集上。Vim 的代码库可以追溯到 1988 年，当时 Moolenaar 开始研究它。另一方面，“ wq 文本编辑器”——关于 Unix-y 文本编辑器应该如何工作的更广泛的愿景——可以追溯到半个世纪以前。“ wq 文本编辑器”有一些不同的具体表达方式，但在某种程度上要感谢 Bill Joy 和 Bram Moolenaar 对向后兼容性非比寻常的关注，才使好的想法逐渐积累起来。从这个意义上说，“ wq 文本编辑器”是运行时间最长、最成功的开源项目之一，得益于计算机世界中一些最伟大的思想贡献。我不认为“创业公司无视所有先例来创造颠覆性的新软件”的开发方式都是不妥的，但 Vim 提醒我们，这种协作和增量的方式同样能产生奇迹。

*If you enjoyed this post, more like it come out every two weeks! Follow@TwoBitHistory on Twitter or subscribe to the RSS feed to make sure you know when a new post is out.*

*@TwoBitHistory 每两周更新一次类似文章，如果你喜欢本文请在 Twitter 上关注或者订阅 RSS，以便及时知晓更新发布。伯乐在线已获授权同步翻译中文版，敬请关注*

1. Butler Lampson, “Systems,” Butler Lampson, accessed August 5, 2018, <http://bwlampson.site/Systems.htm>. [↩](https://twobithistory.org/2018/08/05/where-vim-came-from.html#fnref:1)
2. Dennis Ritchie, “An Incomplete History of the QED Editor,” accessed August 5, 2018, <https://www.bell-labs.com/usr/dmr/www/qed.html>. [↩](https://twobithistory.org/2018/08/05/where-vim-came-from.html#fnref:2)
3. Peter Salus, “The Daemon, the GNU, and the Penguin,” Groklaw, April 14, 2005, accessed August 5, 2018, <http://www.groklaw.net/article.php?story=20050414215646742>. [↩](https://twobithistory.org/2018/08/05/where-vim-came-from.html#fnref:3)
4. ibid. [↩](https://twobithistory.org/2018/08/05/where-vim-came-from.html#fnref:4)
5. Dennis Ritchie, “An Incomplete History of the QED Editor,” accessed August 5, 2018, <https://www.bell-labs.com/usr/dmr/www/qed.html>. [↩](https://twobithistory.org/2018/08/05/where-vim-came-from.html#fnref:5)
6. Donald Norman, “The Truth about Unix: The User Interface Is Horrid,” Datamation, accessed August 5, 2018, <http://www.ceri.memphis.edu/people/smalley/ESCI7205_misc_files/The_truth_about_Unix_cleaned.pdf>. [↩](https://twobithistory.org/2018/08/05/where-vim-came-from.html#fnref:6)
7. George Coulouris, “George Coulouris: A Bit of History,” George Coulouris’ Homepage, September 1998, accessed August 5, 2018, <http://www.eecs.qmul.ac.uk/~gc/history/index.html>. [↩](https://twobithistory.org/2018/08/05/where-vim-came-from.html#fnref:7)
8. “Second Berkeley Software Distribution Manual,” Roguelife, accessed August 5, 2018, <http://roguelife.org/~fujita/COOKIES/HISTORY/2BSD/vi.u.html>. [↩](https://twobithistory.org/2018/08/05/where-vim-came-from.html#fnref:8)
9. Sven Guckes, “VIM Wishlist,” Vmunix, May 15, 1995, accessed August 5, 2018, <https://web.archive.org/web/20080520075925/http://www.vmunix.com/vim/wish.html>. [↩](https://twobithistory.org/2018/08/05/where-vim-came-from.html#fnref:9)
10. Bram Moolenaar, “Vim 25” (lecture, Zurich, November 2, 2016), December 13, 2016, accessed August 5, 2018, <https://www.youtube.com/watch?v=ayc_qpB-93o&t=4m58>s [↩](https://twobithistory.org/2018/08/05/where-vim-came-from.html#fnref:10)
11. ibid. (?t=6m15s) [↩](https://twobithistory.org/2018/08/05/where-vim-came-from.html#fnref:11)
12. ibid. (?t=7m6s) [↩](https://twobithistory.org/2018/08/05/where-vim-came-from.html#fnref:12)
13. “Fish Disks 1 - 1120,” Amiga Stuff, accessed August 5, 2018, <http://www.amiga-stuff.com/pd/fish.html>. [↩](https://twobithistory.org/2018/08/05/where-vim-came-from.html#fnref:13)
14. “2005 Linux Journal Reader’s Choice Awards,” Linux Journal, September 28, 2005, accessed August 5, 2018, <https://www.linuxjournal.com/article/8520#N0x850cd80.0x87983bc>. [↩](https://twobithistory.org/2018/08/05/where-vim-came-from.html#fnref:14)
15. “Stack Overflow Developer Survey 2018,” Stack Overflow, accessed August 5, 2018, <https://insights.stackoverflow.com/survey/2018/#development-environments-and-tools>. [↩](https://twobithistory.org/2018/08/05/where-vim-came-from.html#fnref:15)
16. Bruce Byfield, “The End of the Editor Wars,” Linux Magazine, May 11, 2015, accessed August 5, 2018, <http://www.linux-magazine.com/Online/Blogs/Off-the-Beat-Bruce-Byfield-s-Blog/The-End-of-the-Editor-Wars>. [↩](https://twobithistory.org/2018/08/05/where-vim-came-from.html#fnref:16)
