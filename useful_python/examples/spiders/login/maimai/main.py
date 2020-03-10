import time

import requests

from useful_python.examples.spiders.utils.tools import get_cookie



login_headers = {
        'authority': "acc.maimai.cn",
        'cache-control': "max-age=0,no-cache",
        'origin': "https://acc.maimai.cn",
        'upgrade-insecure-requests': "1",
        'content-type': "application/x-www-form-urlencoded",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'referer': "https://acc.maimai.cn/login",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    }


headers = {
        'cache-control': "max-age=0,no-cache",
        'upgrade-insecure-requests': "1",
        'content-type': "application/x-www-form-urlencoded",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    }


def login():
    cookies = get_cookie(host=".maimai.cn")
    cookies_2 = get_cookie(host="maimai.cn")
    ret = {
        **cookies,
        **cookies_2
    }
    return ret


def use_company_search_user(page = 0, query = "成都索贝数码科技股份有限公司"):
    url = "https://maimai.cn/search/contacts?count=20&page={page}&query={query}&dist=0&searchTokens=&highlight=true&jsononly=1&pc=1".format(page = page, query=query)

    ret = requests.get(url=url, headers=headers, verify=False, cookies=login())

    print(ret.json())

    return ret.json()






def user_detail():
    users = use_company_search_user()

    contacts = users.get("data", {}).get("contacts")

    for user in contacts:
        encode_mmid = user.get("contact", {}).get("encode_mmid", "")
        mmid = user.get("contact", "").get("mmid", "")
        user_name = user.get("contact", {}).get("name")

        # 影响力和高管字段
        tag = user.get("contact", {}).get("line4", "")
        high = True if "高管" in tag else False

        # 影响力
        rank = user.get("contact", {}).get("rank")

        # 职位
        position = user.get("contact", {}).get("position")

        # 用户头像
        avatar = user.get("contact", {}).get("avatar")

        # 地区
        loc = user.get("contact", {}).get("loc", "")
        city = user.get("contact", {}).get("city", "")
        area = loc + " " + city if city else loc


        # 会员 等于1表是会员
        judge = True if user.get("contact", {}).get("judge") == 1 else False

        print(user_name, high, position, judge, area, rank, avatar, mmid)





if __name__ == "__main__":

    # login()
    # pass
    # use_company_search_user()

    total_index = 0
    for i in range(10000):
        total_index += 1
        user_detail()
        time.sleep(1)
        print(total_index)



