# Notes to Myself on Software Engineering

## A laundry list of personal reminders
## 个人提醒细目清单

## On the Development Process
## 关于开发过程

1.Code isn’t just meant to be executed. Code is also a means of communication across a team, a way to describe to others the solution to a problem. Readable code is not a nice-to-have, it is a fundamental part of what writing code is about. This involves factoring code clearly, picking self-explanatory variable names, and inserting comments to describe anything that’s implicit.

1.代码不仅仅意味着执行。代码也是团队间的沟通方式，一种向他人描述问题解决方案的途径。代码可读性不是可有可无，而是写代码的基本目的之一。这涉及清晰地分解代码，选择能不言自明的变量名，以及插入注释来说明任何隐含的内容。

2.Ask not what your pull request can do for your next promotion, ask what your pull request can do for your users and your community. Avoid “conspicuous contribution” at all cost. Let no feature be added if it isn’t clearly helping with the purpose of your product.

2.不要询问你的合并请求（pull request）是否有益于你的升职，而是询问这一合并请求为你的用户和社区能带来什么。尽可能地避免 “表现贡献”。不要添加那些不能明确地有益于你的产品目的的功能。

3.Taste applies to code, too. Taste is a constraint-satisfaction process regularized by a desire for simplicity. Keep a bias toward simplicity.

3.代码也是有品味的。品味是一种因由追求简洁而调整的约束满意过程。始终保持对简单性的偏向。

4.It’s okay to say no — just because someone asks for a feature doesn’t mean you should do it. Every feature has a cost that goes beyond the initial implementation: maintenance cost, documentation cost, and cognitive cost for your users. Always ask: Should we really do this? Often, the answer is simply no.

4.可以说不 - 仅仅因为有人要求某个功能并不意味着你就必须实现它。每个功能都有隐含在初始实现之后的成本：维护成本，文档成本，以及用户的认知成本。总是问一问：我们真的要实现这个功能吗？答案常常是 NO。

5.When you say yes to a request for supporting a new use case, remember that literally adding what the user requested is often not the optimal choice. Users are focused on their own specific use case, and you must counter this with a holistic and principled vision of the whole project. Often, the right answer is to extend an existing feature.

5.当你同意支持一个新的用例需求时，要记得，仅仅添加用户所要求的通常不是最佳选择。用户只关心他们自己的特定用例，而你却必须结合整个项目的整体功能和基本原则来考虑。正确答案一般是扩展现有的某个功能。

6.Invest in continuous integration and aim for full unit test coverage. Make sure you are in an environment where you can code with confidence; if that isn’t the case, start by focusing on building the right infrastructure.

6.增加在持续集成上的投入并且以100%单元测试覆盖率为目标。确保在你所处的环境中你可以自信地编程。如果不是这样的话，着手建立一个好的基础设施。

7.It’s okay not to plan everything in advance. Try things and see how they turn out. Revert incorrect choices early. Make sure you create an environment where that is possible.

7.不需要提前规划所有事情。尝试看看初步效果。及早扭转错误选择。确保你建立了一个可以这么做的环境。

8.Good software makes hard things easy. Just because a problem looks difficult at first doesn’t mean the solution will have to be complex or hard to use. Too often, engineers go with reflex solutions that introduce undesirable complexity (Let’s use ML! Let’s build an app! Let’s add blockchain!) in situations where a far easier, though maybe less obvious, alternative is available. Before you write any code, make sure your solution of choice cannot be made any simpler. Approach everything from first principles.

8.好的软件让事情变容易。一个最初看上去很困难的问题并不意味着解决方案也会很复杂或者很难使用。常常可以看到，工程师下意识提供的方案引入了不必要的复杂度（我们用 ML 吧！写个 APP！加个区块链！），其实可以有简单得多的替换方案，尽管这些方案可能不是那么显而易见。在写任何代码之前，确保你选择的方案不能更简化了。从基本原则入手。

9.Avoid implicit rules. Implicit rules that you find yourself developing should always be made explicit and shared with others or automated. Whenever you find yourself coming up with a recurring, quasi-algorithmic workflow, you should seek to formalize it into a documented process, so that other team members will benefit from the experience. In addition, you should seek to automate in software any part of such a workflow that can be automated (e.g., correctness checks).

