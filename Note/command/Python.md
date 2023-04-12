**[Home](../Menu.md)**
[TOC]
# Python
## 共通
### 常用命令
* Windows python安装路径
C:\Users\luqingjuan\AppData\Local\Programs\Python\Python37-32\
* 查看安装的lib
    pip list
* 安装lib
    pip install 软件
* 卸载lib
    pip uninstall 软件
---
### 离线安装包下载
去 [网站](https://pypi.org/)检索
* 离线tar.gz包选择
`import pip._internal
print(pip._internal.pep425tags.get_supported())`
`PS D:\Notes> & C:/Users/luqingjuan/AppData/Local/Programs/Python/Python37-32/python.exe d:/Notes/Test/test.py
[('cp37', 'cp37m', 'win32'), ('cp37', 'none', 'win32'), ('py3', 'none', 'win32'), ('cp37', 'none', 'any'), ('cp3', 'none', 'any'), ('py37', 'none', 'any'), ('py3', 'none', 'any'), ('py36', 'none', 'any'), ('py35', 'none', 'any'), ('py34', 'none', 'any'), ('py33', 'none', 'any'), ('py32', 'none', 'any'), ('py31', 'none', 'any'), ('py30', 'none', 'any')]`
* 离线安装whl包
    pip install whl包
* 离线安装tar.gz包
    方式：python.exe setup.py --help
    根据帮助信息执行以下命令：
    编译：python.exe .\setup.py build
    安装：python.exe .\setup.py install
---
## 插件系列
### Python Web自动化工具 selenium
1. Windows环境 安装Chrome或火狐浏览器（安装selenium浏览器插件）
2. Windows环境 安装python3 用于控制浏览器

* [selenium webdriver - Web自动化工具](https://blog.csdn.net/weixin_36279318/article/details/79475388)
    - 安装urllib3
    - 安装selenium：
    - pip3 install selenium
    - Windows 环境下载浏览器插件
    - [Chrome浏览器设定](https://cloud.tencent.com/developer/article/1778586)
    - [find_element_by_xpath()方法汇总](https://www.cnblogs.com/huangjiyong/p/12217660.html)
	- [selenium专题](https://blog.csdn.net/huilan_same/category_6364985.html)
这个可以实现GUI的哪些操作？
用户名 密码的输入  可以吗
[下拉框的选择](https://www.cnblogs.com/mumianhuasayyes/p/7088836.html)
[表格里内容的取得？](https://www.cnblogs.com/lucky0425/p/10564690.html)
[导入文件 导出文件](https://www.cnblogs.com/lycun-0426/p/13596845.html)


[【python】Selenium+python3使用总结（一）](https://blog.csdn.net/qq_35061334/article/details/122868502)


---
### dot 转图形工具（Graphviz）
<b>参考</b>
* 能一边写一边看图的在线网站[graphviz Online](http://dreampuf.github.io/GraphvizOnline/#digraph%20G%20%7B%0A%0A%20%20subgraph%20cluster_0%20%7B%0A%20%20%20%20style%3Dfilled%3B%0A%20%20%20%20color%3Dlightgrey%3B%0A%20%20%20%20node%20%5Bstyle%3Dfilled%2Ccolor%3Dwhite%5D%3B%0A%20%20%20%20a0%20-%3E%20a1%20-%3E%20a2%20-%3E%20a3%3B%0A%20%20%20%20label%20%3D%20%22process%20%231%22%3B%0A%20%20%7D%0A%0A%20%20subgraph%20cluster_1%20%7B%0A%20%20%20%20node%20%5Bstyle%3Dfilled%5D%3B%0A%20%20%20%20b0%20-%3E%20b1%20-%3E%20b2%20-%3E%20b3%3B%0A%20%20%20%20label%20%3D%20%22process%20%232%22%3B%0A%20%20%20%20color%3Dblue%0A%20%20%7D%0A%20%20start%20-%3E%20a0%3B%0A%20%20start%20-%3E%20b0%3B%0A%20%20a1%20-%3E%20b3%3B%0A%20%20b2%20-%3E%20a3%3B%0A%20%20a3%20-%3E%20a0%3B%0A%20%20a3%20-%3E%20end%3B%0A%20%20b3%20-%3E%20end%3B%0A%0A%20%20start%20%5Bshape%3DMdiamond%5D%3B%0A%20%20end%20%5Bshape%3DMsquare%5D%3B%0A%7D)
* [Dot脚本语言语法整理](https://blog.csdn.net/jy692405180/article/details/52077979)

---
### 自动生成UML类图（pylint）
#### 安装
* 安装Graphviz
    1. [官网](https://link.zhihu.com/?target=http%3A//www.graphviz.org/download/)下载
    2. 安装时，选择自动添加到系统路径。
    3. 安装完成后，`Win + R`，输入`cmd`，启动终端，输入 `dot -V` 确认安装版本。

* 安装pylint`Pyreverse已集成于pylint模块中`
    pylint依赖包
    - 安装[setuptools-59.6.0](https://pypi.org/project/setuptools/59.6.0/#files)
    - 安装[wrapt-1.14.1](https://pypi.org/project/wrapt/1.14.1/#files)
    - 安装[typing-extensions-4.1.1](https://pypi.org/project/typing-extensions/4.1.1/#files)
    - 安装[lazy-object-proxy-1.7.1](https://pypi.org/project/lazy-object-proxy/1.7.1/#files)
    - 安装[typed-ast-1.5.3](https://pypi.org/project/typed-ast/1.5.3/#files)
    - 安装[astroid-2.11.5](https://pypi.org/project/astroid/2.11.5/#files)
    - 安装[isort-5.10.1](https://pypi.org/project/isort/5.10.1/#files)
    - 安装[tomli-1.2.3](https://pypi.org/project/tomli/1.2.3/#files)
    - 安装[dill-0.3.4](https://pypi.org/project/dill/0.3.4/#files)
    - 安装[platformdirs-2.4.0](https://pypi.org/project/platformdirs/2.4.0/#files)
    - 安装[mccabe-0.7.0](https://pypi.org/project/mccabe/0.7.0/#files)
    - 安装[colorama-0.4.4](https://pypi.org/project/coloram/0.4.4/#files)
    - 安装[pylint-2.13.8](https://pypi.org/project/pylint/2.13.8/#files)
#### 使用
* 生成新结构文件classes.dot
`pyreverse py文件列表`
* 生成新PDF文件classes.pdf
`dot -Tpdf classes.dot -o classes.pdf`
eg:
`$ pyreverse.exe SSHClass.py  criticallog.py  ems.py  ems_pyautogui.py  ems_selenium.py  innerlog.py  iperf.py  main.py  ping.py  simnovator.py  syslog.py  ttl_ssh.py  ueaction.py`
`$ dot -Tpdf classes.dot -o class_L5GC_CI2_dev_6a2dbc32b26ea31fece3b33a93fa81e88cb9a845.pdf`
`$ dot -Tpdf packages.dot -o packages_L5GC_CI2_dev_6a2dbc32b26ea31fece3b33a93fa81e88cb9a845.pdf`

* 命令行方式(没有尝试)
`pyreverse -o png -p Pyreverse pylint/pyreverse/`
<b>参考资料</b>
* [Pyreverse结合Graphviz自动绘制Python类图](https://zhuanlan.zhihu.com/p/365953969)

### 自动生成函数动态调用图（pycallgraph）
#### 安装
* 安装Graphviz
    1. [官网](https://link.zhihu.com/?target=http%3A//www.graphviz.org/download/)下载
    2. 安装时，选择自动添加到系统路径。
    3. 安装完成后，`Win + R`，输入`cmd`，启动终端，输入 `dot -V` 确认安装版本。

* 安装pycallgraph
    - 安装[pycallgraph](https://pypi.org/project/pycallgraph/#files)
#### 使用
* 代码方式
`from pycallgraph import PyCallGraph`
`from pycallgraph.output import GraphvizOutput`
`...`
`with PyCallGraph(output=GraphvizOutput(output_file='filter_exclude.png')):`
`    code_to_profile()`
*  命令行方式(没有尝试)
`pycallgraph graphviz -- ./mypythonscript.py`

<b>参考资料</b>
* [Python自动绘制UML类图、函数调用图（Call Graph）](https://blog.csdn.net/Bit_Coders/article/details/120722430)
---

### 自动生成函数静态调用图（pyan3）
#### 安装
* 安装pyan3
    - 安装[MarkupSafe](https://pypi.org/project/MarkupSafe/#files)
    - 安装[jinja2](https://pypi.org/project/jinja2/#files)
    - 安装[pyan3-1.1.1](https://pypi.org/project/pyan3/1.1.1/#files)
#### 使用
*  命令行方式
`pyan3.exe *.py --uses --no-defines --colored --grouped --annotated --dot >myuses.dot`
`dot -Tsvg myuses.dot >myuses.svg`
`dot -Tpng Python/classes.dot >aa.png`
`dot -Tpdf classes.dot -o classes.pdf`
eg:
`pyan3.exe SSHClass.py                        --uses --no-defines --colored --grouped --annotated --dot >SSHClass.dot`
`pyan3.exe SSHClass.py  criticallog.py  ems.py  ems_pyautogui.py  ems_selenium.py  innerlog.py  iperf.py  main.py  ping.py  simnovator.py  syslog.py  ttl_ssh.py  ueaction.py --uses --no-defines --colored --grouped --annotated --dot >functionuses.dot`

<b>参考资料</b>
* [Python中动态与静态 Call Graph（调用关系图）分析工具](https://zhuanlan.zhihu.com/p/108481835
)

---
### 解析L5GC_CI代码
branch：L5GC_CI2_dev
commit：6a2dbc32b26ea31fece3b33a93fa81e88cb9a845
**WSL**

#### classes.png

cd Python/

ls *.py
SSHClass.py  criticallog.py  ems.py  ems_pyautogui.py  ems_selenium.py  innerlog.py  iperf.py  main.py  ping.py  simnovator.py  syslog.py  ttl_ssh.py  ueaction.py  useless_dstat.py

pyreverse.exe SSHClass.py  criticallog.py  ems.py  ems_pyautogui.py  ems_selenium.py  innerlog.py  iperf.py  main.py  ping.py  simnovator.py  syslog.py  ttl_ssh.py  ueaction.py;    dot -Tpng classes.dot >UML.png


#### **.png
ls -l *.py
-rwxrwxrwx 1 luqingjuan luqingjuan 14567 Apr 10 10:47 Python/SSHClass.py
-rwxrwxrwx 1 luqingjuan luqingjuan 13238 Apr 10 10:46 Python/criticallog.py
-rwxrwxrwx 1 luqingjuan luqingjuan  7282 Apr 10 10:46 Python/ems.py
-rwxrwxrwx 1 luqingjuan luqingjuan  1469 Apr 10 10:46 Python/ems_pyautogui.py
-rwxrwxrwx 1 luqingjuan luqingjuan 33686 Apr 10 10:46 Python/ems_selenium.py
-rwxrwxrwx 1 luqingjuan luqingjuan  9603 Apr 10 10:46 Python/innerlog.py
-rwxrwxrwx 1 luqingjuan luqingjuan 35391 Apr 10 10:46 Python/iperf.py
-rwxrwxrwx 1 luqingjuan luqingjuan 88051 Apr 10 10:47 Python/main.py
-rwxrwxrwx 1 luqingjuan luqingjuan 15193 Apr 10 10:46 Python/ping.py
-rwxrwxrwx 1 luqingjuan luqingjuan 16258 Apr 10 11:01 Python/simnovator.py
-rwxrwxrwx 1 luqingjuan luqingjuan  8657 Apr 10 10:46 Python/syslog.py
-rwxrwxrwx 1 luqingjuan luqingjuan 14973 Apr 10 10:46 Python/ttl_ssh.py
-rwxrwxrwx 1 luqingjuan luqingjuan 14777 Apr 10 10:47 Python/ueaction.py


pyan3.exe SSHClass.py --uses --no-defines --colored --grouped --annotated --dot >SSHClass.dot;    dot -Tpng SSHClass.dot >SSHClass.png
pyan3.exe criticallog.py --uses --no-defines --colored --grouped --annotated --dot >criticallog.dot;    dot -Tpng criticallog.dot >criticallog.png
pyan3.exe ems.py --uses --no-defines --colored --grouped --annotated --dot >ems.dot;    dot -Tpng ems.dot >ems.png
pyan3.exe ems_pyautogui.py --uses --no-defines --colored --grouped --annotated --dot >ems_pyautogui.dot;    dot -Tpng ems_pyautogui.dot >ems_pyautogui.png
pyan3.exe ems_selenium.py --uses --no-defines --colored --grouped --annotated --dot >ems_selenium.dot;    dot -Tpng ems_selenium.dot >ems_selenium.png
pyan3.exe innerlog.py --uses --no-defines --colored --grouped --annotated --dot >innerlog.dot;    dot -Tpng innerlog.dot >innerlog.png
pyan3.exe iperf.py --uses --no-defines --colored --grouped --annotated --dot >iperf.dot;    dot -Tpng iperf.dot >iperf.png
pyan3.exe main.py --uses --no-defines --colored --grouped --annotated --dot >main.dot;    dot -Tpng main.dot >main.png
pyan3.exe ping.py --uses --no-defines --colored --grouped --annotated --dot >ping.dot;    dot -Tpng ping.dot >ping.png
pyan3.exe simnovator.py --uses --no-defines --colored --grouped --annotated --dot >simnovator.dot;    dot -Tpng simnovator.dot >simnovator.png
pyan3.exe syslog.py --uses --no-defines --colored --grouped --annotated --dot >syslog.dot;    dot -Tpng syslog.dot >syslog.png
pyan3.exe ttl_ssh.py --uses --no-defines --colored --grouped --annotated --dot >ttl_ssh.dot;    dot -Tpng ttl_ssh.dot >ttl_ssh.png
pyan3.exe ueaction.py --uses --no-defines --colored --grouped --annotated --dot >ueaction.dot;    dot -Tpng ueaction.dot >ueaction.png



#### 分析python 调用关系
grep -E "^class|def " *.py
luqingjuan@G08CNXDJFTTY049:/mnt/d/Git/L5G_CI/Python$ grep -E "python3" ../Jenkins/*
grep -E "python3" *.py
---
### excel 读写修改操作（xlwings）
#### 安装
* 安装xlwings
    - 安装[xlwings](https://pypi.org/project/xlwings/#files)
