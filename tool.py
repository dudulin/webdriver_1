import datetime
import time
import pyautogui
# import win32clipboard as w
# import win32con
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

import os
from time import sleep

# 修改剪贴板内容
# 传入需要的值即可修改剪贴板


# def set_clipboard(str):
#     w.OpenClipboard()
#     w.EmptyClipboard()
#     w.SetClipboardData(win32con.CF_UNICODETEXT, str)
#     w.CloseClipboard()


def get_time(hour=-1, minute=-1, second=-1, microsecond=-1):

    time_now = datetime.datetime.now()
    h = hour if hour != -1 else time_now.hour
    m = minute if minute != -1 else time_now.minute
    s = second if second != -1 else time_now.second
    mic = microsecond if microsecond != -1 else time_now.microsecond

    time_start = datetime.datetime(
        time_now.year,
        time_now.month,
        time_now.day,
        h,
        m,
        s,
        mic)
    # time_difference = time_start - time_now
    # time1 = time_difference.total_seconds()
    return time_start


def create_driver(useLocal):
    options = webdriver.ChromeOptions()
    print(options, 'options')
    # 第一步，使用chrome开发者模式
    # options.add_experimental_option('excludeSwitches',
    # ['enable-automation']) # 和本地浏览器不兼容
    # argument = 'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
    # options.add_argument(argument)

    # options.add_argument('--window-size=600,600')  # 设置窗口大小
    # options.add_argument('--start-maximized')  # 最大化运行（全屏窗口）,不设置，取元素会报错
    # options.add_argument('--incognito')  # 无痕模式
    # options.add_argument('--disable-infobars')  # 去掉chrome正受到自动测试软件的控制的提示
    # options.add_argument('user-agent="XXXX"')  # 添加请求头
    # options.add_argument("--proxy-server=http://200.130.123.43:3456")  # 代理服务器访问
    # options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 开发者模式
    # options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})  # 禁止加载图片
    # options.add_experimental_option('prefs',
    #                           {'profile.default_content_setting_values': {'notifications': 2}})  # 禁用浏览器弹窗
    # options.add_argument('blink-settings=imagesEnabled=false')  # 禁止加载图片
    options.add_argument('lang=zh_CN.UTF-8')  # 设置默认编码为utf-8
    # o.add_argument('--disable-gpu')  # 这个属性可以规避谷歌的部分bug

    # cmd=> cd C:\Program Files\Google\Chrome\Application
    # cmd=>chrome.exe --remote-debugging-port=9222 --user-data-dir=“D:\auto”
    if useLocal:
        # os.system("cmd")
        pyautogui.PAUSE = 0.5  # 意味着所有pyautogui的指令都要暂停0.5
        path = 'cd C:/Program Files/Google/Chrome/Application'
        path2 = 'chrome.exe --remote-debugging-port=9222 --user-data-dir=“D:auto”'

        pyautogui.hotkey('win', 'r')
        pyautogui.hotkey('enter')
        # 调用测试
        set_clipboard(path)  # 使用复制  使用复制 避免 输入时候中英文 混淆
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey('enter')
        set_clipboard(path2)  # 使用复制
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey('enter')
        options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")  #

    # 调用原来的浏览器，不用再次登录即可重启
    chrome_driver = Chrome(options=options)

    # 加载 反 反爬虫 js

    chrome_driver.implicitly_wait(3)  # 隐式 等待
    with open('stealthFile/stealth.min.js') as f:
        js = f.read()

    chrome_driver.execute_cdp_cmd(
        "Page.addScriptToEvaluateOnNewDocument", {
            "source": js})

    chrome_driver.execute_cdp_cmd(
        "Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                        Object.defineProperty(navigator, 'webdriver', {
                          get: () => undefined
                        })
                      """
        })

    return chrome_driver


url_dict = {
    'jd': 'https://www.jd.com/',
    'taobao': 'https://www.taobao.com/',
    'bili': 'https://www.bilibili.com/',
    'baidu': 'https://www.baidu.com/'
}


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


class WebDriver(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def test(self):
        self.driver.get(url_dict['baidu'])
        time.sleep(1)
        self.driver.find_element(By.ID, 'kw').send_keys('5555')
        time.sleep(1)
        self.driver.find_element(By.ID, 'su').click()
        time.sleep(5)
        self.driver.quit()
