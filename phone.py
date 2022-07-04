# Android SDK 部署 ==》 手机开发者模式 ==》 正规数据线连接 ==》 python规范 adb代码
# adb devices   #查看已连接设备  31203622
from time import sleep
import os
from tool import get_time
import datetime


def adb_shell(cmd):
    adb_str = 'adb shell {}'.format(cmd)
    os.system(adb_str)


def input_tab(x, y):  # 点击
    str_1 = 'input tap {} {}'.format(x, y)
    adb_shell(str)


def input_key(key):  # 点击按钮
    str_1 = 'input keyevent {}'.format(key)  # 25
    adb_shell(str_1)


def screencap(name='a'):  # 点击按钮
    str_1 = 'screencap -p /sdcard/{}.png'.format(name)
    adb_shell(str_1)
    os.system('adb pull /sdcard/{}.png img'.format(name))  # img 是路径


set_time = get_time(second=50, microsecond=0)
now = datetime.datetime.now()
diff = set_time - now
# sleep(diff.total_seconds())
# input_tab(50, 600)
# input_key(24)
screencap('now')  # 数据线 竟然 会影响到，差的数据线 会断开
