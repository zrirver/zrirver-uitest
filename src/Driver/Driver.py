'''selenium 搭配js方法更加灵活，部分selenium点击失效事件可以使用js方法尝试'''

from selenium import webdriver
import time
from src import env
import platform
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def pc_browser():
    computer_os_info = platform.platform()
    # 服务器搭建的环境使用docker环境部署的远程浏览器，需要优先判断
    if 'Linux' in computer_os_info:
        browser = webdriver.Remote(
            command_executor="http://chrome:4444/wd/hub",
            desired_capabilities=DesiredCapabilities.CHROME)
    elif 'Chrome' in env.LOCAL_BROWSER:
        browser = webdriver.Chrome(env.CHROME_PATH)
    elif 'Firefox' in env.LOCAL_BROWSER:
        browser = webdriver.Firefox()
    else:
        raise Exception('undefined browser,please check your env file')
    browser.implicitly_wait(10)
    browser.maximize_window()
    time.sleep(2)
    return browser


def mobile_driver():
    computer_os_info = platform.platform()
    driver_path = env.CHROME_PATH
    mobile_emulation = {"deviceName": "iPhone 6/7/8"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    chrome_options.add_argument("lang=en.UTF-8")
    chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument("--auto-open-devtools-for-tabs")
    # chrome_options.add_argument("--devtools-flags=Console")
    # chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])

    if 'Linux' in computer_os_info:
        driver = webdriver.Remote(
            command_executor="http://chrome:4444/wd/hub",
            desired_capabilities=chrome_options.to_capabilities())
    else:
        driver = webdriver.Chrome(driver_path, chrome_options=chrome_options)
    driver.implicitly_wait(10)
    time.sleep(2)
    return driver
