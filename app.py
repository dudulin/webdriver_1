# -- coding: utf-8 --    # 编码规则
# 若出现 Python编 码问题，可按照以下操作尝试解决
# import sys # 导入系统
# reload(sys)
# sys.setdefaultencoding('utf-8') # 设置规范

# (二)命名规范:
# 1、包名、模块名、局部变量名、函数名  this_is_var


import time
import pyautogui
from selenium.webdriver.common.by import By

from tool import get_time
from tool import create_driver
from tool import url_dict


def find_ele(id):
    return driver.find_element(By.ID, id)  # find_element_by_id 旧方法 已经 淘汰
    # driver.find_element(By.XPATH, '//*[@id="cc"]/div/button')


is_local_web = True
driver = create_driver(is_local_web)
driver.get(url_dict['jd'])

now = get_time()
print(now, 'now')

jd_id = driver.current_window_handle  # 当前窗口 id
windows = driver.window_handles  # 所有浏览器窗口

time.sleep(3)
btn = find_ele('ttbar-navs')
# btn.rect # {'height': 30, 'width': 77, 'x': 743, 'y': 0}
rect = btn.rect
center = pyautogui.center(
    (rect['x'],
     rect['y'],
     rect['width'],
     rect['height']))  # 入参元组 (a,b,c)
print(btn.size['width'], 'btn', rect, center)

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
