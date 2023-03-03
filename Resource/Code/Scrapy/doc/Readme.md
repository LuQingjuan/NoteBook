# 环境构筑
1. 环境
Windows系统

2. 软件
Python3
Google Chrome

3. 安装selenium插件
[【python】Selenium+python3使用总结（一）](https://blog.csdn.net/qq_35061334/article/details/122868502)
* 安装 selenium
* 安装 chromedriver
* 配置环境变量
* 简单示例
```
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
```

4. 通过调试Chrome浏览器，避开反爬虫机制
[使用python+selenium控制手工已打开的浏览器](https://www.cnblogs.com/HJkoma/p/9936434.html)
* Chrome浏览器路径加到patch中
* 在命令行输入`chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Users\luqingjuan\Downloads\selenum\AutomationProfile"`
    * 对于-remote-debugging-port值，可以指定任何打开的端口。
    * 对于-user-data-dir标记，指定创建新Chrome配置文件的目录。它是为了确保在单独的配置文件中启动chrome，不会污染你的默认配置文件。**建议使用爬虫脚本所在的目录**
* 简单示例：
```
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
print(driver.title)
```

# 脚本运行方式
1. 启动调试Chrome浏览器
* 在命令行输入`chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Users\luqingjuan\Downloads\selenum\AutomationProfile"`

2. 启动脚本 
* python .\Scrapy.py "检索内容" 网页加载次数(可以不填，默认30)