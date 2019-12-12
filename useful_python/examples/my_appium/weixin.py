import os
import random
import re
import sqlite3
import time

import requests
from win32crypt import CryptUnprotectData




def get_cookie(host='mp.weixin.qq.com'):
    cookiepath = os.environ[
                     'LOCALAPPDATA'] + r"\Google\Chrome\User Data\Default\Cookies"
    print(cookiepath)
    sql = "select host_key,name,encrypted_value from cookies where host_key='%s'" % host
    with sqlite3.connect(cookiepath) as conn:
        cu = conn.cursor()
        cookies = {name: CryptUnprotectData(encrypted_value)[1].decode() for
                   host_key, name, encrypted_value in
                   cu.execute(sql).fetchall()}
        # print(type(cookies))
        return cookies

cookies = get_cookie()







def get_article( query=''):

    url = 'https://mp.weixin.qq.com'

    # 设置headers
    headers={"HOST":
          "mp.weixin.qq.com",
      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
      }

    # 登录之后的微信公众号首页url变化为：https://mp.weixin.qq.com/cgi-bin/home?t=home/index&lang=zh_CN&token=1849751598，

    # 从这里获取token信息
    # response = requests.get(url = url, cookies=cookies)
    # token = re.findall(r'token=(\d+)', str(response.url))[0]
    # time.sleep(2)
    token = '919771470'

    print('正在查询[ %s ]相关公众号' % query)
    search_url = 'https://mp.weixin.qq.com/cgi-bin/searchbiz?'

    # 搜索微信公众号接口需要传入的参数，


    # 有三个变量：微信公众号token、随机数random、搜索的微信公众号名字


    params = {'action': 'search_biz', 'token': token, 'random': random.random(),
              'query': query, 'lang': 'zh_CN', 'f': 'json', 'ajax': '1',
              'begin': '0', 'count': '5'}

    # 打开搜索微信公众号接口地址，需要传入相关参数信息如：cookies、params、headers
    response = requests.get(search_url, cookies=cookies, headers=headers,
                            params=params)

    time.sleep(2)

    # 取搜索结果中的第一个公众号

    lists = response.json().get('list')[0]

    # 获取这个公众号的fakeid，后面爬取公众号文章需要此字段

    fakeid = lists.get('fakeid')
    nickname = lists.get('nickname')

    # 微信公众号文章接口地址

    search_url = 'https://mp.weixin.qq.com/cgi-bin/appmsg?'

    # 搜索文章需要传入几个参数：登录的公众号token、要爬取文章的公众号fakeid、随机数random


    params = {'action': 'list_ex', 'token': token, 'random': random.random(),
              'fakeid': fakeid, 'lang': 'zh_CN', 'f': 'json', 'ajax': '1',
              'begin': '0', 'count': '5', 'query': '', 'type': '9'}

    # 打开搜索的微信公众号文章列表页


    response = requests.get(search_url, cookies=cookies, headers=headers,
                            params=params)

    # print(search_url)
    time.sleep(2)

    for index, per in enumerate(response.json().get('app_msg_list', [])):
        print('%s-->title ---> %s\n' % (index, per.get('title')))
        print('link ---> %s\n' % per.get('link'))


if __name__ == "__main__":
    print(cookies)
    st = time.time()
    cnt = 0
    while True:
        try:
            querys = ['格力电器','CSDN', '新浪新闻', '深圳']
            for i in querys:
                cnt += 1
                print('当前次数', cnt)
                get_article(i)
        except Exception as e:
            print(e)
            et = time.time()
            print('运行时间', et-st)
            print('查询次数', cnt)
            time.sleep(60*10)
            st = time.time()
            cnt = 0
    pass