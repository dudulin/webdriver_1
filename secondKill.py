import os
from time import sleep


class CreateAdb():
    def swipe(self):
        sleep(2)
        # 模拟从下往上滑动 x y => x y
        os.system('adb shell input swipe 900 1200 900 500')
        sleep(2)

    # 返回上一页面
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


adb = CreateAdb()
print(adb.get_size())  # Physical size: 1080x2340
adb.text('666')
cc = adb.get_ip()

print(cc)
