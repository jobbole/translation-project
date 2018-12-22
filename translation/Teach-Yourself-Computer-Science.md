# Teach Yourself Computer Science #
If you’re a self-taught engineer or bootcamp grad, you owe it to yourself to learn computer science. Thankfully, you can give yourself a world-class CS education without investing years and a small fortune in a degree program.

如果你是一名自学工程师或者是一名软件集训课程毕业的学生，你需要这份资料来帮助你更加高效的学习计算机科学。幸好，你不需要花上几年的时间和学费去获得编程方向的学位就能获得世界顶级的CS（计算机科学）课程。

There are plenty of resources out there, but some are better than others. You don’t need yet another “200+ Free Online Courses” listicle. You need answers to these questions:

网上有很多学习资源，良莠不齐。你不需要另外的“200+免费在线课程”列表。你需要的是如下问题的答案：


>Which subjects should you learn, and why?
>>你应该学习哪门课程？为什么？

>What is the best book or video lecture series for each subject?
>>每门课程最好的书籍或者视频，讲座是什么？

This guide is our attempt to definitively answer these questions.

我写这篇文章的目的就是尝试对于这些问题给出的明确答案：

## TL;DR: ##
Study all nine subjects below, in roughly the presented order, using either the suggested textbook or video lecture series, but ideally both. Aim for 100-200 hours of study of each topic, then revisit favorites throughout your career.

  使用建议的书籍或者视频讲座来学习以下的九门科目，最好是书籍和讲座都仔细的研究一下，可以不严格按照列出的顺序来。每一门科目都需要花上100-200小时来研读，然后在你的职业生涯中对于最热爱的方向进行反复重温。


|Subject	|Why study?	|Best book	|Best videos|
|:---:|:---:|:---:|:---:|
|Programming	|Don’t be the person who “never quite understood” something like recursion.|Structure and Interpretation of Computer|Programs	Brian Harvey’s Berkeley CS 61A|
|Computer Architecture	|If you don’t have a solid mental model of how a computer actually works, all of your higher-level abstractions will be brittle.	|Computer Organization and Design|	Berkeley CS 61C|
|Algorithms and Data Structures	|If you don’t know how to use ubiquitous data structures like stacks, queues, trees, and graphs, you won’t be able to solve hard problems.|The Algorithm Design Manual|	Steven Skiena’s lectures|
|Math for CS|	CS is basically a runaway branch of applied math, so learning math will give you a competitive advantage.|	Mathematics for Computer Science|	Tom Leighton’s MIT 6.042J|
|Operating Systems|	Most of the code you write is run by an operating system, so you should know how those interact.|	Operating Systems: Three Easy Pieces	|Berkeley CS 162|
|Computer Networking|	The Internet turned out to be a big deal: understand how it works to unlock its full potential.|	Computer Networking: A Top-Down Approach	|Stanford CS 144|
|Databases	|Data is at the heart of most significant programs, but few understand how database systems actually work.	|Readings in Database Systems|	Joe Hellerstein’s Berkeley CS 186|
|Languages and Compilers	|If you understand how languages and compilers actually work, you’ll write better code and learn new languages more easily.	|Compilers: Principles, Techniques and Tools|	Alex Aiken’s course on Lagunita|
|Distributed Systems|	These days, most systems are distributed systems.|	Distributed Systems, 3rd Edition by Maarten van Steen|	🤷‍|

## Why learn computer science? 
## 为什么要学习计算机科学 

There are 2 types of software engineer: those who understand computer science well enough to do challenging, innovative work, and those who just get by because they’re familiar with a few high level tools.

有两种软件工程师：一种人对于电脑科学有很好的理解从而去从事挑战性的、富有创造力的工作。另外一种人仅仅熟悉一些高级工具，对其原理持得过且过的态度。
 
Both call themselves software engineers, and both tend to earn similar salaries in their early careers. But Type 1 engineers grow in to more fulfilling and well-remunerated work over time, whether that’s valuable commercial work or breakthrough open-source projects, technical leadership or high-quality individual contributions.

两者都叫做软件工程师，而且两者在早期的职业生涯中可能领着同样的薪水。但是第一种工程师，不管他从事的是商业工作，还是突破性的开源工程，都会由于他的技术领导力或者杰出的个人贡献一点一点成长成一名对于编程更加痴迷而且待遇更高的工程师。

