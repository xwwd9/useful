[返回上一级](../../README.md)


# appium
* 安装appium
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple Appium-Python-Client
    
* appium配置参数
    ```
    {
      "platformName": "Android",
      //安卓版本号
      "platformVersion": "6",
      //设备名，安卓上可以随便填写
      "deviceName": "127.0.0.1:62001",
      //以下2个分别是app包名和启动入口
      "appPackage": "com.android.settings",
      "appActivity": "com.oppo.settings.SettingsActivity",
      //每回启动是重置命令
      "noReset": true,
      //每回启动是否需要安装一些服务
      "skipServerInstallation": false,
      "skipDeviceInitialization": false
    }
    ```
  
    * 定位元素
     * 可直接通过xpath的属性定位，比如：//*[@text="关注公众号"]

    * 报错集合  
        * appium  Could not proxy command to remote server. Original error: Error: socket hang up 重新安装手机上的appium apk 是由于上回运行资源未释放


# uiautomator2 使用

* 安装插件pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simpl --pre weditor

* 运行python -m  weditor 启动元素查看器



[返回上一级](../../README.md)
