

###1.把常用的函数统一 规范到tool.py  方便整理 记忆
###2.命名统一 小写  + 下划线 
###3.import 模版 必须 备注 
###4.bool变量一般加上前缀 is_ 如：is_success  
###5.代码排序 模块=>变量=>函数=>执行代码

pip install pynput
目前支持鼠标和键盘的控制与监听

使用 pyautogui.confirm  来关闭浏览器

import win32clipboard as w # 剪切板
import win32con # 转码

find_element(By.ID, 'abc')

### ctrl + 鼠标左键  ==> 打开模块源码 ！！！


# Android SDK 部署 ==》 手机开发者模式 ==》 正规数据线连接 ==》 python规范 adb代码

screencap() # 数据线 竟然 会影响到，差的数据线 会断开


---

### autopep8 运行出错  是 指向问题  cmd  系统中 安装 autopep8 

手机连接adb 通过wifi 需要 电脑和 手机同在一个 局域网
电脑：wlan 查看 


    os.system('adb tcpip 55555') # 192.168.123.4
    sleep(2)
    os.system('adb connect {}'.format('192.168.123.4:55555')) #42389



'''
    思路：
    1.observers 收集监听对象的 box 
    2.add     添加到box 的函数
    3.remove  移除  box 的函数
    
    触发=发布 方法 这里使用了 修改 字符串 来触发 box 里面的函数
    @property  && @startStr.setter  成对出现，缺少了会报错
    
    4.@startStr.setter 触发时候 传入需要的数据 ：self._startStr

'''