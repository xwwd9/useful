const esprima = require('esprima');// 生成语法树
const estraverse = require('estraverse');// 遍历语法树
const escodegen = require('escodegen');// 语法树转代码
const fs = require('fs');// 文件读写


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

var code = fs.readFileSync("./hello_demo.js", {
    encoding: "utf-8"
});

function decode(ast) {
    estraverse.replace(ast,{
        enter(node) {
            // 判断node节点位置
            if(node.type === 'CallExpression' && node.callee.name === "_0x3137") {
                var res = _0x3137(node.arguments[0].value);
                // console.log(res, "***");
                // 将节点替换
                return {
                    "type": "Literal",
                    "value": res,
                    "raw": "'" + res + "'"
                };
            }
        }
    });
}


//生成AST抽象树
var tree = esprima.parseScript(code);


// console.log(tree);




// let a = JSON.stringify(tree);
// console.log(JSON.parse(a))
// console.log(JSON.stringify(tree))

decode(tree);
code = escodegen.generate(tree);

console.log(code);