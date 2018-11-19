---
translator: http://www.jobbole.com/members/hearingdog/
reviewer: http://www.jobbole.com/members/hanxiaomax/
via: https://zwischenzugs.com/2018/03/26/git-log-the-good-parts/
---

# git log – the Good Parts

# 巧用 git log

If you’re managing a complex git codebase with multiple developers, then you may well be using a tool like GitHub or BitBucket to delve into the history and figure out branch and merge issues.

如果你正在与多个开发人员一起管理复杂的 git 代码库，那么你可能正在使用 GitHub 或 BitBucket 等工具来深入研究历史提交记录并找出分支和合并的问题。

These GUIs are great for providing a nice user interface for managing pull requests and simple histories and the like, but when the workflow SHTF there’s no substitute for using `git log` and its relatively little-known flags to really dig into the situation.

GUI 工具为拉取请求和简单历史记录管理等提供良好的用户界面，但当你的工作流面临灭顶之灾时，`git log` 就显得无可比拟了，它的一些鲜为人知的参数选项可以让你真正地了解实际情况。

## An Example Git Repository

## 一个 Git 仓库示例

Run this to download a fairly typical git repository that I work on:

执行以下命令来下载接下来讲述的典型 Git 仓库：

```shell
$ git clone https://github.com/ianmiell/cookbook-openshift3-frozen
$ cd cookbook-openshift3-frozen
```

*NB this is a copy of the original repo, ‘frozen’ here to provide stable output.* 

_注意：这是原始仓库的副本，这里的“frozen”是为了提供稳定的输出版本。_

## `git log`

`git log` is the vanilla log command you are probably already familiar with:

`git log` 可能是你再也熟悉不过的日志命令了：

```shell
$ git log

commit f40f8813d7fb1ab9f47aa19a27099c9e1836ed4f 
Author: Ian Miell <ian.miell@gmail.com>
Date: Sat Mar 24 12:00:23 2018 +0000

pip

commit 14df2f39d40c43f9b9915226bc8455c8b27e841b
Author: Ian Miell <ian.miell@gmail.com>
Date: Sat Mar 24 11:55:18 2018 +0000

ignore

commit 5d42c78c30e9caff953b42362de29748c1a2a350
Author: Ian Miell <ian.miell@gmail.com>
Date: Sat Mar 24 09:43:45 2018 +0000

latest
```

It outputs 5+ lines per commit, with date, author commit message and id. It goes in reverse time order, which makes sense for most cases, as you are mostly interested in what happened recently.

每个提交会输出 5+ 行的内容，包括日期、作者提交信息和 id。它按照时间逆序排列，这对于大多数情况都是合理的，因为你对最近发生的提交最感兴趣。

*NOTE: output can vary depending on version, aliases, and whether you are outputting to a terminal!My version here was 2.7.4.*

_注意：输出的内容可能因为版本、别名以及使用的终端的不同而有所不同！我的 git 版本是 2.7.4。_

## `--oneline`

Most of the time I don’t care about the author or the date, so in order that I can see more per screen, I use `--oneline` to only show the commit id and comment per-commit.

大多数时候，我不关心作者或日期，所以为了能在屏幕上显示更多内容，我会使用 `--oneline` 参数，来只显示每个提交的 id 和注释。

```shell
$ git log --oneline
ecab26a JENKINSFILE: Upgrade from 1.3 only
886111a JENKINSFILE: default is master if not a multi-branch Jenkins build
9816651 Merge branch 'master' of github.com:IshentRas/cookbook-openshift3
bf36cf5 Merge branch 'master' of github.com:IshentRas/cookbook-openshift3
```

## `--decorate`

You might want more information than that, though, like which branch was that commit on? Where are the tags?

但你可能需要更多信息，例如提交的分支、便签。

The `--decorate` flag provides this.

使用 `--decorate` 标志可以做到这一点。

```shell
$ git log --oneline --decorate
ecab26a (HEAD -> master, origin/master, origin/HEAD) JENKINSFILE: Upgrade from 1.3 only
886111a JENKINSFILE: default is master if not a multi-branch Jenkins build
9816651 Merge branch 'master' of github.com:IshentRas/cookbook-openshift3
```

More recent versions of git put this in the terminal by default, so things are improving for my fingers.

最新版本的 git 默认把它加在终端中，你可以手动优化它。

(Remember that your version might do `--decorate` by default fir `git log` when output goes to the terminal instead of a file).

（记住，当你是输出到终端而不文件时，你使用版本的 `--decorate` 可能默认执行了 `git log`。）

