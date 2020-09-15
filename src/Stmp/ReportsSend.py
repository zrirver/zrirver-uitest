#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# @Time : 2020/5/16 16:35
# @Author : zhaohe

import os
from src.Stmp.EmailSender import WriteEmails
from src.env import ROOT_PATH


def mail_send():
    htmlf = open(ROOT_PATH + r'/src/Reports/report.html', 'r', encoding='UTF-8')
    mail_msg = htmlf.read()
    content = mail_msg
    msg_type = 'html'
    attachment = ROOT_PATH + r'/src/Reports/report.html'
    m = WriteEmails(content, msg_type, attachment)
    m.senf_send_email()


if __name__ == '__main__':
    print(ROOT_PATH)
    mail_send()
