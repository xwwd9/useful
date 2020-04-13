




# pip 改源

* linux下，修改 ~/.pip/pip.conf (没有就创建一个)， 修改 index-url至tuna，内容如下：
    ```
    [global]
    index-url = https://pypi.tuna.tsinghua.edu.cn/simple
    ```

* windows下，直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，新建文件pip.ini，内容如下
    ```
     [global]
     index-url = https://pypi.tuna.tsinghua.edu.cn/simple
    ```





# 安卓刷机
1. 去[这里](https://www.romzhijia.net/)下载手机的固件  
2. 采用线刷或者直接9008端口刷机  
3. 需要安装高通端口驱动
4. 手机进入高通刷机模式
5  一般在下载的zip固件中会有对应的配套设备






# Pycharm 使用技巧

* Kite
    * ctrl+p 查看文档
    * ctrl+shift+a 输入Kite: Docs at cursor 查看文档



# 爬虫技巧
* 在测试cookie哪个有效的时候，如果删除了某个cookie失效了，不一定是这个cookie失效，可能是服务端判断你有连续的2次相同访问，或者没有走正常流程，而访问失效，比如搜狗微信。




# supervisor 使用

* 使用步骤：
    * 创建配置文件：echo_supervisord_conf > /work/supervisor/supervisord.conf
    * 编写配置文件
    * 启动supervisor：supervisord -c /work/supervisor/supervisord.conf

* 编写配置文件：
    * 如果需要web页面查看，需要打开[inet_http_server]配置
    * 可以将配置单独写到另外的文件件中去
        ```
        * supervisord.conf(在主配置文件中添加如下配置)
        [include]
        files = /usr/supervisor/supervisord/*.conf
      
        在supervisord文件件下的所有.conf文件都会启动
        ```
    * 常用命令
        * 查看进程：supervisorctl status
        * 启动进程：supervisorctl start xxxx
        * 停在进程：supervisorctl stop xxxx
        * 重启进程：supervisorctl restart xxxx
        * 停止服务：supervisorctl shutdown 要进入配置文件中启动
        * 启动服务：supervisord -c /work/supervisor/supervisord.conf
    * 配置样例
        ```
            [program:scrapyd]
            directory = /usr/               ; 程序的启动目录
            command = /usr/bin/scrapyd      ; 启动命令，与命令行启动的命令是一样的
            priority=1                      ; 数字越高，优先级越高
            numprocs=1                      ; 启动几个进程
            autostart = true                ; 在 supervisord 启动的时候也自动启动
            startsecs = 5                   ; 启动 5 秒后没有异常退出，就当作已经正常启动了
            autorestart = true              ; 程序异常退出后自动重启
            startretries = 3                ; 启动失败自动重试次数，默认是 3
            user = root                     ; 用哪个用户启动
            redirect_stderr = true          ; 把 stderr 重定向到 stdout，默认 false
            stdout_logfile_maxbytes = 20MB  ; stdout 日志文件大小，默认 50MB
            stdout_logfile_backups = 20     ; stdout 日志文件备份数
            stdout_logfile = /etc/supervisord.d/log/confd.log  ;日志统一放在log目录下
            ; 可以通过 environment 来添加需要的环境变量，一种常见的用法是修改 PYTHONPATH
            environment=PYTHONPATH=$PYTHONPATH:/path/to/somewhere
            

            stopsignal=KILL               ; 用来杀死进程的信号
            stopwaitsecs=10               ; 发送SIGKILL前的等待时间

        ```

        ```
        - command：启动程序使用的命令，可以是绝对路径或者相对路径
        - process_name：一个python字符串表达式，用来表示supervisor进程启动的这个的名称，默认值是%(program_name)s
        - numprocs：Supervisor启动这个程序的多个实例，如果numprocs>1，则process_name的表达式必须包含%(process_num)s，默认是1
        - numprocs_start：一个int偏移值，当启动实例的时候用来计算numprocs的值
        - priority：权重，可以控制程序启动和关闭时的顺序，权重越低：越早启动，越晚关闭。默认值是999
        - autostart：如果设置为true，当supervisord启动的时候，进程会自动重启。
        - autorestart：值可以是false、true、unexpected。false：进程不会自动重启，unexpected：当程序退出时的退出码不是exitcodes中定义的时，进程会重启，true：进程会无条件重启当退出的时候。
        - startsecs：程序启动后等待多长时间后才认为程序启动成功
        - startretries：supervisord尝试启动一个程序时尝试的次数。默认是3
        - exitcodes：一个预期的退出返回码，默认是0,2。
        - stopsignal：当收到stop请求的时候，发送信号给程序，默认是TERM信号，也可以是 HUP, INT, QUIT, KILL, USR1, or USR2。
        - stopwaitsecs：在操作系统给supervisord发送SIGCHILD信号时等待的时间
        - stopasgroup：如果设置为true，则会使supervisor发送停止信号到整个进程组
        - killasgroup：如果设置为true，则在给程序发送SIGKILL信号的时候，会发送到整个进程组，它的子进程也会受到影响。
        - user：如果supervisord以root运行，则会使用这个设置用户启动子程序
        - redirect_stderr：如果设置为true，进程则会把标准错误输出到supervisord后台的标准输出文件描述符。
        - stdout_logfile：把进程的标准输出写入文件中，如果stdout_logfile没有设置或者设置为AUTO，则supervisor会自动选择一个文件位置。
        - stdout_logfile_maxbytes：标准输出log文件达到多少后自动进行轮转，单位是KB、MB、GB。如果设置为0则表示不限制日志文件大小
        - stdout_logfile_backups：标准输出日志轮转备份的数量，默认是10，如果设置为0，则不备份
        - stdout_capture_maxbytes：当进程处于stderr capture mode模式的时候，写入FIFO队列的最大bytes值，单位可以是KB、MB、GB
        - stdout_events_enabled：如果设置为true，当进程在写它的stderr到文件描述符的时候，PROCESS_LOG_STDERR事件会被触发
        - stderr_logfile：把进程的错误日志输出一个文件中，除非redirect_stderr参数被设置为true
        - stderr_logfile_maxbytes：错误log文件达到多少后自动进行轮转，单位是KB、MB、GB。如果设置为0则表示不限制日志文件大小
        - stderr_logfile_backups：错误日志轮转备份的数量，默认是10，如果设置为0，则不备份
        - stderr_capture_maxbytes：当进程处于stderr capture mode模式的时候，写入FIFO队列的最大bytes值，单位可以是KB、MB、GB
        - stderr_events_enabled：如果设置为true，当进程在写它的stderr到文件描述符的时候，PROCESS_LOG_STDERR事件会被触发
        - environment：一个k/v对的list列表
        - directory：supervisord在生成子进程的时候会切换到该目录
        - umask：设置进程的umask
        - serverurl：是否允许子进程和内部的HTTP服务通讯，如果设置为AUTO，supervisor会自动的构造一个url
        ```



# docker使用

* 进入容器：docker exec -it scrapy /bin/bash
* 删除镜像：docker rmi xxx
* 将容器重新打包成镜像：docker commit test xxx/common
* 将镜像推入厂库：docker push 192.168.4.125:5000/xxx_common
* 给镜像打标签：docker tag xxx/common 192.168.4.125:50xxx00/xxx_common
* * 更改容器时区：ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime。  
  * 或者使用tzselect设置时区。  
  * 注意一定要用ln，不要用cp，如果设置了不生效，请查看文件内的内容是否是正确的+8小时。
  * 注意还要修改/etc/timezone文件中的内容为Asia/Shanghai，不然在程序中会时区报错。 
  * 如果上述修改后还不行，可以尝试设置TZ环境变量：TZ='Asia/Shanghai'; export TZ并将这行命令添加到.profile中，然后退出并重新登录
  * 将文件拷贝进入docker：docker cp sources.list  scrapyweb:/work
  
* docker 镜像加速
    ```
        sudo mkdir -p /etc/docker
        sudo tee /etc/docker/daemon.json <<-'EOF'
        {
            "registry-mirrors": [
                "https://1nj0zren.mirror.aliyuncs.com",
                "https://docker.mirrors.ustc.edu.cn",
                "http://f1361db2.m.daocloud.io",
                "https://registry.docker-cn.com"
            ]
        }
        EOF
        sudo systemctl daemon-reload
        sudo systemctl restart docker
    ```
* 开机启动：systemctl enable docker



# 常用linux命令
* 查看系统磁盘使用：df -h
* 查看文件目录大小：  
    * 先用：du -sh查看总目录大小
    * 再用：du -sh * 查看分目录的大小 
    
# docker命令
* 查看docker磁盘使用情况：docker system df
* 查看命令：docker ps --no-trunc
* 以supervisor的方式启动docker ：docker run -itd -p 7000:7000 -p 7001:7001 -p 7002:7002 -p 7003:7003 -p 7004:7004 --restart unless-stopped --name scrapydweb scrapy  supervisord -nc /work/supervisor/supervisord.conf 
* 重启docker：systemctl restart docker
* 进入docker：docker exec -it scrapydweb /bin/bash
* 开机自启动：systemctl enable docker
* 配置更新命令：docker container update --restart=unless-stopped myredis
* 容器提交成镜像：docker commit test pgy/common (这种方式会把历史记录打包进去，容器可能会越来越大)
* 保存镜像：docker save ID > xxx.tar
           docker load < xxx.tar
* 保存容器：docker export ID >xxx.tar
           docker import xxx.tar containr:v1

# redis常用命令
* config set requirepass FNpn 设置密码，重启后失效
* redis-cli -h 40.96.33.234 -p 6379 连接redis
* 进入redis后使用auth认证
* select 13 选取数据库
* key * 查看当前有哪些keys
* 一些常用命令查看：http://doc.redisfans.com/





# anyproxy使用
* 启动anyproxy -i --rule 文件.js: -i是表是抓取https
* 注意开启防火墙，和代理设置。



# nodejs
* 安装nodejs
    * yum install npm
    * 安装工具n（用于管理npm版本）：npm install -g n
    * 想升级到一个指定的版本，则可以使用n 12.16.0来升级

# ssdb查询命令：
* 查看keys：
    1. keys　 '' '' 10　   字符串类型
    
    2. qlist　'' '' 10　　 列表类型
    
    3. hlist　'' '' 10　　 哈希类型
    
    4. zlist  '' '' 10　  有序集合类型





# 防火墙
 * iptables -I INPUT -p tcp --dport 3000 -j ACCEPT
 * firewall-cmd --zone=public --add-port=3001/tcp --permanent  
   命令含义: –zone #作用域 –add-port=80/tcp #添加端口，格式为：端口/通讯协议 –permanent #永久生效，没有此参数重启后失效  
   **开启端口后记得重启**  
   **firewall-cmd --reload**







# 阿里云
* 阿里云 查看公网ip：curl httpbin.org/ip









# 代理总结：
* 使用过的代理：http://www.moguproxy.com/http
```
目前来说代理服务主要提供2种代理：
1.常规代理：直接提供代理ip，访问一次接口，得到5-10个代理ip地址。
	优点：较为灵活，不限制并发量。可以控制哪个请求用的是哪一个代理ip，在cookie和ip绑定的场景很实用。
	缺点：服务端限制了获取代理ip的频率（一般是每10s获取5个ip代理），需要编写服务，维护ip代理池。
	套餐配置：目前看到的有：1.每日获取ip量固定（ip短期有效/或长期有效） 2.每日获取ip量不固定（ip短期有效/或长期有效）
2.转发代理：提供一个统一的服务端地址，请求到服务端后，由服务端随机分配代理ip。
	优点：使用方便，不用自己维护代理池。
	缺点：服务端会限制访问次数， 如每秒的并发请求次数不能超过5次，或者总请求量不能超过多少次。用的代理不能够自己安排，每回都是服务端随机分配的一个。
	套餐配置：目前看到的有1.限制并发量的套餐 2.限制总请求次数的套餐。（平局要比常规代理的贵）


总结：推荐使用常规代理服务（每日ip不限量,ip短期有效的套餐），自己维护ip代理池。
	  转发代理服务限制并发数量，1-2个爬虫跑没有问题，但是爬虫多了每秒的并发量会很大，购买对应的套餐会很贵。
```