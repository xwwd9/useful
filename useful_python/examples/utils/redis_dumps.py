

"""
redis 数据库复制操作
"""

import redis

if __name__ == "__main__":

    key = "alidetail1688:requests"

    host = "39.96.81.234"
    password = 'FNlowtF!^fpn'

    r = redis.StrictRedis(host=host, port=6379, db=14, password=password)
    ret = r.zrange(key, 0, -1)
    print(ret)

    r2 = redis.StrictRedis(host=host, port=6379, db=15, password=password)

    r2.keys()

    for index, i in enumerate(ret):
        ret = r2.execute_command('ZADD', key, 0, i)
        print(ret, index)










