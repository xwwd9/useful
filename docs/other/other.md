[返回上一级](../../README.md)

- [1. pip 改源](#1-pip-改源)
  - [1.1. linux下，修改 ~/.pip/pip.conf (没有就创建一个)， 修改 index-url至tuna，内容如下：](#11-linux下修改pippipconf没有就创建一个-修改index-url至tuna内容如下)
  - [1.2. windows下，直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，新建文件pip.ini，内容如下](#12-windows下直接在user目录中创建一个pip目录如cusersxxpip新建文件pipini内容如下)
  - [1.3. linux 设置交换分区 设置swap](#13-linux-设置交换分区-设置swap)
- [2. 安卓刷机](#2-安卓刷机)
- [3. Pycharm 使用技巧](#3-pycharm-使用技巧)
  - [3.1. Kite](#31-kite)
- [4. pm2 使用](#4-pm2-使用)
  - [4.1. 启动next.js: pm2 start yarn --name hope -- run start](#41-启动nextjs-pm2-start-yarn---name-hope----run-start)
- [5. supervisor 使用](#5-supervisor-使用)
  - [5.1. 使用步骤：](#51-使用步骤)
  - [5.2. 编写配置文件：](#52-编写配置文件)
- [6. docker使用](#6-docker使用)
  - [6.1. 进入容器：docker exec -it scrapy /bin/bash 或者/bin/sh](#61-进入容器docker-exec--it-scrapy-binbash-或者binsh)
  - [6.2. 删除镜像：docker rmi xxx](#62-删除镜像docker-rmi-xxx)
  - [6.3. 将容器重新打包成镜像：docker commit test xxx/common](#63-将容器重新打包成镜像docker-commit-test-xxxcommon)
  - [6.4. 将镜像推入厂库：docker push 192.168.4.125:5000/xxx_common](#64-将镜像推入厂库docker-push-19216841255000xxx_common)
  - [6.5. 给镜像打标签：docker tag xxx/common 192.168.4.125:50xxx00/xxx_common](#65-给镜像打标签docker-tag-xxxcommon-192168412550xxx00xxx_common)
  - [6.6. 更改容器时区：](#66-更改容器时区)
  - [6.7. docker 镜像加速](#67-docker-镜像加速)
  - [6.8. 开机启动：systemctl enable docker](#68-开机启动systemctl-enable-docker)
  - [6.9. 常用docker启动](#69-常用docker启动)
- [7. docker命令](#7-docker命令)
  - [7.1. 查看docker磁盘使用情况：docker system df](#71-查看docker磁盘使用情况docker-system-df)
  - [7.2. 查看命令：docker ps --no-trunc](#72-查看命令docker-ps---no-trunc)
  - [7.3. 以supervisor的方式启动docker ：docker run -itd -p 7000:7000 -p 7001:7001 -p 7002:7002 -p 7003:7003 -p 7004:7004 --restart unless-stopped --name scrapydweb scrapy  supervisord -nc /work/supervisor/supervisord.conf](#73-以supervisor的方式启动docker-docker-run--itd--p-70007000--p-70017001--p-70027002--p-70037003--p-70047004---restart-unless-stopped---name-scrapydweb-scrapy-supervisord--nc-worksupervisorsupervisordconf)
  - [7.4. 重启docker：systemctl restart docker](#74-重启dockersystemctl-restart-docker)
  - [7.5. 进入docker：docker exec -it scrapydweb /bin/bash](#75-进入dockerdocker-exec--it-scrapydweb-binbash)
  - [7.6. 开机自启动：systemctl enable docker](#76-开机自启动systemctl-enable-docker)
  - [7.7. 配置更新命令：docker container update --restart=unless-stopped myredis](#77-配置更新命令docker-container-update---restartunless-stopped-myredis)
  - [7.8. 容器提交成镜像：docker commit test pgy/common (这种方式会把历史记录打包进去，容器可能会越来越大)](#78-容器提交成镜像docker-commit-test-pgycommon-这种方式会把历史记录打包进去容器可能会越来越大)
  - [7.9. 保存镜像：docker save ID > xxx.tar](#79-保存镜像docker-save-id--xxxtar)
  - [7.10. 保存容器：docker export ID >xxx.tar](#710-保存容器docker-export-id-xxxtar)
  - [7.11. 安装错误](#711-安装错误)
- [8. nginx 常用配置](#8-nginx-常用配置)
  - [8.1. 多个域名，通一个ip。在域名服务商处查看域名前缀，一般@表明主机名为空](#81-多个域名通一个ip在域名服务商处查看域名前缀一般表明主机名为空)
- [9. 常用linux命令](#9-常用linux命令)
  - [9.1. 查看系统磁盘使用：df -h](#91-查看系统磁盘使用df--h)
  - [9.2. 查看文件目录大小：](#92-查看文件目录大小)
  - [9.3. 修改history条数](#93-修改history条数)
  - [9.4. 利用awk批量kill](#94-利用awk批量kill)
- [10. sh脚本](#10-sh脚本)
  - [10.1. 获取时间](#101-获取时间)
  - [10.2. sleep](#102-sleep)
- [11. redis常用命令](#11-redis常用命令)
  - [11.1. config set requirepass FNpn 设置密码，重启后失效](#111-config-set-requirepass-fnpn-设置密码重启后失效)
  - [11.2. redis-cli -h 40.96.33.234 -p 6379 连接redis](#112-redis-cli--h-409633234--p-6379-连接redis)
  - [11.3. 进入redis后使用auth认证](#113-进入redis后使用auth认证)
  - [11.4. select 13 选取数据库](#114-select-13-选取数据库)
  - [11.5. key * 查看当前有哪些keys](#115-key--查看当前有哪些keys)
  - [11.6. 一些常用命令查看：http://doc.redisfans.com/](#116-一些常用命令查看httpdocredisfanscom)
- [12. wordpress使用](#12-wordpress使用)
  - [12.1. docker启动wordpress](#121-docker启动wordpress)
  - [12.2. css自定义](#122-css自定义)
  - [12.3. 错误排查](#123-错误排查)
- [13. mysql](#13-mysql)
  - [13.1. docker 启动](#131-docker-启动)
  - [13.2. 创建一个库](#132-创建一个库)
- [14. anyproxy使用](#14-anyproxy使用)
  - [14.1. 启动anyproxy -i --rule 文件.js: -i是表是抓取https](#141-启动anyproxy--i---rule-文件js--i是表是抓取https)
  - [14.2. 注意开启防火墙，和代理设置。](#142-注意开启防火墙和代理设置)
- [15. nodejs](#15-nodejs)
  - [15.1. 安装nodejs](#151-安装nodejs)
- [16. ssdb查询命令：](#16-ssdb查询命令)
  - [16.1. 查看keys：](#161-查看keys)
- [17. 防火墙](#17-防火墙)
  - [17.1. iptables -I INPUT -p tcp --dport 3000 -j ACCEPT](#171-iptables--i-input--p-tcp---dport-3000--j-accept)
  - [17.2. firewall-cmd --zone=public --add-port=3001/tcp --permanent](#172-firewall-cmd---zonepublic---add-port3001tcp---permanent)
- [18. 阿里云](#18-阿里云)
- [19. 搜索技巧（google）](#19-搜索技巧google)
  - [19.1. "空格-号"排除关键词](#191-空格-号排除关键词)
  - [19.2. 英文双引号精确搜索](#192-英文双引号精确搜索)
  - [19.3. or 多个关键词搜索](#193-or-多个关键词搜索)
  - [19.4. *号模糊匹配](#194-号模糊匹配)
  - [19.5. filetype:pdf ppt doc 指定文件类型搜索](#195-filetypepdf-ppt-doc-指定文件类型搜索)
  - [19.6. site:网站 对指定网站进行搜索](#196-site网站-对指定网站进行搜索)
  - [19.7. inurl:（表示其中一个包含）或者allinurl（表示后续都要包含）:](#197-inurl表示其中一个包含或者allinurl表示后续都要包含)
  - [19.8. intitle: allintitle:在标题中进行搜索](#198-intitle-allintitle在标题中进行搜索)
  - [19.9.](#199)
- [20. 代理总结：](#20-代理总结)



# 1. pip 改源

## 1.1. linux下，修改 ~/.pip/pip.conf (没有就创建一个)， 修改 index-url至tuna，内容如下：
    ```
    [global]
    index-url = https://pypi.tuna.tsinghua.edu.cn/simple
    ```

## 1.2. windows下，直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，新建文件pip.ini，内容如下
    ```
     [global]
     index-url = https://pypi.tuna.tsinghua.edu.cn/simple
    ```



## 1.3. linux 设置交换分区 设置swap
    * dd if=/dev/zero of=/tmp/swap bs=1M count=2048 （创建 SWAP 文件，设置大小，这里我设置为 1G。（bs * count = SWAP 大小））
    * chmod 600 /tmp/swap （设置文件权限）
    * mkswap /tmp/swap （创建 SWAP）
    * swapon /tmp/swap （启用）
    * swapon -s 或者 free -m （查看 SWAP 状态）
    
    * echo '/var/swap   swap   swap   default 0 0' >> /etc/fstab（ 添加开机启动)
    * swapoff /tmp/swap（停用）
    * swapoff /tmp/swap（关闭）
    * rm -rf /tmp/swap （删除）
    * sed -i '/\/var\/swap   swap   swap   default 0 0/d'  /etc/fstab（去掉开机启动）

    



# 2. 安卓刷机
1. 去[这里](https://www.romzhijia.net/)下载手机的固件  
2. 采用线刷或者直接9008端口刷机  
3. 需要安装高通端口驱动
4. 手机进入高通刷机模式
5  一般在下载的zip固件中会有对应的配套设备






# 3. Pycharm 使用技巧

## 3.1. Kite
    * ctrl+p 查看文档
    * ctrl+shift+a 输入Kite: Docs at cursor 查看文档




# 4. pm2 使用
## 4.1. 启动next.js: pm2 start yarn --name hope -- run start
```
    0 pm2需要全局安装 nnpm install -g pm2
    1 启动进程/应用 pm2 start bin/www 或 pm2 start app.js
    2 重命名进程/应用 pm2 start app.js --name wb123
    3 添加进程/应用 watch pm2 start bin/www --watch
    4 结束进程/应用 pm2 stop www
    5 结束所有进程/应用 pm2 stop all
    6 删除进程/应用 pm2 delete www
    7 删除所有进程/应用 pm2 delete all
    8 列出所有进程/应用 pm2 list
    9 查看某个进程/应用具体情况 pm2 describe www
    10 查看进程/应用的资源消耗情况 pm2 monit
    11 查看pm2的日志 pm2 logs
    12 若要查看某个进程/应用的日志,使用 pm2 logs www
    13 重新启动进程/应用 pm2 restart www
    14 重新启动所有进程/应用 pm2 restart all
```


# 5. supervisor 使用

## 5.1. 使用步骤：
    * 创建配置文件：echo_supervisord_conf > /work/supervisor/supervisord.conf
    * 编写配置文件
    * 启动supervisor：supervisord -c /work/supervisor/supervisord.conf

## 5.2. 编写配置文件：
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



# 6. docker使用

## 6.1. 进入容器：docker exec -it scrapy /bin/bash 或者/bin/sh
## 6.2. 删除镜像：docker rmi xxx
## 6.3. 将容器重新打包成镜像：docker commit test xxx/common
## 6.4. 将镜像推入厂库：docker push 192.168.4.125:5000/xxx_common
## 6.5. 给镜像打标签：docker tag xxx/common 192.168.4.125:50xxx00/xxx_common
## 6.6. 更改容器时区：
  * ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime。  
  * 或者使用tzselect设置时区。  
  * 注意一定要用ln，不要用cp，如果设置了不生效，请查看文件内的内容是否是正确的+8小时。
  * 注意还要修改/etc/timezone文件中的内容为Asia/Shanghai，不然在程序中会时区报错。 
  * 如果上述修改后还不行，可以尝试设置TZ环境变量：TZ='Asia/Shanghai'; export TZ并将这行命令添加到.profile中，然后退出并重新登录
  * 将文件拷贝进入docker：docker cp sources.list  scrapyweb:/work
  
## 6.7. docker 镜像加速
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
## 6.8. 开机启动：systemctl enable docker
## 6.9. 常用docker启动
    ```
        启动redis：
          docker run -p 6379:6379 --restart=unless-stopped --name myredis -d --requirepass "password" redis:latest redis-server
  
        启动mongo：
          docker run -p 27017:27017 --restart=unless-stopped --name mymongo -d mongo --auth
        启动mongo后再用以下创建用户名密码
            $ docker exec -it mongo mongo admin
            # 创建一个名为 admin，密码为 123456 的用户。
            >  db.createUser({ user:'admin',pwd:'123456',roles:[ { role:'userAdminAnyDatabase', db: 'admin'}]});
            # 尝试使用上面创建的用户信息进行连接。
            > db.auth('admin', '123456')
  
        启动centos：
          docker run -itd --net="host" --restart=unless-stopped --name centos centos /bin/bash
          可以使用systemctl命名：
          docker run -itd -p 8899:22 --restart=unless-stopped --privileged=true --name centos centos /usr/sbin/init
         
         centos ssh dockerfile
         **********************
            # 生成的新镜像以centos镜像为基础
                FROM centos
                # 指定作者信息
                MAINTAINER by Test
                # 安装openssh-server
                RUN yum -y install openssh-server
                
                RUN mkdir /var/run/sshd
                RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key
                RUN ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key
                
                # 指定root密码
                RUN /bin/echo 'root:123456'|chpasswd
                RUN /bin/sed -i 's/.*session.*required.*pam_loginuid.so.*/session optional pam_loginuid.so/g' /etc/pam.d/sshd
                RUN /bin/echo -e "LANG=\"en_US.UTF-8\"" > /etc/default/local
                EXPOSE 22
                CMD /usr/sbin/sshd -D
                
                # docker build -t my-centos:v1.0.0 .
                # docker run -itd -p 5522:22 --name centos --restart=always my-centos:v1.0.0
                
                然后访问5522端口就可以ssh
         **********************
          
          

        启动ss:
          docker run -e PASSWORD=WERsdf123 -e METHOD=aes-256-cfb -p 8377:8388 --name ss --restart=unless-stopped -d shadowsocks/shadowsocks-libev

        启动mysql:
          docker run -itd --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=**** mysql:5.7.30
    ```

    
# 7. docker命令
## 7.1. 查看docker磁盘使用情况：docker system df
## 7.2. 查看命令：docker ps --no-trunc
## 7.3. 以supervisor的方式启动docker ：docker run -itd -p 7000:7000 -p 7001:7001 -p 7002:7002 -p 7003:7003 -p 7004:7004 --restart unless-stopped --name scrapydweb scrapy  supervisord -nc /work/supervisor/supervisord.conf 
## 7.4. 重启docker：systemctl restart docker
## 7.5. 进入docker：docker exec -it scrapydweb /bin/bash
## 7.6. 开机自启动：systemctl enable docker
## 7.7. 配置更新命令：docker container update --restart=unless-stopped myredis
## 7.8. 容器提交成镜像：docker commit test pgy/common (这种方式会把历史记录打包进去，容器可能会越来越大)
## 7.9. 保存镜像：docker save ID > xxx.tar
           docker load < xxx.tar
## 7.10. 保存容器：docker export ID >xxx.tar
           docker import xxx.tar containr:v1

## 7.11. 安装错误
```

  Problem: package docker-ce-3:19.03.12-3.el7.x86_64 requires containerd.io >= 1.2.2-3, but none of the providers can be installed
  - cannot install the best candidate for the job

  解决：
  containerd.io软件包下载地址：https://download.docker.com/linux/centos/7/x86_64/edge/Packages/containerd.io-1.2.6-3.3.el7.x86_64.rpm

  yum -y install containerd.io-1.2.6-3.3.el7.x86_64.rpm
```

           
           
# 8. nginx 常用配置
## 8.1. 多个域名，通一个ip。在域名服务商处查看域名前缀，一般@表明主机名为空
```
server {
        listen 80 default_server;
        server_name _;
        return 404; # 过滤其他域名的请求，返回444状态码
    }
    server {
        listen       80;
        server_name  xxx1.com;


        location / {
        proxy_pass   http://0.0.0.0:9085;
        }
    }
    server {
        listen       80;
        server_name  xxx.com;
        location / {
        proxy_pass   http://0.0.0.0:9086;
       }

    }
```


# 9. 常用linux命令
## 9.1. 查看系统磁盘使用：df -h
## 9.2. 查看文件目录大小：  
    * 先用：du -sh查看总目录大小
    * 再用：du -sh * 查看分目录的大小 
## 9.3. 修改history条数
```
    vim /etc/profile
    HISTSIZE = 100000
    source /etc/profile
```
## 9.4. 利用awk批量kill
```
  1. kill -9 `ps -ef | grep -i xxx | grep -v grep | awk '{print $2}'` 
  2. ps aux | grep xxx | awk '{print $2}' | xargs kill -9
```

# 10. sh脚本
## 10.1. 获取时间
```
  time=$(date -d "2 days ago" "+%Y-%m-%d")//2天前
```
## 10.2. sleep
```
  sleep 1 睡眠1秒
  sleep 1s 睡眠1秒
  sleep 1m 睡眠1分
  sleep 1h 睡眠1小时
```


    
    
# 11. redis常用命令
## 11.1. config set requirepass FNpn 设置密码，重启后失效
## 11.2. redis-cli -h 40.96.33.234 -p 6379 连接redis
## 11.3. 进入redis后使用auth认证
## 11.4. select 13 选取数据库
## 11.5. key * 查看当前有哪些keys
## 11.6. 一些常用命令查看：http://doc.redisfans.com/







# 12. wordpress使用
## 12.1. docker启动wordpress
```
docker run -d --name wordpress -e WORDPRESS_DB_HOST=mysql -e WORDPRESS_DB_USER=root -e WORDPRESS_DB_PASSWORD=*** -e WORDPRESS_DB_NAME=myword -p 9086:80 --link mysql:mysql wordpress
```

## 12.2. css自定义
```
.header {
  background: #fff url('https://movie-image-hope.oss-cn-shanghai.aliyuncs.com/static/header.jpg') repeat-x 0 100%;
}

.footer{
    background: #fff url('https://movie-image-hope.oss-cn-shanghai.aliyuncs.com/static/header.jpg') repeat-x;
}

p{
	font-size: 2rem;
  line-height: 3.2rem;
}

```

## 12.3. 错误排查
```
打开 wp-config.php 文件，将原来的 WP_Debug 设置改成如下设置：
define('WP_DEBUG', true);
define('WP_DEBUG_DISPLAY', true);
保存之后，再刷新前台或者后台，就可以看到错误的 log 了。

打开 wp-config.php 文件，将原来的 WP_Debug 设置改成如下设置：

define('WP_DEBUG', true);
define('WP_DEBUG_DISPLAY', false);
define('WP_DEBUG_LOG', true);
然后就可以在 wp-content/debug.log 文件中看到相应的错误信息了。
```

# 13. mysql 
## 13.1. docker 启动
```
docker run -itd --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=**** mysql:5.7.30
```
## 13.2. 创建一个库
```
create database  hope CHARSET=UTF8;
```



# 14. anyproxy使用
## 14.1. 启动anyproxy -i --rule 文件.js: -i是表是抓取https
## 14.2. 注意开启防火墙，和代理设置。



# 15. nodejs
## 15.1. 安装nodejs
    * yum install npm
    * 安装工具n（用于管理npm版本）：npm install -g n
    * 想升级到一个指定的版本，则可以使用n 12.16.0来升级

# 16. ssdb查询命令：
## 16.1. 查看keys：
    1. keys　 '' '' 10　   字符串类型
    
    2. qlist　'' '' 10　　 列表类型
    
    3. hlist　'' '' 10　　 哈希类型
    
    4. zlist  '' '' 10　  有序集合类型





# 17. 防火墙
## 17.1. iptables -I INPUT -p tcp --dport 3000 -j ACCEPT
## 17.2. firewall-cmd --zone=public --add-port=3001/tcp --permanent  
   命令含义: –zone #作用域 –add-port=80/tcp #添加端口，格式为：端口/通讯协议 –permanent #永久生效，没有此参数重启后失效  
   **开启端口后记得重启**  
   **firewall-cmd --reload**







# 18. 阿里云
* 阿里云 查看公网ip：curl httpbin.org/ip






# 19. 搜索技巧（google）
## 19.1. "空格-号"排除关键词
```
  apple -iphone -ipad
```
## 19.2. 英文双引号精确搜索
## 19.3. or 多个关键词搜索
## 19.4. *号模糊匹配
## 19.5. filetype:pdf ppt doc 指定文件类型搜索
## 19.6. site:网站 对指定网站进行搜索
## 19.7. inurl:（表示其中一个包含）或者allinurl（表示后续都要包含）: 
```
  电影 inurl:movie
```
## 19.8. intitle: allintitle:在标题中进行搜索
## 19.9. 




# 20. 代理总结：
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


[返回上一级](../../README.md)
