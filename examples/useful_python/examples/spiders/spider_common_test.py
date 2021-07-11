import requests


def req():
    url = "https://m.zhaopin.com/company/CZ259897210.htm"

    headers = {
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 6.0.1; OPPO R9s Build/MMB29M)",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
        }

    cookies = {
    "acw_tc":"2760820615832333770751600e459fcf2bed193b73a7b22e00191ad8aea2cf",
	"FSSBBIl1UgzbN7N443S":"OLGRgaQ0qLMOD77NhIPFMBn8F20Rv1CAWnOuxuZ5P_5VhxoNTHMckRhwN.kqPhmF",
	"FSSBBIl1UgzbN7N443T":"5uSe39BebHaEqpXXSuLtKeaLWWNAczUc39MtnWE_lkH2M1xq282KPQ8Oal.wV2bXp04hanqEXVy3pv3_YeePherBsZCVawBw2kqYzUQ.1NiH0IAFhzlh1MtdnLueLRVZ8d2T2A1QbyqZIFN_lMlhACjxuZ6k9A_yS4URh4wRX9.Jst2j53ntzEVH1X8mH5E12bP_Rg_xiJms8s7iCl3O3VFfoJI_MrQZq8KO3qfVCvY2LvxKbHIS44JESIAxFEGw2rD7eUjgpHUAjuvyo.w7wyJdvr42WxRTw_S5wdZKFN7dhMCO1qsZKodqvlQj_66HewI_MPL7u0n9s.JQuRELasN00QHStc8G0uaJq5y9.7z.XbqQvy2lVmCtS9.IHwgsf7P3"
    }

    ret = requests.get(url=url, verify=False, headers=headers, cookies=cookies)

    # cookie = ret.cookies
    #
    # headers2 = {
    #     "Host": "m.zhaopin.com",
    #     "Connection": "keep-alive",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    #     "Accept": "*/*",
    #     "Sec-Fetch-Site": "same-origin",
    #     "Sec-Fetch-Mode": "no-cors",
    #     "Referer": "https://m.zhaopin.com/company/CZ259897210.htm",
    #     "Accept-Encoding": "gzip, deflate, br",
    #     "Accept-Language": "zh,zh-CN;q=0.9,ru;q=0.8,en;q=0.7,en-US;q=0.6",
    #         }
    #
    # cookie['acw_tc'] =
    # ret = requests.get(url=url, verify=False, headers=headers, )

    print(ret.text)




if __name__ == '__main__':
    req()




