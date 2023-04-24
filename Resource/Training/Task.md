[TOC]
# 准备工作
1. 软件：
   * VS Code
2. 插件：
   * Markdown All in One
   * Markdown Preview Enhanced

# 任务书1
## 学习内容
1. 了解Linux文件系统（参考《鸟哥的Linux私房菜》）
2. man命令的使用（查询命令，系统函数使用说明等）
3. 了解Linux常用系统命令（man、apt、cd、ls、pwd、cat、tail、head、mkdir、mv、rm、tar等）
4. 了解ssh，学习使用ssh和scp命令

## 扩展
1. ctrl组合键相关命令（如ctrl+c等）
2. 整理查看系统资源（磁盘空间、内存、网卡、进程等）的相关命令（如ps、netstat等）

## 要求
<font color="red">注：在理解的基础上，练习命令，保存练习记录（截图），并记[笔记](Task1/Note/Linux.md)。</font>
1. **概念**
    需要理解，用自己的语言可以复述。
2. **命令**
    常用的参数搭配，可以条件反射。
    不常用的参数，有个概念，通过笔记能够查到就可以。

## 考核形式
==整个学习周期==，根据要求，敲命令。


# 任务书2
## 学习内容
1. git介绍，流程、常用操作学习
[GIT 菜鸟教程](https://www.runoob.com/git/git-tutorial.html)
[git学习网站](https://learngitbranching.js.org/?locale=zh_CN)
《基于git的分支开发流程介绍.pdf》
1. gitlab使用，http://10.0.31.16
2. vim使用（三种模式切换，常用命令，快捷键等）
[VIM 菜鸟教程](https://www.runoob.com/linux/linux-vim.html)

## 扩展
1. git merge和cherry-pick的区别

## 要求
<font color="red">注：在理解的基础上，练习命令，保存练习记录（截图），并记[Git笔记](Task2/Note/Git.md)和[Vim笔记](Task2/Note/Vim.md)。</font>
1. Git
    能够熟练使用Git工具；通过命令导入、导出diff。
2. Vim
    能够熟练使用Vim工具。学习期间，唯一官方指定编辑器。

## 考核形式
==整个学习周期==，根据要求，敲命令。


# 任务书3
## 学习内容
1. shell脚本（变量、参数传递、数组、运算符、echo、输入输出重定向，可参考菜鸟教程）
<font color="red">注：shell脚本的学习分两天，这是第一天的内容。</font>
[shell 菜鸟教程](https://www.runoob.com/linux/linux-shell.html)
2. grep, sed, awk命令（能使用这三个命令对文件内容实施增删查改操作，可参考菜鸟教程）
[grep 菜鸟教程](https://www.runoob.com/linux/linux-comm-grep.html)
[sed 菜鸟教程](https://www.runoob.com/linux/linux-comm-sed.html)
[awk 菜鸟教程](https://www.runoob.com/linux/linux-comm-awk.html)
<font color="red">注：不局限于以上参考资料，可结合man命令和其它资料学习。</font>
3. 文件操作命令（文件的创建、删除、查找、内容修改、权限设置）

## 扩展
1. 使用crontab设置一个定时任务，每隔1分钟在用户目录下创建一个文件，文件中保存的内容为hello world。（退出终端后10分钟，再进入应存在10个文件，文件名要有顺序，如1.txt，2.txt，或者以创建的时间点命名）。

## 要求
<font color="red">注：动手练习，保存练习记录（截图或文件），并记[shell笔记](Task3/Note/Shell.md)，拷贝原Linux笔记到当前任务中，并在此基础上整理[Linux笔记](Task3/Note/Linux.md)。</font>
1. 了解shell基本语法，能编写简单的脚本。
2. 熟记文件操作命令及常用参数。

## 考核形式
==整个学习周期==，口头问答或根据要求，敲命令。


# 任务书4
## 学习内容
1. shell脚本（流程控制if/for/while/until/case，函数封装，Shell文件包含，正则表达式基础）
[shell 菜鸟教程](https://www.runoob.com/linux/linux-shell.html)
2. 了解Linux环境变量及如何配置。
3. Linux程序的前/后台执行和切换。
4. 查看和结束进程。

## 扩展
1. 编写一个自动ping并分析结构的脚本，有以下要求：
    a. ping 某个ip地址10秒，如ping 10.0.31.16这个地址10秒，IP地址通过脚本参数传入。
    b. 收集ping的日志，保存为ping_result.txt。
    c. 处理ping的日志并输出以下格式的结果：
    ```
       例：./ping_ip.sh 10.0.31.16
       ping x.x.x.x
       packets transmitted: 10
       packets received: 10
       packet loss: %0
       time: 9024ms
       rtt max: 1.802 ms
    ```

## 要求
<font color="red">注：动手练习，保存练习记录（截图或文件），拷贝[shell笔记](Task3/Note/Shell.md)到当前任务中并在此基础上整理shell笔记，拷贝原Linux笔记到当前任务中，并在此基础上整理[Linux笔记](Task3/Note/Linux.md)。</font>
1. 了解shell基本语法，能编写简单的脚本。
2. 掌握环境变量的定义和设置方法。
3. 熟练掌握linux任务的前后台切换操作。
4. 掌握查看和结束进程的方法。

## 考核形式
==整个学习周期==，口头问答或根据要求，敲命令。


# 任务书5
## 学习内容
1. 了解C语言变量、数据类型、printf、scanf、循环、判断、数组、内存中的存储空间、函数。
参考：[C语言-菜鸟教程](https://www.runoob.com/cprogramming/c-tutorial.html) [C语言中文网](http://c.biancheng.net/c/)
3. 学习gcc的使用，了解C语言的编译过程。
4. 学习C语言编程规范。（自行安排学习计划，3天内看完，建议先浏览标题，不懂再看具体内容）
5. 了解makefile。
参考：[跟我一起写 Makefile](https://blog.csdn.net/whitefish520/article/details/103968609)

## 要求
<font color="red">注：动手练习，保存练习记录（截图或文件），并整理笔记到[C 语言](Task5/Note/C.md)和[代码规范](Task5/Note/Rule.md)。</font>
1. 掌握当天的C语言相关语法和知识点。
2. 掌握gcc的使用方法。
3. 掌握Makefile的基本语法。
4. 练习过程中使用vim，并按照C语言编程规范进行实践。


# 任务书6
## 学习内容
1. c语言。（结构体、共用体、枚举、内存中的存储空间、指针、函数指针和回调函数）
参考：[C语言-菜鸟教程](https://www.runoob.com/cprogramming/c-tutorial.html) [C语言中文网](http://c.biancheng.net/c/)
2. 学习gdb使用。
3. 学习C语言编程规范。（第二天）

## 要求
<font color="red">注：动手练习，保存练习记录（截图或文件），拷贝原[C 语言](Task5/Note/C.md)笔记到当前任务中并整理笔记到[C 语言](Task6/Note/C.md)，拷贝原[代码规范](Task5/Note/Rule.md)笔记到当前任务中并整理笔记到[代码规范](Task6/Note/Rule.md)。</font>
1. 掌握当天的C语言相关语法和知识点。
2. 掌握gdb的使用方法。
3. 练习过程中使用vim，并按照C语言编程规范进行实践。


# 任务书7
## 学习内容
1. c语言（宏定义，typedef，内存管理，文件读写）
参考：[C语言-菜鸟教程](https://www.runoob.com/cprogramming/c-tutorial.html) [C语言中文网](http://c.biancheng.net/c/)
2. [文件描述符](https://zhuanlan.zhihu.com/p/108744787)
3. 学习C语言编程规范。（第三天）

## 要求
<font color="red">注：动手练习，保存练习记录（截图或文件），拷贝原[C 语言](Task6/Note/C.md)笔记到当前任务中并整理笔记到[C 语言](Task7/Note/C.md)，拷贝原[代码规范](Task6/Note/Rule.md)笔记到当前任务中并整理笔记到[代码规范](Task7/Note/Rule.md)。</font>
1. 掌握当天的C语言相关语法和知识点。
2. 了解文件描述符。
3. 练习过程中使用vim，并按照C语言编程规范进行实践。


# 任务书8
## 学习内容
1. 了解进程线程的定义和区别，及如何用代码创建进程和线程。
2. 线程同步和互斥。
3. 线程间通信方式。

## 要求
<font color="red">注：动手练习，保存练习记录（截图或文件），拷贝原[C 语言](Task7/Note/C.md)笔记到当前任务中并整理笔记到[C 语言](Task8/Note/C.md)。</font>
1. 掌握当天的C语言相关语法和知识点。
2. 了解进程线程的定义和区别。
3. 掌握进程线程相关函数的用法。
4. 了解线程同步和互斥。
5. 了解线程间通信方式。


# 任务书9

## 学习内容
1. 按以下要求编写代码，使用函数封装功能并在main中调用：
    - 创建一个空链表。
    - 创建一个线程，线程名字叫thread_push。
      - 该线程的功能是每2秒获取一次当前系统时间，然后创建一个节点并把时间按"2022-08-25 16:35:40"格式的字符串存入结点，并将节点插入到链表的头部。
      - 当链表长度为10的时候，停止获取时间和向链表插入结点。
      - 当链表长度小于等于4的时候，重新开始获取时间和向链表插入结点，如此循环。
    - 创建一个线程，线程名字叫thread_pop。
      - 该线程的功能是每3秒获取一次链表尾节点存储的字符串，并将字符串写入文件record.txt，一个节点存储的字符串记录为一行，字符串记录成功后删除尾结点。
      - 当链表长度小于等于4的时候，停止获取字符串和写入文件以及删除结点的操作。
      - 当链表长度大于等于8的时候，重新开始之前的操作，如此循环。

## 要求
<font color="red">注：保存写码过程中的笔记（截图或文件），整理笔记到[综合练习笔记](Task9/Note/training.md)，代码保存到笔记的同级目录。</font>
<font color="red">1天完成，下班前进行任务汇报。</font>
1. 功能完整且代码能正常运行。
2. 代码符合编程规范。
3. 能流畅的描述代码逻辑。
4. 能流畅描述使用的各种函数的用法。


# 任务书10
## 学习内容
1. 完成项目实训，编写一个聊天室，包括但不限于以下功能：
    - C/S架构：
      - 服务端支持多客户端连接。
      - 使用select实现。
      - 多线程。
      - 读写分离。
    - 用户注册：
      - 用户信息保存在服务端sqlite3数据库。
    - 用户登录：
      - 用户名和密码验证。
    - 群聊。
    - 私聊。
    - 查看在线人数并显示在线和离线的用户名。
    - 查看聊天记录：
      - 客户端以文件形式保存群聊和私聊记录。
      - 服务端聊天记录保存在数据库。
    - 项目涉及的知识点见[Task10](Process.md#Task10)。
2. 将代码提交到gitlab。
3. 了解白盒黑盒测试。

## 要求
<font color="red">注：保存写码过程中的笔记（截图或文件），整理笔记到[项目练习](Task10/Note/training.md)。</font>
<font color="red">任务期限13天，按1中的顺序分阶段完成项目，每天汇报进度，自己合理安排时间。</font>
1. 根据项目需求编写IT测试项目书。
2. 完成项目的代码编写。
3. 根据代码完成CT测试项目书。
4. 根据CT测试项目书，完成CT测试，每个用例的测试log保存为一个文件。
5. 根据IT测试书，完成IT测试，每个用例的测试log保存为一个文件。

