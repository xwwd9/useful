import logging
import time
import logging.config
import cv2
import numpy as np
import pyautogui as pyautogui
import pywinauto
from airtest.core.api import touch, exists, find_all
from airtest.core.cv import Template
from airtest.core.win import Windows
from pywinauto.win32functions import GetSystemMetrics

from useful_python.examples.my_pywinauto.tools import init_weixin, air_init

logger = logging.getLogger("main")

X_MAX = GetSystemMetrics(0)
Y_MAX = GetSystemMetrics(1)
X_MIDDLE = int(X_MAX / 2)
Y_MIDDLE = int(Y_MAX / 2)
X_BACK = -1
Y_BACK = -1

# 列表页向下移动像素
SUBSCRIBE_DOWN_MOVE = int(Y_MAX * 0.064)
SUBSCRIBE_RIGHT_MOVE = 700
# 从下方点击订阅文章的初始位置
SUBSCRIBE_DETAIL_START = int(Y_MAX * 0.88)
# 详情页每上一步的距离
SUBSCRIBE_DETAIL_UP = int(Y_MAX * 0.064)
# 在详情页鼠标上移多少次
SUBSCRIBE_DETAIL_UP_TIMES = 2

IMG_PATH = 'imgs/'
# 动作定义
CLICK_SUBSCRIBE = IMG_PATH + 'subscription.png'
CLICK_BACK = IMG_PATH + 'back.png'
CLICK_NEW = IMG_PATH + 'new.png'
SUBSCRIBE_TEXT = IMG_PATH + 'sub_text.png'
MORE_TEXT = IMG_PATH + 'more.png'
PIC_AM = IMG_PATH + 'am.png'
PIC_PM = IMG_PATH + 'pm.png'
PIC_NEW = IMG_PATH + 'new.png'
# PIC_NEW = IMG_PATH + 'fake_new.png'

# 图片序列名字
img_index = 0
bac_pos = False

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
    pos = ret
    ret = exists(Template(MORE_TEXT))
    if not ret:
        return ret
    if ret[1] > 70 and ret[0] < X_MIDDLE:
        return False
    return pos


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
    for i in range(SUBSCRIBE_DETAIL_UP_TIMES):
        pywinauto.mouse.move(coords=(x, y))
        pywinauto.mouse.click(coords=(x, y))
        time.sleep(4)
        dlg.set_focus()
        pywinauto.mouse.move(coords=(x, y))
        y -= SUBSCRIBE_DETAIL_UP
        time.sleep(1)
        logger.info('点击第%d篇文章' % i)


def find_news():
    ret_news = find_all(Template(PIC_NEW))
    # ret_am = find_all(Template(PIC_AM))
    # ret_pm = find_all(Template(PIC_PM))

    if ret_news:
        print(ret_news)

        print(len(ret_news))
    else:
        ret_news = []

    return ret_news


# def run():
#     while True:
#         x, y = X_MIDDLE, 30
#         for i in range(10):
#             print(x, y)
#             pywinauto.mouse.move(coords=(x, y + 70))
#             pywinauto.mouse.click(coords=(x, y + 70))
#
#             click_detail_list()
#
#
#             if is_in_detail():
#                 set_back_position(*is_in_detail())
#                 do_action(CLICK_BACK)
#
#             # time.sleep(2)
#             x, y = x, y + 70
#
#         pywinauto.mouse.scroll(coords=(x, y), wheel_dist=-30)


def scroll_to_top():
    x, y = X_MIDDLE, Y_MIDDLE
    for i in range(100):
        pywinauto.mouse.scroll(coords=(x, y), wheel_dist=30)


def screen_shot():
    """

    """

    global img_index

    img = pyautogui.screenshot(region=[0, 0, X_MAX, Y_MAX])  # x,y,w,h
    img.save('screen_shot/' + str(img_index) + '.png')
    img_index += 1
    if img_index == 300:
        img_index = 0

    # img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)


def run_new():
    global bac_pos
    scroll_to_top()
    for i in range(10):
        time.sleep(2)
        x, y = X_MIDDLE, Y_MIDDLE

        rets = find_news()

        logger.info('当前新消息的位置'+str(rets))
        screen_shot()

        for ret in rets:
            result = ret.get('result', (0, 0))
            pywinauto.mouse.move(coords=result)
            time.sleep(1)

            pywinauto.mouse.click(coords=result)

            logger.info('点击进入公众号')
            screen_shot()


            click_detail_list()

            logger.info("开始判断是否在公众号页面,需不需要返回")
            if not bac_pos:
                bac_pos = is_in_detail()
            if is_in_detail():
                logger.info("当前在公众号详情页面，需要返回")
                # set_back_position(*bac_pos)
                # do_action(CLICK_BACK)
                pywinauto.mouse.click(coords=bac_pos)
            else:
                # 没识别到返回页面，流程可能出错需要从进订阅号页面
                do_action(CLICK_SUBSCRIBE)
                logger.info("没识别到返回页面，流程可能出错需要从进订阅号页面")
                screen_shot()

        time.sleep(1)

        pywinauto.mouse.scroll(coords=(x, y), wheel_dist=-30)


if __name__ == "__main__":

    logging.config.fileConfig('logging.cfg')

    # logger.debug("debug")
    # logger.info("info")
    # logger.error("error")

    dlg = init_weixin()
    uuid = dlg.handle
    air_init(uuid)
    do_action(CLICK_SUBSCRIBE)

    screen_shot()

    pywinauto.mouse.move(coords=(X_MIDDLE, 0))

    while True:
        try:
            run_new()
        except Exception as e:
            print(e)
            logger.error(e)
            time.sleep(10)
