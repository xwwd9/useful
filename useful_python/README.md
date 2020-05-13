

[返回主目录](../README.md)




# 常用库总结和技巧总结(如需实列，请跳转到具体页面查看)
* [re正则模块总结](./examples_jupyter/re.ipynb)
    * match     ：从开头匹配
    * search    ：在字符串中返回匹配的第一个结果
    * findall   ：匹配字符串的所用内容
    * sub       ：替换匹配的字符串(**代替的字符在前， 匹配的字符在后**)
    * 贪婪模式和非贪婪模式


* [mongo模块](./examples_jupyter/mongo.ipynb)

* [selenium模块](./examples_jupyter/selenium.ipynb)

* [excel模块](./examples_jupyter/excel.ipynb)

* [一些技巧总结](./examples_jupyter/tips.ipynb)
    * 下载文件，获取文件名，并保存。以下载百度文库举例




* [scrapy笔记](examples_jupyter/docs/scrapy.md)
    * 获取scrapy的配置文件 
    * 可以用SpiderLoader通过名字来加载爬虫  
    * 命令行工具scrapy是通过当前目录下的scrapy.cfg配置文件中指定的scrapy工程配置文件来启动
    * middlerware跟新header
    * 下载图片需重写ImagesPipeline
    * 如果在spider中用了custom_settings,需要注意不是和全局的setting合并，而是只用spider中自己的settings
    * xpath总结
        * //后有多个节点直接通过[1]来选取，1是代表第一个
            ```
               // 有多个div选第一个
               response.xpath("//div[@class='hy-mainLeftA'][1]/ul/li").extract_first()
            ```
        * 选取兄弟节点 following-sibling::li[1]




* [django笔记]



* 小工具
    * 提取搜狗的scel词库()

    
    

# 坑
*  读取.ini或者cfg这些配置文件都是字符串，所以在配置文件中不必写引号，或者读取的时候记得转换为数字

* pattern = re.compile(r"/([^/.]+)/") 中.代表的是点号，不是任意字符。


* 有了GIL，也需要线程同步  
    * GIL是字节码程度的保证，保证一个进程中同一时刻只能有一个线程。  
    * 线程同步需要线程安全的变量或者加锁。

    