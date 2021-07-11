import re

import requests
from scrapy import Selector

from examples.useful_python.examples.spiders.字体爬虫.剑鱼标讯.tools import decode_content, get_date, font_map, \
    decode_content_python

headers = {
        'cache-control': "max-age=0,no-cache",
        'upgrade-insecure-requests': "1",
        'content-type': "application/x-www-form-urlencoded",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    }

# 采购人
# url = "https://api.jianyu360.com/open/article/3ABCY2ZSZD04Iyw7JHt4c3U8DzNfASB3V3xxKygnKz0wWlJiYgksORlESArL.html"
# 采购人
# url = "https://api.jianyu360.com/open/article/3ABCY2EFYSkoMDw6GXRhcHUJJzACHj1mZnB%2FKw4oOCEgfFNiYgksLglESAnR.html"
# 采购人和代理机构
# url = "https://api.jianyu360.com/open/article/3ABCY2Zrfz1YLD06And1ZGI8DCc4QTJjR2hxKA4oPSEee3liYgksFy9ESArV.html"
# 代理机构采购人
url = "https://api.jianyu360.com/open/article/3ABCY2EEdT1YJDgvAnt2c2UoDScoGj10XFJ%2BPygvJiEeWlFiYgkvLAlESAoG.html"
# 采购人 代理机构
# url = "https://api.jianyu360.com/open/article/3ABCY2EAcilYGSs6RGRhcHUJJzACHj1mZnB%2FPCgCPzogdFViYgksSj9ESApx.html"
# 采购人 代理机构
# url = "https://api.jianyu360.com/open/article/3ABCY2EEdTIoJyAsJHN2c2UoDScoGj10XFJ%2BKT8zKCEgaFZiYgkvKT9ESAoc.html"
# 地址非常长的情况
# url = "https://api.jianyu360.com/open/article/3ABCY2EAfzIOLyA6RHxhcHUJJzACHj1mZnB%2FKB4zKS5FZGhiYgkvLAlESAoo.html"
# url = "https://api.jianyu360.com/open/article/3ABCY2Zrfi4eBSw6Amt1ZGI8DCc4QTJjR2hxPCgoOS4eXlNiYgkvIAlESAoh.html"
# url = "https://api.jianyu360.com/open/article/3ABCY2ZdcClYOyg7EmRhZAcsCjNfCSBgYUFlKzg3Kj0gc31iYgkvDC9ESAoj.html"
# url = "https://api.jianyu360.com/open/article/3ABCY2ZaYTIoMy86EnxlZ3UzIzIvHjF3ZmNgKD8FLy9FaFRiYgkvNxlESAqS.html"





