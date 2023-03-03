**[Home](../Menu.md)**
[TOC]
# Keyevent
* Home键
`shell input keyevent KEYCODE_HOME`
* Back键
`adb shell input keyevent KEYCODE_BACK`

# Tapevent
* 点击
`adb shell input tap $x $y`

# Swipevent
* 滑动
`adb shell input swipe $start_x $start_y  $stop_x $stop_y`

# Inputevent
* 输入
`adb shell input text "HelloADB"`
注意： 空格需要用`%s`代替
`adb shell input text "Hello%sADB"`
借助shell命令
```
adb shell input text `echo "Hello ADB" | sed 's/ /%s/g'`
```
测试中经常会用到am start命令去进行操作，基本上也只用到 am start -n 和 am start -a ** -d **,后来测试activity启动用到了am start -W，才惊觉这个命令的功能还是很强大的，所以总结了一下，存档以备以后查看。

# AM Start
1. 启动一个activity
`am start -n <Activity>`
启动android原生设置的一级页面
`am start -n com.android.settings/.Settings`

2. 启动一个activity同时传入-d后面的参数
`am start -a <Activity> -d <parameter>`
打开拨号盘并拨打电话给10086
`am start -a android.intent.action.CALL -d tel:10086`
启动google键盘并定位到北京
`am start -a android.intent.action.VIEW geo:0,0?q=beijing`

3. 将应用设置成可调式模式，打开会提示waiting for debugger
`am start -D <Activity>`

4. 等待完全启动，并记录了启动时间
`am start -W <Activity>`
应用完全启动，并记录启动时间
`am start -W com.android.settings/.Settings`
结果如下：
```
Starting: Intent { act=android.intent.action.MAIN cat=[android.intent.category.LAUNCHER] cmp=com.android.settings/.Settings
Status: ok
Activity: com.android.settings/.MiuiSettings
ThisTime: 414
TotalTime: 718
WaitTime: 801
Complete
```
   
5. am start -P <FILE>
   解释：类似 –start-profiler，不同的是当app进入idle状态，则停止profiling
   
6. am start -S
   解释：启动activity之前，需要先调用forceStopPackage()方法强制停止应用，比如如果activity打开，-n只会重新起一遍activity，-S会杀掉原来的应用，重新启动activity
   
7. am start --opengl-trace
   解释：运行获取OpenGL函数的trace
   
8. am start --user <USER_ID> | current
   解释：指定用户来运行App,默认为当前用户。

