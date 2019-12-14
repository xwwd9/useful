

# 安装appium
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple Appium-Python-Client





# appium配置参数
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


