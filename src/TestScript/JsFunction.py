

def scroll_by(x, y, driver):
    js = "window.scrollBy({0}, {1})".format(x, y)
    driver.execute_script(js)


def locate_xpath(ele_xpath, driver):
    target = driver.find_elements_by_xpath(ele_xpath)[0]
    driver.execute_script("arguments[0].scrollIntoView();", target)


def click_xpath(ele_xpath, driver):
    target = driver.find_elements_by_xpath(ele_xpath)[0]
    driver.execute_script("arguments[0].click();", target)