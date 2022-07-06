import os
from time import sleep


class CreateAdb():

    def __init__(self):
        self.ip_list = {
            'wx': 'com.tencent.mm/com.tencent.mm.ui.LauncherUI',
            'yd': 'com.youdao.dict/com.youdao.dict.activity.MainActivity',
            'mt': 'com.moutai.mall/com.moutai.mall.MainActivity'
        }

    def swipe_end(self, limt=1):
        sleep(1)
        for i in range(0, limt):
            os.system('adb shell input swipe 900 500 100 500')
            sleep(1)

    def goback(self):
        os.system('adb shell input keyevent KEYCODE_BACK')
        sleep(2)
        print('退出')

    def get_size(self):
        size = os.popen('adb shell wm size')
        return size.read()

    def wifi_connect(self):
        os.system('adb tcpip 5555')
        sleep(2)
        os.system('adb connect {}'.format(''))

    def get_ip(self):
        message = os.popen('adb shell ifconfig "| grep Mask"')  # 10.24.22.209
        return message.read()

    def text(self, text):
        os.system('adb shell input text {}'.format(text))

    def open_wx(self):
        os.system('adb shell am start com.tencent.mm/com.tencent.mm.ui.LauncherUI')

    def open_app(self, key):
        os.system('adb   shell   am   start {}'.format(self.ip_list[key]))

    def stop_app(self, key):
        sleep(3)
        os.system('adb shell am force-stop {}'.format(self.ip_list[key]))

    def get_app_ip(self):
        message = os.popen('adb shell dumpsys window | findstr mCurrentFocus')
        print(message.read(), 'app_ip')

    def swipe_y(self, start=100, end=0):
        sleep(1)
        os.system('adb shell input swipe 800 {} 400 {}'.format(start, end))

    def swipe_x(self, start=100, end=0):
        sleep(1)
        os.system('adb shell input swipe  {} 100  {} 100'.format(start, end))

    def click(self, x, y):
        sleep(1)
        os.system('adb shell input tap {} {}'.format(x, y))

    def screencap(self, name='a'):  # 点击按钮
        os.system(
            'adb shell screencap -p /sdcard/{}.png'.format(name))  # img 是路径

        os.system('adb pull /sdcard/{}.png img'.format(name))  # img 是路径

    def project_mt(self):
        self.open_app('mt')
        sleep(5)
        self.swipe_y(1000, 0)
        self.click(500, 2000)

        print('操作完成')
        sleep(1)
        self.stop_app('mt')


adb = CreateAdb()
# print(adb.get_size())  # Physical size: 1080x2340
# adb.text('sss')
# cc = adb.get_ip()
# print(cc)
# adb.swipe_end(3)
# adb.open_wx()

# adb.get_app_ip()
# com.youdao.dict/com.youdao.dict.activity.MainActivity}
# adb.project_mt()
adb.screencap()
# uiautomatorviewer.bat  界面控制
