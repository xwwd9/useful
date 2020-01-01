

"""
爬取搜狗微信爬虫：
1. 需要先分别通过3个url获得对应的cookie
2. 需要构造&k=**&h=** 参数
3. 直接访问列表页的url是一个重定向，需要构造cookie和k，h参数，访问，的到如图sogo_wechat.png所示的结果，需要先访问第一个url，然后再访问第二个url，不然需要验证

参考：https://www.cnblogs.com/hyonline/p/11812977.html
"""



import re
import time
import random
from urllib import parse

import requests
from scrapy import Selector

from useful_python.examples.spiders.test import get_proxy


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",

}

cookie_params = {}


def get_cookies():
    global cookie_params
    # 获取3个cookie
    url = "https://weixin.sogou.com/"

    ret = requests.get(url, headers=headers, verify=False)

    cookies = ret.headers['Set-Cookie']
    cookie_params = {
        **cookie_params,
        "ABTEST": re.findall('ABTEST=(.*?);', cookies, re.S)[0],
        # "SNUID": re.findall('SNUID=(.*?);', cookies, re.S)[0],
        "IPLOC": re.findall('IPLOC=(.*?);', cookies, re.S)[0],
        "SUID": re.findall('SUID=(.*?);', cookies, re.S)[0],
    }

    # print(cookies)

    # 获取suv cookie
    url = "https://pb.sogou.com/pv.gif"
    temp_headers = {
        **headers,
        "Cookie": "SNUID={}; IPLOC={}; SUID={}".format(cookie_params['SNUID'],
                                                       cookie_params['IPLOC'],
                                                       cookie_params['SUID']),
    }

    ret = requests.get(url, headers=headers, verify=False)

    cookies = ret.headers['Set-Cookie']
    cookie_params['SUV'] = re.findall('SUV=(.*?);', cookies, re.S)[0]
    # cookie_params['SNUID'] = re.findall('SNUID=(.*?);', cookies, re.S)[0]

    # print(cookies)

    # 获取jsessionid cookie

    url = "https://weixin.sogou.com/websearch/wexinurlenc_sogou_profile.jsp"
    temp_headers = {
        **headers,
        "Cookie": "ABTEST={}; IPLOC={}; SUID={}".format(
            cookie_params['ABTEST'],
            cookie_params['IPLOC'],
            cookie_params['SUID']),
    }
    response3 = requests.get(url, headers=headers, verify=False)
    cookies = response3.headers['Set-Cookie']
    cookie_params['JSESSIONID'] = \
        re.findall('JSESSIONID=(.*?);', cookies, re.S)[0]

    # print(cookie_params)

def get_k_h(url):
    b = int(random.random() * 100) + 1
    a = url.find("url=")
    url = url + "&k=" + str(b) + "&h=" + url[a + 4 + 21 + b: a + 4 + 21 + b + 1]
    return url



def get_info(url):
    times = 0

    while True:
        if times>200:
            break
        times += 1

        proxies = {
            'http': get_proxy(),
            'https': get_proxy()
        }

        try:
            ret = requests.get(url=url, headers=headers, verify=False, allow_redirects=False, proxies=proxies)
        except Exception as e:
            print(e)
            continue

        if ret.status_code == 200:
            print(ret.text)
            break
        # print(ret.text)



def send_link_with_proxy(url, cookie_params, prox):
    temp_headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Referer": "https://weixin.sogou.com/weixin",
        "Cookie": "ABTEST={}; SNUID={}; IPLOC={}; SUID={};".format(
            cookie_params['ABTEST'], cookie_params['SNUID'],
            cookie_params['IPLOC'], cookie_params['SUID'])
    }

    url = get_k_h(url)

    proxies = prox
    while True:

        try:
            ret = requests.get(proxies=proxies, url="https://weixin.sogou.com"+url,
                                     headers=temp_headers, verify=False,
                                     allow_redirects=False, timeout=2)
        except Exception as e:
            print(e)
            proxies = {
                'http': get_proxy(),
                'https': get_proxy()
            }
            continue

        proxies = {
            'http': get_proxy(),
            'https': get_proxy()
        }
        print(ret.status_code, ret.text)
        if ret.status_code == 200:
            fragments = re.findall("url \+= '(.*?)'", ret.text, re.S)
            itemurl = ''
            for i in fragments:
                itemurl += i
                print(itemurl)
                # get_info(itemurl)
                # ret = requests.get(itemurl, headers=headers, verify=False)

            get_info(itemurl)
            break



def send_list_with_proxy(url):
    times = 0

    ret_urls = []
    while True:
        if times>200:
            break
        proxies = {
            'http': get_proxy(),
            'https': get_proxy()
        }

        try:
            ret = requests.get(url, verify=False, allow_redirects=False,
                               headers=headers, proxies=proxies, timeout=5)
        except Exception as e:
            print(e)
            print(times)
            times += 1
            continue

        if ret.status_code == 200:

            ret_xpath = Selector(text=ret.text)

            boxs = ret_xpath.xpath('//div[@class="txt-box"]')

            cookies = requests.utils.dict_from_cookiejar(ret.cookies)


            for box in boxs:

                url = box.xpath("./h3/a/@href").extract_first()

                # 发布时间
                pub_time = box.xpath(".//div[@class='s-p']/@t").extract_first()

                # 发布人
                pub_name = box.xpath(".//div[@class='s-p']/a/text()").extract_first()
                # 标题
                title = box.xpath("string(./h3/a)").extract_first()

                ret_urls.append(url)

            return ret_urls, cookies, proxies
            # yield url

    return ret_urls, {}, proxies









if __name__ == "__main__":

    texts = ['格力电器', '新东方', 'a', "w", "asdf"]
    for text in texts:
        url = 'https://weixin.sogou.com/weixin?type=2&s_from=input&query={}&_sug_=n&_sug_type_=&page=2'.format(
            parse.quote(text))

        urls, cookie, proxy = send_list_with_proxy(url)
        for item_url in urls:
            send_link_with_proxy(item_url, cookie, proxy,)



