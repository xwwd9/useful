import hashlib

from useful_python.examples.spiders.utils.tools import char_code_at,  md5



def get_m(QN48, QN668):
    """
    获取_m_参数
    """
    t = encrypt(QN48, QN668)
    return md5(t)

def encrypt(QN48, QN668):
    t = QN48
    n = getQtTime(QN668)
    code = t+n

    r = int(n)%2

    if r == 0:
        # 先sha1加密，再md5加密
        sha1 = hashlib.sha1(code.encode('utf-8'))
        sha1_ed = sha1.hexdigest()
        md5_ed = hashlib.md5(sha1_ed.encode('utf-8')).hexdigest()
        return md5_ed
    else:
        # 先md5加密，再sha1加密
        md5_ed = hashlib.md5(code.encode('utf-8')).hexdigest()
        sha1 = hashlib.sha1(md5_ed.encode('utf-8'))
        sha1_ed = sha1.hexdigest()
        return sha1_ed


def getQtTime(QN668):
    ret = ""
    for item in QN668.split(","):
        code = int(item)-2
        ret += chr(code)

    return ret



def random_key(QN48, QN668):
    """
        获取一个随机的参数
    """
    ret = {}
    t = getQtTime(QN668)
    r = t[4:]
    temp = ""
    for item in r:
        temp += str(char_code_at(item))

    temp = md5(temp)[-6:]

    ret[temp] = encrypt(QN48, QN668)

    print(ret)
    return ret







if __name__ == '__main__':
    # print(getQtTime("51,55,59,50,50,52,57,53,58,54,57,57,50"))
    a = "tc_1a845960527cfe22_1722be10e4f_8417"
    b = "51,55,59,50,50,53,54,57,51,58,56,56,53"
    print(get_m(a, b))
    random_key(a, b)