def request_with_js():
    """
    python运行js进行解密
    """
    global headers
    ret = requests.get(url=url, headers=headers, verify=False)

    selector = Selector(text=ret.text)

    content = selector.xpath("//div[@class='col-xs-12 col-sm-12 com-detail tft']/text()").extract_first()

    content = content.strip()

    # 获取加密key

    headers = {
        **headers,
        "Referer": url,
    }

    body = {
        "c": "",
        "d": get_date(),
    }

    ret = requests.post(url="https://api.jianyu360.com/open/getConSecretKey", data=body, headers=headers,
                        verify=False)
    secretKey = ret.json().get("secretKey")
    print(secretKey)

    # print(content)

    content = decode_content(content, secretKey)

    # 去掉无用标签
    remove_tag = re.compile(r'</?.+?/?>')
    content = remove_tag.sub(" ", content)
    content = content.replace("&nbsp;", "")
    # 将多个空格合并成一个
    space = re.compile(r'\s{2,10}')
    content = space.sub(" ", content)

    # 字体解密
    content_decoder = ""
    for i in content:
        code = ord(i)
        if code in font_map:
            temp = font_map[ord(i)]
            temp = temp.replace("uni", "")
            content_decoder += chr(int(temp, 16))
        else:
            content_decoder += i

    company_key_words = ["采购人名称", "代理机构名称", "采购人", "采购单位", "代理机构", "采购代理机构全称：", ]
    phone_key_words = ['联系方式', '联系电话', '电话', '热线', '联系', '座机', '总线', '总机', '手机', '联系人', '号码', ]
    pattern_1 = re.compile(
        r'(%s).{0,3}[：:\s]{1,4}([\u4e00-\u9fa5]{4,15})[^\u4e00-\u9fa5].{1,35}(%s).{0,3}\D((\d{8,12})|(\d{2,4}-\d{7,8}))[^\d]' % (
        '|'.join(company_key_words), '|'.join(phone_key_words)), re.S)

    pattern_2 = re.compile(
        r'(%s).{0,3}[：:\s]{1,4}([\u4e00-\u9fa5]{4,15})[^\u4e00-\u9fa5].{1,15}地址.*?.{1,20}(%s).{0,3}\D((\d{8,12})|(\d{2,4}-\d{7,8}))[^\d]' % (
        '|'.join(company_key_words), '|'.join(phone_key_words)), re.S)

    seached = pattern_1.findall(content_decoder)
    print(content_decoder)
    print(seached)

    seached = pattern_2.findall(content_decoder)
    print(seached)



def request_with_py():
    """
    python 翻译js的方式运行
    """
    global headers
    ret = requests.get(url=url, headers=headers, verify=False)

    selector = Selector(text=ret.text)

    content = selector.xpath("//div[@class='col-xs-12 col-sm-12 com-detail tft']/text()").extract_first()

    content = content.strip()

    # 获取加密key

    headers = {
        **headers,
        "Referer": url,
    }

    body = {
        "c": "",
        "d": get_date(),
    }

    ret = requests.post(url="https://api.jianyu360.com/open/getConSecretKey", data=body, headers=headers,
                        verify=False)
    secretKey = ret.json().get("secretKey")
    print(secretKey)

    # print(content)

    content = decode_content_python(content, secretKey)

    # 去掉无用标签
    remove_tag = re.compile(r'</?.+?/?>')
    content = remove_tag.sub(" ", content)
    content = content.replace("&nbsp;", "")
    # 将多个空格合并成一个
    space = re.compile(r'\s{2,10}')
    content = space.sub(" ", content)

    # 字体解密
    content_decoder = ""
    for i in content:
        code = ord(i)
        if code in font_map:
            temp = font_map[ord(i)]
            temp = temp.replace("uni", "")
            content_decoder += chr(int(temp, 16))
        else:
            content_decoder += i

    company_key_words = ["采购人名称", "代理机构名称", "采购人", "采购单位", "代理机构", "采购代理机构全称：", ]
    phone_key_words = ['联系方式', '联系电话', '电话', '热线', '联系', '座机', '总线', '总机', '手机', '联系人', '号码', ]
    pattern_1 = re.compile(
        r'(%s).{0,3}[：:\s]{1,4}([\u4e00-\u9fa5]{4,15})[^\u4e00-\u9fa5].{1,35}(%s).{0,3}\D((\d{8,12})|(\d{2,4}-\d{7,8}))[^\d]' % (
        '|'.join(company_key_words), '|'.join(phone_key_words)), re.S)

    pattern_2 = re.compile(
        r'(%s).{0,3}[：:\s]{1,4}([\u4e00-\u9fa5]{4,15})[^\u4e00-\u9fa5].{1,15}地址.*?.{1,20}(%s).{0,3}\D((\d{8,12})|(\d{2,4}-\d{7,8}))[^\d]' % (
        '|'.join(company_key_words), '|'.join(phone_key_words)), re.S)

    seached = pattern_1.findall(content_decoder)
    print(content_decoder)
    print(seached)

    seached = pattern_2.findall(content_decoder)
    print(seached)


if __name__ == '__main__':
    request_with_py()













