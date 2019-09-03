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



* xpath  
    * 同时满足2种属性：
    ```
    //div[@class='para-title level-2' and @label-module='para-title']
    ```
    * 获取文本(有个括号)：
    ```
    /text()
    ```
    * 获取兄弟节点
    ```
    /following-sibling::div[1]    
    /preceding-sibling::div[1]
    ```
    * 获取当前节点的所有文本内容
    ```
    string(./)
    ```