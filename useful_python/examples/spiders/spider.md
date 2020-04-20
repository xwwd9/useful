


* chrome 调试技巧
    * 勾选preservelog，可以查看跳转记录
    
    
    
    
* debugger反调试
    * [资料1](https://segmentfault.com/a/1190000012359015) 
    * [资料2](https://blog.csdn.net/sergiojune/article/details/100681506) 
    * 如果debugger是个函数，可以在控制台直接设置该函数为空 function startDebug() {};
    * 如果debugger是写在多行的，可以通过过条件断点去除。条件断电直接设置false，或者
    * 如果debug在一行，可以替换当前的debug函数。
    
    
    
