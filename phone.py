# Android SDK 部署 ==》 手机开发者模式 ==》 正规数据线连接 ==》 python规范 adb代码
# adb devices   #查看已连接设备  31203622
from time import sleep
import os
from tool import get_time
import datetime


def execute(cmd):
    adbstr = 'adb shell {}'.format(cmd)
    print(adbstr, 'adbstr')
    os.system(adbstr)


def input_tab(x, y):  # 点击
    str = 'input tap {} {}'.format(x, y)
    execute(str)


def input_key(key):  # 点击按钮
    str = 'input keyevent {}'.format(key)  # 25
    execute(str)


def screencap(name='a'):  # 点击按钮
    str = 'screencap -p /sdcard/{}.png'.format(name)
    execute(str)
    os.system('adb pull /sdcard/{}.png img'.format(name))  # img 是路径


set_time = get_time(second=50, microsecond=0)
now = datetime.datetime.now()
diff = set_time - now
# sleep(diff.total_seconds())
# input_tab(50, 600)
# input_key(24)
screencap('now')  # 数据线 竟然 会影响到，差的数据线 会断开
