# __author__ ='wuwa'
# -*- coding: utf-8 -*-

"""
email：构造邮件
1.发送邮件的账号、密码
2.连接邮件服务
3.设置邮件标题、内容
smtplib：发送邮件
4.发送邮件
"""

import sys
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os
from src import env


class WriteEmails:
    def __init__(self, content, msg_type, attachment):
        self.smtp_server = env.MAIL_CONFIG["server"]
        self.stmp_port = env.MAIL_CONFIG["port"]
        self.sender = env.MAIL_CONFIG["sender"]
        self.password = env.MAIL_CONFIG["password"]
        self.reveiver = env.MAIL_CONFIG["receiver"]
        self.subject = 'web test report'
        self.content = content
        self.msg_type = msg_type
        self.attachment = attachment

    def __content_of_email(self, msg_type):
        """
        邮件正文为文本内容
        :param content:
        :return:
        """
        msg = MIMEMultipart()
        msg["From"] = self.sender
        msg["To"] = ";".join(self.reveiver)
        msg['Subject'] = Header(self.subject, "utf-8")

        # 如果msg为plain,则邮件正文为文本
        if msg_type == 'plain':
            msg.attach(MIMEText(self.content, "plain", "utf-8"))
        # 如果msg为html,则邮件正文为html
        elif msg_type == "html":
            msg.attach(MIMEText(self.content, "html", "utf-8"))
        else:
            print("邮件内容类型不正确")

        if self.attachment is not None:

            # 读取附件内容
            with open(self.attachment, 'r', encoding='UTF-8')as f:
                contents = f.read()
            # 设置html格式参数
            html_content = MIMEText(contents, 'base64', 'utf-8')
            html_content["Content-Type"] = 'application/octet-stream'
            html_content.add_header("Content-Disposition", "attachment", filename=os.path.basename(self.attachment))
            msg.attach(html_content)
            # with open(self.attachment, 'rb') as fp:
            #     img_data = fp.read()
            # image = MIMEImage(img_data, _subtype='octet-stream')
            # image.add_header('Content-Disposition', 'attachment', filename='paypal-check.png')
            # msg.attach(image)

        return msg

    def senf_send_email(self):
        """
        发邮件
        :return: 
        """
        msg = self.__content_of_email(self.msg_type)

        try:
            # 构建smtp对象
            smtp = smtplib.SMTP()

            # 连接到smtp服务
            smtp.connect(self.smtp_server, self.stmp_port)

            # 登录smtp服务
            smtp.login(self.sender, self.password)

            # 发送邮件
            print('receiver: ', self.reveiver)
            res = smtp.sendmail(self.sender, self.reveiver, msg.as_string())
            print("send result: ", res)

            # 退出
            smtp.quit()
            print("send email finish")

        except smtplib.SMTPException as e:
            print('error', e)
