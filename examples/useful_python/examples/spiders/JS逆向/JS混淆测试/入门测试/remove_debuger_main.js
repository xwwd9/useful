

const esprima = require('esprima');
const fs = require('fs');// 文件读写


var code = fs.readFileSync("./remove_debugger.js", {
    encoding: "utf-8"
});

function isConsoleCall(node) {
    return (node.type === 'DebuggerStatement')
}

function removeCalls(source) {
    const entries = [];
    esprima.parseScript(source, {}, function (node, meta) {
        if (isConsoleCall(node)) {
            entries.push({
                start: meta.start.offset,
                end: meta.end.offset
            });
        }
    });
    entries.sort((a, b) => { return b.end - a.end }).forEach(n => {
        source = source.slice(0, n.start) + source.slice(n.end);
    });
    return source;
}


let ret = removeCalls(code);
console.log(ret);


// var tree = esprima.parseScript(code);
// console.log(JSON.stringify(tree));
// console.log(tree)




