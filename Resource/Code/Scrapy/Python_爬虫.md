[Python爬虫篇：爬虫笔记合集](https://blog.csdn.net/AI19970205/article/details/124282549)
[python爬虫(廖雪峰商业爬虫)](https://blog.csdn.net/baidu_41867252/article/details/86821355)
[Python爬虫利器之Beautiful Soup入门详解，实战总结！！！](https://blog.csdn.net/llllllkkkkkooooo/article/details/108511964)
[Python爬虫-爬取知乎（小结）](https://blog.csdn.net/weixin_49345590/article/details/109848459)
[Python 爬虫（一）：Header cookies 的设置](https://zhuanlan.zhihu.com/p/518788491?utm_id=0)
1. 在Chrome浏览器的网页上：右键 ——> 检查 ——> Network ——> Doc ——> 在 Name 里找到对应的请求文件
2. 右键该文件，copy ——> **copy as cURL (bash)**，注意不是【copy as cURL (cmd)】
3. 打开[解析网站](https://curl.trillworks.com/) ，粘贴 cURL (bash) 到左边 curl command，右边会自动出 Python 代码

[23个Python爬虫开源项目代码：微信、淘宝、豆瓣、知乎、微博...](https://blog.csdn.net/CVGao/article/details/109475601?spm=1001.2101.3001.6650.5&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-5-109475601-blog-128267024.pc_relevant_aa2&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-5-109475601-blog-128267024.pc_relevant_aa2&utm_relevant_index=9)

---
[Python爬虫之Js逆向案例(1)-知乎搜索](https://www.ngui.cc/el/522173.html?action=onClick)

[可能可行jsrpc Python爬虫之Js逆向案例(13)-某乎最新x-zse-96的rpc方案后续](https://blog.csdn.net/li11_/article/details/127658491)



# 安装selenium
pip3 install seleniumpip

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

[使用python+selenium控制手工已打开的浏览器](https://www.cnblogs.com/HJkoma/p/9936434.html)
* Chrome浏览器路径加到patch中
* 在命令行输入`chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Users\luqingjuan\Downloads\selenum\AutomationProfile"`
    * 对于-remote-debugging-port值，可以指定任何打开的端口。
    * 对于-user-data-dir标记，指定创建新Chrome配置文件的目录。它是为了确保在单独的配置文件中启动chrome，不会污染你的默认配置文件。
* 现在，我们需要接管上面的浏览器。新建一个python文件，运行以下代码：
```
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
 
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
print(driver.title)
```









[python3+selenium4自动化测试环境搭建-基础篇1](https://blog.csdn.net/qq_18298049/article/details/117001377)
[python3+selenium4自动化测试操作启动不同的浏览器-基础篇2](https://blog.csdn.net/qq_18298049/article/details/117047377)
[python3+selenium4自动化测试-浏览器常用基本操作-基础篇3](https://blog.csdn.net/qq_18298049/article/details/117048850)
[python3+selenium4自动化测试-元素定位之find_element()-基础篇4](https://blog.csdn.net/qq_18298049/article/details/117136214)
[python3+selenium4自动化测试-元素定位之find_elements()、层级定位与selenium4相对定位-基础篇5](https://blog.csdn.net/qq_18298049/article/details/117194464)
* 返回指定元素上方的元素：above
* 返回指定元素下方的元素：below
* 返回指定元素左侧的元素：toLeftOf
* 返回指定元素右侧的元素：toRightOf
* 返回指定元素附件的一个元素，要求该元素离指定元素不超过50px：near

[python3+selenium4自动化测试-元素常用操作-基础篇6](https://blog.csdn.net/qq_18298049/article/details/117231879)
* 输入内容：send_keys()
* 鼠标点击：click()
* 获取元素可见文本：text
* 清空输入框：clear()
* 获取属性值：get_attribute()
* 判断元素是否启用编辑：is_enabled()
* 判断元素是否显示：is_displayed()
* 判断元素是否被选中：isSelected()
* 提交输入框内容：submit()

[python3+selenium4自动化测试-显式等待、隐式等待与强制等待-基础篇7](https://blog.csdn.net/qq_18298049/article/details/117264022)
* 隐式等待：implicitly_wait(10)
* 显式等待：WebDriverWait(driver, 5).until
```
from selenium import webdriver

driver = webdriver.Edge()
WebDriverWait(driver, timeout=5, poll_frequency=1, ignored_exceptions='ElementNotVisibleException').until(some_condition)
```
* 强制等待：time.sleep(5)
[python3+selenium4自动化测试-切换窗口与iframe-基础篇8](https://micheng.blog.csdn.net/article/details/117303257?spm=1001.2014.3001.5502)














[爬虫神器Selenium全攻略(2w字,建议收藏)](https://zhuanlan.zhihu.com/p/456436039)
[解决selenium + chromedriver被知乎反爬的问题](https://www.ancii.com/asrq5llpl/)
