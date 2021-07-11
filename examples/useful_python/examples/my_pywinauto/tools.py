import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pywinauto
from airtest.core.api import init_device, touch
from airtest.core.cv import Template
from pywinauto import Application


def init_weixin():


    # app = Application().connect(
    #     path=r"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe")
    #
    # if not app.windows():
    #     app = Application().connect(
    #         path=r"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe")
    #
    #
    #
    # dlg = app.window(title=u"微信", class_name="WeChatMainWndForPC")
    # dlg.move_window(0, 0)
    # dlg.maximize()
    # dlg.set_focus()


    dlgs = []
    rets = pywinauto.findwindows.find_windows(class_name="WeChatMainWndForPC")
    for ret in rets:
        app = Application().connect(handle=ret)
        dlg = app.window(title=u"微信", class_name="WeChatMainWndForPC")
        dlg.move_window(0, 0)
        dlg.maximize()
        dlg.set_focus()
        dlgs.append(dlg)
        time.sleep(1)


    return dlgs




def air_init(uuid):
    init_device(platform='Windows', uuid=uuid)





def mail_sender(text, file_path = None):
    receivers = ["18200159908@139.com"]

    sender = "18200159908@139.com"
    mail_pass = "migu111112@"  # 邮箱的三方授权客户端密码

    mail_subject = "美滋滋"  # 邮件的标题
    mail_context = text  # 邮件正文内容

    # 创建一个带附件的实例
    msg = MIMEMultipart()
    msg["From"] = sender  # 发件人
    msg["To"] = ";".join(receivers)  # 收件人
    msg["Subject"] = mail_subject  # 邮件标题


    # ---------------------------------------附件内容-------------------------------------#
    # 邮件正文
    msg.attach(MIMEText(mail_context, 'plain', 'utf-8'))
    # 构造附件
    if file_path:
        file_name = file_path.split('/')[-1]
        att = MIMEText(open(file_path, "rb").read(), "base64", "utf-8")
        att.add_header('Content-Disposition', 'attachment',
                       filename=("utf-8", "", file_name))

        msg.attach(att)

    try:
        # 启动网易SMTP服务，端口４６５
        smtpObj = smtplib.SMTP_SSL('smtp.139.com', 465)
        # 登陆账号
        smtpObj.login(sender, mail_pass)
        # 发送
        smtpObj.sendmail(sender, msg["To"].split(','), msg.as_string())
        print('邮件发送成功!')
        # 退出登录
        smtpObj.quit()
    except smtplib.SMTPException as e:
        print(e)

