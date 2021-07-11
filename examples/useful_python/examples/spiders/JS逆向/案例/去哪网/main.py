import execjs
import requests
from scrapy import Selector

from examples.useful_python.examples.spiders.JS逆向.案例.去哪网.tools import get_m, random_key

headers = {
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'Connection': 'keep-alive',
    'If-Modified-Since': 'Tue, 19 Feb 2019 06:15:57 GMT',
    'If-None-Match': '"5c6b9f1d-2d12"',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Dest': 'script',
    'Accept-Language': 'zh,zh-CN;q=0.9,ru;q=0.8,en;q=0.7,en-US;q=0.6',
    'Origin': 'https://flight.qunar.com',
}

detail_headers = {
        "csht": "",
        "w": "0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
        "X-Requested-With": "XMLHttpRequest",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://flight.qunar.com/site/oneway_list.htm?searchDepartureAirport=%E5%8C%97%E4%BA%AC&searchArrivalAirport=%E6%98%86%E6%98%8E&searchDepartureTime=2020-05-23&searchArrivalTime=2020-05-26&nextNDays=0&startSearch=true&fromCode=BJS&toCode=KMG&from=qunarindex&lowestPrice=null",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh,zh-CN;q=0.9,ru;q=0.8,en;q=0.7,en-US;q=0.6",
    }

# QN668 = "51%2C55%2C59%2C50%2C50%2C53%2C58%2C57%2C54%2C50%2C52%2C52%2C54"
QN668 = "51,55,59,50,50,54,51,58,59,51,57,58,57"
QN48 = "tc_1a845960527cfe22_1722be10e4f_8417"
cookies = {
        "QN668": "51%2C55%2C59%2C50%2C50%2C55%2C52%2C51%2C57%2C51%2C50%2C52%2C53",
        "QN48": QN48,
        "Alina":"aff7719a-c7f036-7448d655-449ef600-22bc5ec39345",
    }

def get_pre():
    """
    获取pre参数，还需要修改。这样获取出来是不正确的
    :return:
    """
    url_template = "https://flight.qunar.com/site/oneway_list.htm?searchDepartureAirport=%E5%8C%97%E4%BA%AC&searchArrivalAirport=%E6%98%86%E6%98%8E&searchDepartureTime=2020-05-23&searchArrivalTime=2020-05-26&nextNDays=0&startSearch=true&fromCode=BJS&toCode=KMG&from=qunarindex&lowestPrice=null"

    ret = requests.get(url=url_template, verify=False, headers=headers, cookies=cookies)

    html_text = ret.text

    selector = Selector(text=html_text)

    # 获取加密脚本
    script = selector.xpath("//script/text()").extract()[1]

    js_content = r"""
    document = {
    	getElementsByTagName: function(meta){
    		return {

    		}
    	},

    	head:{
    	    getElementsByTagName: function(meta){
    		return {

                }
            }
        }
    };

    window = {
        location:{
            href:"https://flight.qunar.com/touch/api/domestic/wbdflightlist",
            protocol:"http:",
            host:"",
            hash: "",

        },
    };

    location = {};

    function get_pre(){
        %s
        return window._pt_
    }

    """

    ex = execjs.compile(js_content % script)

    pre = ex.call("get_pre")
    return pre


def get_data():
    url_template = "https://flight.qunar.com/touch/api/domestic/wbdflightlist?departureCity=%E5%8C%97%E4%BA%AC&arrivalCity=%E6%B7%B1%E5%9C%B3&departureDate=2020-05-23&ex_track=&__m__={m}&st=1590032443871&sort=&_v=4"

    # detail_headers['pre'] = get_pre()
    detail_headers['pre'] = '0748a91e-d82951-2843d956-488cf063-52fb3e17c7c1'

    # kv = random_key(QN48, QN668)
    # for k, v in kv.items():
    #     detail_headers[k] = v
    # detail_headers['f8427e'] = 'd2f4885e6f699213d73e983a6c0ff3dd'

    m = get_m(QN48, QN668)


    headers = {
        # "d8b728": "5b906ecd8f9b939af204bfec535a96e00b9147ef",
        "csht": "",
        "pre": "2752da3e-f2d256-58411056-43b52533-a8fbc160865d",
        "w": "0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
        "X-Requested-With": "XMLHttpRequest",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://flight.qunar.com/site/oneway_list.htm?searchDepartureAirport=%E5%8C%97%E4%BA%AC&searchArrivalAirport=%E6%98%86%E6%98%8E&searchDepartureTime=2020-05-23&searchArrivalTime=2020-05-26&nextNDays=0&startSearch=true&fromCode=BJS&toCode=KMG&from=qunarindex&lowestPrice=null",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh,zh-CN;q=0.9,ru;q=0.8,en;q=0.7,en-US;q=0.6",
        # "Cookie": "QN48=tc_1a845960527cfe22_1722be10e4f_8417;     Alina=aff7719a-c7f036-7448d655-449ef600-22bc5ec39345; QN668=51%2C55%2C59%2C50%2C50%2C53%2C59%2C51%2C50%2C59%2C50%2C56%2C58; ",
    }

    # headers['pre'] = get_pre()

    ret = requests.get(url="https://flight.qunar.com/touch/api/domestic/wbdflightlist?departureCity=%E5%8C%97%E4%BA%AC&arrivalCity=%E6%98%86%E6%98%8E&departureDate=2020-05-23&ex_track=&__m__=910632a814aefaa95ec38d200bddee75&st=1590041890529&sort=&_v=4", headers=detail_headers, verify=False, cookies=cookies)

    # ret = requests.get(
    #     url="https://flight.qunar.com/touch/api/domestic/wbdflightlist?departureCity=%E5%8C%97%E4%BA%AC&arrivalCity=%E6%98%86%E6%98%8E&departureDate=2020-05-23&ex_track=&__m__=2a69541928cc8f0fa77cf5c362327a17&st=1590041728547&sort=&_v=4",
    #     headers=headers, verify=False,cookies=cookies)
    print(ret.text)


if __name__ == '__main__':
    # get_pre()
    get_data()
