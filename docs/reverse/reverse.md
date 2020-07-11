[返回上一级](../../README.md)

# 连接夜神模拟器
adb connect 127.0.0.1:62001


# 查看安卓当前activity
adb shell dumpsys window windows | grep mFocusedApp



# 脱360壳
* 查看.so中函数名 nm libart.so |grep OpenMemory
    ```
        # 提取libart.so文件
        # OpenMemory第一个参数为指向dex文件的指针，因此hook OpenMemory函数，读取第一个参数作为dump起始地址，根据dex文件格式，0x20偏移处为dex的长度，进而dump出整个dex文件。
        adb pull /system/lib/libart.so
        oppo libart.so 中 OpenMemory名字
        32位（一般用这个）：_ZN3art7DexFile10OpenMemoryEPKhjRKNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEjPNS_6MemMapEPKNS_10OatDexFileEPS9_
        64位：_ZN3art7DexFile10OpenMemoryEPKhmRKNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEjPNS_6MemMapEPKNS_10OatDexFileEPS9_
  
        Huawei 6p 8.0 OpenCommon
        _ZN3art7DexFile10OpenCommonEPKhjRKNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEjPKNS_10OatDexFileEbbPS9_PNS0_12VerifyResultE
            
    ```
* dump出来的壳需要放在/data/data/包名/ 下


# dex转smail
*  java -jar baksmali.jar disassemble -o ./a/ 5904.dex
    


# 通过adb上传文件

# dex转smail
*  java -jar baksmali.jar disassemble -o ./a/ 5904.dex
    
前可能会提示read-only
```
重新挂载mount -o remount -w 目录
mount -o remount -w /data
adb push frida-server /data/frida_server 
```

# [frida-server下载地址](https://github.com/frida/frida/releases)


# 上传运行frida-server
1. 直接adb push基本上不成功，adb root也不成功
2. 先将软件通过奇兔刷机上传到手机上
3. 上传的目录用adb shell进去大概是/mnt/sdcard/data/frida_server
4. 再将frida_server 复制到/data/local/tmp/frida-server下
5. 然后运行 adb shell "/data/local/tmp/frida-server &"



# android studio 设置Java为1.8
* File -> Project Structure -> Modules，将如下最后两个勾选1.8的选项

* 修改build.gradle中为1.8

* 光标放到错误的地方，直接点击出设置，然后设置1.8


# xposed模块使用

* 创建工程
    * 创建工程在app目录下的gradle中添加配置如下
        ```
        dependencies {
            compileOnly 'de.robv.android.xposed:api:82'
            compileOnly 'de.robv.android.xposed:api:82:sources'
            ......
        }
        ```
      dependencies 表是项目依赖项，compileOnly表示只在编译时有效，不会参与打包，后边82表示版本
     
    * 然后在Manifest.xml中的<application/>中添加
        ```
            <meta-data
                android:name="xposedmodule"
                android:value="true" />
            <meta-data
                android:name="xposeddescription"
                android:value="myhook" />
            <meta-data
                android:name="xposedminversion"
                android:value="82" />
        ```
    分别表示这个是一个xposed模块， 描述是myhook ，支持的最小xposed版本是82
    
    * 在assets目录下新建一个名为xposed_init的文件，并将hook的类写入该文件中，如有多个类，则每行写一个，如下。
        ```
        xxx.xxx.myhook1
        xxx.xxx.myhook2
        ```
    assets目录默认是没有的，可以手动创建，或者选择Android模式，右键点击new->Folder->Assets Folder



# frida笔记
* 启动或附加到程序
```
    # 启动并附加
    device = frida.get_usb_device()
    pid = device.spawn(["com.roysue.demo02"])
    device.resume(pid)
    session = device.attach(pid)

    # 直接附加到
    session = frida.get_usb_device().attach('com.tencent.mm')
```

* 加载启动脚本
```
    # 通过文件的方式加载启动
    with open("s1.js") as f:
        script = session.create_script(f.read())
    script.load()

    # 直接传入js字符串
    script = process.create_script(native_hook_code)
    script.load()
```


