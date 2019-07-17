

[返回主目录](../README.md)









# 坑
*  读取.ini或者cfg这些配置文件都是字符串，所以在配置文件中不必写引号，或者读取的时候记得转换为数字











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



# redis笔记

* 查看zset集合个数
    ```
    zcard key
    ```
    
    
    