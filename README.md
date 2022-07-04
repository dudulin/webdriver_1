

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


pyinstaller -F app.py
 必须ignore 文件 否则太多上传不了
---