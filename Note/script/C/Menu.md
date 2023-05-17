## 获取命令Option参数 int getopt(int argc, char * const argv[], const char *optstring);
获取命令Option参数 
* optstring的格式规范简单总结如下
    * 单个字符：               该选项Option不需要参数。
    * 单个字符后接一个冒号":"： 表示该选项Option需要一个选项参数Option argument。选项参数Option argument可以紧跟在选项Option之后，或者以空格隔开。选项参数Option argument的首地址赋给optarg。
    * 单个字符后接两个冒号"::"：表示该选项Option的选项参数Option argument是可选的。当提供了Option argument时，必须紧跟Option之后，不能以空格隔开，否则getopt()会认为该选项Option没有选项参数Option argument，optarg赋值为NULL。相反，提供了选项参数Option argument，则optarg指向Option argument。

* getopt()设置的全局变量包括：
    * char *optarg  －－ 当匹配一个选项后，如果该选项带选项参数，则optarg指向选项参数字符串；若该选项不带选项参数，则optarg为NULL；若该选项的选项参数为可选时，optarg为NULL表明无选项参数，optarg不为NULL时则指向选项参数字符串。
    * int optind  －－ 下一个待处理元素在argv中的索引值。即下一次调用getopt的时候，从optind存储的位置处开始扫描选项。当getopt()返回-1后，optind是argv中第一个Operands的索引值。optind的初始值为1。
    * int opterr  －－ opterr的值非0时，在getopt()遇到无法识别的选项，或者某个选项丢失选项参数的时候，getopt()会打印错误信息到标准错误输出。opterr值为0时，则不打印错误信息。
    * int optopt  －－ 在上述两种错误之一发生时，一般情况下getopt()会返回'?'，并且将optopt赋值为发生错误的选项。 

* 参考：[getopt()函数详解](https://blog.csdn.net/c1523456/article/details/79173776)
* [demo](getopt_test.c)
    * 编译；`clang getopt_test.c -o getopt_test -Wall` 
    * 运行：`./getopt_test -a aaaa -b bbbb -c cccc -d dddd -eeeee`