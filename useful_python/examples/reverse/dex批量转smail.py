

# 需要将dex文件和baksmali.jar放在一起，然后在该目录下运行该脚本
import os

import time
files = os.listdir("./")

for file in files:
    tfile = file.split(".")
    if len(tfile)>1:
        pre = tfile[0]
        tail = tfile[1]
        if tail == "dex":
            print("java -jar baksmali.jar disassemble -o ./out/%s/ %s"%(pre, file))
            os.system("java -jar baksmali.jar disassemble -o ./out/%s/ %s"%(pre, file))


