[返回上一级](../../README.md)


目录：JS逆向/JS混淆测试

* 参考链接
    * https://www.jianshu.com/p/47d9b2a365c5



* 在线代码混淆
    * https://obfuscator.io/

# 混淆环境
* npm install esprima estraverse escodegen -S



# 逆向大纲
* hello world，console.log 混淆解密
* 利用AST去除debugger无限循环



# AST笔记
* 节点含义

    * 可将混淆代码转换成AST树，从而替换节点，达到解密的目的。
    * CallExpression函数对应的AST和源码
    ![avatar](../../../../../docs/imgs/js_ast_tree_hello_word.png)  
        ```
            _0x3137('0x1')
        ```
    * ExpressionStatement对应的源码
        ```
            console[_0x3137('0x1')](_0x3137('0x0'));
        ```
      
    * MemberExpression ：对应下方有object和property，object为对应的变量信息(如name表明对象名称)，property为要读取的属性，property节点下又有value节点表明属性名称
        ```
        //源码
        _0x4e7910["PVc"]
        //对应AST中有object和property
        //AST
        "callee": {
              "type": "MemberExpression",
              "start": 15,
              "end": 31,
              "loc": {
                "start": {
                  "line": 3,
                  "column": 0
                },
                "end": {
                  "line": 3,
                  "column": 16
                }
              },
              "object": {
                "type": "Identifier",
                "start": 15,
                "end": 24,
                "loc": {
                  "start": {
                    "line": 3,
                    "column": 0
                  },
                  "end": {
                    "line": 3,
                    "column": 9
                  },
                  "identifierName": "_0x4e7910"
                },
                "name": "_0x4e7910"
              },
              "property": {
                "type": "StringLiteral",
                "start": 25,
                "end": 30,
                "loc": {
                  "start": {
                    "line": 3,
                    "column": 10
                  },
                  "end": {
                    "line": 3,
                    "column": 15
                  }
                },
                "extra": {
                  "rawValue": "PVc",
                  "raw": "\"PVc\""
                },
                "value": "PVc"
              },
              "computed": true
            },
        ```

    * VariableDeclarator：对应下方有id和init，id为变量信息(其中name表明标量名称)，init为初始化信息
        ```
        
        //源码
        var _0x3f0c99 = arguments
        //AST代码
        Node {
          type: 'VariableDeclarator',
          start: 37288,
          end: 37309,
          loc: SourceLocation {
            start: Position { line: 481, column: 12 },
            end: Position { line: 481, column: 33 }
          },
          id: Node {
            type: 'Identifier',
            start: 37288,
            end: 37297,
            loc: SourceLocation {
              start: [Position],
              end: [Position],
              identifierName: '_0x3f0c99'
            },
            name: '_0x3f0c99'
          },
          init: Node {
            type: 'Identifier',
            start: 37300,
            end: 37309,
            loc: SourceLocation {
              start: [Position],
              end: [Position],
              identifierName: 'arguments'
            },
            name: 'arguments'
          }
        }

        ```
      
    * CallExpression: 中有callee和arguments,callee中如果是Identifier会有name,  
        callee就是括号左边的值，如a\['a'\](),callee就是a\['a'\],是个MemberExpression。
        ```
        //源码
        _0x8787()
        //AST
        "expression": {
              "type": "CallExpression",
              "start": 163,
              "end": 172,
              "loc": {
                "start": {
                  "line": 6,
                  "column": 0
                },
                "end": {
                  "line": 6,
                  "column": 9
                }
              },
              "callee": {
                "type": "Identifier",
                "start": 163,
                "end": 170,
                "loc": {
                  "start": {
                    "line": 6,
                    "column": 0
                  },
                  "end": {
                    "line": 6,
                    "column": 7
                  },
                  "identifierName": "_0x8787"
                },
                "name": "_0x8787"
              },
              "arguments": []
            }
        ```
      
    * NumericLiteral和StringLiteral：
        ```
        // 对于，16进制转换成人可读的数组和字符串，只需要去掉extra就可以
        // delete path.node.extra
        // 0xa3
        // '\x70\x75\x73\x68'
      
        //AST
        "expression": {
          "type": "NumericLiteral",
          "start": 185,
          "end": 189,
          "loc": {
            "start": {
              "line": 9,
              "column": 0
            },
            "end": {
              "line": 9,
              "column": 4
            }
          },
          "extra": {
            "rawValue": 163,
            "raw": "0xa3"
          },
          "value": 163
        }
      
      
      
      
      
        "expression": {
          "type": "StringLiteral",
          "start": 190,
          "end": 208,
          "loc": {
            "start": {
              "line": 10,
              "column": 0
            },
            "end": {
              "line": 10,
              "column": 18
            }
          },
          "extra": {
            "rawValue": "push",
            "raw": "'\\x70\\x75\\x73\\x68'"
          },
          "value": "push"
        }
        ```
      
    * WhileStatement和IfStatement
        ```
        //源码
        
        while(true){
          
        }
        if(true){
        }
      
        //AST
        {
            "type": "WhileStatement",
            "start": 179,
            "end": 196,
            "loc": {
              "start": {
                "line": 8,
                "column": 0
              },
              "end": {
                "line": 10,
                "column": 1
              }
            },
            "test": {
              "type": "BooleanLiteral",
              "start": 185,
              "end": 189,
              "loc": {
                "start": {
                  "line": 8,
                  "column": 6
                },
                "end": {
                  "line": 8,
                  "column": 10
                }
              },
              "value": true
            },
            "body": {
              "type": "BlockStatement",
              "start": 190,
              "end": 196,
              "loc": {
                "start": {
                  "line": 8,
                  "column": 11
                },
                "end": {
                  "line": 10,
                  "column": 1
                }
              },
              "body": [],
              "directives": []
            },
            "leadingComments": [
              {
                "type": "CommentBlock",
                "value": "*\n * Paste or drop some JavaScript here and explore\n * the syntax tree created by chosen parser.\n * You can use all the cool new features from ES6\n * and even more. Enjoy!\n ",
                "start": 0,
                "end": 177,
                "loc": {
                  "start": {
                    "line": 1,
                    "column": 0
                  },
                  "end": {
                    "line": 6,
                    "column": 3
                  }
                }
              }
            ]
          },
          {
            "type": "IfStatement",
            "start": 200,
            "end": 211,
            "loc": {
              "start": {
                "line": 14,
                "column": 0
              },
              "end": {
                "line": 15,
                "column": 1
              }
            },
            "test": {
              "type": "BooleanLiteral",
              "start": 203,
              "end": 207,
              "loc": {
                "start": {
                  "line": 14,
                  "column": 3
                },
                "end": {
                  "line": 14,
                  "column": 7
                }
              },
              "value": true
            },
            "consequent": {
              "type": "BlockStatement",
              "start": 208,
              "end": 211,
              "loc": {
                "start": {
                  "line": 14,
                  "column": 8
                },
                "end": {
                  "line": 15,
                  "column": 1
                }
              },
              "body": [],
              "directives": []
            },
            "alternate": null
          }

        ```

    * SwitchStatement: 中有个discriminant，就是switch(d)中的d
    
    * ReturnStatement:中有个argument，为返回值
    
* AST小结
    ```
    Esprima 本质上将 js 代码解析成了两大部分：
    
    1. 3 种变量声明（函数、变量和类）
    2. 表达式
  
    其中表达式又被分为了两大类：
    1.关键字组成的 statement，如 IfStatement, ForStatement等，这里面的BlockStatement有些特殊，因为其body又是 StatementListItem，产生递归。
    2.运算语句（赋值、计算之类的操作）组成的 ExpressionStatement
    
  
    利用path.toString()可以将当前AST对应的源码打印出来
  
    ```
  

[返回上一级](../../README.md)