
[返回上一级](../../README.md)

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
  
    # 这种方式是如果该字段不存在就会用setdefault的，如果存在不会更新。
    request.headers.setdefault('User-Agent', ua)
    # 推荐用以下方式更新
    request.headers['User-Agent'] = ua
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
    
    
* 运行spider,可使用CrawlerProcess， 和CrawlerRunner， 一般使用CrawlerRunner。

    ```python
    import scrapy
    from twisted.internet import reactor
    from scrapy.crawler import CrawlerRunner
    from scrapy.utils.log import configure_logging
    
    class MySpider1(scrapy.Spider):
        # Your first spider definition
        ...
    
    class MySpider2(scrapy.Spider):
        # Your second spider definition
        ...
    
    configure_logging()
    runner = CrawlerRunner()
    runner.crawl(MySpider1)
    runner.crawl(MySpider2)
    d = runner.join()
    d.addBoth(lambda _: reactor.stop())
    
    reactor.run() # the script will block here until all crawling jobs are finished
    ```


* cookie的使用
    * "COOKIES_ENABLED":True 是否使用cookie
    * 在使用Request()构造请求，或者直接在中间件中设置cookies的时候需要注意meta中donot_merge_cookies参数的设置，donot_merge_cookies = False 时，自己设置的cookie不会生效，也就是自己的cookie不会和scrapy的cookie合并。
    
    * 总而言之，要使用cookie，需要把设置打开，自己设置的cookie会合scrapy的进行合并。直接在header中设置cookie，这些参数是否生效，还未尝试。
    

[返回上一级](../../README.md)