## `--all`

```shell
$ git log --oneline --decorate --all
ecab26a (HEAD -> master, origin/master, origin/HEAD) JENKINSFILE: Upgrade from 1.3 only
886111a JENKINSFILE: default is master if not a multi-branch Jenkins build
9816651 Merge branch 'master' of github.com:IshentRas/cookbook-openshift3
[...]
a1eceaf DOCS: Known issue added to upgrade docs
774a816 (origin/first_etcd, first_etcd) first_etcd
7bbe328 first_etcd check
654f8e1 (origin/iptables_fix, iptables_fix) retry added to iptables to prevent race conditions with iptables updates
e1ee997 Merge branch 'development'
```

Can you see what it does? If you can’t, compare it to `--oneline` above and dig around to figure it out.

发现它的作用没？如果没有，可以仔细对比上面使用 `--oneline` 的输出结果。

That’s great, but what would be great is a visual representation of all those branches…

这很好，但最强的功能是对所有的分支可视化……

## `--graph`

`--graph` gives you that visual representation, but in the terminal. While it might not look as slick as some git GUIs, it does have the benefit of being consistently viewed anywhere, and much more configurable to your specific needs.

`--graph` 可以提供可视化显示，但在终端中，它可能看起来不像某些 git GUI 那样灵巧，但它确实对想要浏览各处提交日志提供了很大的便利，并且可以根据你的特定需求进行更多的配置。

And when you’re trying to piece together what happened on a 15-team project that doesn’t rebase, it can be essential…

当你试图拼凑一个 15 人团队没有变基的提交历史时，它可能至关重要……

```shell
$ git log --oneline --decorate --all --graph
* ecab26a (HEAD -> master, origin/master, origin/HEAD) JENKINSFILE: Upgrade from 1.3 only
* 886111a JENKINSFILE: default is master if not a multi-branch Jenkins build
* 9816651 Merge branch 'master' of github.com:IshentRas/cookbook-openshift3
|\ 
| * bf36cf5 Merge branch 'master' of github.com:IshentRas/cookbook-openshift3
| |\ 
| | * 313c03a JENKINSFILE: quick mode is INFO level only
| | * 340a8f2 JENKINSFILES: divided up into separate jobs
| | * 79e82bc JENKINSFILE: upgrades-specific Jenkinsfile added
| * | dce4c71 Add logic for additional FW for master (When not a node)
* | | d21351c Update utils/atomic
|/ / 
* | 3bd51ba Fix issue with ETCD
* | b87091a Add missing FW for HTTPD
|/ 
* a29df49 Missing (s)
* 51dff3a Fix rubocop
```

**DON’T PANIC!**

__不要惊慌__

The above can be hard for the newcomer to parse, and there is little out there to guide you, but a few tips here can make it much easier to read.

上面内容对于新手来说的确是晦涩难懂，并且没有可以指引你的东西，但这里一些技巧可能帮助你更易于阅读。

The `*` indicates that there is a commit on the line, and the details of the commit (here the commit id, and first line of the comment) are on the right hand side.

线上的 `*` 表示一个提交，在右侧则显示了该提交的细节（这里包含提交 id 和提交注释首行）。

The lines and position of the `*` indicate the lineage (or parentage) of each change. So, to take these three lines for example:

线条和 `*` 表示每个变化的系谱（或亲子关系）。以这三行为例：

```shell
| * bf36cf5 Merge branch 'master' of github.com:IshentRas/cookbook-openshift3
| |\ 
| | * 313c03a JENKINSFILE: quick mode is INFO level only
```

The green pipes indicate that while the two changes listed here were going on, another branch had a gap between its two changes (9816651 and d21351c).

绿色的线条表示此处列出两个正在进行的更改，在另外一个分支中，两个更改（9816651 和 d21351c）存在差异。

The blue line takes you to one parent of the bf36cf5 merge (what’s the commit id of the blue parent?), and the pink one goes to the other parent commit (313c03a).

蓝线将告诉你 bf36cf5 合并的父级关系（蓝线父级的提交 id 是什么），粉色的线转向父级的另外一个提交（313c03a）。

It’s worth taking a bit of time to figure out what’s going on here, as it will pay dividends in a crisis later…

这些内容值得你花时间搞清楚，日后遇到棘手问题的时候，你会感到庆幸的。

## `--simplify-by-decoration`

If you’re looking at the whole history of a project and want to get a feel for its shape before diving in, you may want to see only the significant points of change (ie the lines affected by `-–decorate` above).