9.避免隐性规则。你开发的任何隐性规则总是可以明确表达并且和他人分享，或者自动化。每当你想到一个会反复出现的准算法工作流，你就应该将这个流程用正式的方式形成文档化的流程，这样其它团队成员可以受益于你的经验。此外，你应寻求将任何可能自动化的工作流用软件自动化（比如，正确性检查）。

10.The total impact of your choices should be taken into account in the design process, not just the bits you want to focus on — such as revenue or growth. Beyond the metrics you are monitoring, what total impact does your software have on its users, on the world? Are there undesirable side effects that outweigh the value proposition? What can you do to address them while preserving the software’s usefulness?

10.在设计过程中考虑你的选择的总体影响，而不是仅关注某些点滴 - 比如利润和增长。除了你在监测的那些指标，考虑你的软件对用户有哪些整体影响，对这个世界有哪些影响？是否有不受欢迎的副作用超过了设想的价值？你可以做什么来解决这些问题同时保留软件的可用性？

## Design for ethics. Bake your values into your creations.

# 道德设计。将你的价值观融入你的创作

## On API Design

## 关于 API 设计

1.Your API has users, thus it has a user experience. In every decision you make, always keep the user in mind. Have empathy for your users, whether they are beginners or experienced developers.

1.API 是给用户使用的，因此它有用户体验。在你做的每个决定中，始终牢记用户。不管你的用户是初学者还是有经验的开发者，都对他们抱着同理心。

2.Always seek to minimize the cognitive load imposed on your users in the course of using your API. Automate what can be automated, minimize the actions and choices needed from the user, don’t expose options that are unimportant, design simple and consistent workflows that reflect simple and consistent mental models.

2.在用户使用 API 的过程中，始终寻求最小化他们的认知负担。自动化那些可以自动化的部分，尽量减少用户所需的操作和选择，不要暴露不重要的选项，设计简单一致的工作流以反映简单一致的心理模型。

3.Simple things should be simple, complex things should be possible. Don’t increase the cognitive load of common use cases for the sake of niche use cases, even minimally.

3.简单的事情就是简单的，复杂的事情只是有可能。不要因为小众用例而增加常规用例的认知负担，即使是最低程度地。

4.If the cognitive load of a workflow is sufficiently low, it should be possible for a user to go through it from memory (without looking up a tutorial or documentation) after having done it once or twice.

4.如果一个工作流的认知负担足够低，用户在在做过一、两次之后，应该就可以通过记忆来完成（而不需要查询教程或者文档）。

5.Seek to have an API that matches the mental models of domain experts and practitioners. Someone who has domain experience, but no experience with your API, should be able to intuitively understand your API using minimal documentation, mostly just by looking at a couple of code examples and seeing what objects are available and what their signatures are.

5.寻求与领域专家和从业者的心理模型相匹配的 API。拥有行业经验但没有使用过你的 API 的人，通过最少的文档应该就可以直观地理解你的API，主是要通过查看几个代码范例，以及查看哪些对象可用和它们的特征是怎样的。

6.The meaning of an argument should be understandable without having any context about the underlying implementation. Arguments that have to be specified by users should relate to the mental models that the users have about the problem, not to implementation details in your code. An API is all about the problem it solves, not about how the software works in the background.

6.即使底层实现的上下文不可见，参数的含义应该是可理解的。必须由用户指定的参数应该是与用户对问题的心理模型相关，而不是与代码的实现细节相关。API 的定义归根结底是在于它所解决的问题，而不是在于软件在后台如何工作。

7.The most powerful mental models are modular and hierarchical: simple at a high level, yet precise as you need to go into details. In the same way, a good API is modular and hierarchical: easy to approach, yet expressive. There is a balance to strike between having complex signatures on fewer objects, and having more objects with simpler signatures. A good API has a reasonable number of objects, with reasonably simple signatures.

7.最有效的心理模型是模块化和层次化的：高层简洁，然而但在你需要细节时又是精确的。同样，好的 API 也是模块化和层次化的：易于实现 ，但具有表现力。较少的对象但具有复杂特性，较多的对象但特征简单，这两者之间力争达到平衡。好的 API 拥有合理数量的对量和合理简化的特征。

