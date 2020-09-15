#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/6/16 17:57
# @Author : zhaohe

import os
import platform


BASE_URL = r'https://xxx.xxxxxx.com'
PRO_BASE_URL = r'https://www.xxxxxx.com'
CHROME_PATH = './Driver/DriverFile/chromedriver'

ROOT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
OS = 'macOS'
DEBUG = False  # skip some foo
LOCAL_BROWSER = 'Chrome'  # Chrome or Firefox
MAIL_CONFIG = {
    "server": "smtp.163.com",
    "port": 25,
    "sender": "********@163.com",
    "password": "********",
    "receiver": ["*********@dingtalk.com", "********@dingtalk.com"],
}
DATABASE = {
    "host": "****",
    "port": 3306,
    "user": "root",
    "passwd": "123456",
    "db": "test"
}