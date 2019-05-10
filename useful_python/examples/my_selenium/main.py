import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()



# try:
#     browser.get('http://www.baidu.com')
#     input = browser.find_element_by_id('kw')
#     input.send_keys('Python')
#     time.sleep(10)
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser, 10)
#     wait.until(EC.presence_of_all_elements_located((By.ID, 'content_left')))
#     print(browser.current_url)
#     print(browser.get_cookies())
#     print(browser.page_source)
# finally:
#     browser.close()



# browser = webdriver.Chromze()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input.size)


# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
#
#
# try:
#     logo = browser.find_element_by_class_name('logo')
# except Exception as e:
#     print('no')
#
# browser.switch_to.parent_frame()
# logo = browser.find_element_by_class_name('logo')
# print(logo.text)


browser.get('https://www.baidu.com')
browser.execute_script('window.open()')





