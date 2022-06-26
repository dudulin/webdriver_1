# Android SDK 部署 ==》 手机开发者模式 ==》 正规数据线连接 ==》 python规范 adb代码
# adb devices   #查看已连接设备  31203622
import time
import os


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
    os.system('adb pull /sdcard/{}.png'.format(name))

# input_tab(50, 600)
# input_key(24)
screencap() # 数据线 竟然 会影响到，差的数据线 会断开
