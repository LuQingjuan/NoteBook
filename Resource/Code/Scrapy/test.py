
import pyautogui
import time
import random

def get_random(date):
    if 1 == random.randint(0,1):
        return date + random.random()
    else:
        return date - random.random()

def random_sleep(_time):
    time.sleep(get_random(_time))


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

def Test():
    id = 0
    screenWidth, screenHeight = pyautogui.size()
    print(str(screenWidth) + " : " + str(screenHeight))
    while True:
        x = screenWidth-random.uniform(1,20)
        y = random.uniform(screenHeight*4/5,screenHeight-80)
        print("click " + str(x) + " : " + str(y))
        pyautogui.click(x, y, button='left')
        time.sleep(random.uniform(1,3))
        id += 1
        if id >20:
            break
    #pyautogui.mouseDown()
    #random_sleep(15)
    #random_sleep(1)
   # pyautogui.mouseUp()
   # 

#Test_X_Y()
Test()