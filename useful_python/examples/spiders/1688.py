import re
import time
import traceback

import requests
from scrapy import Selector

from useful_python.examples.utils.get_proxy import get_proxy


def get_cna(proxy=False):
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



    if proxy:
        proxy = get_proxy()
        proxies = {
            'http': proxy,
            'https': proxy
        }
    else:
        proxies = {}

    ret = requests.get(url, verify=False, allow_redirects=False, headers=headers, proxies=proxies, timeout=10)

    cookies = ret.headers['Set-Cookie']

    cna = re.findall('cna=(.*?);', cookies, re.S)[0]




    return cna, proxy





def get_companys_list(cna, proxy=None, search_word="女鞋"):

    # url = "https://s.1688.com/company/company_search.htm?keywords={keywords}&n=y&netType=1%2C11&encode=utf-8&spm=a260k.dacugeneral.search.0"

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

    keywords = ""
    for i in search_word.encode('gbk'):
        keywords += str(hex(i)).replace("0x", "%")

    url = template_url.format(keywords=keywords, page=1)

    if proxy:
        proxies = {
            'http': proxy,
            'https': proxy
        }
    else:
        proxies = {}

    ret = requests.get(url, headers=headers, verify=False, allow_redirects=False, proxies=proxies, timeout=10)

    print("返回码%d"%ret.status_code)
    selector = Selector(text = ret.text)

    page_selector = selector.xpath("//span[@class='total-page']/text()")

    total_page = page_selector.re("(\d+.*?)")

    if len(total_page)>0:
        total_page = total_page[0]
    else:
        assert "当前提取不到页数"

    print(total_page)
    for i in range(2,int(total_page)):
        try:
            print("当前遍历页数%d"%i)
            url = template_url.format(keywords=keywords, page=i)
            ret = requests.get(url, headers=headers, verify=False,
                               allow_redirects=False, proxies=proxies, timeout=10)
            if ret.status_code == 200:
                companys_selector = Selector(text=ret.text)
                companys = companys_selector.xpath("//a[@class='list-item-title-text']/@title").extract()
                print(companys)
            else:
                print("返回为302,重新申请cna和proxy")
                cna, proxy = get_cna(proxy=True)
                proxies = {
                                'http': proxy,
                                'https': proxy
                            }
                headers['Cookie'] = "cna={cna};".format(cna=cna)

        except Exception as e:
            print(traceback.format_exc())
            time.sleep(15)

            cna, proxy = get_cna(proxy=True)
            proxies = {
                'http': proxy,
                'https': proxy
            }
            headers['Cookie'] = "cna={cna};".format(cna=cna)
            continue



    print(ret)





if __name__ == "__main__":


    while True:
        try:
            cns, proxy = get_cna(proxy=True)
            get_companys_list(cns, proxy=proxy)
            break
        except  Exception as e:
            print(traceback.format_exc())
            time.sleep(10)
            continue