Type 1 engineers find ways to learn computer science in depth, whether through conventional means or by relentlessly learning throughout their careers. Type 2 engineers typically stay at the surface, learning specific tools and technologies rather than their underlying foundations, only picking up new skills when the winds of technical fashion change.
 
第一种工程师可以通过常规手段或者在职业生涯中不断学习来加深对于计算机科学的理解深度。第二种工程师通常停留在表面，学习具体的工具或者技巧而不是其中的基础，当前流行什么技术，他们就仅仅捡起新的技能学习一下。

Currently, the number of people entering the industry is rapidly increasing, while the number of CS grads is essentially static. This oversupply of Type 2 engineers is starting to reduce their employment opportunities and keep them out of the industry’s more fulfilling work. Whether you’re striving to become a Type 1 engineer or simply looking for more job security, learning computer science is the only reliable path.

近些年来，越来越多的人进入软件领域工作，但是本质上计算机科学的毕业生数量是没有改变的。第二种工程师的供应过量开始导致他们的就业机会变少而且导致他们离企业中令人感觉充实的工作更远。不管你是努力要成为第一种工程师或者仅仅是保险起见地想找到更多的工作，学习计算机科学是唯一一种可靠的途径。

## Subject guides ##
## 课程指南

### Programming ###
### 编程

Most undergraduate CS programs start with an “introduction” to computer programming. The best versions of these courses cater not just to novices, but also to those who missed beneficial concepts and programming models while first learning to code.

大多数大学的计算机编程课程通常以“入门类”计算机的课程开始。这些课程最好是不仅仅针对于初学者，而且对于第一次学习编程，基本概念和编程模型不是很熟悉的人也有所启发的。

Our standard recommendation for this content is the classic Structure and Interpretation of Computer Programs, which is available online for free both as a book, and as a set of MIT video lectures. While those lectures are great, our video suggestion is actually Brian Harvey’s SICP lectures (for the 61A course at Berkeley) instead. These are more refined and better targeted at new students than are the MIT lectures.