* 定位类
```
    my_class = Java.use("com.roysue.demo02.MainActivity");
```
* 更改方法实现
```
    直接重写一个类中的函数
    my_class.fun.implementation = function(x,y){}
    有重载的情况写一个函数
    my_class.fun.overload('int', 'int').implementation
```

* 新建一个变量
```
    新建一个String
    var newString = Java.use("java.lang.String").$new("MYTESTSTRING2");
```

* 打印堆栈
```
    console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()));
```

* 调用函数或者设置变量    
```

    # 静态函数的调用
    clazz = Java.use("xxx.xxx.xxx")
    clazz.static_fun()
    # 静态变量直接设置结果
    clazz.static_bool_var.value = true;
    

    # 先是找到实列，然后在回调中写逻辑，有多少个实列就会调用多少次，可以再找到的时候调用隐藏函数.
    Java.choose("com.r0ysue.a0512demo02.MainActivity",{
            onMatch : function(instance){
                console.log("found instance :"+ instance);
                // 设置成员变量
                instance.bool_var.value = true ;
                // 调用实列函数
                console.log("Result of scerect func:"+instance.secret());
                // 调用成员变量（类成员和方法重名的时候需要在前面加下滑线_，表明是成员变量
                instance._same_name_bool_var.value = true ;
        },
            onComplete : function(){
                console.log("Search Completed!")
            }
        })

    
    # 调用构造函数
    Java.use("com.tlamb96.kgbmessenger.b.a").$init.implementation = ...
    
    # new一个对象和析构一个对象
    var ins = Exception.$new("Exception");
    Exception.$dispose();
```

* 内部类的hook
```
    # 可以查看smail，遭到$符号后边的名字，然后hook
    Java.use("com.example.androiddemo.Activity.FridaActivity4$InnerClasses").check1.implementation = function(){return true;}
```


* 注意传参
```
    可用以下变为字符串
    x.toString()
```

* 发送消息和回调
```
    js中
    send(string_to_send); // send data to python code
    recv(function (received_json_object) {
        string_to_recv = received_json_object.my_data
        console.log("string_to_recv: " + string_to_recv);
    }).wait();

    python中
    def my_message_handler(message, payload):
        print(message)
        print(payload)
        script.post({"my_data": data}) 
    
    script.on("message", my_message_handler)
```

* 打印堆栈
```

    # 一行代码打印调用堆栈
    console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Throwable").$new()));
    # 或者
    function printStack(name) {
    Java.perform(function () {
        var Exception = Java.use("java.lang.Exception");
        var ins = Exception.$new("Exception");
        var straces = ins.getStackTrace();
        if (straces != undefined && straces != null) {
            var strace = straces.toString();
            var replaceStr = strace.replace(/,/g, "\\n");
            console.log("=============================" + name + " Stack strat=======================");
            console.log(replaceStr);
            console.log("=============================" + name + " Stack end=======================\r\n");
            Exception.$dispose();
        }
    });
}   
```


* frida 常用函数
```
    # byte转String
    function byte2string(array){
        var result = "";
        for(var i = 0; i < array.length; ++i){
            result+= (String.fromCharCode(array[i]));
        }
       return result;
    }


    # 将String转换为Json对象然后取值
    var content = JSON.parse(a)
    console.log(content.c, "ccc")


    # 将object转换为一个json进行输出
    Java.openClassFile("/data/local/tmp/r0gson.dex").load();
    const gson = Java.use('com.r0ysue.gson.Gson');
    console.log(gson.$new().toJson(ret))


```


* frida js 编写自动补全
```
    git clone https://github.com/k3v1n1990s/frida-agent-example.git 后npm安装
    或者直接用package.json安装，将node_modules文件夹拷贝到工程最外边
```


* frida使用
```
    查看进程包名
    frida-ps -U | grep xx.xx.xx

    spawn启动js文件
    （肯能会启动太快，找不到实列变量）
    frida -U -f xx.xx.xx -l a.js

    attach启动js文件
    frida -U xx.xx.xx -l a.js

```



