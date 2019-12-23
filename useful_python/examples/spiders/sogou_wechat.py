

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


if __name__ == "__main__":

    url = 'https://weixin.sogou.com/weixin?type=2&s_from=input&query={}&_sug_=n&_sug_type_=&page=2'.format(
        parse.quote("格力电器"))

    list_url = url


    ret = requests.get(url, headers=headers, verify=False)

    cookies = ret.headers['Set-Cookie']
    cookie_params['SNUID'] = re.findall('SNUID=(.*?);', cookies, re.S)[0]
    cookie_params['ABTEST'] = re.findall('ABTEST=(.*?);', cookies, re.S)[0]

    get_cookies()
    get_cookies()


    from lxml import etree

    html = etree.HTML(ret.text)
    urls = ['https://weixin.sogou.com' + i for i in
            html.xpath('//div[@class="img-box"]/a/@href')]

    url = urls[0]

    for index, url in enumerate(urls):
        # if index :
        #     continue

        temp_headers = {
            "Host": "weixin.sogou.com",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
            "Sec-Fetch-User":"?1",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Referer": "https://weixin.sogou.com/weixin?type=2&query=%E6%A0%BC%E5%8A%9B%E7%94%B5%E5%99%A8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh,zh-CN;q=0.9,ru;q=0.8,en;q=0.7,en-US;q=0.6",
            "Cookie": "ABTEST={}; SNUID={}; IPLOC={}; SUID={}; JSESSIONID={}; SUV={}; weixinIndexVisited=1; sct=1; PHPSESSID=ii081dbh6596muqc2eu66j9080".format(
                cookie_params['ABTEST'], cookie_params['SNUID'],
                cookie_params['IPLOC'], cookie_params['SUID'],
                cookie_params['JSESSIONID'],
                cookie_params['SUV'])
        }

        url = get_k_h(url)
        response3 = requests.get(url=url, headers=temp_headers, verify=False)

        fragments = re.findall("url \+= '(.*?)'", response3.text, re.S)
        itemurl = ''
        for i in fragments:
            itemurl += i


        print(itemurl + '**************')
        if not itemurl:
            continue

        # 先发送一个许可
        apprve_url = re.findall("src = (.*?);", response3.text, re.S)
        print(apprve_url)

        temp_headers = {
            **headers,
            "Cookie": "ABTEST={}; SNUID={}; IPLOC={}; SUID={}; JSESSIONID={}; SUV={}; weixinIndexVisited=1; sct=1; PHPSESSID=ii081dbh6596muqc2eu66j9080".format(
                cookie_params['ABTEST'], cookie_params['SNUID'],
                cookie_params['IPLOC'], cookie_params['SUID'],
                cookie_params['JSESSIONID'],
                cookie_params['SUV'])
        }

        ret = requests.get(url=eval(apprve_url[0]), headers=temp_headers, verify=False)


        # 文章url拿正文
        # headers4 = {
        #     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        #     "accept-encoding": "gzip, deflate, br",
        #     "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        #     "cache-control": "max-age=0",
        #     "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
        # }
        ret = requests.get(itemurl, headers=headers, verify=False)
        print(itemurl, ret.status_code, index)
        time.sleep(2)