如果你正在查看项目的整个历史记录，并希望在深入了解之前有个大概的认识，或许你只是想看到一些关键的变更点（即上述没有受到 `-–decorate` 影响的线条）。

These remove any commit that wasn’t tagged, branched (ie there’s no reference). The root commit is always there too.

这里移除了所有没有标记、分支（即没有受到影响）的提交的输出。这些根提交也始终存在。

```shell
$ git log --oneline --decorate --all --graph --simplify-by-decoration
* ecab26a (HEAD -> master, origin/master, origin/HEAD) JENKINSFILE: Upgrade from 1.3 only
| * 774a816 (origin/first_etcd) first_etcd
|/ 
| * 654f8e1 (origin/iptables_fix) retry added to iptables to prevent race conditions with iptables updates
|/ 
* 652b1ff (origin/new-logic-upgrade) Fix issue iwith kitchen and remove sensitive output
* ed226f7 First commit
```

Try tagging a specific commit not listed above, and then re-run the command.

尝试标记上面未列出的某些特定提交，然后重新运行该命令。

## File Info

## 文件信息

Using `--oneline` can be a bit sparse, so `--stat` can give you useful information about what changed.

使用 `--oneline` 可能觉得信息太少，所以 `--stat` 选项可以给你提供更多有关变更内容的有用信息。

The number indicates the numbers of lines that were changed, with insertions represented by a `+` sign, and deletions by a `-`. There’s no concept of a ‘change’ to a line as such: the old line is deleted, and then the new one added even if only one character changed.

数字表示已更改的行数，插入由 `+` 表示，删除由 `-` 表示。这里对行内的“更改”没有支持，例如，删除旧行，这时即使只更改了一个字符也会认为是添加新行。

```shell
$ git log --oneline --decorate --all --graph --stat
* ecab26a (HEAD -> master, origin/master, origin/HEAD) JENKINSFILE: Upgrade from 1.3 only
| Jenkinsfile.upgrades | 2 +-
| 1 file changed, 1 insertion(+), 1 deletion(-)
* 886111a JENKINSFILE: default is master if not a multi-branch Jenkins build
| Jenkinsfile.full | 2 +-
| Jenkinsfile.upgrades | 2 +-
| 2 files changed, 2 insertions(+), 2 deletions(-)
```

If you find `--stat` hard to remember, then an alternative is to use `--name-only`, but with that you lose the information about numbers of changes to files.

如果你觉得 `--stat` 很难记，你可以使用 `--name-only`，但随之而来的是你缺失了有关文件更改次数的信息。

## Regex on Commits

## 对提交使用正则表达式

This one’s also *really* handy. The `-G` flag allows you to search for all commits and only return commits and their files whose changes include that regexp.

这个也很_相当_方便。使用 `-G` 标志可以让你在搜索所有提交时，仅返回符合正则表达式的提交。

This one, for example, looks for changes that contain the text `chef-client`

例如，这个查找包含文字 `chef-client`：

```shell
$ git log -G 'chef-client' --graph --oneline --stat
...
* 22c2b1b Fix script for deploying origin
| scripts/origin_deploy.sh | 65 ++++++++++++-----------------------------------------------------
| 1 file changed, 12 insertions(+), 53 deletions(-)
... 
| * | 1a112bf - Move origin_deploy.sh in scripts folder - Enable HTTPD at startup
| | | origin_deploy.sh | 148 ----------------------------------------------------------------------------------------------------------------------------------------------------
| | | scripts/origin_deploy.sh | 148 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
| | | 2 files changed, 148 insertions(+), 148 deletions(-)
... 
| * | 9bb795d - Add MIT LICENCE model - Add script to auto deploy origin instance
|/ / 
| | origin_deploy.sh | 93 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
| | 1 file changed, 93 insertions(+)
```

If you’ve ever spent ages searching through `git log --patch` output looking for a specific change this is a godsend…

如果你常年使用 `git log --patch` 输出来搜寻特定的变更，那么使用该技巧你将发现一个新世界……

The eccentrically-named `--pickaxe-all` gives you information about *all* files that changed in the commit, rather than just the ones that matched the regexp in the commit.

命名反常的 `--pickaxe-all` 选项可以提供提交中_所有_更改文件的信息，而不是仅仅与提交中与正则表达式匹配的文件。

```shell
$ git log -G 'chef-client' --graph --oneline --stat --pickaxe-all
```

Try it out!

来试试吧！
