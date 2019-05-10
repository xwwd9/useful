import json
import os
import re
import sqlite3
import time

import requests

from examples.hope.auto_video import auto_process
from examples.hope.cookies import cookies
from win32crypt import CryptUnprotectData
import requests

headers = {
    'Origin': 'https://sucai.wangpu.taobao.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3702.0 Safari/537.36',
    'Accept': '*/*',
    'Referer': 'https://sucai.wangpu.taobao.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh,zh-CN;q=0.9,ru;q=0.8,en;q=0.7,en-US;q=0.6',
}


# 获取指定目录的id号
def get_folder_id(name):
    return '1119116485793671191'
    # 获取文件夹id
    folder_url = 'https://tadget.taobao.com/redaction/redaction/json.json?cmd=json_dirTree_query&count=true&_input_charset=utf-8'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3702.0 Safari/537.36',
        'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
        'Referer': 'https://sucai.wangpu.taobao.com/',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    ret = requests.get(folder_url, headers=headers, cookies=cs, verify=False)
    json_content = ret.json()
    dirs = json_content['module']['dirs']['children']
    for dir in dirs:
        if '自动上传' == dir['name']:
            return dir['id']


def make_new_folder(name, dir_id='1119116485793671191'):
    # 创建新的文件夹
    global _tb_token_
    new_folder_url = 'https://tadget.taobao.com/redaction/redaction/json.json?cmd=json_add_dir&_input_charset=utf-8&dir_id={_id}&name={name}&_tb_token_={_tb_token_}&callback=reqwest_1550896094821'

    ret = requests.get(
        new_folder_url.format(name=name, _id=dir_id, _tb_token_=_tb_token_),
        verify=False,
        headers=headers, cookies=cs)
    text = ret.text
    cp = re.compile(r'"jsonData":{"id":"(\d+?)"}}')
    # print(text)
    ret = cp.findall(text)[0]
    return ret


def upload_files(full_name, name, folder_id):
    error_cnt = 0

    # 上传文件
    files = {'name': (None, name), 'file': open(full_name, 'rb')}
    upload_url = 'https://stream.taobao.com/api/upload.api?appkey=tu&folderId={folder_id}&watermark=false&autoCompress=false&_input_charset=utf-8'

    while error_cnt < 10:
        try:
            requests.post(upload_url.format(folder_id=folder_id),
                          headers=headers,
                          cookies=cs,
                          verify=False, files=files)
            break
        except Exception as e:
            error_cnt += 1
    print('ok')


def get_cookie(host='.taobao.com'):
    cookiepath = os.environ[
                     'LOCALAPPDATA'] + r"\Google\Chrome\User Data\Default\Cookies"
    sql = "select host_key,name,encrypted_value from cookies where host_key='%s'" % host
    with sqlite3.connect(cookiepath) as conn:
        cu = conn.cursor()
        cookies = {name: CryptUnprotectData(encrypted_value)[1].decode() for
                   host_key, name, encrypted_value in
                   cu.execute(sql).fetchall()}
        print(type(cookies))
        return cookies


def auto_upload(dir_name):
    # 在服务器下新建文件夹
    folder_name = os.path.split(os.path.split(dir_name)[0])[1]
    p_id = make_new_folder(folder_name)

    # 该目录下的文件夹全部上传到服务器
    dirs = os.listdir(dir_name)
    for dr in dirs:
        # print(dr)
        if os.path.isfile(dir_name + os.sep + dr):
            continue

        _id = make_new_folder(dr, p_id)

        ok_path = dir_name + os.sep + dr + os.sep + 'ok'

        while not os.path.exists(ok_path):
            print('%s  当前ps处理未完成' % dr)
            time.sleep(2)

        file_path = dir_name + os.sep + dr + os.sep + 'web'
        files = os.listdir(file_path)
        for file in files:
            cp = re.compile(r'(\d+?.jpg)')
            file_no = cp.findall(file)
            if len(file_no) == 0:
                continue
            else:
                file_no = file_no[0]
            os.rename(os.path.join(file_path, file),
                      os.path.join(file_path, file_no))

            upload_files(file_path + os.sep + file_no, file, _id)
            print(file)


def traverse_dir(path, music=r'C:\Users\pugui\Desktop\鞋\music'):
    dir_list = os.listdir(path)

    # 提交图片
    for dr in dir_list:
        path = os.path.join(path, dr)
        if os.path.isdir(path):
            auto_upload(path)
    # 处理视频
    for dr in dir_list:
        path = os.path.join(path, dr)
        if os.path.isdir(path):
            auto_process(path, music)



_tb_token_ = ''
cs = {}


cookies = get_cookie('.taobao.com')
for k, v in cookies.items():
    cs[k] = v
    if k == '_tb_token_':
        _tb_token_ = v

print(cs)

if __name__ == '__main__':
    # pass
    # print(get_folder_id('自动上传'))
    # make_new_folder('333')

    # getcookiefromchrome()

    auto_upload(r'C:\Users\pugui\Desktop\鞋\new')
    # auto_upload('C:\\Users\\pugui\\Desktop\\鞋\\F361\\F361 帆布小白鞋')
