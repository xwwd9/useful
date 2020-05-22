# 心得
* bytes类型中存的就是每个字符对应的编码，只不过print的时候自动显示成了对应的ASCII字符



# 常用代码片段
* bytesarray 转 string
    ```python
    b = bytes('我', encoding='utf8')
    c = [*b]
    # 这里的c实际就为对应的ASCII编码对应的数组
    bytearray(c).decode(encoding="utf8")
    ```






# js解密
* 剑鱼标讯 （2020/3/10）
    * 通过class名称找到解密片段，分析发现需要发送请求单独获取解密key。
    * 通过execjs的方式直接解密，或者翻译js代码成python

* 去哪网 （2020/5/20）
    * 先是通过油猴hook，window._pt_的生成位置。注意hook的时候一定要注意hook的url和hook的时机
    ``` 
        油猴头部
        // @match        https://flight.qunar.com/*
        // @run-at       document-start
    ```
    * 发现pre参数是通过html中的script脚本生成的，这时候需要单独把script脚本弄出来调试。调试过程如下
    ```
        1. 找到代码格式化检测的部分，去掉检测。
        2. 去掉检测后还是无法出现正确结果，发现有try catch，再catch中打印错误。
        3. 将错误补全后，可以得到window._pt_的值，但是这个值不正确。（其中有多处生成这个值得地方，但是只有一个是对的）
        4. 修改script代码，让window._pt_得到正确的赋值。
    ```
    * __m__, 随机header，直接是md5和sha1的结果。
    









# 字体解密
* 剑鱼标讯
    * 先通过控制台查看用的是哪一套字体，然后下载下来用python转换成xml格式进行分析，发现字体和编码是一一对应的。



