#coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#ID = "id"
#XPATH = "xpath"
#LINK_TEXT = "link text"
#PARTIAL_LINK_TEXT = "partial link text"
#NAME = "name"
#TAG_NAME = "tag name"
#CLASS_NAME = "class name"
#CSS_SELECTOR = "css selector"
import pyautogui
import time
import random
import sys
import re
from bs4 import BeautifulSoup           # 网页解析



def get_random(date):
    if 1 == random.randint(0,1):
        return date + random.random()
    else:
        return date - random.random()

def random_sleep(_time):
    time.sleep(get_random(_time))


class ZhiHu():
    def __init__(self):
        #[【python】Selenium+python3使用总结（一）](https://blog.csdn.net/qq_35061334/article/details/122868502)
        #* 安装 selenium
        #* 安装 chromedriver
        #* 配置环境变量
        #* 简单示例
        #```
        #from selenium import webdriver
        #
        #driver = webdriver.Chrome()
        #driver.get("https://www.baidu.com/")
        #```
        #
        #[使用python+selenium控制手工已打开的浏览器](https://www.cnblogs.com/HJkoma/p/9936434.html)
        #* Chrome浏览器路径加到patch中
        #* 在命令行输入`chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Users\luqingjuan\Downloads\selenum\AutomationProfile"`
        #    * 对于-remote-debugging-port值，可以指定任何打开的端口。
        #    * 对于-user-data-dir标记，指定创建新Chrome配置文件的目录。它是为了确保在单独的配置文件中启动chrome，不会污染你的默认配置文件。
        #* 现在，我们需要接管上面的浏览器。新建一个python文件，运行以下代码：
        #```
        #from selenium import webdriver
        #from selenium.webdriver.chrome.options import Options
        #
        #chrome_options = Options()
        #chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        #chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        #driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
        #print(driver.title)
        #```




        # chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Users\luqingjuan\Downloads\selenum\AutomationProfile"
        # chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\NoteBook\Code\Scrapy\AutomationProfile"
        #os.system("chrome.exe --remote-debugging-port=9222 --user-data-dir=\"" + str(pathlib.Path().absolute()) + "\\AutomationProfile\"")
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

        self.driver.maximize_window()
        self.driver.get("https://www.zhihu.com")
        random_sleep(1)

    def load_all(self, load_times):
        screenWidth, screenHeight = pyautogui.size()
        #print(str(screenWidth) + " : " + str(screenHeight))
        while load_times > 0:
            load_times -= 1
            x = screenWidth-random.uniform(1,20)
            y = random.uniform(screenHeight*4/5,screenHeight-80)
            #print("click " + str(x) + " : " + str(y))
            #print("click " + str(x) + " : " + str(y) + "[" + str(len(self.driver.find_elements(By.CLASS_NAME, "SearchResult-Card"))) + "]")
            pyautogui.click(x, y, button='left')
            time.sleep(random.uniform(1,3))

        if len(self.driver.find_elements(By.CLASS_NAME, 'CornerAnimayedFlex--hidden')) == 0:
            #print(BeautifulSoup(self.driver.find_element(By.CLASS_NAME, 'CornerButtons').get_property("outerHTML"), 'html.parser').prettify())
            self.driver.find_element(By.CLASS_NAME, 'CornerButtons').find_element(By.TAG_NAME, 'button').click() # click Top
            random_sleep(5)
        self.driver.execute_script("scrollBy(0,250);")

    def load_all_old(self):
        if 1:
            print("Please load all page. Then goto Top")
            input('Press enter to continue: ')
        else:#debug
            screenWidth, screenHeight = pyautogui.size()
            #x1 = screenWidth - 1
            #y1 = screenHeight - 60
            #print(str(x1)+":"+str(y1))
            #x1=1919
            #y1=1020
            #print(str(x1)+":"+str(y1))
            pyautogui.click(screenWidth-get_random(2), screenHeight-get_random(60), button='left')
            pyautogui.mouseDown()
            random_sleep(15)
            #random_sleep(1)
            pyautogui.mouseUp()
            random_sleep(1)

        if len(self.driver.find_elements(By.XPATH, '/html/body/div[1]/div/div[5]/div/button')) > 0:
            self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div/button').click() # click Top
            random_sleep(5)


    def KfeCollection_PcCollegeCard_wrapper(self, id, data):
        #杂志文章
        title_item =   data.find_element(By.CLASS_NAME, "KfeCollection-PcCollegeCard-title").find_elements(By.TAG_NAME, "span")[0]
        content_item = data.find_element(By.CLASS_NAME, "KfeCollection-PcCollegeCard-meta").find_element(By.CLASS_NAME, "KfeCollection-PcCollegeCard-description ")
        #support_item = 
        #comment_item = 
        #date_item =    
        print(str(id) + "《" + title_item.text + "》")
        print(content_item.text)

    def AnswerItem_ArticleItem_ZvideoItem_Comment(self, data):
        for list_data in data.find_elements(By.XPATH, "div"):
            #print()
            if len(list_data.find_elements(By.XPATH, "div")) >0:
                id = 0
                for comment_data in list_data.find_elements(By.XPATH, "div"):
                    if 0 != id:
                        comment_data = comment_data.find_element(By.XPATH, "div")
                    #print("0++++++++++++++++++++++")
                    #print(BeautifulSoup(comment_data.get_property("outerHTML"), 'html.parser').prettify())
                    #print("1++++++++++++++++++++++")
                    #print(BeautifulSoup(comment_data.find_elements(By.XPATH, "div")[1].get_property("outerHTML"), 'html.parser').prettify())
                    #print("2++++++++++++++++++++++")
                    #print(BeautifulSoup(comment_data.find_elements(By.XPATH, "div")[1].find_elements(By.XPATH, "div")[0].get_property("outerHTML"), 'html.parser').prettify())
                    #print("3++++++++++++++++++++++")
                    #comment_infos = comment_data.find_elements(By.XPATH, "div")[1].find_elements(By.XPATH, "div")
                    #print(BeautifulSoup(comment_infos[0].get_property("outerHTML"), 'html.parser').prettify())
                    #print(BeautifulSoup(comment_infos[1].get_property("outerHTML"), 'html.parser').prettify())
                    #print(BeautifulSoup(comment_infos[2].get_property("outerHTML"), 'html.parser').prettify())
                    #print("++++++++++++++++++++++")
                    writer_item = comment_data.find_elements(By.XPATH, "div")[1].find_elements(By.XPATH, "div")[0].find_element(By.TAG_NAME, "a")
                    comment_item = comment_data.find_elements(By.XPATH, "div")[1].find_elements(By.XPATH, "div")[1]
                    date_item = comment_data.find_elements(By.XPATH, "div")[1].find_elements(By.XPATH, "div")[2].find_element(By.XPATH, "div")
                    #stemp_num = 
                    temp_support_item = comment_data.find_elements(By.XPATH, "div")[1].find_elements(By.XPATH, "div")[2].find_elements(By.TAG_NAME, "button")
                    support_item = temp_support_item[len(temp_support_item)-1]
                    #print(BeautifulSoup(writer_item.get_property("outerHTML"), 'html.parser').prettify())
                    if 0 == id:
                        print("        * " + writer_item.text + " : " + comment_item.text.replace('\n' , '\n            ') + "    [" + date_item.text + " · 赞同 " + support_item.text.replace('赞','') + "]")
                    else:
                        print("            * " + writer_item.text + " : " + comment_item.text.replace('\n' , '\n                ')  + "    [" + date_item.text + " · 赞同 " + support_item.text.replace(' 赞','') + "]")
                    id += 1

    def AnswerItem_ArticleItem_ZvideoItem(self, id, data):
        #print(BeautifulSoup(data.get_property("outerHTML"), 'html.parser').prettify())
        title_item =   data.find_element(By.CLASS_NAME, "ContentItem-title")
        content_item = data.find_element(By.CLASS_NAME, "RichContent-inner").find_element(By.XPATH,"div")
        support_item = data.find_elements(By.TAG_NAME, "button")[1]
        comment_item = data.find_elements(By.TAG_NAME, "button")[3]
        #print(BeautifulSoup(support_item.get_property("outerHTML"), 'html.parser').prettify())
        #print(BeautifulSoup(comment_item.get_property("outerHTML"), 'html.parser').prettify())
        date_item =    data.find_element(By.CLASS_NAME, "SearchItem-time")
        print(str(id) + "《" + title_item.text + "》    ["  + date_item.text + ' · ' + support_item.text + "]")
        print("    " + content_item.text)
        print("    " + comment_item.text)

        result = re.search('(?P<comment_num>\d+) 条评论', comment_item.text)
        if result is None:
            comment_num = 0
        else:
            comment_num = int(result.group('comment_num'))
        #print("comment_num : " + str(comment_num))
        if comment_num > 0:
            comment_item.click()
            random_sleep(int(comment_num/10+2))
            self.AnswerItem_ArticleItem_ZvideoItem_Comment(data.find_element(By.CLASS_NAME, "Comments-container").find_element(By.XPATH,'div/div[2]/div[2]/div'))

    def ContentItem_actions(self, id, data):
        #关注问题
        title_item =   data.find_element(By.CLASS_NAME, "ContentItem-title")
        comment_item = data.find_element(By.CLASS_NAME, "ContentItem-actions").find_element(By.TAG_NAME, "a")
        date_item =    data.find_element(By.CLASS_NAME, "SearchItem-time")
        print(str(id) + "《" + title_item.text + "》    ["  + date_item.text + "]")
        print("    " + comment_item.text)

    def Not_ContentItem_actions(self, id, data):
        title_item =   data.find_element(By.CLASS_NAME, "ContentItem-title").find_element(By.TAG_NAME, "a")
        #content_item = 
        #support_item = 
        comment_item = data.find_element(By.CLASS_NAME, "SearchItem-meta")
        #comment_item = data.find_element(By.CLASS_NAME, "ContentItem-actions").find_element(By.TAG_NAME, "a")
        #date_item =    data.find_element(By.CLASS_NAME, "SearchItem-time")
        print(str(id) + " " + title_item.text + " ")
        print("    " + comment_item.text)

    ########################################################################
    def search_info(self, info, load_times):
        self.driver.find_element(By.CLASS_NAME, "SearchBar-input").find_element(By.TAG_NAME, 'input').send_keys(info)
        self.driver.find_element(By.CLASS_NAME, "SearchBar-input").find_element(By.TAG_NAME, 'button').click() # click search
        random_sleep(2)

        self.load_all(load_times)

        id = 1
        comment_list = []
        #for data in self.driver.find_elements(By.XPATH, '/html/body/div[1]/div/main/div/div[2]/div[2]/div/div/div/div/div'):
        for data in self.driver.find_elements(By.CLASS_NAME, "SearchResult-Card"):
            print("------------------------------------------------------------------------------------------------")
            #print("------------------------------------------------------------------------------------------------\n" + str(id)+" : \n"+data.text)
            data = data.find_element(By.XPATH,'div/div')
            content_type = data.get_attribute('class')
            #print(content_type)
            if 'KfeCollection-PcCollegeCard-wrapper' in content_type:
                self.KfeCollection_PcCollegeCard_wrapper(id, data)
            elif 'AnswerItem' in content_type or 'ArticleItem'  in content_type or 'ZvideoItem' in content_type:
                self.AnswerItem_ArticleItem_ZvideoItem(id, data)
            elif 'ContentItem' in content_type:
                if len(data.find_elements(By.CLASS_NAME, "ContentItem-actions")) > 0:
                    self.ContentItem_actions(id, data)
                else:
                    print("********************")
                    self.Not_ContentItem_actions(id, data)
            else:
                continue
            id += 1
            random_sleep(2)

if len(sys.argv) == 1:
    print("Need search info")
    exit(1)
elif len(sys.argv) == 2:
    search_info = sys.argv[1]
    download_times = 30
elif len(sys.argv) == 3:
    search_info = sys.argv[1]
    download_times = int(sys.argv[2])

zhihu = ZhiHu()
zhihu.search_info(search_info, download_times)

