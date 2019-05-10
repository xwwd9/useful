import win32api
from ctypes import windll

import win32con


def move_cur(x, y):
    windll.user32.SetCursorPos(x, y)


def click_left_cur():
    win32api.mouse_event(
        win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0)


if __name__ == '__main__':
    move_cur(10, 10)
    click_left_cur()

