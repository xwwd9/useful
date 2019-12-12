import logging
import time

import pyautogui as pyautogui
import pywinauto
from airtest.core.api import touch, exists
from airtest.core.cv import Template
from pywinauto.win32functions import GetSystemMetrics

from useful_python.examples.my_pywinauto.tools import init_weixin, air_init

logger = logging.getLogger(__name__)

X_MAX = GetSystemMetrics(0)
Y_MAX = GetSystemMetrics(1)
X_MIDDLE = int(X_MAX / 2)
Y_MIDDLE = int(Y_MAX / 2)
X_BACK = -1
Y_BACK = -1

# 列表页向下移动像素
SUBSCRIBE_DOWN_MOVE = 70
SUBSCRIBE_RIGHT_MOVE = 700
# 从下方点击订阅文章的初始位置
SUBSCRIBE_DETAIL_START = 950

IMG_PATH = 'imgs/'
# 动作定义
CLICK_SUBSCRIBE = IMG_PATH + 'subscription.png'
CLICK_BACK = IMG_PATH + 'back.png'
CLICK_NEW = IMG_PATH + 'new.png'
SUBSCRIBE_TEXT = IMG_PATH + 'sub_text.png'
MORE_TEXT = IMG_PATH + 'more.png'


dlg = None

def do_action(action):
    touch(Template(action))


def is_in_detail():
    ret = exists(Template(CLICK_BACK))
    # 直接返回False
    if not ret:
        return ret
    if ret[1] > 70 and ret[0] > X_MIDDLE:
        return False
    ret = exists(Template(MORE_TEXT))
    if not ret:
        return ret
    if ret[1] > 70 and ret[0] < X_MIDDLE:
        return False
    return ret


def set_back_position(x, y):
    global X_BACK
    global Y_BACK
    X_BACK = x
    Y_BACK = y


def click_detail_list():
    """
    依次点击详情页
    """
    x = X_MIDDLE
    y = SUBSCRIBE_DETAIL_START
    for i in range(2):
        pywinauto.mouse.move(coords=(x, y))
        pywinauto.mouse.click(coords=(x, y))
        time.sleep(2)
        dlg.set_focus()
        pywinauto.mouse.move(coords=(x, y))
        y -= 70
        time.sleep(2)



def run():
    while True:
        x, y = X_MIDDLE, 30
        for i in range(10):
            print(x, y)
            pywinauto.mouse.move(coords=(x, y + 70))
            pywinauto.mouse.click(coords=(x, y + 70))

            click_detail_list()


            if is_in_detail():
                set_back_position(*is_in_detail())
                print("当前在某个公众号页面")
                do_action(CLICK_BACK)

            # time.sleep(2)
            x, y = x, y + 70

        pywinauto.mouse.scroll(coords=(x, y), wheel_dist=-30)


if __name__ == "__main__":


    dlg = init_weixin()
    uuid = dlg.handle
    air_init(uuid)
    do_action(CLICK_SUBSCRIBE)

    pywinauto.mouse.move(coords=(X_MIDDLE, 0))

    run()



