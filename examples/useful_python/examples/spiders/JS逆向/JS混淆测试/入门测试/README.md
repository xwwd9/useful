

npm install esprima estraverse escodegen -S

hello_demo.js:混淆的js文件
hello_main.js：hello_demo.js 生产AST树，将AST树中的内容替换翻译。

mix.js:混淆的js文件
main.js：生产AST树，将AST树中的内容替换翻译。


remove_debuger_main.js: 去除混淆代码中的debugger语句
remove_debugger.js: debuger混淆文件


