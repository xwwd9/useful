import json
import time

import requests

if __name__ == '__main__':
    url = "https://m.flight.qunar.com/flight/api/touchInnerList"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; Nexus 6P Build/OPM7.181205.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36",
        "Content-Type": "application/json",
        "Accept": "application/json, text/javascript",
        "X-Requested-With": "XMLHttpRequest",
        "wps": "6",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8",
    }

    s_time = time.time()*1000

    body = {"arrCity": "上海", "baby": "0", "cabinType": "0", "child": "0", "depCity": "重庆",
            "from": "touch_index_search", "goDate": "2020-05-22", "firstRequest": True,
            "startNum": 0, "sort": 5, "r": s_time, "_v": 2, "underageOption": "",
            "st": s_time
            }

    ret = requests.post(url, data=json.dumps(body), headers=headers, verify=False)
    json_content = json.loads(ret.text)
    # js = json.loads('"'+json_content.get("data"))
    print(json_content.get("data"))