对于这种介绍的内容的我们给出的标准建议是经典的计算机程序的结构与解释，在网络上能找到很多这样的资料，它们可能是[电子书](https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book.html)或者是MIT的一系列讲座[视频](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-001-structure-and-interpretation-of-computer-programs-spring-2005/video-lectures/)。这些讲座都很不错，但是我们的视频推荐的实际上是伯克利的一门课程：[Brian Harvey’s SICP lectures](https://archive.org/details/ucberkeley-webcast-PL3E89002AA9B9879E?sort=titleSorter) ，这个系列的课程比起MIT的讲座更精炼而且对于入门者更具有针对性。

We recommend working through at least the first three chapters of SICP and doing the exercises. For additional practice, work through a set of small programming problems like those on exercism.

我们推荐观看完至少前三章节的SICP（计算机程序的结构与解释）并且做完相应训练。额外地，可以在 exercism 进行一些编程问题训练。

![image](https://teachyourselfcs.com/sicp.jpg)

For those who find SICP too challenging, we recommend How to Design Programs. For those who find it too easy, we recommend Concepts, Techniques, and Models of Computer Programming.
 
如果你觉得SICP太难，我们推荐*[How to Design Programs](http://www.htdp.org/)*.这本书。如果你觉得它太简单，我们推荐*[Concepts, Techniques, and Models of Computer Programming](https://smile.amazon.com/Concepts-Techniques-Models-Computer-Programming/dp/0262220695/)* 这本书。

### Computer Architecture 
### 计算机体系结构

>Hardware is the platform

– Mike Acton, Engine Director at Insomniac Games
([收看他在Cpp大会上的演讲](https://www.youtube.com/watch?v=rX0ItVEVjHc))


Computer Architecture—sometimes called “computer systems” or “computer organization”—is an important first look at computing below the surface of software. In our experience, it’s the most neglected area among self-taught software engineers.

计算机结构--有的时候被称为“计算机系统”或者“计算机组织”--是了解程序外表下计算机运行的第一步。根据我们的经验，这是自学软件工程师最容易忽略的地方。

The Elements of Computing Systems, also known as “Nand2Tetris” is an ambitious book attempting to give you a cohesive understanding of how everything in a computer works. Each chapter involves building a small piece of the overall system, from writing elementary logic gates in HDL, through a CPU and assembler, all the way to an application the size of a Tetris game.
 
*The Elements of Computing Systems*，也被称为“从与非门到俄罗斯方块”。这是一本让你对于计算机中的每一个零件是怎么工作的有一个整体的理解的雄心勃勃的书。每个章节涉及到建立整体系统中一个小的部分，从写基本的逻辑门到HDL，到CPU和汇编语言，一直到完成一个俄罗斯方块应用程序。

![elements-computing-systems](https://teachyourselfcs.com/elements-computing-systems.jpg)

We recommend reading through the first six chapters of the book and completing the associated projects. This will develop your understanding of the relationship between the architecture of the machine and the software that runs on it.
 
我们推荐阅读书的前六章节并且完成相关的工程。这会提高你对于计算机结构和运行的软件之间关系的理解。

The first half of the book (and all of its projects), are available for free from the Nand2Tetris website. It’s also available as a Coursera course with accompanying videos.

这本书的前半部分（和它的全部工程）在[the Nand2Tetris website](http://www.nand2tetris.org/)上可以免费获得。在[Coursera course with accompanying videos](https://www.coursera.org/learn/build-a-computer)上你也可以找到它们。

In seeking simplicity and cohesiveness, Nand2Tetris trades off depth. In particular, two very important concepts in modern computer architectures are pipelining and memory hierarchy, but both are mostly absent from the text.
 
为了保证课程简单并吸引人，Nand2Tetris 舍弃了深度。特别是现代计算机结构中两个很重要的概念：流水线(pipelining)和内存层级(memory hierarchy)，在书中都没有提及。

Once you feel comfortable with the content of Nand2Tetris, our next suggestion is Patterson and Hennessy’s Computer Organization and Design, an excellent and now classic text. Not every section in the book is essential; we suggest following Berkeley’s CS61C course“Great Ideas in Computer Architecture” for specific readings. The lecture notes and labs are available online, and past lectures are on the Internet Archive.
 
当你觉得看Nand2Tetris已经很简单了，我们下一个建议是Patterson和Hennessy合著的*Computer Organization and Design*——一本杰出的现代经典书籍。不是书中所有的部分都很重要；我们建议跟随[Berkeley’s CS61C 课程](http://inst.eecs.berkeley.edu/~cs61c/sp15/)——Great Ideas in Computer Architecture，作为特殊读物。讲座的笔记和实验环境都是在线的，而且可以在[在这个归档链接](https://archive.org/details/ucberkeley-webcast-PL-XXv-cvA_iCl2-D-FS5mk0jFF6cYSJs_)回看讲座。

### Algorithms and Data Structures ###
### 算法和数据结构

>I have only one method that I recommend extensively—it’s called think before you write.

>— Richard Hamming

We agree with decades of common wisdom that familiarity with common algorithms and data structures is one of the most empowering aspects of a computer science education. This is also a great place to train one’s general problem-solving abilities, which will pay off in every other area of study.

我们根据几十年的通识来看，熟悉通用的算法和数据结构是计算机科学教育中最重要的方面之一。这是一个训练一个人解决问题的通用能力的方式，而且这种能力还可以迁移到其他领域的学习。

There are hundreds of books available, but our favorite is The Algorithm Design Manual by Steven Skiena. He clearly loves this stuff and can’t wait to help you understand it. This is a refreshing change, in our opinion, from the more commonly recommended Cormen, Leiserson, Rivest & Stein, or Sedgewick books. These last two texts tend to be too proof-heavy for those learning the material primarily to help them solve problems.

这个领域有很多优秀的书籍，但是我们最喜欢的是Steven Skiena的*The Algorithm Design Manual* 。他显然喜欢这东西而且也迫不及待地想帮助你学习数据结构和算法。这是令人耳目一新的变化，我们认为这本书相对于被更多人所推荐的Cormen, Leiserson, Rivest & Stein 或者 Sedgewick 的书来说更好。后两本书有些太过于引经据典，对于想通过阅读来解决问题的人来说并不是一个好的选择。

![skiena](https://teachyourselfcs.com/skiena.jpg)


For those who prefer video lectures, Skiena generously provides his online. We also really like Tim Roughgarden’s course, available from Stanford’s MOOC platform Lagunita, or on Coursera. Whether you prefer Skiena’s or Roughgarden’s lecture style will be a matter of personal preference.

对于那些更喜欢讲座视频的人来说，我们推荐Skiena的[讲座](http://www3.cs.stonybrook.edu/~algorith/video-lectures/). 我们也喜欢Tim Roughgarden的课程，在斯坦福的MOOC平台或者[Coursera](https://www.coursera.org/specializations/algorithms)上面可以获得。你喜欢 Skiena 还是 Roughgarden 的讲课风格就是你的个人喜好问题了。

For practice, our preferred approach is for students to solve problems on Leetcode. These tend to be interesting problems with decent accompanying solutions and discussions. They also help you test progress against questions that are commonly used in technical interviews at the more competitive software companies. We suggest solving around 100 random leetcode problems as part of your studies.

说到练习，我们倾向于让学生在Leetcode上面解决问题。LeetCode上面的问题都比较有趣而且有答案和讨论。这上面还可以通过解决各大软件公司广泛应用的技术问题来帮助你测试你的进步。我们建议解决你学习的时候解决大约随机100道LeetCode上面的问题。

Finally, we strongly recommend How to Solve It as an excellent and unique guide to general problem solving; it’s as applicable to computer science as it is to mathematics.

最后，我们强烈推荐《怎样解题》这本书，它针对如何解题进行了精彩绝伦和独特的讲解，既适用于数学也适用于电脑科学。

![polya](https://teachyourselfcs.com/polya.jpg)

### Mathematics for Computer Science ###
### 计算机科学领域的数学

>If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.

>— John von Neumann

In some ways, computer science is an overgrown branch of applied mathematics. While many software engineers try—and to varying degrees succeed—at ignoring this, we encourage you to embrace it with direct study. Doing so successfully will give you an enormous competitive advantage over those who don’t.

在某些方面，计算机科学是应用数学的一个扩展。虽然许多软件工程师忽略了这一点，我们建议你去学习它。好好学习数学会给你比那些不学习它们的人巨大的竞争优势。

The most relevant area of math for CS is broadly called “discrete mathematics”, where “discrete” is the opposite of “continuous” and is loosely a collection of interesting applied math topics outside of calculus. Given the vague definition, it’s not meaningful to try to cover the entire breadth of “discrete mathematics”. A more realistic goal is to build a working understanding of logic, combinatorics and probability, set theory, graph theory, and a little of the number theory informing cryptography. Linear algebra is an additional worthwhile area of study, given its importance in computer graphics and machine learning.

和CS最相关的数学领域是“离散数学”，离散是连续对立面。是微积分之外的一系列的有趣的应用数学的主题。从大体上说，尝试学会全部范围的“离散数学”是没有意义的。更现实一点的做法是对于逻辑学，组合学和概率学，集合论，图论和一些数论告知密码学有一个了解。对于计算机图像学和机器学习来说，线性代数也是一门值得学习的课程。

Our suggested starting point for discrete mathematics is the set of lecture notes by László Lovász. Professor Lovász did a good job of making the content approachable and intuitive, so this serves as a better starting point than more formal texts.

我们建议从László Lovász的[讲座](http://www.cs.elte.hu/~lovasz/dmbook.ps)学起. 这一系列开始学习离散数学。Lovász 教授让学习的内容变得直观生动，比起拘谨的文字，这更利于你学习。

For a more advanced treatment, we suggest Mathematics for Computer Science, the book-length lecture notes for the MIT course of the same name. That course’s video lectures are also freely available, and are our recommended video lectures for discrete math.

接下来，我们推荐[Mathematics for Computer Science](https://courses.csail.mit.edu/6.042/spring17/mcs.pdf), 它是MIT同名课程的讲义。[讲座课程](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/video-lectures/)的视频也是免费的，而且是我们推荐的离散数学的视频课程。

For linear algebra, we suggest starting with the Essence of linear algebra video series, followed by Gilbert Strang’s book and video lectures.

线性代数，我们建议从 [Essence of linear algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) 系列开始学习，接着是Gilbert Strang的[书籍](https://www.amazon.com/Introduction-Linear-Algebra-Gilbert-Strang/dp/0980232775/)和[视频](https://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/video-lectures/)。

### Operating Systems ###
### 操作系统

Operating System Concepts (the “Dinosaur book”) and Modern Operating Systems are the “classic” books on operating systems. Both have attracted criticism for their writing styles, and for being the 1000-page-long type of textbook that gets bits bolted onto it every few years to encourage purchasing of the “latest edition”.

《操作系统的概念》（恐龙书）和《现代操作系统》是经典的操作系统的书籍。这两本书的写作方式都饱受争议，而且为了鼓励你去购买新版，这些长达1000页的书每几年就会添加一些内容。

Operating Systems: Three Easy Pieces is a good alternative that’s freely available online. We particularly like the structure of the book and feel that the exercises are well worth doing.

《Operating Systems: Three Easy Pieces》这本书是一本比较好的可供选择的线上免费读物。我们特别喜欢书的结构和它经典的练习题。

![ostep](https://teachyourselfcs.com/ostep.jpeg)


After OSTEP, we encourage you to explore the design decisions of specific operating systems, through “{OS name} Internals” style books such as Lion's commentary on Unix, The Design and Implementation of the FreeBSD Operating System, and Mac OS X Internals.

读完这本书，我们推荐你去探索一种特定的操作系统的设计方式，比如那些书名中有系统名字的书籍，比如Lion‘s commentary on Unix, The Design and Implementation of the FreeBSD Operating System, 还有 Mac OS X Internals.

A great way to consolidate your understanding of operating systems is to read the code of a small kernel and add features. A great choice is xv6, a port of Unix V6 to ANSI C and x86 maintained for a course at MIT. OSTEP has an appendix of potential xv6 labs full of great ideas for potential projects.

巩固你对于操作系统的理解很好的方式是去读一个小的内核并且添加功能。xv6是一个不错的选择，它是 Unix V6 和 ANSI C 和 X86 的接口，MIT专门有一门课程就是讲这个的。OSTEP（之前提到的）这本书有一个 XV6 的实验附录，里面都是充满潜力项目的好点子。

### Computer Networking ###
### 计算机网络

>You can’t gaze in the crystal ball and see the future. What the Internet is going to be in the future is what society makes it.

>— Bob Kahn

Given that so much of software engineering is on web servers and clients, one of the most immediately valuable areas of computer science is computer networking. Our self-taught students who methodically study networking find that they finally understand terms, concepts and protocols they’d been surrounded by for years.

考虑到很多软件项目都是基于web服务器和客户端的，计算机网络变成计算机科学中一门有实用价值的学科。系统学习过该课程的自学学生发现他们终于理解了围绕了伴随它们很多年的术语，概念，协议等等。

Our favorite book on the topic is Computer Networking: A Top-Down Approach. The small projects and exercises in the book are well worth doing, and we particularly like the “Wireshark labs”, which they have generously provided online.

关于这个主题我们最推荐的书是：《计算机网络——自顶向下方法》。书中的小工程和实验都很好，值得一做。我们非常喜欢它们提供的[Wireshark labs](http://www-net.cs.umass.edu/wireshark-labs/)。

![](https://teachyourselfcs.com/top-down.jpg)

For those who prefer video lectures, we suggest Stanford’s Introduction to Computer Networking course available on their MOOC platform Lagunita.

对于那些喜欢视频课程的人，我们推荐斯坦福MOOC平台上的[Introduction to Computer Networking course](https://lagunita.stanford.edu/courses/Engineering/Networking-SP/SelfPaced/about)

The study of networking benefits more from projects than it does from small exercises. Some possible projects are: an HTTP server, a UDP-based chat app, a mini TCP stack, a proxy or load balancer, and a distributed hash table.

学习网络的好处不仅仅在于做小的实验而且对于工程来说也有很大的好处。可能涉及到的有：一个HTTP的服务器，一个UDP协议的聊天软件，一个[迷你的TCP协议栈](http://jvns.ca/blog/2014/08/12/what-happens-if-you-write-a-tcp-stack-in-python/)，一个代理或者负载平衡器，还有分布式的哈希表等等。

### Databases ###
### 数据库

It takes more work to self-learn about database systems than it does with most other topics. It’s a relatively new (i.e. post 1970s) field of study with strong commercial incentives for ideas to stay behind closed doors. Additionally, many potentially excellent textbook authors have preferred to join or start companies instead.

对于自学者来说，学习数据库系统会比学习其他花费更多的时间。这是一个相对较新的（即1970年代后期）的研究领域。比起写书，许多潜在的杰出教科书作者更愿意去加入或者创办一家公司。

Given the circumstances, we encourage self-learners to generally avoid textbooks and start with the Spring 2015 recording of CS 186, Joe Hellerstein’s databases course at Berkeley, and to progress to reading papers after.

在这种情况下，我们建议自学者放弃教科书而去学习伯克利的Joe Hellerstein的[数据库课程](https://archive.org/details/UCBerkeley_Course_Computer_Science_186)，看完课程再去阅读论文。

One paper particularly worth mentioning for new students is “Architecture of a Database System”, which uniquely provides a high-level view of how relational database management systems (RDBMS) work. This will serve as a useful skeleton for further study.

对于初学者有一篇论文比较推荐的是：“[Architecture of a Database System](http://db.cs.berkeley.edu/papers/fntdb07-architecture.pdf)”,它高屋建瓴地讲解了关系数据库管理系统是如果工作的这一问题。它会为你未来的学习提供一个有用的纲要。

Readings in Database Systems, better known as the databases “Red Book”, is a collection of papers compiled and edited by Peter Bailis, Joe Hellerstein and Michael Stonebraker. For those who have progressed beyond the level of the CS 186 content, the Red Book should be your next stop.

*[Readings in Database Systems](http://www.redbook.io/)*这本书，又被称为数据库红皮书、是一本Peter Bailis、Joe Hellerstein和Michael Stonebraker编辑地论文集。对于那些理解了CS 186内容的人来说，红皮书是你的不二之选。

![](https://teachyourselfcs.com/redbook.jpg)


If you insist on using an introductory textbook, we suggest Database Management Systemsby Ramakrishnan and Gehrke. For more advanced students, Jim Gray’s classic Transaction Processing: Concepts and Techniques is worthwhile, but we don’t encourage using this as a first resource.

如果你坚持要使用一本引导性的教科书，我们推荐Ramakrishnan 和Gehrke的[*Database Management Systems*](https://smile.amazon.com/Database-Management-Systems-Raghu-Ramakrishnan/dp/0072465638/)，对于更优秀的学生，Jim Gray的传统课程[*Transaction Processing: Concepts and Techniques*](https://www.amazon.com/Transaction-Processing-Concepts-Techniques-Management/dp/1558601902)值得一看，但是我们不建议把它当成入门书。

It’s hard to consolidate databases theory without writing a good amount of code. CS 186 students add features to Spark, which is a reasonable project, but we suggest just writing a simple relational database management system from scratch. It will not be feature rich, of course, but even writing the most rudimentary version of every aspect of a typical RDBMS will be illuminating.

不编大量的代码是不能很好的巩固数据库的理论的，CS 186的学生往Spark中添加功能，这是一个很有意义的工程。但是我们建议仅仅是从头写一个简单的关系数据库管理系统。功能可能不是很丰富，但是即使每一个部分都涉及到一些基本功能也很有启发性。

Finally, data modeling is a neglected and poorly taught aspect of working with databases. Our suggested book on the topic is Data and Reality: A Timeless Perspective on Perceiving and Managing Information in Our Imprecise World.

最后，数据模型是一个数据库使用中被忽略和没有被重点学习的方面。我们对于这个课题建议的书籍是：[*Data and Reality: A Timeless Perspective on Perceiving and Managing Information in Our Imprecise World*](https://www.amazon.com/Data-Reality-Perspective-Perceiving-Information/dp/1935504215)

![](https://teachyourselfcs.com/data-reality.jpg)

### Languages and Compilers ###
### 语言和编译器

>Don’t be a boilerplate programmer. Instead, build tools for users and other programmers. Take historical note of textile and steel industries: do you want to build machines and tools, or do you want to operate those machines?

>— Ras Bodik at the start of his compilers course


Most programmers learn languages, whereas most computer scientists learn about languages. This gives the computer scientist a distinct advantage over the programmer, even in the domain of programming! Their knowledge generalizes; they are able to understand the operation of a new language more deeply and quickly than those who have merely learned specific languages.

大部分程序员学习如何使用一门编程语言，然而大部分的计算机科学家则学习这门语言本身。这给了计算机科学家比起程序员很明显的优势。他们的知识能够更好的泛化，他们能比简简单单地掌握一门语言的更加深入和快速的理解一门新语言的操作。

The canonical introductory text is Compilers: Principles, Techniques & Tools, commonly called “the Dragon Book”. Unfortunately, it’s not designed for self-study, but rather for instructors to pick out 1-2 semesters worth of topics for their courses. It’s almost essential then, that you cherry-pick the topics, ideally with the help of a mentor.

经典的教科书《编译器：原理、技术与工具》通常又被称为“龙书”。不幸的是，这本书并不适合自学者，它比较适合教师从中选出1-2个章节并在课堂上讲授。这本书是有必要看的，你可以挑选里面的主题，最好再有个师傅指导你。

![](https://teachyourselfcs.com/dragon.jpg)

If you choose to use the Dragon Book for self-study, we recommend following a video lecture series for structure, then dipping into the Dragon Book as needed for more depth. Our recommended online course is Alex Aiken’s, available from Stanford’s MOOC platform Lagunita.

如果你选择在自学中使用龙书，我们推荐你一系列门视频讲座，然后再沉浸在对于龙书的研究中。我们推荐的在线课程是：Alex Aiken 的[讲座](https://lagunita.stanford.edu/courses/Engineering/Compilers/Fall2014/about)，你可以在斯坦福大学的幕课平台上观看。

As a potential alternative to the Dragon Book we suggest Language Implementation Patterns by Terence Parr. It is written more directly for the practicing software engineer who intends to work on small language projects like DSLs, which may make it more practical for your purposes. Of course, it sacrifices some valuable theory to do so.
 
也有可以替代龙书的教材：Terence Parr写的[*Language Implementation Patterns*](https://smile.amazon.com/Language-Implementation-Patterns-Domain-Specific-Programming/dp/193435645X/)，它更适合那些工作中使用类似特定领域语言的小众语言的有经验的编程者，它显得更加实用。当然，为了达到这个目的它也删去了一些有价值的理论。

![](https://teachyourselfcs.com/parr.jpg)

For project work, we suggest writing a compiler either for a simple teaching language like COOL, or for a subset of a language that interests you. Those who find such a project daunting could start with Make a Lisp, which steps you through the project.

对于工程实践，我们推荐你写一个编译器，你可以选择像COOL这种简单的教学语言或者你感兴趣的一门语言。如果你觉得太难，你可以参考[Make a Lisp](https://github.com/kanaka/mal),你可以参考它作为开始。

### Distributed Systems ###
### 分布式系统

As computers have increased in number, they have also spread. Whereas businesses would previously purchase larger and larger mainframes, it’s typical now for even very small applications to run across multiple machines. Distributed systems is the study of how to reason about the trade-offs involved in doing so, an increasingly important skill.

计算机的数量增长了，它们的分布也更广了。企业之前会购买越来越大型的主机，但是现在大家更倾向于在很多机器上分布式的运行多个小型的应用程序。分布式系统研究的就是这样的技术，这一技术变得越来越重要了。
  
Our suggested textbook for self-study is Maarten van Steen and Andrew Tanenbaum’s Distributed Systems, 3rd Edition. It’s a great improvement over the previous edition, and is available for free online thanks to the generosity of its authors. Given that the distributed systems is a rapidly changing field, no textbook will serve as a trail guide, but Maarten van Steen’s is the best overview we’ve seen of well-established foundations.

我们建议的自学教科书是Maarten van Steen和Andrew Tanenbaum的[*Distributed Systems, 3rd Edition*](https://www.distributed-systems.net/index.php/books/distributed-systems-3rd-edition-2017/) 针对于之前的版本做了很大的改进，而且作者慷慨地把书放在了网上共享。由于分布式计算是一门变化很快的领域，所以没有教科书可以很好的涵盖所有的内容。但是Maarten van Steen的书是我们读过的所有书中最好的书。

![](https://teachyourselfcs.com/distsys.png)

A good course for which some videos are online is MIT’s 6.824 (a graduate course), but unfortunately the audio quality in the recordings is poor, and it’s not clear if the recordings were authorized.

研究生在线课程[MIT’s 6.824](https://www.youtube.com/watch?v=hBWfjkGKRas&list=PLkcQbKbegkMqiWf7nF8apfMRL4P4sw8UL) 也是一个不错的选择，但可惜视频中的音质不太好，而且不清楚这些视频是不是都被授权过。

No matter the choice of textbook or other secondary resources, study of distributed systems absolutely mandates reading papers. A good list is here, and we would highly encourage attending your local Papers We Love chapter.

尽管有参考书或者其它的资源，但学习分布式系统是绝对要读论文的。链接中有一个很好的[清单](http://dsrg.pdos.csail.mit.edu/papers/)，而且我们十分推荐你从[Papers We Love](http://paperswelove.org/) 上面下载论文到本地学习。
  
## Frequently asked questions
## 常见问题

