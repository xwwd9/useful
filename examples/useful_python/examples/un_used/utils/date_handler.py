

"""
https://www.cnblogs.com/tkqasn/p/6001134.html
"""

import datetime

def get_current_date():
    cur_data = datetime.date.today().strftime("%Y%m%d")
    # print(cur_data)
    return cur_data


def date_add(interval):
    """
    用于计算日期的间隔
    :param interval:
    :return:
    """
    cur_data = datetime.date.today()
    cur_data = (cur_data + datetime.timedelta(interval)).strftime("%Y%m%d")
    # print(cur_data)
    return cur_data

def get_cur_week_day():
    """
    获取当前是星期几
    isoweekday() 返回 1 2 3 4 5 6 7
    :return:
    """

    return  datetime.datetime.now().isoweekday()


def utcfromtimestamp(timestamp):
    """
    根据时间戳，返回datetime的datetime对象
    """

    return datetime.datetime.utcfromtimestamp(timestamp)

#
# def get_cur_time_millisecond():
#     """
#     返回当前时间戳，毫秒
#     :return:
#     """




if __name__ == "__main__":
    print(get_current_date())
    print(date_add(10))
