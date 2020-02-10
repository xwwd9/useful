import json
import re

import requests

from useful_python.examples.spiders.tools import RedisClient

requests.packages.urllib3.disable_warnings()


server = RedisClient()


dup_list = []


def get_cna(proxy=True):
    """
    获取cookie
    """
    url = "https://log.mmstat.com/6.gif?"

    headers = {
        "Host": "log.mmstat.com",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "no-cors",
        "Referer": "https://www.1688.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh,zh-CN;q=0.9,ru;q=0.8,en;q=0.7,en-US;q=0.6"
    }



    # 获取代理
    if proxy:
        proxy = server.get_one()
        proxy = json.loads(proxy)
        proxy = proxy.get('proxy')
        proxies = {
            'http': "http://"+proxy,
            'https': "http://"+proxy
        }
    else:
        proxies = {}

    # if proxy.split(':')[0] in dup_list:
    #     print("代理重复*********")
    dup_list.append(proxy.split(':')[0])


    # 请求网址，并获取cookie
    ret = requests.get(url, verify=False, allow_redirects=False, headers=headers, proxies=proxies, timeout=2)
    cookies = ret.headers['Set-Cookie']
    cna = re.findall('cna=(.*?);', cookies, re.S)[0]


    return cna



def get_companys_list(cna, proxy=None, search_word="女鞋"):
    "获取搜索页"

    template_url = "https://s.1688.com/company/company_search.htm?keywords={keywords}&netType=1%2C11&button_click=top&n=y&pageSize=30&offset=0&beginPage={page}"

    headers = {
        "Host": "s.1688.com",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Sec-Fetch-User": "?1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "navigate",
        "Referer": "https://www.1688.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh,zh-CN;q=0.9,ru;q=0.8,en;q=0.7,en-US;q=0.6",
        "Cookie": "cna={cna};".format(cna=cna),
    }

    #构造请求url
    keywords = ""
    for i in search_word.encode('gbk'):
        keywords += str(hex(i)).replace("0x", "%")
    url = template_url.format(keywords=keywords, page=1)

    # 获取代理
    proxy = server.get_one()
    proxy = json.loads(proxy)
    proxy = proxy.get('proxy')
    print("当前代理", proxy)
    proxies = {
        'http': "http://"+proxy,
        'https': "http://"+proxy
    }

    if proxy.split(':')[0] in dup_list:
        print("代理重复*********")
    dup_list.append(proxy.split(':')[0])


    # 发送请求
    ret = requests.get(url, headers=headers, verify=False, allow_redirects=False, proxies=proxies, timeout=2)

    if ret.status_code == 302:
        print(ret.text)

    print("返回码%d"%ret.status_code)

    return ret





if __name__ == "__main__":


    while True:
        try:
            # 获取cookie
            cna = get_cna(proxy=True)
            # 请求列表页
            ret = get_companys_list(cna)
            print(ret)
        except  Exception as e:
            print(e)
            continue




