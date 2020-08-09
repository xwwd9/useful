[返回上一级](../../README.md)


- [1. 搜索关键字](#1-搜索关键字)
  - [1.1. 通过以jquery为关键字搜索](#11-通过以jquery为关键字搜索)
- [2. 加密总结](#2-加密总结)
  - [2.1. RSA加密](#21-rsa加密)
- [3. 无限debugger](#3-无限debugger)
  - [3.1. 直接添加条件跳过](#31-直接添加条件跳过)
  - [3.2. 直接在控制台中将函数设置为空函数](#32-直接在控制台中将函数设置为空函数)
  - [3.3. 将constructor函数设置为空](#33-将constructor函数设置为空)
- [4. nodejs](#4-nodejs)
  - [4.1. nodejs 和 浏览器环境区别](#41-nodejs-和-浏览器环境区别)
- [5. 变量生成的hook](#5-变量生成的hook)
  - [5.1. 简单的直接通过油候脚本hook](#51-简单的直接通过油候脚本hook)
  - [5.2. 需要通过fiddler修改js文件,将如下代码加入js中](#52-需要通过fiddler修改js文件将如下代码加入js中)

# 1. 搜索关键字
## 1.1. 通过以jquery为关键字搜索
```
$("#输入框的id")
$(".输入框的classname")
```
## 查找拦截器(用户发送请求和接受请求时候的http处理)
```
    # axios的拦截器
    axios.interceptors
    # 还有其他库的拦截器
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


# 5. 变量生成的hook
## 5.1. 简单的直接通过油候脚本hook
## 5.2. 需要通过fiddler修改js文件,将如下代码加入js中
```
  Object.defineProperty(_,"*", {})
```



# chrome 中技巧
## 在控制台输入copy(变量)，可以直接复制变量。