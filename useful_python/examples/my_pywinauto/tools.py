from airtest.core.api import init_device, touch
from airtest.core.cv import Template
from pywinauto import Application


def init_weixin():
    app = Application().start(
        r"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe")
    if not app.windows():
        app = Application().connect(
            path=r"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe")
    dlg = app.window(title=u"微信", class_name="WeChatMainWndForPC")
    dlg.move_window(0, 0)
    # ie_dlg = app.window(title=u"微信", class_name="CefWebViewWnd")
    # ie_dlg.move_window(0, 0)
    # ie_dlg.set_focus()
    dlg.maximize()
    dlg.set_focus()
    # print(ie_dlg.print_control_identifiers())
    return dlg




def air_init(uuid):
    init_device(platform='Windows', uuid=uuid)







