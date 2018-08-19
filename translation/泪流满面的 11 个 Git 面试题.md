---
translator: http://www.jobbole.com/members/hearingdog/
reviewer: http://www.jobbole.com/members/hanxiaomax/
via: https://dev.to/aershov24/11-painful-git-interview-questions-you-will-cry-on-1n2g
---

# 泪流满面的 11 个 Git 面试题

# 11 Painful Git Interview Questions You Will Cry On

[![11 Painful Git Interview Questions and Answers You Will Cry On](https://res.cloudinary.com/practicaldev/image/fetch/s--ZdnrNCoZ--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://images.pexels.com/photos/929382/pexels-photo-929382.jpeg%3Fauto%3Dcompress%26cs%3Dtinysrgb%26h%3D350)](https://res.cloudinary.com/practicaldev/image/fetch/s--ZdnrNCoZ--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://images.pexels.com/photos/929382/pexels-photo-929382.jpeg%3Fauto%3Dcompress%26cs%3Dtinysrgb%26h%3D350)

According to the latest Stack Overflow developer survey, more than 70 percent of developers use Git, making it the most-used VCS in the world. Git is commonly used for both open source and commercial software development, with significant benefits for individuals, teams and businesses.

在最新的 Stack Overflow 开发者调查报告中，超过 70% 的开发者使用 Git，使其成为世界上使用人数最多的 VCS。Git 通常用于开源和商业软件开发，对个人、团队和企业都颇有益处。

### Q1: What is Git fork? What is difference between fork, branch and clone?

### 问题一：什么是 Git 复刻（fork）？复刻（fork）、分支（branch）和克隆（clone）之间有什么区别？

> 主题：**Git**
> 难度：⭐⭐

- A **fork** is a remote, server-side copy of a repository, distinct from the original. A fork isn't a Git concept really, it's more a political/social idea.
- A **clone** is not a fork; a clone is a local copy of some remote repository. When you clone, you are actually copying the entire source repository, including all the history and branches.
- A **branch** is a mechanism to handle the changes within a single repository in order to eventually merge them with the rest of code. A branch is something that is within a repository. Conceptually, it represents a thread of development.

- __复刻（fork）__ 是对存储仓库（repository）进行的远程的、服务器端的拷贝，从源头上就有所区别。复刻实际上不是 Git 的范畴。它更像是个政治/社会概念。
- __克隆（clone）__ 不是复刻，克隆是个对某个远程仓库的本地拷贝。克隆时，实际上是拷贝整个源存储仓库，包括所有历史记录和分支。
- __分支（branch）__ 是一种机制，用于处理单一存储仓库中的变更，并最终目的是用于与其他部分代码合并。

🔗**来源：** [stackoverflow.com](https://stackoverflow.com/questions/3329943/git-branch-fork-fetch-merge-rebase-and-clone-what-are-the-differences/)

### Q2: What's the difference between a "pull request" and a "branch"?

### 问题二：“拉取请求（pull request）”和“分支（branch）”之间有什么区别？

> 主题：**Git**
> 难度：⭐⭐

- A **branch** is just a separate version of the code.
- A **pull request** is when someone take the repository, makes their own branch, does some changes, then tries to merge that branch in (put their changes in the other person's code repository).

- __分支（branch）__ 是代码的一个独立版本。
- __拉取请求（pull request）__ 是当有人用仓库，建立了自己的分支，做了些修改并合并到该分支（把自己修改应用到别人的代码仓库）。

🔗**来源：** [stackoverflow.com](https://stackoverflow.com/questions/19059838/whats-the-difference-between-a-pull-request-and-a-branch)

### Q3: What is the difference between "git pull" and "git fetch"?

### 问题三：“git pull”和“git fetch”之间有什么区别？

> 主题：**Git**
> 难度：⭐⭐

In the simplest terms, `git pull` does a `git fetch` followed by a `git merge`.

简单来说，`git pull` 是 `git fetch` + `git merge`。

- When you use `pull`, Git tries to automatically do your work for you. **It is context sensitive**, so Git will merge any pulled commits into the branch you are currently working in. `pull` **automatically merges the commits without letting you review them first**. If you don’t closely manage your branches, you may run into frequent conflicts.
- When you `fetch`, Git gathers any commits from the target branch that do not exist in your current branch and **stores them in your local repository**. However, **it does not merge them with your current branch**. This is particularly useful if you need to keep your repository up to date, but are working on something that might break if you update your files. To integrate the commits into your master branch, you use `merge`.

- 当你使用 `pull`，Git 会试着自动为你完成工作。__它是上下文（工作环境）敏感的__，所以 Git 会把所有拉取的提交合并到你当前处理的分支中。`pull` 则是 __自动合并提交而没有让你复查的过程__。如果你没有细心管理你的分支，你可能会频繁遇到冲突。
- 当你 `fetch`，Git 会收集目标分支中的所有不存在的提交，并__将这些提交存储到本地仓库中__。但__Git 不会把这些提交合并到当前分支中__。这种处理逻辑在当你需要保持仓库更新，在更新文件时又希望处理可能中断的事情时，这将非常实用。而将提交合并到主分支中，则该使用 `merge`。

🔗**来源：** [stackoverflow.com](https://stackoverflow.com/questions/292357/what-is-the-difference-between-git-pull-and-git-fetch)

### Q4: How to revert previous commit in git?

### 问题四：如在 Git 恢复先前的提交？

> 主题：**Git**
> 难度：⭐⭐⭐

Say you have this, where C is your HEAD and (F) is the state of your files.

假设你的情形是这样，其中 C 是你的 HEAD，(F) 是你文件的状态。

```
   (F)
A-B-C
    ↑
  master
```

- To nuke changes in the commit:

- 要修改提交中的更改：

```shell
git reset --hard HEAD~1
```

Now B is the HEAD. Because you used --hard, your files are reset to their state at commit B.

现在 B 是 HEAD，因为你使用了 `--hard`，所以你的文件将重置到提交 B 时的状态。

- To undo the commit but keep your changes:

- 要撤销提交但保留更改：

```shell
git reset HEAD~1
```

Now we tell Git to move the HEAD pointer back one commit (B) and leave the files as they are and `git status` shows the changes you had checked into C.

现在我们告诉 Git 将 HEAD 指针移回（后移）一个提交（B），并保留文件原样，然后你可以 `git status` 来显示你已经检入 C 的更改。

- To undo your commit but leave your files and your index

- 撤销提交但保留文件和索引：

```
git reset --soft HEAD~1
```

When you do `git status`, you'll see that the same files are in the index as before.

执行此操作后，`git status`，你讲看到索引中的文件跟以前一致。

🔗**来源：** [stackoverflow.com](https://stackoverflow.com/questions/927358/how-to-undo-the-most-recent-commits-in-git)

### Q5: What is "git cherry-pick"?

### 问题五：什么是“git cherry-pick”？

> 主题：**Git**
> 难度：⭐⭐⭐

The command git *cherry-pick* is typically used to introduce particular commits from one branch within a repository onto a different branch. A common use is to forward- or back-port commits from a maintenance branch to a development branch.

命令 `git cherry-pick` 通常用于把特定提交从存储仓库的一个分支引入到其他分支中。常见的用途是从维护的分支到开发分支进行向前或回滚提交。

This is in contrast with other ways such as merge and rebase which normally apply many commits onto another branch.

这与其他操作（例如：合并（merge）、变基（rebase））形成鲜明对比，后者通常是把许多提交应用到其他分支中。

Consider:

小结：

```shell
git cherry-pick <commit-hash>
```

🔗**来源：** [stackoverflow.com](https://stackoverflow.com/questions/9339429/what-does-cherry-picking-a-commit-with-git-mean)

### Q6: Explain the advantages of Forking Workflow

### 问题六：解释 Forking 工作流程的优点

> 主题：**Git**
> 难度：⭐⭐⭐

The **Forking Workflow** is fundamentally different than other popular Git workflows. Instead of using a single server-side repository to act as the “central” codebase, it gives every developer their own server-side repository. The Forking Workflow is most often seen in public open source projects.

__Forking 工作流程__与其他流行的 Git 工作流程有着根本的区别。它不是用单个服务端仓库充当“中央”代码库，而是为每个开发者提供自己的服务端仓库。Forking 工作流程最常用于公共开源项目中。

The *main advantage* of the Forking Workflow is that contributions can be integrated without the need for everybody to push to a single central repository that leads to a clean project history. Developers push to their own server-side repositories, and only the project maintainer can push to the official repository.

Forking 工作流程的__主要优点__是可以汇集提交贡献，又无需每个开发者提交到一个中央仓库中，从而实现干净的项目历史记录。开发者可以推送（push）代码到自己的服务端仓库，而只有项目维护人员才能直接推送（push）代码到官方仓库中。

When developers are ready to publish a local commit, they push the commit to their own public repository—not the official one. Then, they file a pull request with the main repository, which lets the project maintainer know that an update is ready to be integrated.

当开发者准备发布本地提交时，他们的提交会推送到自己的公共仓库中，而不是官方仓库。然后他们向主仓库提交请求拉取（pull request），这会告知项目维护人员有可以集成的更新。

🔗**来源：** [atlassian.com](https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow)

### Q7: Tell me the difference between HEAD, working tree and index, in Git?

### 问题七：告诉我 Git 中 HEAD、工作树和索引之间的区别？

> 主题：**Git**
> 难度：⭐⭐⭐

- The **working tree/working directory/workspace** is the directory tree of (source) files that you see and edit.
- The **index/staging area** is a single, large, binary file in /.git/index, which lists all files in the current branch, their sha1 checksums, time stamps and the file name - it is not another directory with a copy of files in it.
- **HEAD** is a reference to the last commit in the currently checked-out branch.

- 该__工作树/工作目录/工作空间__是你看到和编辑的（源）文件的目录树。
- 该__索引/中转区（staging area）__是个在 `/.git/index`，单一的、庞大的二进制文件，该文件列出了当前分支中所有文件的 SHA1 检验和、时间戳和文件名，它不是个带有文件副本的目录。
- __HEAD__是当前检出分支的最后一次提交的引用/指针。

🔗**来源：** [stackoverflow.com](https://stackoverflow.com/questions/3689838/whats-the-difference-between-head-working-tree-and-index-in-git)

### Q8: Could you explain the Gitflow workflow?

### 问题八：你能解释下 Gitflow 工作流程吗？

> 主题：**Git**
> 难度：⭐⭐⭐

Gitflow workflow employs two parallel *long-running* branches to record the history of the project, `master` and `develop`:

Gitflow 工作流程使用两个并行的、__长期运行__的分支来记录项目的历史记录，分别是 `master` 和 `develop` 分支。

- **Master** - is always ready to be released on LIVE, with everything fully tested and approved (production-ready).
	- **Hotfix** - Maintenance or “hotfix” branches are used to quickly patch production releases. Hotfix branches are a lot like release branches and feature branches except they're based on `master`instead of `develop`.

- __Master__，随时准备发布线上版本的分支，其所有内容都是经过全面测试和核准的（生产就绪）。
	+ __Hotfix__，维护（maintenance）或修复（hotfix）分支是用于给快速给生产版本修复打补丁的。修复（hotfix）分支很像发布（release）分支和功能（feature）分支，除非它们是基于 `master` 而不是 `develop` 分支。

- **Develop** - is the branch to which all feature branches are merged and where all tests are performed. Only when everything’s been thoroughly checked and fixed it can be merged to the `master`.
	- **Feature** - Each new feature should reside in its own branch, which can be pushed to the `develop` branch as their parent one.

- __Develop__，是合并所有功能（feature）分支，并执行所有测试的分支。只有当所有内容都经过彻底检查和修复后，才能合并到 `master` 分支。
	+ __Feature__，每个功能都应留在自己的分支中开发，可以推送到 `develop` 分支作为功能（feature）分支的父分支。

[![Gitflow workflow](https://res.cloudinary.com/practicaldev/image/fetch/s--pLQxGakq--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://wac-cdn.atlassian.com/dam/jcr:61ccc620-5249-4338-be66-94d563f2843c/05%2520%282%29.svg%3FcdnVersion%3Dji)](https://res.cloudinary.com/practicaldev/image/fetch/s--pLQxGakq--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://wac-cdn.atlassian.com/dam/jcr:61ccc620-5249-4338-be66-94d563f2843c/05%2520%282%29.svg%3FcdnVersion%3Dji)

🔗**来源：** [atlassian.com](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)

### Q9: When should I use "git stash"?

### 问题九：什么时候应使用 “git stash”？

> 主题：**Git**
> 难度：⭐⭐⭐

The `git stash` command takes your uncommitted changes (both staged and unstaged), saves them away for later use, and then reverts them from your working copy.

`git stash` 命令把你未提交的修改（已暂存（staged）和未暂存的（unstaged））保存以供后续使用，以后就可以从工作副本中进行还原。

Consider:

回顾：

```shell
$ git status
On branch master
Changes to be committed:
new file: style.css
Changes not staged for commit:
modified: index.html
$ git stash
Saved working directory and index state WIP on master: 5002d47 our new homepage
HEAD is now at 5002d47 our new homepage
$ git status
On branch master
nothing to commit, working tree clean
```

The one place we could use stashing is if we discover we forgot something in our last commit and have already started working on the next one in the same branch:

我们可以使用暂存（stash）的一个地方是，如果我们发现在上次提交中忘记了某些内容，并且已经开始在同一分支中处理下一个提交了：

```shell
# Assume the latest commit was already done
# start working on the next patch, and discovered I was missing something

# stash away the current mess I made
$ git stash save

# some changes in the working dir

# and now add them to the last commit:
$ git add -u
$ git commit --ammend

# back to work!
$ git stash pop
```

🔗**来源：** [atlassian.com](https://www.atlassian.com/git/tutorials/saving-changes/git-stash)

### Q10: How to remove a file from git without removing it from your file system?

### 问题十：如何从 git 中删除文件，而不将其从文件系统中删除？

> 主题：**Git**
> 难度：⭐⭐⭐⭐

If you are not careful during a `git add`, you may end up adding files that you didn’t want to commit. However, `git rm` will remove it from both your staging area (index), as well as your file system (working tree), which may not be what you want.

如果你在 `git add` 过程中误操作，你最终会添加不想提交的文件。但是，`git rm` 则会把你的文件从你暂存区（索引）和文件系统（工作树）中删除，这可能不是你想要的。

Instead use `git reset`:

换成 `git reset` 操作：

```
git reset filename          # or
echo filename >> .gitingore # add it to .gitignore to avoid re-adding it
```

This means that `git reset <paths>` is the opposite of `git add <paths>`.

上面意思是，`git reset <paths>` 是 `git add <paths>` 的逆操作。

🔗**来源：** [codementor.io](https://www.codementor.io/citizen428/git-tutorial-10-common-git-problems-and-how-to-fix-them-aajv0katd)

### Q11: When do you use "git rebase" instead of "git merge"?

### 问题十一：是么时候使用“git rebase”代替“git merge”？

> 主题：**Git**
> 难度：⭐⭐⭐⭐⭐

Both of these commands are designed to integrate changes from one branch into another branch - they just do it in very different ways.

这两个命令都是把修改从一个分支集成到另一个分支上，它们只是以非常不同的方式进行。

Consider before merge/rebase:

考虑一下场景，在合并和变基前：

```
A <- B <- C    [master]
^
 \
  D <- E       [branch]
```

after `git merge master`:

在 `git merge master` 之后：

```
A <- B <- C
^         ^
 \         \
  D <- E <- F
```

after `git rebase master`:

在 `git rebase master` 之后：

```
A <- B <- C <- D <- E
```

With rebase you say to use another branch as the new base for your work.

使用变基时，意味着使用另一个分支作为集成修改的新基础。

**When to use:**

__何时使用：__

1. If you have any doubt, use merge.
2. The choice for rebase or merge based on what you want your history to look like.

1. 如果你对修改不够果断，请使用合并操作。
2. 根据你希望的历史记录的样子，而选择使用变基或合并操作。

**More factors to consider:**

__更多需要考虑的因素：__

1. **Is the branch you are getting changes from shared with other developers outside your team (e.g. open source, public)?** If so, don't rebase. Rebase destroys the branch and those developers will have broken/inconsistent repositories unless they use `git pull --rebase`.
2. **How skilled is your development team?** Rebase is a destructive operation. That means, if you do not apply it correctly, you could lose committed work and/or break the consistency of other developer's repositories.
3. **Does the branch itself represent useful information?** Some teams use the *branch-per-feature* model where each branch represents a feature (or bugfix, or sub-feature, etc.) In this model the branch helps identify sets of related commits. In case of *branch-per-developer* model the branch itself doesn't convey any additional information (the commit already has the author). There would be no harm in rebasing.
4. **Might you want to revert the merge for any reason?** Reverting (as in undoing) a rebase is considerably difficult and/or impossible (if the rebase had conflicts) compared to reverting a merge. If you think there is a chance you will want to revert then use merge.

1. __分支是否与团队外部的开发人员共享修改（如开源、公开项目）？__如果是这样，请不要使用变基操作。变基会破坏分支，除非他们使用 `git pull --rebase`，否则这些开发人员将会得到损坏的或不一致的仓库。
2. __你的开发团队技术是否足够娴熟？__变基是一种破坏性操作。这意味着，如果你没有正确使用它，你可能会丢失提交，并且/或者会破坏其他开发者仓库的一致性。
3. __分支本身是否代表有用的信息？__一些团队使用__功能分支（branch-per-feature）__模式，每个分支代表一个功能（或错误修复，或子功能等）。在此模式中，分支有助于识别相关提交的集合。在每个__开发人员分支（branch-per-developer）__模式中，分支本身不会传达任何其他信息（提交信息已有作者）。则在这种模式下，变基不会有任何破坏。
4. __是否无论如何都要还原合并？__恢复（如在撤销中）变基，是相当困难的，并且/或者在变基中存在冲突时，是不可能完成的。如果你考虑到日后可能需要恢复，请使用合并操作。

🔗**来源：** [stackoverflow.com](https://stackoverflow.com/questions/804115/when-do-you-use-git-rebase-instead-of-git-merge)
