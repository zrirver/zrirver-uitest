#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/9/15下午11:49
# @Author : zhaohe

from src import env
from selenium.webdriver.support.wait import WebDriverWait
from src.Driver.Driver import pc_browser


class BasePage:
	url_path = '/'
	title = '测试小站 | 学习小技巧，成就大智慧'
	navigation = ''
	reply_input = ''
	xpaths = {
		"input_search": "//input[@id='q']",
		"button_search": "//input[@id='searchsubmit']"
	}

	@classmethod
	def get_url(cls, driver):
		if cls.url_path not in driver.current_url:
			driver.get(env.BASE_URL+cls.url_path)
		WebDriverWait(driver, 20, 0.5).until(
			lambda x: x.find_element_by_xpath(cls.xpaths['input_search']).is_displayed(),
			'not found search input'
		)
		assert cls.title == driver.title


if __name__ == '__main__':
	driver = pc_browser()
	BasePage.get_url(driver)
	driver.quit()
