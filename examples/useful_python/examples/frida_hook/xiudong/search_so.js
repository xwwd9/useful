function test() {
    console.log("Entering")
    var modules = Process.enumerateModules()
    console.log(modules.length)
    for(var i = 0; i<modules.length; i++){
        var module = modules[i]
        var module_name = modules[i].name
        if(module_name.indexOf("wall")>-1)
            console.log(module_name)
        var exports = module.enumerateExports()
        for(var index = 0; index<exports.length; index++){
            var export_name = exports[index].name
            if(export_name.indexOf("restoreString")>-1){
                console.log(module_name, export_name)
            }
        }
    }
}
setImmediate(test);

