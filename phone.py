# Android SDK 部署 ==》 手机开发者模式 ==》 正规数据线连接 ==》 python规范 adb代码
import time
import os


def execute(cmd):
    adbstr = 'adb shell {}'.format(cmd)
    print(adbstr, 'adbstr')
    os.system(adbstr)


def input_tab(x, y):  # 点击
    str = 'input tap {} {}'.format(x, y)
    execute(str)


input_tab(50, 600)
