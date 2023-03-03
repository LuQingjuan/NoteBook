**[Home](../Menu.md)**
[TOC]
# Linux系统
## 文件系统
### 目录树结构

### 特殊文件
* 软链接
  * 介绍
    
  * 基本操作
    * 创建
        
    * 删除
        
* 硬链接
  >同上

* 两者之间的什么区别


## 命令
### 万能命令
#### man
* 常用参数搭配：

#### yum


#### 实操
* 安装 git
  1. 
  2. 
  3. 
  4. 查看git版本：
* 卸载 git

### 文件操作相关
#### cd
* 介绍：跳转到某个文件夹下。
* 语法：`cd [目录名]`
* 常用参数搭配：

| 命令  | 说明         |
| ----- | ------------ |
| cd .. | 跳转到上一级 |
|       |              |
|       |              |
|       |              |
PS:表格快速格式化:`Shift`+`Alt`+`F`

* 练习记录
![](image/Linux/cd/1.png)

#### pwd

#### ls

#### mkdir

#### cat

#### tail

#### head

#### mv

#### cp

#### rm

### 其他命令
#### tar
tar -czvf 
tar -xzvf 

#### ssh

#### scp

### mount
* 挂载
`mkdir vbbu; sudo mount -t cifs //10.37.193.212/vbbu -o username=oaivbbu,password=oaivbbu,rw,file_mode=0644,dir_mode=0755,vers=1.0 vbbu/`
### umount
* 非挂载
`sudo umount vbbu`
#### 实操
* 任务书，上传文件到Linux服务器，压缩成Task1.tar.gz文件，将Task1.tar.gz文件下载到本地

* Linux环境，解压Task1.tar.gz文件

### 系统资源命令
#### TODO
* 介绍：查看磁盘空间信息

#### TODO
* 介绍：查看内存信息

#### TODO
* 介绍：查看网卡信息

#### TODO
* 介绍：查看进程信息

## 快捷键（Ctrl组合键）
| 命令          | 说明 |
| ------------- | ---- |
| `Ctrl`+`C` .. | 清屏 |
|               |      |
|               |      |
|               |      |
|               |      |
|               |      |
ps:表格快速格式化:`Shift`+`Alt`+`F`