# objection使用
* 查看so函数
```
    memory list exports  **.so 
    # 导出到json文件
    memroy list exports **.so --json a.txt
```
* 查看堆上实列
```
    android heap search instance 包名.类名 

    # 有了实列handle id可以直接调用实列中的函数
    # 没有重载的情况
    android heap execute handle_id 函数
    # 有重载的情况
    android heap evalute handle_id
    然后在控制台写js代码调用函数
```

* 查看当前activates
```
    # 列出当前程序活动中的activities，都有哪些页面
    android hooking list activities
    # 直接启动一个activity,相当于直接去到一个页面
    android intent lanuch_activity 上个命令列出来的东西
    # 查看当前hook的class
    android hooking list classes
    android hooking search classname
    # 查看方法
    android hooking search methods name
    # 生成hook方法
    android hooking generate simple 包名.类名.方法
```


```
    # hook到app
    objection -g com.r0ysue.a0512demo02  explore
    # 通过类名查找
    android hooking search classes MainActi
    # 然后具体查看类中的方法
    android hooking watch class com.r0ysue.a0512demo02.MainActivity --dump-args --dump-backtrace --dump-return
    # 查看具体的一个方法,调用的时候都会被打印
    android hooking watch class_method com.r0ysue.a0512demo02.MainActivity.fun --dump-args --dump-backtrac
e --dump-return

```

* 加载插件
```
    进入objection REPL 然后： plugin load 插件路径 
```



# ida pro笔记

```
    1. shift + f12:打开字符串窗口
    2. vxx的这种变量上按y，改为  JNIEnv*  就行了
    3. 是个函数调用，点击右键，再点击Force call type可以查看参数
```



# 技巧
* 通过file可以查看文件类型

* 解压ab文件
```
    java -jar ade.jar unpack 1.ab 1.tar 
```

* 连接夜神模拟器
```
    adb connect 127.0.0.1:21503
```

* 通过adb输入input
```
    adb shell input text "ok"
```

* JNI动态注册
```
     jint RegisterNatives(jclass clazz, const JNINativeMethod* methods, jint nMethods)
    
    第一个参数：需要注册native函数的上层Java类
    
    第二个参数：注册的方法结构体信息
    这里当然是重点看第二个参数，这里当然也需要知道方法结构体信息：
    typedef struct {
        const char* name;
        const char* signature;
        void*       fnPtr;
    } JNINativeMethod;
    结构体包含三部分分别是：方法名、方法的签名、对应的native函数地址
    如下就是一个结构体
    static JNINativeMethod getMethods[] = {
        {"getRandomNum","()I",(void*)get_random_num},
    };
    
    第三个参数：需要注册的方法个数
```

* jni编译的so中查看函数名，有很长一串名字，这个是没有加extern c， 可用c++flit进行还原


* jin静态注册函数，前2个参数是必填的，一个是env，还有个一个是object


* 逆向搜索关键
```
    # 搜索body中的关键字
    .put("xxx

    
    

```


反射
```
    通过反射可以获取到Java中的类，类成员变量，类函数等，可通过反射操作实列。可编写so，通过反射操作Java。
```



dex

* dex文件格式，0x20偏移处为dex的长度



# nodejs
* nodejs 和 浏览器环境区别
```
1. 内置对象不同
    浏览器环境中提供了 window 全局对象
    NodeJS 环境中的全局对象不叫 window , 叫 global
2. this 默认指向不同
    浏览器环境中全局this默认指向 window
    NodeJS 环境中全局this默认指向空对象 {}
3. API 不同
    浏览器环境中提供了操作节点的 DOM 相关 API 和操作浏览器的 BOM 相关 API
    NodeJS 环境中没有 HTML 节点也没有浏览器, 所以 NodeJS 环境中没有 DOM / BOM
```




# 错误解决



[返回上一级](../../README.md)