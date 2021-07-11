import win32clipboard as wc
import win32con
from pywinauto.application import *
from PIL import ImageGrab
import time


def get_screenxy_from_bmp(main_bmp, son_bmp):
    # 获取屏幕上匹配指定截图的坐标->(x,y,width,height)
    from PIL import Image
    img_main = Image.open(main_bmp)
    img_son = Image.open(son_bmp)
    datas_a = list(img_main.getdata())
    datas_b = list(img_son.getdata())
    for i, item in enumerate(datas_a):
        if datas_b[0] == item and datas_a[i + 1] == datas_b[1]:
            yx = divmod(i, img_main.size[0])
            main_start_pos = yx[1] + yx[0] * img_main.size[0]

            match_test = True
            for n in range(img_son.size[1]):
                main_pos = main_start_pos + n * img_main.size[0]
                son_pos = n * img_son.size[0]

                if datas_b[son_pos:son_pos + img_son.size[0]] != datas_a[
                                                                 main_pos:main_pos +
                                                                          img_son.size[
                                                                              0]]:
                    match_test = False
                    break
            if match_test:
                return (yx[1], yx[0], img_son.size[0], img_son.size[1])
    return False


def getCopyText():
    wc.OpenClipboard()
    copy_text = wc.GetClipboardData(win32con.CF_TEXT)
    wc.CloseClipboard()
    return copy_text


oks = []
app = Application().start(r"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe")
if not app.windows():
    app = Application().connect(
        path=r"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe")
app.window(title=u"微信", class_name="WeChatMainWndForPC").move_window(0, 0)
nb = 0
while 1:
    if nb > 140:
        break
    else:
        nb = nb + 1
        app.window(title=u"微信", class_name="WeChatMainWndForPC").TypeKeys(
            "{DOWN}")
        time.sleep(.5)
        pic = ImageGrab.grab((0, 0, 623, 454))
        # pic.save('1.bmp')
        ok = get_screenxy_from_bmp(u'1.bmp', u'weixin.bmp')
        # 选中
        print('dd')
        app.window(title=u"微信",
                    class_name="WeChatMainWndForPC").click(
            coords=(ok[0] + 100, ok[1] + 10))
        # 拷贝
        # app.window(title=u"微信", class_name="WeChatMainWndForPC").TypeKeys("^c")
        # app.window(title=u"微信", class_name="WeChatMainWndForPC").click_input(
        #     coords=(208, 477))
        # weixin = getCopyText()
        # if weixin not in oks:
        #     print(weixin)
        #     oks.append(weixin)
        #     f = open("weixin.txt", "a")
        #     f.write(weixin + "\n")
        #     f.close()
        # else:
        #     print(u"失败一个")
        time.sleep(2)