## 三剑客
### gerp
[Linux grep命令详解：查找文件内容](http://c.biancheng.net/view/4017.html)

### sed
sed [选项] [脚本命令] 文件名
| 选项        | 说明                                              |
| ----------- | ------------------------------------------------- |
| -e command  | 默认，以选项中的指定的command来处理输入的文本文件 |
| -f file.sed | 以选项中的指定的script文件来处理输入的文本文件    |
| -n          | 仅显示script处理后的结果                          |
| -i          | 直接修改源文件                                    |

**脚本命令**
*address*
* 以数字形式指定行区间, 第一行编号为 1
格式：`number`command
单个行号：2
区间行号：2,3
某行开始的所有行:2,$
* 用文本模式指定行区间
格式：/`pattern`/command
eg: `sed '/demo/s/bash/csh/' /etc/passwd`

file.sed中是脚本命令 以 `;` 分割
| 脚本命令 |                                         | 格式                                                                    | 例子                                                   |
| -------- | --------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------ |
| s        | 字符替换                                | `address`s/`pattern`/`replacement`/`flags`                              |                                                        |
|          |                                         | 特殊字符用`\`转义                                                       |                                                        |
|          | eg                                      | 替换每行中, 第 2 次匹配的字符串                                         | `sed 's/test/trial/2' data4.txt`                       |
|          |                                         | 替换所有匹配的字符串                                                    | `sed 's/test/trial/g' data4.txt`                       |
|          |                                         | 只输出被替换命令修改过的行                                              | `sed -n 's/test/trial/p' data5.txt`                    |
|          |                                         | 将匹配后的结果保存到指定文件中                                          | `sed 's/test/trial/w test.txt' data5.txt`              |
|          |                                         | 使用正则表示式给所有第一个的h1、h2、h3添加<>，给第二个h1、h2、h3添加</> | ``                                                     |
| d        | 删除                                    | `address`d                                                              |                                                        |
|          | eg                                      | 删除文件中所有内容                                                      | `sed 'd' data1.txt`                                    |
|          |                                         | 删除第 3 行的内容                                                       | `sed '3d' data6.txt`                                   |
|          |                                         | 删除第 2、3 行的内容                                                    | `sed '2,3d' data6.txt`                                 |
|          |                                         | 删除第 [2~3] 行之间的所有行                                             | `sed '/1/,/3/d' data6.txt`                             |
|          |                                         | 删除第 3 行开始的所有行                                                 | `sed '3,$d' data6.txt`                                 |
| a        | 追加一行                                | [address]a\新文本内容                                                   |                                                        |
|          |                                         | 多行数据之间用`\`换行                                                   |                                                        |
|          | eg                                      | 一个新行附加到数据流中第三行后                                          | `sed '3a\This is an appended line.' data6.txt`         |
| i        | 插入一行                                | [address]i\新文本内容                                                   |                                                        |
|          |                                         | 多行数据之间用`\`换行                                                   |                                                        |
|          | eg                                      | 一个新行附加到数据流中第三行后                                          | `sed '3i\This is an insert line.' data6.txt`           |
| c        | 行替换                                  | [address]c\用于替换的新文本                                             |                                                        |
|          |                                         | 多行数据之间用`\`换行                                                   |                                                        |
|          | eg                                      | 修改第三行中的文本                                                      | `sed '3c\This is a changed line of text.' data6.txt`   |
| y        | 字符逐一替换                            | [address]y/inchars/outchars/                                            |                                                        |
|          | eg                                      | 全局替换，将1->7;2->8;3->9                                              | `sed 'y/123/789/' data8.txt`                           |
| p        | 输出该行的内容                          | [address]p                                                              |                                                        |
|          | 显示匹配文本模式的行                    | `sed -n '3p' test.md`                                                   |                                                        |
|          | 显示第 3 行，修改前后的信息             | `sed -n '3{p;s/body/waht/p}' test.md`                                   |                                                        |
| w        | 指定行的内容写入文件中                  | [address]w filename                                                     |                                                        |
|          | eg                                      | 前两行保存到文本中                                                      | `sed '1,2w test.txt' data6.txt`                        |
|          | 将包含文本模式的数据行写入目标文件 grep | `sed -n '/Browncoat/w Browncoats.txt' data11.txt`                       |                                                        |
| r        | 插入其他文件                            | [address]r filename                                                     |                                                        |
|          | eg                                      | 插入到第 3 行的后面                                                     | `sed '3r data12.txt' data6.txt`                        |
|          |                                         | 插入到末尾                                                              | `sed '$r data12.txt' data6.txt`                        |
| q        | 退出 sed 程序                           |                                                                         |                                                        |
|          | eg                                      | 第 2 行之后，就停止                                                     | `sed '2q' test.txt`                                    |
|          |                                         | number 1 第一次替换成 number 0，然后直接退出                            | `sed '/number 1/{ s/number 1/number 0/;q; }' test.txt` |

**脚本**
test.txt
```txt
<html>
<title>First Wed</title>
<body>
h1Helloh1
h2Helloh2
h3Helloh3
</body>
</html>
```
```sed
#sed.sh
/h[0-9]/{
    s//\<&\>/1
    s//\<\/&\>/2
}
```
脚本
`sed -f sed.sh test.txt`


**sed 正则**
| 元字符集   | 说明                            | 例子                                           |                       |
| ---------- | ------------------------------- | ---------------------------------------------- | --------------------- |
| `^`        | 锚定行的开始                    | 匹配所有以sed开头的行。                        | `/^sed/`              |
| `$`        | 锚定行的结束                    | 匹配所有以sed结尾的行。                        | `/sed$/`              |
| `.`        | 匹配一个非换行符的字符          | 匹配s后接一个任意字符，然后是d。               | `/s.d/`               |
| `*`        | 匹配零或多个字符                | 匹配所有模板是一个或多个空格后紧跟sed的行。    | `/*sed/`              |
| `[]`       | 匹配一个指定范围内的字符，      | 匹配sed和Sed。                                 | `/[Ss]ed/`            |
| `[^]`      | 匹配一个不在指定范围内的字符，  | 匹配不包含A-R和T-Z的一个字母开头，紧跟ed的行。 | `/[^A-RT-Z]ed/`       |
| `\(..\)`   | 保存匹配的字符，                | loveable被替换成lovers。                       | `s/\(love\)able/\1rs` |
| `&`        | 保存搜索字符用来替换其他字符，  | love这成\*\*love\*\*。                         | `s/love/**&**/`       |
| `\<`       | 锚定单词的开始，                | 匹配包含以love开头的单词的行。                 | `/\<love/`            |
| `\>`       | 锚定单词的结束，                | 匹配包含以love结尾的单词的行。                 | `/love\>/`            |
| `x\{m\}`   | 重复字符x，m次，                | 匹配包含5个o的行。                             | `/0\{5\}/`            |
| `x\{m,\}`  | 重复字符x,至少m次，             | 匹配至少有5个o的行。                           | `/o\{5,\}/`           |
| `x\{m,n\}` | 重复字符x，至少m次，不多于n次， | 匹配5--10个o的行。                             | `/o\{5,10\}/`         |

| 特殊           | 标准 | sed   |
| -------------- | ---- | ----- |
| 十进制数       | \d   | [0-9] |
| 表示一个或多个 | +    | \+    |
[Linux sed命令完全攻略（超级详细）]([Linux_sed.mhtml](http://c.biancheng.net/view/4028.html))

sed //
\[([^\[\]]+)\]\^\(([^\(\)]+)\)

echo "111(222)333" | sed 's/     (\(.*\))\(.*\)     /\1     \2/'

 "<ruby>$1<rp>(</rp><rt>$2</rt><rp>)</rp></ruby>");
### awk
awk [选项] '脚本命令' 文件名
| 选项       | 说明                                                             |
| ---------- | ---------------------------------------------------------------- |
| -F fs      | 指定以 fs 作为输入行的分隔符，awk 命令默认分隔符为空格或制表符。 |
| -f file    | 从脚本文件中读取 awk 脚本指令，以取代直接在命令行中输入指令。    |
| -v var=val | 在执行处理过程之前，设置一个变量 var，并给其设备初始值为 val。   |
**脚本命令**
/`pattern`/{`command`}

| 脚本命令 |     | 格式 | 例子 |
| -------- | --- | ---- | ---- |
|          |     |      |      |

**脚本**
```awk
#awk.sh
BEGIN {print "The data3 File Contents:"}
> {print $0}
> END {print "End of File"}'
```
`awk   'BEGIN{commands }   pattern{ commands }   END{ commands }'   filename`
* BEGIN 语句块： 在 awk 从输入流中 读取行之前 被执行，是可选的语句块。比如：变量等…通常可以写在 BEGIN语句块中。
* pattern 语句块： 这个语句块中的通用命令是最重要的部分，但是也是可选的，如果没有提供pattern语句块，则默认执行 print，即打印每一个读取到的行。
* END 语句块： 在 awk 从输入流中 读取完所有行之后 被执行，比如：打印完所需要的行之后，需要一个信息汇总情况，这时候就可以写在 END 语句块中。
————————————————
版权声明：本文为CSDN博主「郑泽林」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/ljlfather/article/details/104530474
[Linux awk命令详解](http://c.biancheng.net/view/4082.html)
[AWK 从入门 ———>放弃](https://blog.csdn.net/ljlfather/article/details/104629216)

# 参考资料