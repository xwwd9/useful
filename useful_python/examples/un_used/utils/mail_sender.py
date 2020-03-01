# -*- coding: UTF-8 -*-

"""
发送带附件的邮件
"""
import argparse
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



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



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="邮件名字")
    a = parser.parse_args()

    mail_sender(a.file)
