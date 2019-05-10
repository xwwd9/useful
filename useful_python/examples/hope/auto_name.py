# encoding=utf-8
import functools
import random
import time
import urllib

import requests

from examples.hope.utils import get_cookie

headers = {
    'Origin': 'https://subway.simba.taobao.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3702.0 Safari/537.36',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh,zh-CN;q=0.9,ru;q=0.8,en;q=0.7,en-US;q=0.6',
}

basic_words = ["2019",
               "春季",
               "新款",
               "小白鞋",
               "百搭",
               "韩版",
               "学生",
               "超火",
               "ins",
               "春季",
               "原宿",
               "平底",
               "板鞋",
               "系带",
               "可爱"
               "简约",
               "休闲",
               "文艺",
               "清新",
               "瘦板",
               "休闲风",
               "个性",
               "街拍",
               "复古",
               "网红",
               "原宿",
               "港风", ]


def get_temp_cookies():
    cs = {}

    cookies = get_cookie('.taobao.com')
    for k, v in cookies.items():
        cs[k] = v

    cookies = get_cookie('subway.simba.taobao.com')
    for k, v in cookies.items():
        cs[k] = v

    return cs


def judeg_word(word):
    ex_words = ['内增高', '厚底', '代购', '增高', '人本', '高帮', '老北京', '匡威',
                '网面', '宝宝','2018'
                '大码',
                '童',
                '男',
                '回力',
                '真皮',
                '单鞋',
                '护士',
                '婴儿',
                ]

    for i in ex_words:
        if i in word:
            return False

    return True


def cmp(x, y):
    f = len(x)
    s = len(y)
    if f > s:
        return -1
    elif f == s:
        return 0
    else:
        return 1


def extract_word(word, word_list):
    for i in word_list:
        # index = i.find(word)
        index = word.find(i)
        if index == -1:
            continue

        # if word[len(i)+1:2] == '白鞋':
        #     time.sleep(1)

        return word[0:index] + word[index + len(i):]

    # word = word.split(' ')
    # for have in word_list:
    #     have = have.split(' ')

    return word


def get_long_word(word, word_list, deep):
    if deep == 5 or len(word_list) > 30:
        return
    url_template = 'https://subway.simba.taobao.com/bidword/tool/adgroup/getSuggestWord.htm?adgroupId=1211608955    &word={word}'
    quot_word = urllib.parse.quote(word)

    cs = get_temp_cookies()

    error_cnt = 0
    while error_cnt < 10:
        try:
            ret = requests.get(url=url_template.format(word=quot_word),
                               cookies=cs,
                               verify=False, headers=headers)
            break
        except Exception as e:
            error_cnt += 1
            time.sleep(5)

    json_content = ret.json()
    # print(ret.json())

    datas = json_content.get('result')

    if datas[0]['flag'] == '0':
        return

    for data in datas:
        new_word = data.get('word')
        if new_word in word_list or data.get('flag') == '0':
            continue

        if judeg_word(new_word):
            # start = new_word.find(word)
            get_long_word(new_word, word_list, deep + 1)
            new_word = extract_word(new_word, word_list)
            if new_word == '':
                continue
            word_list.append(new_word)
            time.sleep(0.5)
            # print(word_list)


def cal_len(text):
    length = len(text)
    utf8_length = len(text.encode('utf-8'))
    length = (utf8_length - length) / 2 + length
    return int(length)


