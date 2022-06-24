from selenium import webdriver
from selenium.webdriver import Chrome
import time
import pyautogui


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
        pyautogui.PAUSE = 1  # 意味着所有pyautogui的指令都要暂停0.5

        pyautogui.hotkey('win', 'r')
        pyautogui.hotkey('enter')
        # pyautogui.hotkey('shift') # 看实际 避免中文
        pyautogui.typewrite(
            'cd C:/Program Files/Google/Chrome/Application'
        )
        pyautogui.hotkey('enter')
        pyautogui.typewrite(
            'chrome.exe --remote-debugging-port=9222 --user-data-dir=“D:\auto”')
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


useLocal = True
driver = create_driver(useLocal)

driver.get('https://www.jd.com/')

jd_id = driver.current_window_handle  # 当前窗口 id

windows = driver.window_handles  # 所有浏览器窗口

time.sleep(3)
a = pyautogui.confirm('选择一项', buttons=['关闭', 'title', 'C', 'D'])
if a == '关闭':
    driver.close()
    driver.quit()
if a == 'title':
    print(driver.title, 'title')
    driver.close()
    driver.quit()
if a == 'C':
    driver.switch_to.window(jd_id)
    print(driver.title, 'title')
if a == 'D':
    driver.switch_to.window(windows[-1])  # 切换到当前最新打开的窗口
    print(driver.title, 'title')
