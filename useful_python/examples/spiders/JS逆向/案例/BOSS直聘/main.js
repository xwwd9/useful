

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

        // console.log(res)

        path.replaceWith(t.stringLiteral(res))

    },
});



// let { code } = generator(ast)
// code = code.replace(/!!\[\]/g, 'true').replace(/!\[\]/g, 'false')
// fs.writeFile('./result1.js', code, function (err) {
//     if (err) console.error(err);
//     console.log('数据写入的数据');
//     console.log('-------------------');
// });


traverse(ast, {
    VariableDeclaration(path){
        let node = path.node

        // 第一步 找到var _0xb20cd3 = {};这样的变量
        if(node.declarations.length !== 1)
            return;
        let declara = node.declarations[0];
        if(!t.isObjectExpression(declara.init) || declara.init.properties.length !== 0)
            return;
        // 获取到_0xb20cd3的变量名字
        let object_name = declara.id.name;

        // 获取父节点为函数的节点
        let start_fun_path = path.getFunctionParent();
        // let fun_bodys = start_fun_path.node.body.body;




        // 遍历整个函数，找到对应的语句直接替换
        // console.log(start_fun_path)
        if(start_fun_path){
            start_fun_path.traverse({
                ExpressionStatement(path){
                let node = path.node
                if(!t.isAssignmentExpression(node.expression))
                    return

                    // console.log("okkk")

                let exp = node.expression
                    if(t.isFunctionExpression(exp.right)){


                        if(!t.isMemberExpression(exp.left) || !t.isFunctionExpression(exp.right) || !t.isIdentifier(exp.left.object) || exp.left.object.name !== object_name)
                            return
                        // 当前节点确定为一个函数赋值表达式,确定替换体
                        let property_name = exp.left.property.value;
                        let retStmt = exp.right.body.body[0] // 替换体





                        // 将满足条件的语句替换
                        start_fun_path.traverse({
                             CallExpression: function (_path) {

                                if (!t.isMemberExpression(_path.node.callee)) return

                                 if(_path.node.callee.property.value !== property_name)
                                     return
                                let node = _path.node.callee
                                if (!t.isIdentifier(node.object)) return
                                let args = _path.node.arguments // 调用传入的参数

                                if (t.isBinaryExpression(retStmt.argument) && args.length === 2) {
                                    _path.replaceWith(t.binaryExpression(retStmt.argument.operator, args[0], args[1]))
                                }
                                if (t.isLogicalExpression(retStmt.argument) && args.length === 2) {
                                    _path.replaceWith(t.logicalExpression(retStmt.argument.operator, args[0], args[1]))
                                }
                                if (t.isCallExpression(retStmt.argument) && t.isIdentifier(retStmt.argument.callee)) {
                                    // console.log(_path.toString())
                                    _path.replaceWith(t.callExpression(args[0], args.slice(1)))
                                }
                            }
                        })
                    }

                    if(t.isMemberExpression(exp.left)){
                        if(!t.isMemberExpression(exp.left) || !t.isStringLiteral(exp.right) || exp.left.object.name !== object_name)
                        return

                    // 当前节点确定为一个函数赋值表达式,确定替换体
                    //     console.log(exp.right.property)
                    let property_name = exp.left.property.value;
                    let retStmt = exp.right.value // 替换体

                     start_fun_path.traverse({
                         MemberExpression(_path){
                             let node = path.node

                            if(!t.isStringLiteral(node.property) || t.property.value !== property_name)
                                return

                             _path.replaceWith(t.stringLiteral(retStmt))
                         }
                     })

                    }


                path.remove()
            },

        })
        }


        // path.stop()

    },


})


let { code } = generator(ast)
code = code.replace(/!!\[\]/g, 'true').replace(/!\[\]/g, 'false')
fs.writeFile('./result2.js', code, function (err) {
    if (err) console.error(err);
    console.log('数据写入的数据');
    console.log('-------------------');
});