def get_title(a, b):
    # b = ['帆布鞋女学生韩版 原宿 ulzzang', '帆布鞋女学生韩版百搭 学院风', '低帮帆布鞋女韩版ulzzang潮 学生',
    #      '帆布鞋女学生韩版低帮', '手绘帆布鞋女 低帮 韩版 学生', '帆布鞋女学生韩版春秋', '帆布鞋女学生韩版原宿街拍',
    #      '帆布鞋女学生韩版 港风', ' 小白', '帆布鞋女学生韩版', '帆布鞋女学生百搭低帮 春季', '帆布鞋女学生百搭低帮', ' 运动',
    #      '帆布鞋女学生百搭低帮', ' 复古', '帆布鞋女学生百搭春秋', '帆布鞋女百搭学生韩版复古港味', '帆布鞋女学生百搭', ' 复古',
    #      '百搭复古', '帆布鞋女学生百搭', '帆布鞋女学生百搭低帮', ' 运动', '防滑', '防滑', '小脏橘', '黑', '黑',
    #      '帆布鞋女ulzzang', 'ins', '帆布鞋低帮女ulzzang 原宿', '韩版帆布鞋女潮ulzzang',
    #      '帆布鞋女韩版ulzzang 原宿 百搭', 'ins', 'ins 百搭', 'ins 韩版', '帆布鞋女ulzzangins',
    #      'ins', '港味帆布鞋女ulzzang 原宿', '帆布鞋女复古港味 原宿', '帆布鞋女复古港味', ' ulzzang', '网红',
    #      '低帮', '白色', ' 街拍', ' ulzzang 原宿', ' ulzzang', '网红', '网红', '低帮',
    #      '色港味复古帆布鞋女低帮', '低帮', '白色', '白色', ' 街拍', ' 街拍', '帆布鞋女韩版百搭', ' 港风',
    #      '帆布鞋女2018新款韩版百搭 休闲', ' 春季', '帆布鞋女2018新款韩版百搭学生', '帆布小白鞋女 百搭 韩版',
    #      '白色帆布鞋女 韩版 百搭', ' 港风', ' 港风', ' 春季', ' 春季', '白色帆布鞋女 韩版 百搭',
    #      '帆布鞋女2019春季新款 韩版', '帆布鞋女2019春季', ' 休闲 韩版', '帆布鞋女2019春季']
    # a = ['小白鞋女2019春季新款 网红', '小白鞋女2019春季新款 平底 网红', '小白鞋女百搭2019春季新款 网红',
    #      '小白鞋女2019春季新款 超火', '小白鞋女2019春季新款', '韩版春季2019新款系带小白鞋女', '百搭', '帆布鞋',
    #      ' 平底', '透气', '百搭 平底', '小白鞋女2019春季新款', '小白鞋女春季2019新款韩版',
    #      '小白鞋女春季2019新款 休闲', ' 百搭 原宿', '小白鞋女2019春季新款 春款', '运动百搭', '韩版百搭', '百搭',
    #      '帆布鞋', ' 平底', ' 平底 百搭', '皮平底', ' 平底', '2019春季新款皮面小白鞋女', '透气', '百搭 平底',
    #      '小白鞋女2019春季新款', '小白鞋女春季2019新款韩版', '小白鞋女春季2019新款 休闲', ' 百搭 原宿',
    #      '小白鞋女2019春季新款 春款', '运动百搭', '韩版百搭', '百搭', '帆布鞋', ' 平底', ' 平底 百搭', '皮平底',
    #      ' 平底', ' 平底 百搭', '皮平底', ' 平底', '透气', '2019春季新款皮面小白鞋女', '透气',
    #      '2019春季新款皮面小白鞋女', '透气', '小白鞋女', '小白鞋女  平底', '小白鞋女  学生',
    #      '小白鞋女  平底 简约 休闲', '小白鞋女', '小白鞋女韩版ulzzang 原宿 ', '小白鞋女  平底',
    #      '小白鞋女  平底 简约 休闲', '小白鞋女平底 帆布 原宿', '小白鞋女  平底 帆布 学生', '小白鞋女  平底 休闲 透气',
    #      '小白鞋女平底一脚蹬', '小白鞋女  平底 皮面 浅口', '小白鞋女  平底春', '小白鞋女学生韩版平底', '小白鞋女  平底布',
    #      '小白鞋女  平底', '小白鞋女学生2019新款', '小白鞋女学生文艺清新', '小白鞋女学生原宿简约', '小白鞋女学生韩版可爱',
    #      '小白鞋女  学生 休闲 运动', '小白鞋女学生学院风', '小白鞋女  学生 布', '小白鞋女  学生贝壳', '小白鞋女  学生',
    #      '小白鞋女  平底 简约 休闲', '白布鞋女 帆布鞋 小白 ', '小白鞋女', '白布鞋女  小白 一脚蹬',
    #      '帆布小白鞋女  学生 原宿风', '帆布', '小白鞋女2019春款帆布', '鞋子女  学生 小白 休闲',
    #      '小白鞋女  平底 帆布 学生', '小白鞋女', '小白鞋女韩版ulzzang 原宿 ', '小白鞋女  平底 帆布',
    #      '小白鞋女平底 帆布 原宿', '魔术贴小白鞋女平底帆布 ', '小白鞋女  平底 帆布 白色', '小白鞋女  平底 帆布 学生',
    #      '小白鞋女  平底 帆布 休闲', '小白鞋女  平底 帆布', '小白鞋女  平底 简约 休闲', '小白鞋女  平底 帆布 学生']

    a = sorted(a, key=functools.cmp_to_key(cmp))
    b = sorted(b, key=functools.cmp_to_key(cmp))
    for i in range(20):
        first = random.randint(0, 20)
        second = random.randint(0, 20)
        key1 = a[first]
        key2 = b[second]

        temp = key1 + key2

        or_len = len(temp)

        for i in basic_words:
            if temp.count(i) > 1:
                index = temp.rfind(i)
                temp = temp[0:index] + temp[index + len(i):]
                # print(temp, ' ***', i)

        space_cnt = temp.count(' ')
        temp_len = cal_len(temp)
        real_cnt = temp_len - space_cnt

        while real_cnt < 59:
            r = random.randint(0, len(basic_words) - 1)
            # print(r, len(basic_words))
            r = basic_words[r]
            if r not in temp:
                if temp.find(' ') != -1:
                    temp = temp.replace(' ', r, 1)
                else:
                    temp += r

            space_cnt = temp.count(' ')
            temp_len = cal_len(temp)
            real_cnt = temp_len - space_cnt

        print(temp, cal_len(temp), or_len)


if __name__ == '__main__':
    woist = []

    a = []
    b = []
    get_long_word('帆布鞋女', a, deep=1)
    get_long_word('小白鞋女', b, deep=1)

    print(a)
    print(b)
    get_title(a, b)

    print(woist)