8.Your API is inevitably a reflection of your implementation choices, in particular your choice of data structures. To achieve an intuitive API, you must choose data structures that naturally fit the domain at hand — that match the mental models of domain experts.

8.你的 API 不可避免地反映了你选择的的实现方式，特别是数据结构的选择。为了实现直观的 API，你得选择能自然地适合当下这一领域的数据结构 - 与领域专家的心理模型相匹配的数据结构。

9.Deliberately design end-to-end workflows, not a set of atomic features. Most developers approach API design by asking: What capabilities should be available? Let’s have configuration options for them. Instead, ask: What are the use cases for this tool? For each use case, what is the optimal sequence of user actions? What’s the easiest API that could support this workflow? Atomic options in your API should answer a clear need that arises in a high-level workflow — they should not be added “because someone might need it.”

9.谨慎地设计端到端工作流，而不是一组原子功能。大多数开发者在设计 API 时会询问：应该具备哪些功能？让我们来为这些功能配置选项吧。相反，开发者应该询问：这个工具的用例是什么？对每一个用例，最佳用户操作顺序是怎样？为了支持这一工作流最简单的 API 是什么？API 中的原子选项应该对应高层工作流中出现的某一明确需求 - 而不是因为某些人可能会需要而添加。

10.Error messages, and in general any feedback provided to a user in the course of interacting with your API, is part of the API. Interactivity and feedback are integral to the user experience. Design your API’s error messages deliberately.

10.错误消息，以及通常在 API 交互过程中提供给用户的任何反馈，都是 API 的一部分。交互性和反馈是用户体验不可或缺的一部分。仔细地设计你的 API 的错误消息。

11.Because code is communication, naming matters — whether naming a project or a variable. Names reflect how you think about a problem. Avoid overly generic names (x, variable, parameter), avoid OverlyLongAndSpecificNamingPatterns, avoid terms that can create unnecessary friction (master, slave), and make sure you are consistent in your naming choices. Naming consistency means both internal naming consistency (don’t call “dim” what is called “axis” in other places) and consistency with established conventions for the problem domain. Before settling on a name, make sure to look up existing names used by domain experts (or other APIs).

11.因为代码即沟通，所以命名很重要，不管是项目命名还是变量命名。名称反映出你对问题的看法。避免过于通用的命名（x,变量，参数），避免过长以及特定命名模式，避免可能导致不必要的摩擦的术语（比如，master,slave）（译注：master和slave有些人认为政治不正确，因为是salve是奴隶的意思），确保在命名选择上保持一致性。命名一致性既包括内部的命名一致性（如果其它地方用的是 “axis"，就不要再用 “dim”)，也包括与问题域既定约定的一致性。在确定名称前，确保查询领域专家在使用的现有名称（或者其它 API)。


12.Documentation is central to the user experience of your API. It is not an add-on. Invest in high-quality documentation; you will see higher returns than investing in more features.

12.文档是用户体检的核心。这可不是附加项。投资高质量的文档，你会看到比投资更多功能具有更高的回报。

13.Show, don’t tell: Your documentation should not talk about how the software works, it should show how to use it. Show code examples for end-to-end workflows; show code examples for each and every common use case and key feature of your API.

13.示范，而不是告知。你的文档不应该讨论软件如何工作，而是示范怎样使用它。给出端到端工作流的代码示例，显示每一 API 及所有常规用例和关键功能的示例代码。

# Productivity boils down to high-velocity decision-making and a bias for action.

生产力归结为快速决策和积极行动

## On Software Careers

## 关于软件职业

1.Career progress is not how many people you manage, it is how much of an impact you make: the differential between a world with and without your work.

1.职业发展不是在于你管理的人数，而是在于你所产生的影响：你的工作存在与否给这个世界造成的差异。

2.Software development is teamwork; it is about relationships as much as it is about technical ability. Be a good teammate. As you go on your way, stay in touch with people.

2.软件开发是团队合作；人际关系与技术能力同样重要。做个好队友。在你继续前进时，和伙伴们保持联系。

