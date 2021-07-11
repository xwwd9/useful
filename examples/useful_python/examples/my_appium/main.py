import logging
import time
import traceback

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

logger = logging.getLogger(__name__)

# def swipeDown(driver, t=500, n=1):
#     '''向下滑动屏幕'''
#     l = driver.get_window_size()
#     x1 = l['width'] * 0.5  # x坐标
#     y1 = l['height'] * 0.25  # 起始y坐标
#     y2 = l['height'] * 0.75  # 终点y坐标
#     for i in range(n):
#         driver.swipe(x1, y1, x1, y2,t)


swip_down_times = 0


def swipe_up(driver, t=1500, n=1):
    s = driver.get_window_size()
    x1 = s['width'] * 0.5  # x坐标
    y1 = s['height'] * 0.85  # 起点y坐标
    y2 = s['height'] * 0.15  # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)


if __name__ == "__main__":

    stop_flag = False
    # 用于失败重爬数据，直接跳过已经爬过的个数
    miss_cnt = 0
    driver = None
    while not stop_flag:
        crawl_cnt = 0
        try:
            SLEET_TIME = 60

            des = dict()

            des['platformName'] = 'Android'
            des['platformVersion'] = '5'
            des['deviceName'] = '127.0.0.1:62001'
            des['appPackage'] = 'com.tencent.mm'
            des['appActivity'] = '.ui.LauncherUI'
            des['noReset'] = True
            des['adbExecTimeout'] = 60000 * 2
            des['uiautomator2ServerLaunchTimeout'] = 60000 * 2
            des['uiautomator2ServerInstallTimeout'] = 60000 * 2
            des['chromeOptions'] = {
                'androidProcess': 'com.tencent.mm:tools'
            }

            driver = webdriver.Remote('http://localhost:4723/wd/hub', des)

            # time.sleep(25)

            WebDriverWait(driver, SLEET_TIME, 2).until(
                lambda dv: dv.find_element_by_id('com.tencent.mm:id/b5m'))

            WebDriverWait(driver, SLEET_TIME, 2).until(
                lambda dv: dv.find_element_by_id('com.tencent.mm:id/b5m'))

            subscription_flag = False
            err_cnt = 0

            while not subscription_flag and err_cnt < 3:
                els = driver.find_elements_by_id('com.tencent.mm:id/bae')
                print(els)
                for el in els:
                    row = el.find_element_by_id('com.tencent.mm:id/bag')
                    print(row)
                    print(row.get_attribute('text'))
                    text = row.get_attribute('text')
                    if text == '订阅号消息':
                        subscription_flag = True
                        row.click()
                        break
                logger.error("查找订阅号消息框")
                driver.implicitly_wait(10)
                time.sleep(3)
                err_cnt += 1

            if not subscription_flag:
                logger.error("未找到订阅号消息框")

            err_cnt = 0

            # driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')

            WebDriverWait(driver, SLEET_TIME, 2).until(
                lambda dv: dv.find_element_by_id('com.tencent.mm:id/a_l'))

            # 下滑爬取过的内容

            # for i in range(swip_down_times):
            #     swipe_up(driver)

            # di点击更多文章

            # 先点击更多元素，然后获取当前页面有的信息，然后下滑

            while not stop_flag:
                mores = driver.find_elements_by_id('com.tencent.mm:id/a_u')
                for more in mores:
                    more.click()

                # 获取一个个微信号的box，遍历box中的element
                # WebDriverWait(driver, SLEET_TIME, 2).until(
                #     lambda dv: dv.find_element_by_id('com.tencent.mm:id/a_v'))

                # driver.implicitly_wait(3)
                WebDriverWait(driver, SLEET_TIME, 2).until(
                    lambda dv: dv.find_element_by_id('com.tencent.mm:id/a_y'))

                contents = driver.find_elements_by_id('com.tencent.mm:id/a_y')
                for content in contents:

                    WebDriverWait(driver, SLEET_TIME, 2).until(
                        lambda dv: dv.find_element_by_id(
                            'com.tencent.mm:id/a_y'))

                    print("点击文章, 当前爬取个数：%d,总个数：%d" % (crawl_cnt, miss_cnt))

                    if crawl_cnt >= miss_cnt:

                        content.click()
                        # driver.find_element_by_accessibility_id()
                        # 等待加载页面
                        try:
                            WebDriverWait(driver, SLEET_TIME, 2).until(
                                lambda dv: dv.find_element_by_accessibility_id(
                                    '更多'))
                        except Exception as e:
                            logger.error(e)

                        tp = driver.find_element_by_accessibility_id('更多')
                        tp.click()

                        WebDriverWait(driver, SLEET_TIME, 2).until(
                            lambda dv: dv.find_elements_by_id(
                                'com.tencent.mm:id/dc'))
                        time.sleep(2)
                        tps = driver.find_elements_by_id('com.tencent.mm:id/dc')
                        # 需要判断是否有悬浮
                        for tp in tps:
                            text = tp.get_attribute('text')
                            if text == '刷新':
                                tp.click()
                                break
                            if text == '悬浮':
                                driver.press_keycode(4)
                                break
                        time.sleep(10)

                        driver.implicitly_wait(1)

                        time.sleep(30)

                        WebDriverWait(driver, SLEET_TIME, 2).until(
                            lambda dv: dv.find_element_by_accessibility_id(
                                '返回'))

                        tp = driver.find_element_by_accessibility_id('返回')
                        tp.click()
                        # 确定爬取完一条
                        miss_cnt += 1
                        crawl_cnt += 1
                    else:
                        crawl_cnt += 1

                WebDriverWait(driver, SLEET_TIME, 2).until(
                    lambda dv: dv.find_element_by_id('com.tencent.mm:id/a_y'))

                swipe_up(driver)
                swip_down_times += 1

                driver.implicitly_wait(3)
                time.sleep(1)

                try:
                    els = driver.find_elements_by_id('com.tencent.mm:id/mg')
                    for el in els:
                        text = el.get_attribute('text')
                        if text == '昨天':
                            stop_flag = True

                    el = driver.find_element_by_id('com.tencent.mm:id/a_5')
                    text = el.get_attribute('text')
                    if text == '已无更多消息':
                        stop_flag = True
                except Exception as e:
                    logger.error(e)
                    msg = traceback.format_exc()
                    logger.error(msg)
                    traceback.print_exc()

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
