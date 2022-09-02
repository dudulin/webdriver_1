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
diff_time = start_time - now
print(diff_time)
# sleep(diff_time.total_seconds())
flag = True
while flag:
    # shift = Key.shift
    # keyboard = Controller()
    # keyboard.press(shift)
    # keyboard.release(shift)
    print('已经点击了')
    seq = [-1, 1]
    x = random.randint(10, 1000) * random.choice(seq)  # random.choice 参数：序列seq 随机其中一个
    y = random.randint(10, 1000) * random.choice(seq)
    print(x, y)
    pyautogui.moveRel(
        x, y, duration=3)
    sleep(3)
    if datetime.datetime.now() > end_time:
        flag = False



# 观察者实现  1.发布  2.监听