# 单列模式
* 通过模块方式进行单列（因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码）
```
mysingleton.py文件如下代码
class Singleton(object):
    def foo(self):
        pass
singleton = Singleton()
然后其他文件映入
from a import singleton
```
* 使用类装饰器
```
def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton


@Singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


a1 = A(2)
a2 = A(3)
```
* 使用classmethod
```
class Singleton(object):
    _instance_lock = threading.Lock()
    def __init__(self):
        pass
    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance
```
* 基于__new__的方式，件文件中


