





import base64
import re
import time
from functools import cmp_to_key
from urllib.parse import quote


def g(t,n="00000008d78d46a"):
    t = [i for i in t]
    a = len(t)
    e = len(n)
    i = 0
    while i<a:
        t[i] = chr(ord(t[i])^ord(n[(i+10)%e]))
        i += 1

    ret = "".join(t)
    print(ret)
    return ret


def s(a):
    b = a.group()[1:]
    return chr(int('0x'+b, 16))
    # return 'a'

def encode(n):
    """
    对应页面上的 _(n) 函数
    """
    # print(n)
    n = quote(n)
    print(n)
    pattern = re.compile(r'%([0-9A-F]{2})')
    ret = pattern.sub(lambda a:s(a), n)

    print(ret, len(ret), len(ret.encode()))

    n = []
    for i in ret:
        n.append(ord(i))

    b = bytearray(n)
    print(b)
    ret = base64.b64encode(b)
    # ret = base64.encodestring(ret)
    print(ret)
    return ret.decode()


def sort_str_int(x, y):
    if type(x) == type(y):
        return x>y
    elif type(x) == int:
        return -1
    else:
        return 1


def base_encoder(api_type, page = 1, appid = "", words = "", market = ""):
    if api_type == 1:
        # 表面是遍历接口
        i = [page, market, words]
        i.sort(key=cmp_to_key(sort_str_int))
        temp = ""
        for k in i:
            temp += str(k)
        i = temp
        base_url = "/search/android"
    elif api_type == 2:
        # 详情页接口
        i = [market, appid]
        i.sort(key=cmp_to_key(sort_str_int))
        temp = ""
        for k in i:
            temp += str(k)
        i = temp
        base_url = "/andapp/appinfo"
    elif api_type == 3:
        i = ""
        base_url = "/andapp/samePubApp"
    elif api_type == 4:
        # 市场信息 和url
        i = [appid]
        i.sort(key=cmp_to_key(sort_str_int))
        temp = ""
        for k in i:
            temp += str(k)
        i = temp
        base_url = "/andapp/shelves"

    x = "@#"
    i = encode(i)
    i += x + base_url
    i += x + str(int(time.time() * 1000 - 1515125653845))
    i += x + '1'
    print(i)
    r = encode(g(i))
    print(r)
    return r


def get_urls(api_type, appid = "", words = "", market = ""):


    # 遍历接口
    if api_type == 1:
        analysis = base_encoder(api_type, page = 1, words = words, market = market)
        analysis = quote(analysis)
        words = quote(words)
        url_template = "https://api.qimai.cn/search/android?analysis={analysis}&page=1&search={words}&market={market}"
        ret = url_template.format(analysis=analysis, market=market, words=words)
        print(ret)
        return ret
    elif api_type == 2:
        analysis = base_encoder(api_type, appid=appid, market=market)
        analysis = quote(analysis)
        url_template = "https://api.qimai.cn/andapp/appinfo?analysis={analysis}&market=100&appid={appid}"
        ret = url_template.format(analysis=analysis, appid=appid)
        print(ret)
        return ret
    elif api_type == 3:
        # 为post请求data为appid=61
        analysis = base_encoder(api_type)
        analysis = quote(analysis)
        url_template = "https://api.qimai.cn/andapp/samePubApp?analysis={analysis}"
        ret = url_template.format(analysis=analysis, appid=appid)
        print(ret)
        return ret
    elif api_type == 4:
        analysis = base_encoder(api_type, appid=appid)
        analysis = quote(analysis)
        url_template = "https://api.qimai.cn/andapp/shelves?analysis={analysis}&appid={appid}"
        ret = url_template.format(analysis=analysis, appid=appid)
        print(ret)
        return ret





    # return url_template.format(analysis=analysis, market=market, words=words)
    # 详情接口




if __name__ == '__main__':
    # get_urls(1, "4", "王者荣耀")
    # get_urls(2, appid="61", market="100")
    # get_urls(3, appid="61")
    get_urls(4, appid="61")






