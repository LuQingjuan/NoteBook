**[Home](../Menu.md)**
[TOC]
# Shell
## 脚本基础
### 文件后缀名
`.sh`

### 解释器申明
`#!/bin/bash`

### 注释
`#`

### 变量
* 赋值
**等号前后不能有空格**
数字   : ``
字符   : ``
字符串 : `value=""`
数组   : `array=(value1 value2)`
* 使用
数字   : ``
字符   : ``
字符串 : ``${value}``
数组 value1 : `${array[0]}`

### IO交互
* 输入
`read -p "Input Kill Process Nane:"`
* 输出
`echo " ${process_name} Process Kill OK."`
---

## 逻辑操作
### 运算符
* 关系
==  : `-eq`
!=  : `-ne`
\>  : `-gt`
<   : `-lt`
\>= : `-ge`
<=  : `-le`
* 布尔
与  : `-a`
或  : `-o`
非  : `!`

### 判断
* if-else
```
if 【condition1】
then
    【Action】
elif 【condition2】
then
    【Action】
else
    【Action】
fi
```
* case-in
```
case ${data} in
    ${value1})
        【Action】
    ;;
    ${value2}))
         【Action】
    ;;
    *)
        【Action】
    ;;
esac
```

### 循环
* for
```
for str in 【list】
do
    【Action】
done
```
* while-do
```
while 【condition】 
do 
    【Action】
done
```
* until-do
```
until 【condition】 
do
    【Action】
done
```

### 循环异常退出
* 结束当前循环，执行下一个循环
`continue`
* 结束循环
`break`

---
## 脚本封装
### 函数
* 定义
```
function(){
    # Param
    $1 $2 $3
    ……
    # Return
    echo "111"
    echo "222"
}
```
* 调用
```
ret_array=($(function param1 param2 param3))
${ret_array[0]}
${ret_array[1]}
```

### 脚本
* 参数传入
`kill_process.sh param1 param2 param3`
* 参数使用
**param1:**`$1`
**param2:**`$2`
**param3:**`$3`

|     |                                                                       |
| --- | --------------------------------------------------------------------- |
| $#  | 传给脚本的参数个数                                                    |
| $0  | 脚本本身的名字                                                        |
| $1  | 传递给该shell脚本的第一个参数                                         |
| $2  | 传递给该shell脚本的第二个参数                                         |
| $@  | 传给脚本的所有参数的列表                                              |
| $*  | 以一个单字符串显示所有向脚本传递的参数，与位置变量不同，参数可超过9个 |
| $$  | 脚本运行的当前进程ID号                                                |
| $?  | 显示最后命令的退出状态，0表示没有错误，其他表示有错误                 |

### 脚本引用
`source 文件名`
---
## 参考资料
[菜鸟教程](https://www.runoob.com/linux/linux-shell.html)