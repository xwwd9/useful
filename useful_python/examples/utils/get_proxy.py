import json

import requests


def get_proxy():
    url = "http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=5549661e2f0942879b302a105e3dd7aa&orderno=YZ2020134221822cGv&returnType=2&count=1"

    ret = requests.get(url)

    json_content = json.loads(ret.text)

    ip = json_content.get("RESULT")[0].get("ip")
    port = json_content.get("RESULT")[0].get("port")

    ret = "http://"+ip+":"+port
    return ret


if __name__ == "__main__":
    print(get_proxy())



