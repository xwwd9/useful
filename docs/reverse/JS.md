[返回上一级](../../README.md)


- [1. 搜索关键字](#1-搜索关键字)
  - [1.1. 通过以jquery为关键字搜索](#11-通过以jquery为关键字搜索)
  - [1.2. 查找拦截器(用户发送请求和接受请求时候的http处理)](#12-查找拦截器用户发送请求和接受请求时候的http处理)
  - [1.3. 对于某些变量赋值搜索不到的，很可能是该赋值是在加密代码中。](#13-对于某些变量赋值搜索不到的很可能是该赋值是在加密代码中)
- [2. 加密总结](#2-加密总结)
  - [2.1. RSA加密](#21-rsa加密)
- [3. 无限debugger](#3-无限debugger)
  - [3.1. 直接添加条件跳过](#31-直接添加条件跳过)
  - [3.2. 直接在控制台中将函数设置为空函数](#32-直接在控制台中将函数设置为空函数)
  - [3.3. 将constructor函数设置为空](#33-将constructor函数设置为空)
- [4. nodejs](#4-nodejs)
  - [4.1. nodejs 和 浏览器环境区别](#41-nodejs-和-浏览器环境区别)
  - [4.2. python 中调用nodejs文件](#42-python-中调用nodejs文件)
- [5. 变量生成的hook](#5-变量生成的hook)
  - [5.1. 简单的直接通过油候脚本hook](#51-简单的直接通过油候脚本hook)
  - [5.2. 需要通过fiddler修改js文件,将如下代码加入js中](#52-需要通过fiddler修改js文件将如下代码加入js中)
- [6. 过程记录](#6-过程记录)
  - [6.1. F12，右键反调试](#61-f12右键反调试)
- [7. chrome 中技巧](#7-chrome-中技巧)
  - [7.1. 在控制台输入copy(变量)，可以直接复制变量。](#71-在控制台输入copy变量可以直接复制变量)
  - [Network中Initiator可以查看发请求的流程，可通过该流程定位打断点。](#network中initiator可以查看发请求的流程可通过该流程定位打断点)
- [8. 模拟登陆相关知识](#8-模拟登陆相关知识)
  - [8.1. 模拟登陆检测网站](#81-模拟登陆检测网站)
- [自执行函数(定义完成后就马上调)](#自执行函数定义完成后就马上调)

# 1. 搜索关键字
## 1.1. 通过以jquery为关键字搜索
```
$("#输入框的id")
$(".输入框的classname")
```
## 1.2. 查找拦截器(用户发送请求和接受请求时候的http处理)
```
    # axios的拦截器
    axios.interceptors
    # 还有其他库的拦截器
```
## 1.3. 对于某些变量赋值搜索不到的，很可能是该赋值是在加密代码中。
```
1. 对于有base64加密的地方，解密后，看变量赋值是不是在其中
2. 对于window.f像这类的赋值，可能被混淆成window['f']或其他
```


# 2. 加密总结
## 2.1. RSA加密
* 一般的rsa加密通常会先声明一个rsa对象
* 本地使用公钥加密即public key
* 通常有Encrypt关键字
* 加密后字符长度为128位或256位


# 3. 无限debugger
## 3.1. 直接添加条件跳过
## 3.2. 直接在控制台中将函数设置为空函数
```
  function tt(){}
  重写之后，点击X关闭f12窗口（切记不要刷新页面，因为刷新的话相当于重新加载一遍，刚才的重写函数也就没了意义），关闭之后再重新打开f12
```
## 3.3. 将constructor函数设置为空
```
  Function.prototype.constructor=function(){};
```


# 4. nodejs
## 4.1. nodejs 和 浏览器环境区别
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
## 4.2. python 中调用nodejs文件
```
  1. 直接使用管道的方式，其中decode.js中有console.log，然后python读取打印出来的值即可。
      nodejs = os.popen('node decode.js ' + ts + '000')
      m = nodejs.read().replace('\n', '') + '丨' + ts
      nodejs.close()
```


# 5. 变量生成的hook
## 5.1. 简单的直接通过油候脚本hook
## 5.2. 需要通过fiddler修改js文件,将如下代码加入js中
```
  Object.defineProperty(_,"*", {})
```



# 6. 过程记录
## 6.1. F12，右键反调试
```
  https://www.aqistudy.cn/historydata/daydata.php?city=%E5%B9%BF%E5%B7%9E&month=202008
  右键可用chrome插件恢复
  1. 在network中点击对应的请求然后右键（Save for Overrides），重写页面文件，保存在source->Overrides中。（需要提前在Overrides中新建一个目录，不然请求右键不会有Save for Overrides
  2. 保存后刷新页面即可看到请求，如果没有多试下其他页面
  3. 然后就是找到ajax的发送和success回调的地方完成解密
```


# 7. chrome 中技巧
## 7.1. 在控制台输入copy(变量)，可以直接复制变量。
## Network中Initiator可以查看发请求的流程，可通过该流程定位打断点。


# 8. 模拟登陆相关知识
## 8.1. [模拟登陆检测网站](https://bot.sannysoft.com/)


# 自执行函数(定义完成后就马上调)
```
  !function () { /* ... */ }();
  ~function () { /* ... */ }();
  -function () { /* ... */ }();
  +function () { /* ... */ }();
  void function () { /* ... */ }();
  (function (){/*...*/}());
  (function (){/*...*/})();
```