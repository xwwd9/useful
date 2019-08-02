

[返回主目录](../README.md)






# 常用库总结和技巧总结(如需实列，请跳转到具体页面查看)
* [re正则模块总结](./examples_jupyter/re.ipynb)
    * match     ：从开头匹配
    * search    ：在字符串中返回匹配的第一个结果
    * findall   ：匹配字符串的所用内容
    * sub       ：替换匹配的字符串


* [mongo模块](./examples_jupyter/mongo.ipynb)

* [selenium模块](./examples_jupyter/selenium.ipynb)

* [excel模块](./examples_jupyter/excel.ipynb)

* [一些偏门技巧总结](./examples_jupyter/tips.ipynb)
    * 下载文件，获取文件名，并保存。以下载百度文库举例













# scrapy笔记

* 获取scrapy的配置文件  
    ```python
    get_project_settings()
    ```
    
* 可以用SpiderLoader通过名字来加载爬虫  
    ```python
    loader = SpiderLoader(settings)
    spider_cls = loader.load(spider_name)
    ```

* 命令行工具scrapy是通过当前目录下的scrapy.cfg配置文件中指定的scrapy工程配置文件来启动 
    

* middlerware跟新header  
    ```python
    request.headers.update(tk_headers)  
  
    request.headers.setdefault('User-Agent', ua)
    ```


* 下载图片需重写ImagesPipeline  [参考](https://docs.scrapy.org/en/latest/topics/media-pipeline.html?highlight=ImagesPipeline)  
    ```python
    注意重写文件路径函数重写要和父函数中参数声明一致，不然传参会有问题，文档中给的example不正确。
    def file_path(self, request, response=None, info=None):
      pass
  
    ```
     设置图片或者文件下载中间件的时候需要注意优先级，优先级高的情况（比如为1），get_media_requests一定要保证有下载请求，不然item不会传给后边的pipeline。  
       
   文件不管下载成功还是失败，都会进入item_completed。
    
* 如果在spider中用了custom_settings,需要注意不是和全局的setting合并，而是只用spider中自己的settings



# redis笔记

* 查看zset集合个数
    ```
    zcard key
    ```
    
    
    

# 坑
*  读取.ini或者cfg这些配置文件都是字符串，所以在配置文件中不必写引号，或者读取的时候记得转换为数字

    