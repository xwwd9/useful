

const { decodeFun, decodeFunName} = require('./module');
// 把js源码转成语法树
const parser = require("@babel/parser");
// 遍历语法树中的节点
const traverse = require("@babel/traverse").default;
// 提供对语法树中Node的一系列方法比如判断Node类型，辅助创建Node等
const t = require("@babel/types");
// 根据语法树生成js代码
const generator = require("@babel/generator").default;
// 读写文件
const fs = require('fs');
// 读操作
var js = fs.readFileSync("./security.js", {
    encoding: "utf-8"
});
// 生成树，和esprima的函数基本相同
let ast = parser.parse(js);


traverse(ast,{
    CallExpression(path){
        let node = path.node
        if(!t.isIdentifier(node.callee) && node.callee.name !== decodeFunName)
            return

        if(!t.isStringLiteral(node.arguments[0]))
            return

        let argument = node.arguments[0].value

        let res = decodeFun(argument)

        console.log(res)

        path.replaceWith(t.stringLiteral(res))

    },
});



let { code } = generator(ast)
code = code.replace(/!!\[\]/g, 'true').replace(/!\[\]/g, 'false')
fs.writeFile('./result1.js', code, function (err) {
    if (err) console.error(err);
    console.log('数据写入的数据');
    console.log('-------------------');
});




