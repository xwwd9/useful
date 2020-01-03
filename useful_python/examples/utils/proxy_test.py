

# 代理测试

import json
import time

import requests
import random


url = 'https://weixin.sogou.com/weixin?type=2&query=%E4%B8%80%E4%B8%AA&ie=utf8&s_from=input&_sug_=y&_sug_type_=&w=01019900&sut=1127&sst0=1578018642107&lkt=1%2C1578018642005%2C1578018642005'

headers = {
    "Host": "weixin.sogou.com",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    "Sec-Fetch-User": "?1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Referer": "https://weixin.sogou.com/antispider/?from=%2fweixin%3Ftype%3d2%26query%3d%E4%B8%80%E4%B8%AA%26ie%3dutf8%26s_from%3dinput%26_sug_%3dy%26_sug_type_%3d%26w%3d01019900%26sut%3d1127%26sst0%3d1578018642107%26lkt%3d1%2C1578018642005%2C1578018642005",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh,zh-CN;q=0.9,ru;q=0.8,en;q=0.7,en-US;q=0.6",

}

proxy_url = 'http://piping.mogumiao.com/proxy/api/get_ip_bs?appKey=be626288027e407eac1da56fa4c60a2f&count=5&expiryDate=0&format=1&newLine=2'

# proxy_url = 'http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=5549661e2f0942879b302a105e3dd7aa&orderno=YZ2020134221822cGv&returnType=2&count=4'


times = 1000


def get_html(ip, port, times):
    # print(times)
    proxies = {
        'http': 'http://' + ip + ":" + port,
        'https': 'http://' + ip + ":" + port,
    }

    try:
        response = requests.get(url, headers=headers, timeout=3,
                                proxies=proxies, allow_redirects=False)
    except Exception as e:
        print(e)
        return 'error'

    # print(response.status_code)
    if response.status_code == 200:
        return 'ok'
    else:
        return 'fail'


success = 0
fail = 0
error = 0

times = 10
curtimes = 0
ss = time.time()
while times > 0:

    proxy_json = requests.get(proxy_url)

    proxys = json.loads(proxy_json.text).get("msg")
    from concurrent.futures import ThreadPoolExecutor, as_completed

    executor = ThreadPoolExecutor(max_workers=20)

    s = time.time()
    times -= 1
    # while True:
    for proxy in proxys:
        print(proxy)
        ip = proxy.get("ip")

        port = proxy.get("port")

        all_task = [executor.submit(get_html, ip, port, curtimes) for i in
                    range(20)]
        curtimes += 20
        print(curtimes)
        for future in as_completed(all_task):
            ret = future.result()
            print(ret)
            if ret == 'ok':
                success += 1
            if ret == 'fail':
                fail += 1
            if ret == 'error':
                error += 1

        e = time.time()

        if e - s > 120:
            break

        print("*****", fail, success, error, times)

    time.sleep(10)


print("失败次数：%d, 成次数：%d, 失败次数：%d， times=%d"%(fail, success, error, times))

ee = time.time()
print(ee-ss, ee, ss)
