## 常见操作
### 基本操作
|                          |                                 |                   |
| ------------------------ | ------------------------------- | ----------------- |
|                          | git clone \<URL\> -b \<branch\> | git clone \<URL\> |
| 更新                     | git pull                        |
| 查看下当前的状态         | git status                      |
| 看下文件到底改了什么内容 | git diff \<file\>               |
| 添加到暂存区             | git add -u                      | git add \<file\>  |
|                          | git commit -m "Command"         |
|                          | git push                        |
### 回退
|                  |                          |                  |
| ---------------- | ------------------------ | ---------------- |
| 查看下历史记录   | git log                  |
| 回退到某个版本   | git reset --hard 6fcfc89 |
|                  |                          |                  |
| 丢弃工作区的修改 | git checkout -- \<file\> | git add 前的修改 |
| 创建分支         | git checkout \<branch\>  |

### 分支
|                  |                            |                                                                      |
| ---------------- | -------------------------- | -------------------------------------------------------------------- |
| 查看分支         | git branch                 |
|                  | git branch --list          |
| 创建分支         | git branch \<branch\>      |
| 切换分支         | git checkout \<branch\>    |
| 创建+切换分支    | git checkout –b \<branch\> | 相当于如下2条命令    git branch \<branch\> & git checkout \<branch\> |
| 删除分支         | git branch -d \<branch\>   | 未合并的变更时，Git会阻止这一次删除操作。                            |
|                  | git branch -D \<branch\>   | 强制删除指定分支                                                     |
| 重命名当前分支   | git branch -m \<branch\>   |
| 列举所有远程分支 | git branch -a              |


### 合并
|                      |                      |                                                                             |
| -------------------- | -------------------- | --------------------------------------------------------------------------- |
| 合并某分支到当前分支 | git merge \<branch\> | \<\<\<HEAD是指当前分支修改的内容 <br>\>\>\>\>\>fenzhi1 是指其他上修改的内容 |

### 冲突
保存到暂存区，再进行stash
|                                                      |                           |     |
| ---------------------------------------------------- | ------------------------- | --- |
|                                                      | git add                   |
| 隐藏修改的文件                                       | git stash save "Command"  |
| 释放出之前修改的文件，并删除stash                    | git stash pop stash@(1)   |
| 释放出之前修改的文件                                 | git stash apply stash@(1) |
| 展示出所有stash信息的列表，左边标题的形式是stash@{n} | git stash list            |
| 这个命令是要丢弃掉指定的一个stash条目                | git stash drop stash@{n}  |
| 清除所有的stash的信息                                | git stash clear           |

### 参考资料
*[Git 使用教程：最详细、最傻瓜、最浅显、真正手把手教！（万字长文）](https://zhuanlan.zhihu.com/p/135183491)
*[stash —— 一个极度实用的Git操作](https://zhuanlan.zhihu.com/p/52429552)