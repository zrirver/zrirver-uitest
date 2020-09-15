#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/9/8下午10:35
# @Author : zhaohe
from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from src.TestScript.Pages.demo import BasePage
from src.Driver.Driver import pc_browser
app = FlaskAPI(__name__)


@app.route("/test", methods=['GET'])
def url_test():
    if request.method == 'GET':
        try:
           BasePage.get_url(driver=pc_browser())
        except Exception as e:
            return e, status.HTTP_500_INTERNAL_SERVER_ERROR
        return status.HTTP_201_CREATED
    else:
        return "Error Request Method"


if __name__ == "__main__":
    app.run(debug=True)