#coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from multiprocessing import Process
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
import os
from bs4 import BeautifulSoup           # 网页解析



class Test_Tools():
    def Test_X_Y():
        try:
            while True:
            # 获取到电脑屏幕分辨率和大小 
                screenWidth, screenHeight = pyautogui.size()
                # 获取鼠标位置
                x, y = pyautogui.position()
                # 输出鼠标位置
                print("Screen size: (%s %s),  Position : (%s, %s)\n" % (screenWidth, screenHeight, x, y))  
                # 每隔一秒执行一次
                time.sleep(1)
        except KeyboardInterrupt:
            print('end')

    def isElementExist(self):
        flag=True
        browser=self.driver
        ele=browser.find_elements_by_css_selector(element)
        if len(ele)==0:
            flag=False
            return flag
        if len(ele)==1:
            return flag
        else:
            flag=False
            return flag 

def get_random(date):
    if 1 == random.randint(0,1):
        return date + random.random()
    else:
        return date - random.random()

def random_sleep(_time):
    time.sleep(get_random(_time))

class Scheduler():
#调度器，说白了把它假设成为一个URL（抓取网页的网址或者说是链接）的优先队列，由它来决定下一个要抓取的网址是什么，同时去除重复的网址（不做无用功）。用户可以自己的需求定制调度器。
    def __init__(self):
        pass

class Downloader():
#下载器，是所有组件中负担最大的，它用于高速地下载网络上的资源。Scrapy 的下载器代码不会太复杂，但效率高，主要的原因是 Scrapy 下载器是建立在 twisted 这个高效的异步模型上的(其实整个框架都在建立在这个模型上的)。
    def __init__(self):
        pass
    
class Spider():
#爬虫，是用户最关心的部份。用户定制自己的爬虫(通过定制正则表达式等语法)，用于从特定的网页中提取自己需要的信息，即所谓的实体(Item)。例如使用 Xpath 提取感兴趣的信息。
#用户也可以从中提取出链接，让Scrapy继续抓取下一个页面。
    def __init__(self):
        pass

    def Get_Info(self):
        pass

class Item_Pipeline():
#实体管道，用于接收网络爬虫传过来的数据，以便做进一步处理。例如验证实体的有效性、清除不需要的信息、存入数据库（持久化实体）、存入文本文件等。
    def __init__(self):
        pass

    def save(self):
        pass

class Scrapy_Engine():
#Scrapy 引擎是整个框架的核心，用来处理整个系统的数据流，触发各种事件。它用来控制调试器、下载器、爬虫。实际上，引擎相当于计算机的CPU，它控制着整个流程。
    def __init__(self):
        # chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\NoteBook\Resource\Code\Scrapy\AutomationProfile"
        #os.system("chrome.exe --remote-debugging-port=9222 --user-data-dir=\"" + str(pathlib.Path().absolute()) + "\\AutomationProfile\"")
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()

        scheduler = Scheduler()
        downloader = Downloader()
        spider = Spider()
        item_pipeline = Item_Pipeline()

class Save_Data():
    def __init__(self, filename):
        self.filename = filename+'.md'
        f = open(self.filename, 'w+')
        f.close()

    def append_title(self, title):
        self.append('# ', title)

    def append_topic(self, topic, href):
        self.append('- [ ] ', '['+topic+']('+href+')')

    def append_info(self, comm):
        self.append('    ', comm)

    def append(self, flag , data):
        with open(self.filename, 'ab+') as f:
            # os.linesep代表当前操作系统上的换行符
            f.write((flag + data + os.linesep).encode('utf-8'))

