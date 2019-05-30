

"""
https://www.cnblogs.com/tkqasn/p/6001134.html
"""



def get_current_date():
    import datetime
    cur_data = datetime.date.today().strftime("%Y%m%d")
    # print(cur_data)
    return cur_data


def date_add(interval):
    """
    用于计算日期的间隔
    :param interval:
    :return:
    """
    import datetime
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
    import datetime
    return  datetime.datetime.now().isoweekday()


if __name__ == "__main__":
    print(get_current_date())
    print(date_add(10))
