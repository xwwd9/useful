

"""
redis 数据库复制操作
"""

import redis

if __name__ == "__main__":

    key = "sogouwechatinfo:requests"

    r = redis.StrictRedis(host="*****", port=6379, db=15, password='*****')
    ret = r.zrange(key, 0, -1)
    print(ret)

    r2 = redis.StrictRedis(host="******", port=6379, db=14, password='****')

    for index, i in enumerate(ret):
        ret = r2.execute_command('ZADD', key, 0, i)
        print(ret, index)








