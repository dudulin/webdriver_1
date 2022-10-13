import datetime
import random
from time import sleep

import pyautogui


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


now = datetime.datetime.now()

start_time = get_time(17, 15)
end_time = get_time(18, 30)

print('开始')
index = 0

diff_time = start_time - now
print(diff_time)
# sleep(diff_time.total_seconds())
flag = True
num = 1
while flag:
    pyautogui.keyDown('shift')    # 按下shift
    pyautogui.keyUp('shift')  # 释放 shift

    print('已经点击了')
    seq = [-1, 1]
    # random.choice 参数：序列seq 随机其中一个
    x = random.randint(10, 100) * random.choice(seq)
    y = random.randint(10, 100) * random.choice(seq)
    num = -num
    x = 100 * num
    y = 100 * num
    index += 1
    print(x, y, index)
    # pyautogui.moveRel(
    #     x, y, duration=3)
    sleep(60)
    if datetime.datetime.now() > end_time:
        # flag = False
        pass


# 观察者实现  1.发布  2.监听
'''
    思路：
    1.observers 收集监听对象的 box
    2.add     添加到box 的函数
    3.remove  移除  box 的函数

    触发=发布 方法 这里使用了 修改 字符串 来触发 box 里面的函数
    @property  && @startStr.setter  成对出现，缺少了会报错

    4.@startStr.setter 触发时候 传入需要的数据 ：self._startStr

'''


class Publisher:
    def __init__(self, name):
        self.observers = []
        self._startStr = ''

    @property  # 属性的查询函数
    def startStr(self):
        return self._startStr

    @startStr.setter  # 属性的设置函数
    def startStr(self, value):
        self._startStr = value
        for i in self.observers:
            i.update(self._startStr)

    def add(self, observer):
        self.observers.append(observer)

    def remove(self, observer):
        try:
            self.observers.remove(observer)  # python 数组 列表 remove 函数

        except ValueError:
            print('移除失败：{}'.format(observer))


class Ob(object):
    def __init__(self, name):
        self.name = name
        self.topic = None

    def update(self, topic):
        self.topic = topic
        print('{0}更新: {1}'.format(self.name, self.topic))


pub = Publisher('xx')

a1 = Ob('a1')
a2 = Ob('a2')
a3 = Ob('a3')

pub.add(a1)
pub.add(a2)

pub.startStr = '开始运行'

pub.remove(a1)

pub.startStr = '开始运行2'
