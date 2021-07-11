
# 函数的顺序就是路由的顺序

# bool类型转换：yes on 1 True true会转换成true, 其它为false
@app03.get("/query/bool/conversion") 
def type_conversion(param: bool = False):
    return param
d     

