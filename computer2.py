from time import sleep

from pynput.keyboard import Key
from pynput.keyboard import Controller
import pyautogui
import datetime
import random


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

action_time = get_time(18, 0)
action_time2 = get_time(19, 0)

diff_time = action_time - now

# sleep(diff_time.total_seconds())
flag = True
while flag:
    shift = Key.shift
    keyboard = Controller()
    keyboard.press(shift)
    keyboard.release(shift)
    print('已经点击了')
    pyautogui.moveRel(
        random.randint(
            50, 1000), random.randint(
            50, 1000), duration=3)
    sleep(5)
    # if datetime.datetime.now() > action_time2:
    #     flag = False