3.Technology is never neutral. If your work has any impact on the world, then this impact has a moral direction. The seemingly innocuous technical choices we make in software products modulate the terms of access to technology, its usage incentives, who will benefit, and who will suffer. Technical choices are also ethical choices. Thus, always be deliberate and explicit about the values you want your choices to support. Design for ethics. Bake your values into your creations. Never think, I’m just building the capability; that in itself is neutral. It is not because the way you build it determines how it will get used.

3.技术从来不是中立的。如果你的工作对这个世界有任何影响，那么这个影响就有道德方向。我们在软件产品中看上去无害的技术选择，影响着技术获取的条件，技术使用的激励，谁将获得利益，谁将蒙受损失。技术选择也是道德选择。因此，始终谨慎而明确地表达您的选择所希望支持的价值观。为道德设计。将你的价值观融入你的创作。永远不要认为，你只是在建立一种能力，而这种能力本身是中立的。不是这样的，因为你构建它的方式决定了它将如何被使用。

4.Self-direction — agency over your work and your circumstances — is the key to life satisfaction. Make sure you grant sufficient self-direction to the people around you, and make sure your career choices result in greater agency for yourself.

4.自我导向 - 掌控你的工作和你的环境 - 这是生活满意度的关键。确保给予身边的人足够的自我导向，并且确保你的职业选择为你带来更多的控制能力。

5.Build what the world needs — not just what you wish you had. Too often, technologists live rarefied lives and focus on products catering to their own specific needs. Seek opportunities to broaden your life experience, which will give you better visibility into what the world needs.

5.制造这个世界需要的东西 - 而不是你希望拥有的东西。技术人员常常过着阳春白雪的生活，专注于满足自身特定需求的产品。你要寻找机会拓宽生活体验，让你更好地了解这个世界的需求。

6.When making any choice with long-term repercussions, place your values above short-term self-interest and passing emotions — such as greed or fear. Know what your values are, and let them guide you.

6.在做任何具有长期影响的决定时，将你的价值观置于短期自身利益和情绪之上 - 例如贪婪或恐惧。了解你的价值观是什么，让它引导你的行动。

7.When we find ourselves in a conflict, it’s a good idea to pause to acknowledge our shared values and our shared goals, and remind ourselves that we are, almost certainly, on the same side.

7.发现自己面对冲突时，明智的做法是暂停冲突并承认共同的价值观和共同目标，提醒自己我们都是在同一阵营的。

8.Productivity boils down to high-velocity decision-making and a bias for action. This requires a) good intuition, which comes from experience, so as to make generally correct decisions given partial information, b) a keen awareness of when to move more carefully and wait for more information, because the cost of an incorrect decision would be greater than cost of the delay. The optimal velocity/quality decision-making tradeoff can vary greatly in different environments.

8.生产力归结为快速决策和积极行动。这需要 a）优秀的直觉，这来源于经验，以便在只给出部分信息的情况下可以做出基本正确的决定，b）敏锐地察觉到何时应更谨慎地行动并求证更多信息，因为错误决策的成本会比延迟决策的成本更高。在不同环境中，最佳速度/最佳质量的决策权衡可以有极大差异。

9.Making decisions faster means you make more decisions over the course of your career, which will give you stronger intuition about the correctness of available options. Experience is key to productivity, and greater productivity will provide you with more experience: a virtuous cycle.

9.快速决策意味着你可以职业生涯中做出更多的决定，这将会让你对可用选项的正确性有更强烈的直觉。经验是生产力的关键，更高的生产力为你提供更多的经验：良性循环。

10.In situations where you are aware that your intuition is lacking, adhere to abstract principles. Build up lists of tried-and-true principles throughout your career. Principles are formalized intuition that generalize to a broader range of situations than raw pattern recognition (which requires direct and extensive experience of similar situations)。
 
10.如果你意识到你缺乏直觉，在这种情况下，请遵循抽象原则。在整个职业生涯中建立一个试探性原则。所谓原则就是形式化的直觉，其相比原始模式识别（需要对类似情况有直接和广泛的经验）可以推广到更广泛的情境。
