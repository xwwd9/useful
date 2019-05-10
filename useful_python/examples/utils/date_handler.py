

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


if __name__ == "__main__":
    print(get_current_date())
    print(date_add(10))
