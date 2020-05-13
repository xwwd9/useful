[返回主目录](../../README.md)




# 常用库总结和技巧总结(如需实列，请跳转到具体页面查看)
* [re正则模块总结](../../useful_python/examples_jupyter/re.ipynb)
    * match     ：从开头匹配
    * search    ：在字符串中返回匹配的第一个结果
    * findall   ：匹配字符串的所用内容
    * sub       ：替换匹配的字符串(**代替的字符在前， 匹配的字符在后**)
    * 贪婪模式和非贪婪模式



* [mongo模块](../../useful_python/examples_jupyter/mongo.ipynb)

* [selenium模块](../../useful_python/examples_jupyter/selenium.ipynb)

* [excel模块](../../useful_python/examples_jupyter/excel.ipynb)

* [一些技巧总结](../../useful_python/examples_jupyter/tips.ipynb)
    * 下载文件，获取文件名，并保存。以下载百度文库举例
    
    
    
* 进程的三中方式：
    * spawn：使用此方式启动的进程，只会执行和 target 参数或者 run() 方法相关的代码。Windows 平台只能使用此方法，事实上该平台默认使用的也是该启动方式。相比其他两种方式，此方式启动进程的效率最低。
    * fork：使用此方式启动的进程，基本等同于主进程（即主进程拥有的资源，该子进程全都有）。因此，该子进程会从创建位置起，和主进程一样执行程序中的代码。注意，此启动方式仅适用于 UNIX 平台，os.fork() 创建的进程就是采用此方式启动的。
    *  forserver：使用此方式，程序将会启动一个服务器进程。即当程序每次请求启动新进程时，父进程都会连接到该服务器进程，请求由服务器进程来创建新进程。通过这种方式启动的进程不需要从父进程继承资源。注意，此启动方式只在 UNIX 平台上有效。
    
    
    
[返回上一级](../../README.md)