class ZhiHu(Scrapy_Engine):
    def __init__(self, info, download_times):
        super(ZhiHu, self).__init__()
        self.driver.get("https://www.zhihu.com")
        random_sleep(1)

        self.saver = Save_Data("知乎_"+info)
        self.search_info(info, download_times)

    def load_all(self, load_times):
        print("Start loading ...")
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
            print("Please load all page.")
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
            random_sleep(30)
            #random_sleep(1)
            pyautogui.mouseUp()
            random_sleep(1)

        if len(self.driver.find_elements(By.XPATH, '/html/body/div[1]/div/div[5]/div/button')) > 0:
            self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div/button').click() # click Top
            random_sleep(5)

    def show_data(self):
        pageSource = self.driver.page_source
        soup = BeautifulSoup(pageSource, 'html.parser')
        id = 1
        for data in soup.find_all("div", class_="Card SearchResult-Card"):
            print(str(id)+"************************************************************************************************")
            #print(str(id)+":"+str(data.div.div.get("class")))
            #print(data.a["href"])
            if 'KfeCollection-PcCollegeCard-wrapper' in data.div.div.get("class"):
                print(data.a["href"])
            elif 'ArticleItem'  in data.div.div.get("class"):
                print("https:"+data.a["href"])
            elif 'ContentItem' in data.div.div.get("class"):
                print("https://www.zhihu.com"+data.a["href"])


            if 'KfeCollection-PcCollegeCard-wrapper' in data.div.div.get("class"):
                print(str(id) + "《" + data.find("div",class_="KfeCollection-PcCollegeCard-title").a.text + "》")
            #    print(data.find("div",class_="KfeCollection-PcCollegeCard-meta").div.text)
            elif 'AnswerItem' in data.div.div.get("class") or 'ArticleItem'  in data.div.div.get("class") or 'ZvideoItem' in data.div.div.get("class"):
                print(str(id) + "《" + data.find("h2",class_="ContentItem-title").text + "》")
                print(data.find("div",class_="RichContent-inner").div.text)
                print(data.find("div",class_="css-q1mqvc").find_all("button")[0].text)
                print(data.find("div",class_="css-q1mqvc").find_all("button")[2].text)
                print(data.find("span",class_="SearchItem-time").text)
            elif 'ContentItem' in data.div.div.get("class"):
                print(str(id) + "《" + data.find("h2",class_="ContentItem-title").text + "》")
                print(data.find("div",class_="ContentItem-actions").a.text)
                print(data.find("span",class_="SearchItem-time").text)

            else:
                continue
            id += 1




    def KfeCollection_PcCollegeCard_wrapper(self, id, data):
        #杂志文章
        title_item =   data.find_element(By.CLASS_NAME, "KfeCollection-PcCollegeCard-title").find_elements(By.TAG_NAME, "span")[0]
        content_item = data.find_element(By.CLASS_NAME, "KfeCollection-PcCollegeCard-meta").find_element(By.CLASS_NAME, "KfeCollection-PcCollegeCard-description ")
        #support_item = 
        #comment_item = 
        #date_item =    
        self.saver.append_topic(title_item.text, data.find_element(By.CLASS_NAME, "KfeCollection-PcCollegeCard-title").find_element(By.TAG_NAME, "a").get_attribute('href'))
        self.saver.append_info(content_item.text)
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
        self.saver.append_topic(title_item.text, data.find_element(By.CLASS_NAME, "ContentItem-title").find_element(By.TAG_NAME, "a").get_attribute('href'))
        self.saver.append_info("["  + date_item.text + ' · ' + support_item.text + "]")
        self.saver.append_info(content_item.text)
        print(str(id) + "《" + title_item.text + "》    ["  + date_item.text + ' · ' + support_item.text + "]")
        print("    " + content_item.text)
        print("    " + comment_item.text)
        result = re.search('(?P<comment_num>\d+) 条评论', comment_item.text)
        if result is None:
            comment_num = 0
        else:
            comment_num = int(result.group('comment_num'))
        #print("comment_num : " + str(comment_num))
    #    if comment_num > 0:
    #        comment_item.click()
    #        random_sleep(int(comment_num/10+2))
    #        self.AnswerItem_ArticleItem_ZvideoItem_Comment(data.find_element(By.CLASS_NAME, "Comments-container").find_element(By.XPATH,'div/div[2]/div[2]/div'))

    def ContentItem_actions(self, id, data):
        #关注问题
        title_item =   data.find_element(By.CLASS_NAME, "ContentItem-title")
        comment_item = data.find_element(By.CLASS_NAME, "ContentItem-actions").find_element(By.TAG_NAME, "a")
        date_item =    data.find_element(By.CLASS_NAME, "SearchItem-time")
        self.saver.append_topic(title_item.text, data.find_element(By.CLASS_NAME, "ContentItem-title").find_element(By.TAG_NAME, "a").get_attribute('href'))
        self.saver.append_info("["  + date_item.text + "]")
        print(str(id) + "《" + title_item.text + "》    ["  + date_item.text + "]")
        print("    " + comment_item.text)

    def Not_ContentItem_actions(self, id, data):
        title_item =   data.find_element(By.CLASS_NAME, "ContentItem-title").find_element(By.TAG_NAME, "a")
        #content_item = 
        #support_item = 
        comment_item = data.find_element(By.CLASS_NAME, "SearchItem-meta")
        #comment_item = data.find_element(By.CLASS_NAME, "ContentItem-actions").find_element(By.TAG_NAME, "a")
        #date_item =    data.find_element(By.CLASS_NAME, "SearchItem-time")
        self.saver.append_topic(title_item.text, title_item.get_attribute('href'))
        print(str(id) + " " + title_item.text + " ")
        print("    " + comment_item.text)



    def search_info(self, info, load_times):
        self.driver.find_element(By.CLASS_NAME, "SearchBar-input").find_element(By.TAG_NAME, 'input').send_keys(info)
        self.driver.find_element(By.CLASS_NAME, "SearchBar-input").find_element(By.TAG_NAME, 'button').click() # click search
        random_sleep(2)

        self.load_all(load_times)

        self.saver.append_title(info)
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


            #if id >5:
            #    break
            #soup = BeautifulSoup(data.get_property("outerHTML"), 'html.parser')
            #print("------------------------------------------------------------------------------------------------\n" + str(id)+" : \n"+soup.prettify())
            #print("*********************************************\n" + str(id)+" : \n"+data.find_element(By.CLASS_NAME, 'ContentItem-title').text+"\n"+data.find_element(By.CLASS_NAME, 'RichContent-inner').text)

            #break
        for comment in comment_list:
            soup = BeautifulSoup(comment.get_property("outerHTML"), 'html.parser')
            print("------------------------------------------------------------------------------------------------\n" + str(id)+" : \n"+soup.prettify())
            comment.click()
        #self.show_data()

class Chrome_Process(Process):
    def __init__(self, name, cmd):
        super().__init__()
        self.name=name
        self.cmd=cmd

    def run(self):
        print(self.name)
        os.system(self.cmd)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Need search info")
        exit(1)
    elif len(sys.argv) == 2:
        search_info = sys.argv[1]
        download_times = 30
    elif len(sys.argv) == 3:
        search_info = sys.argv[1]
        download_times = int(sys.argv[2])


    chrome=Chrome_Process("Chrome process 进程", "python.exe .\Start_Chrome.py")
    chrome.start() #start会自动调用run
    time.sleep(2)

    print('主线程')
    zhihu = ZhiHu(search_info, download_times)
    chrome.stop()


