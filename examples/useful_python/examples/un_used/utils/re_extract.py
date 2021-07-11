
import re




def extract_cell_phone(text):
    pattern = re.compile(r'(1\d{10})')
    ret = pattern.findall(text)
    print(ret)



def extract_phone(text):

    pattern = re.compile(r'>(\d{0,4}?)(\s*?|-*?)(0\d{1,3}?)(\s*?|-*?)(\d{8}?)<')
    rets = pattern.findall(text)



    print(rets)






if __name__ == "__main__":
    # extract_cell_phone("86 0234 31572750")
    extract_phone("008602489738492")

    extract_phone("生活商贸有限公司电话 0086-024-89738492，尚小街8-2号，为您提供手绘鞋;")


