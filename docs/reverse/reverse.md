
[返回上一级](../../README.md)

# 连接夜神模拟器
adb connect 127.0.0.1:62001


# 查看安卓当前activity
adb shell dumpsys window windows | grep mFocusedApp



# 脱360壳
* 查看.so中函数名 nm libart.so |grep OpenMemory
    ```
        oppo libart.so 中 OpenMemory名字
        32位（一般用这个）：_ZN3art7DexFile10OpenMemoryEPKhjRKNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEjPNS_6MemMapEPKNS_10OatDexFileEPS9_
        64位：_ZN3art7DexFile10OpenMemoryEPKhmRKNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEjPNS_6MemMapEPKNS_10OatDexFileEPS9_
            
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

* 定位类：my_class = Java.use("com.roysue.demo02.MainActivity");
* 更改方法实现：my_class.fun.implementation = function(x,y){}




# 错误解决



[返回上一级](../../README.md)