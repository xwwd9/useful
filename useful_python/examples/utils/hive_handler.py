from subprocess import run


def execte_hive_select(sql, out_file, err_file):
    """
    传入sql语句，将执行的结果存入file
    文件
    :param sql: select sql语句
    :param out_file: 结果文件
    :param err_file: 错误文件
    :return: 返回获取的每一个结果
    """
    if ";" != sql[-1]:
        sql = sql + ";"
    # 如果发生错误 循环3次
    err_cnt = 0
    while err_cnt < 3:

        try:
            ret = run('echo \"{sql}\" | hive'.format(sql=sql) , shell=True,
                      stdout=open(out_file, "w"),
                      stderr=open(err_file, "w"))
            if ret.returncode != 0:
                err_cnt += 1
                continue

            with open(out_file, "r") as f:
                line = f.readline()
                while line:
                    if "hive>" not in line:
                        yield line
                    line = f.readline()

            # 执行成功，正常返回
            return 0
        except Exception as e:
            print(e)
            err_cnt += 1

    return 0


if __name__ == "__main__":
    for i in execte_hive_select("a", "b", "c"):
        print(i)
