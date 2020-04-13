# 心得
* bytes类型中存的就是每个字符对应的编码，只不过print的时候自动显示成了对应的ASCII字符



# 常用代码片段
* bytesarray 转 string
    ```python
    b = bytes('我', encoding='utf8')
    c = [*b]
    bytearray(c).decode(encoding="utf8")
    ```






# js解密
* 剑鱼标讯
    * 通过class名称找到解密片段，分析发现需要发送请求单独获取解密key。
    * 通过execjs的方式直接解密，或者翻译js代码成python










# 字体解密
* 剑鱼标讯
    * 先通过控制台查看用的是哪一套字体，然后下载下来用python转换成xml格式进行分析，发现字体和编码是一一对应的。



