import os
import sqlite3
import urllib

from win32crypt import CryptUnprotectData


def get_cookie(host='.taobao.com'):
    cookiepath = os.environ['LOCALAPPDATA'] + r"\Google\Chrome\User Data\Default\Cookies"
    sql = "select host_key,name,encrypted_value from cookies where host_key='%s'" % host
    with sqlite3.connect(cookiepath) as conn:
        cu = conn.cursor()
        cookies = {name: CryptUnprotectData(encrypted_value)[1].decode() for
                   host_key, name, encrypted_value in
                   cu.execute(sql).fetchall()}
        # print(type(cookies))
        return cookies



def url_decoder(text):
    return urllib.parse.unquote(text, encoding='utf-8', errors='replace')


def url_encoder(text):
    return urllib.parse.quote(text, safe='/', encoding=None, errors=None)




def common_header():
     headers = {
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

     return headers