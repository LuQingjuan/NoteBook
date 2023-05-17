**[Home](../Menu.md)**

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
<font color="red">注：动手练习，保存练习记录（截图或文件）。
整理笔记：
[shell笔记](Note/Shell.md)将原shell笔记拷贝到当前任务中，并在此基础上整理
[Linux笔记](Note/Linux.md)将原Linux笔记拷贝到当前任务中，并在此基础上整理</font>
1. 了解shell基本语法，能编写简单的脚本。
2. 掌握环境变量的定义和设置方法。
3. 熟练掌握linux任务的前后台切换操作。
4. 掌握查看和结束进程的方法。

## 考核形式
==整个学习周期==，口头问答或根据要求敲命令、修改脚本。