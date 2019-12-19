import logging
import os
import time
import traceback

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

logger = logging.getLogger(__name__)


# 等待时间
SLEET_TIME = 60
# 搜索按钮ID
SEARCH_ID = '搜索'
# 公众号ID
SEARCH_PUBLIC = 'com.tencent.mm:id/bqc'
# 输入的ID
INPUT = 'com.tencent.mm:id/ji'
# 关注微信号页面
ATTENTION = '//*[@text="关注公众号"]'


if __name__ == "__main__":

    stop_flag = False
    # 用于失败重爬数据，直接跳过已经爬过的个数
    miss_cnt = 0
    driver = None

    names = ['greejs', 'greesc']

    while not stop_flag:
        crawl_cnt = 0
        try:


            des = dict()

            des['platformName'] = 'Android'
            des['platformVersion'] = '6'
            des['deviceName'] = '127.0.0.1:62001'
            des['appPackage'] = 'com.tencent.mm'
            des['appActivity'] = '.ui.LauncherUI'
            des['noReset'] = True
            des['adbExecTimeout'] = 60000 * 2
            des['uiautomator2ServerLaunchTimeout'] = 60000 * 2
            des['uiautomator2ServerInstallTimeout'] = 60000 * 2
            des['skipServerInstallation'] = True
            des['skipDeviceInitialization'] = True

            # des['chromeOptions'] = {
            #     'androidProcess': 'com.tencent.mm:tools'
            # }

            driver = webdriver.Remote('http://localhost:4723/wd/hub', des)

            # 点击搜索
            WebDriverWait(driver, SLEET_TIME, 2).until(
                lambda dv: dv.find_element_by_accessibility_id(SEARCH_ID))

            search = driver.find_element_by_accessibility_id(SEARCH_ID)

            search.click()

            # 点击公众号
            WebDriverWait(driver, SLEET_TIME, 2).until(
                lambda dv: dv.find_element_by_id(SEARCH_PUBLIC))

            public = driver.find_element_by_id(SEARCH_PUBLIC)

            public.click()

            for name in names:
                # 发送公众号
                WebDriverWait(driver, SLEET_TIME, 2).until(
                    lambda dv: dv.find_element_by_id(INPUT))

                input_text = driver.find_element_by_id(INPUT)


                input_text.clear()
                input_text.click()
                input_text.send_keys(name)

                driver.keyevent(66)
                time.sleep(5)

                driver.tap([(130, 480)])
                #
                # os.system("adb shell input tap 130 480")
                #
                #
                # print("22")
                # time.sleep(10)
                #
                # # 关注公众号
                # WebDriverWait(driver, SLEET_TIME, 2).until(
                #     lambda dv: dv.find_element_by_xpath(ATTENTION))
                # attention = driver.find_element_by_xpath(ATTENTION)
                # attention.click()
                #
                #
                # driver.back()

                driver.back()

                # time.sleep(10)
            






        except Exception as e:
            logger.error(e)
            msg = traceback.format_exc()
            logger.error(msg)
            traceback.print_exc()

            # driver.quit()

        # 有新消息时的id：com.tencent.mm:id/baf
# driver.quit()


# driver.keyevent(66)
# driver.press_keycode(66)
