import time

from appium import webdriver

des = dict()

des['platformName'] = 'Android'
des['platformVersion'] = '5.1.1'
des['deviceName'] = '127.0.0.1:62001'
des['appPackage'] = 'com.tencent.mm'
des['appActivity'] = '.ui.LauncherUI'
des['noReset'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', des)

time.sleep(25)

els = driver.find_elements_by_id('com.tencent.mm:id/bae')
# el.click()

# el = driver.find_element_by_class_name('_highlighter-box_619e8')

print(els)

for el in els:
    row = el.find_element_by_id('com.tencent.mm:id/bag')
    print(row)
    print(row.get_attribute('text'))
    text = row.get_attribute('text')
    if text == '订阅号消息':
        row.click()
        break







# 有新消息时的id：com.tencent.mm:id/baf
# driver.quit()



# driver.keyevent(66)
# driver.press_keycode(66)
