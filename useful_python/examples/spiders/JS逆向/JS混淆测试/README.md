

* 参考链接
    * https://www.jianshu.com/p/47d9b2a365c5



* 在线代码混淆
    * https://obfuscator.io/

# 混淆环境
npm install esprima estraverse escodegen -S




* AST树笔记

    * 可将混淆代码转换成AST树，从而替换节点，达到解密的目的。
    * CallExpression函数对应的AST和源码
    ![avatar](../../../../../docs/js_ast_tree_hello_word.png)  
        ```
            _0x3137('0x1')
        ```
    * ExpressionStatement对应的源码
        ```
            console[_0x3137('0x1')](_0x3137('0x0'));
        ```






* AST小结
    ```
    Esprima 本质上将 js 代码解析成了两大部分：
    
    1. 3 种变量声明（函数、变量和类）
    2. 表达式
  
    其中表达式又被分为了两大类：
    1.关键字组成的 statement，如 IfStatement, ForStatement等，这里面的BlockStatement有些特殊，因为其body又是 StatementListItem，产生递归。
    2.运算语句（赋值、计算之类的操作）组成的 ExpressionStatement
    
    ```