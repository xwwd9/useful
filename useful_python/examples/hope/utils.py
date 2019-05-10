import os
import sqlite3
from win32crypt import CryptUnprotectData


def get_cookie(host='.taobao.com'):
    cookiepath = os.environ[
                     'LOCALAPPDATA'] + r"\Google\Chrome\User Data\Default\Cookies"
    sql = "select host_key,name,encrypted_value from cookies where host_key='%s'" % host
    with sqlite3.connect(cookiepath) as conn:
        cu = conn.cursor()
        cookies = {name: CryptUnprotectData(encrypted_value)[1].decode() for
                   host_key, name, encrypted_value in
                   cu.execute(sql).fetchall()}
        # print(type(cookies))
        return cookies