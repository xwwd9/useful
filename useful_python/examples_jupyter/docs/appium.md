

# 安装appium
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple Appium-Python-Client


# 连接夜神模拟器
adb connect 127.0.0.1:62001


# 
adb shell dumpsys window windows | grep mFocusedApp