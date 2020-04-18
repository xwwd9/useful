

* Hello World分析
    * Hello World 加密AST树
        ```
        {
            "type": "Program",
            "body": [
                {
                    "type": "VariableDeclaration",
                    "declarations": [
                        {
                            "type": "VariableDeclarator",
                            "id": {
                                "type": "Identifier",
                                "name": "_0x4ed1"
                            },
                            "init": {
                                "type": "ArrayExpression",
                                "elements": [
                                    {
                                        "type": "Literal",
                                        "value": "Hello World!",
                                        "raw": "'Hello\\x20World!'"
                                    },
                                    {
                                        "type": "Literal",
                                        "value": "log",
                                        "raw": "'log'"
                                    }
                                ]
                            }
                        }
                    ],
                    "kind": "var"
                },
                {
                    "type": "ExpressionStatement",
                    "expression": {
                        "type": "CallExpression",
                        "callee": {
                            "type": "FunctionExpression",
                            "id": null,
                            "params": [
                                {
                                    "type": "Identifier",
                                    "name": "_0x1f7841"
                                },
                                {
                                    "type": "Identifier",
                                    "name": "_0x4ed108"
                                }
                            ],
                            "body": {
                                "type": "BlockStatement",
                                "body": [
                                    {
                                        "type": "VariableDeclaration",
                                        "declarations": [
                                            {
                                                "type": "VariableDeclarator",
                                                "id": {
                                                    "type": "Identifier",
                                                    "name": "_0x3137fe"
                                                },
                                                "init": {
                                                    "type": "FunctionExpression",
                                                    "id": null,
                                                    "params": [
                                                        {
                                                            "type": "Identifier",
                                                            "name": "_0x34ae9a"
                                                        }
                                                    ],
                                                    "body": {
                                                        "type": "BlockStatement",
                                                        "body": [
                                                            {
                                                                "type": "WhileStatement",
                                                                "test": {
                                                                    "type": "UpdateExpression",
                                                                    "operator": "--",
                                                                    "argument": {
                                                                        "type": "Identifier",
                                                                        "name": "_0x34ae9a"
                                                                    },
                                                                    "prefix": true
                                                                },
                                                                "body": {
                                                                    "type": "BlockStatement",
                                                                    "body": [
                                                                        {
                                                                            "type": "ExpressionStatement",
                                                                            "expression": {
                                                                                "type": "CallExpression",
                                                                                "callee": {
                                                                                    "type": "MemberExpression",
                                                                                    "computed": true,
                                                                                    "object": {
                                                                                        "type": "Identifier",
                                                                                        "name": "_0x1f7841"
                                                                                    },
                                                                                    "property": {
                                                                                        "type": "Literal",
                                                                                        "value": "push",
                                                                                        "raw": "'push'"
                                                                                    }
                                                                                },
                                                                                "arguments": [
                                                                                    {
                                                                                        "type": "CallExpression",
                                                                                        "callee": {
                                                                                            "type": "MemberExpression",
                                                                                            "computed": true,
                                                                                            "object": {
                                                                                                "type": "Identifier",
                                                                                                "name": "_0x1f7841"
                                                                                            },
                                                                                            "property": {
                                                                                                "type": "Literal",
                                                                                                "value": "shift",
                                                                                                "raw": "'shift'"
                                                                                            }
                                                                                        },
                                                                                        "arguments": []
                                                                                    }
                                                                                ]
                                                                            }
                                                                        }
                                                                    ]
                                                                }
                                                            }
                                                        ]
                                                    },
                                                    "generator": false,
                                                    "expression": false,
                                                    "async": false
                                                }
                                            }
                                        ],
                                        "kind": "var"
                                    },
                                    {
                                        "type": "ExpressionStatement",
                                        "expression": {
                                            "type": "CallExpression",
                                            "callee": {
                                                "type": "Identifier",
                                                "name": "_0x3137fe"
                                            },
                                            "arguments": [
                                                {
                                                    "type": "UpdateExpression",
                                                    "operator": "++",
                                                    "argument": {
                                                        "type": "Identifier",
                                                        "name": "_0x4ed108"
                                                    },
                                                    "prefix": true
                                                }
                                            ]
                                        }
                                    }
                                ]
                            },
                            "generator": false,
                            "expression": false,
                            "async": false
                        },
                        "arguments": [
                            {
                                "type": "Identifier",
                                "name": "_0x4ed1"
                            },
                            {
                                "type": "Literal",
                                "value": 232,
                                "raw": "0xe8"
                            }
                        ]
                    }
                },
                {
                    "type": "VariableDeclaration",
                    "declarations": [
                        {
                            "type": "VariableDeclarator",
                            "id": {
                                "type": "Identifier",
                                "name": "_0x3137"
                            },
                            "init": {
                                "type": "FunctionExpression",
                                "id": null,
                                "params": [
                                    {
                                        "type": "Identifier",
                                        "name": "_0x1f7841"
                                    },
                                    {
                                        "type": "Identifier",
                                        "name": "_0x4ed108"
                                    }
                                ],
                                "body": {
                                    "type": "BlockStatement",
                                    "body": [
                                        {
                                            "type": "ExpressionStatement",
                                            "expression": {
                                                "type": "AssignmentExpression",
                                                "operator": "=",
                                                "left": {
                                                    "type": "Identifier",
                                                    "name": "_0x1f7841"
                                                },
                                                "right": {
                                                    "type": "BinaryExpression",
                                                    "operator": "-",
                                                    "left": {
                                                        "type": "Identifier",
                                                        "name": "_0x1f7841"
                                                    },
                                                    "right": {
                                                        "type": "Literal",
                                                        "value": 0,
                                                        "raw": "0x0"
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "type": "VariableDeclaration",
                                            "declarations": [
                                                {
                                                    "type": "VariableDeclarator",
                                                    "id": {
                                                        "type": "Identifier",
                                                        "name": "_0x3137fe"
                                                    },
                                                    "init": {
                                                        "type": "MemberExpression",
                                                        "computed": true,
                                                        "object": {
                                                            "type": "Identifier",
                                                            "name": "_0x4ed1"
                                                        },
                                                        "property": {
                                                            "type": "Identifier",
                                                            "name": "_0x1f7841"
                                                        }
                                                    }
                                                }
                                            ],
                                            "kind": "var"
                                        },
                                        {
                                            "type": "ReturnStatement",
                                            "argument": {
                                                "type": "Identifier",
                                                "name": "_0x3137fe"
                                            }
                                        }
                                    ]
                                },
                                "generator": false,
                                "expression": false,
                                "async": false
                            }
                        }
                    ],
                    "kind": "var"
                },
                {
                    "type": "FunctionDeclaration",
                    "id": {
                        "type": "Identifier",
                        "name": "hi"
                    },
                    "params": [],
                    "body": {
                        "type": "BlockStatement",
                        "body": [
                            {
                                "type": "ExpressionStatement",
                                "expression": {
                                    "type": "CallExpression",
                                    "callee": {
                                        "type": "MemberExpression",
                                        "computed": true,
                                        "object": {
                                            "type": "Identifier",
                                            "name": "console"
                                        },
                                        "property": {
                                            "type": "CallExpression",
                                            "callee": {
                                                "type": "Identifier",
                                                "name": "_0x3137"
                                            },
                                            "arguments": [
                                                {
                                                    "type": "Literal",
                                                    "value": "0x1",
                                                    "raw": "'0x1'"
                                                }
                                            ]
                                        }
                                    },
                                    "arguments": [
                                        {
                                            "type": "CallExpression",
                                            "callee": {
                                                "type": "Identifier",
                                                "name": "_0x3137"
                                            },
                                            "arguments": [
                                                {
                                                    "type": "Literal",
                                                    "value": "0x0",
                                                    "raw": "'0x0'"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    "generator": false,
                    "expression": false,
                    "async": false
                },
                {
                    "type": "ExpressionStatement",
                    "expression": {
                        "type": "CallExpression",
                        "callee": {
                            "type": "Identifier",
                            "name": "hi"
                        },
                        "arguments": []
                    }
                }
            ],
            "sourceType": "script"
        }
        ```
    * Hello World 加密代码
        ```
        var _0x4ed1 = ['Hello\x20World!', 'log'];
        (function (_0x1f7841, _0x4ed108) {
            var _0x3137fe = function (_0x34ae9a) {
                while (--_0x34ae9a) {
                    _0x1f7841['push'](_0x1f7841['shift']());
                }
            };
            _0x3137fe(++_0x4ed108);
        }(_0x4ed1, 0xe8));
        var _0x3137 = function (_0x1f7841, _0x4ed108) {
            _0x1f7841 = _0x1f7841 - 0x0;
            var _0x3137fe = _0x4ed1[_0x1f7841];
            return _0x3137fe;
        };
        
        function hi() {
            console[_0x3137('0x1')](_0x3137('0x0'));
        }
        
        hi();
        ```
    * Hello World 未加密AST树
        ```
        {
            "type": "Program",
            "body": [
                {
                    "type": "FunctionDeclaration",
                    "id": {
                        "type": "Identifier",
                        "name": "hi"
                    },
                    "params": [],
                    "body": {
                        "type": "BlockStatement",
                        "body": [
                            {
                                "type": "ExpressionStatement",
                                "expression": {
                                    "type": "CallExpression",
                                    "callee": {
                                        "type": "MemberExpression",
                                        "computed": false,
                                        "object": {
                                            "type": "Identifier",
                                            "name": "console"
                                        },
                                        "property": {
                                            "type": "Identifier",
                                            "name": "log"
                                        }
                                    },
                                    "arguments": [
                                        {
                                            "type": "Literal",
                                            "value": "Hello World!",
                                            "raw": "\"Hello World!\""
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    "generator": false,
                    "expression": false,
                    "async": false
                },
                {
                    "type": "ExpressionStatement",
                    "expression": {
                        "type": "CallExpression",
                        "callee": {
                            "type": "Identifier",
                            "name": "hi"
                        },
                        "arguments": []
                    }
                }
            ],
            "sourceType": "script"
        }
        ```
    * Hello World 未加密代码
        ```
        function hi() {
           console.log("Hello World!");
         }
        hi();
        ```