// hook 加密前传的参数
// 主要查看函数 com.cmcc.dependency.b.b.d
function hookai() {

    Java.perform(function () {


        Java.openClassFile("/data/local/tmp/r0gson.dex").load();
        const gson = Java.use('com.r0ysue.gson.Gson');

        // // hook到解密参数的前一步
        // var clazz = Java.use("com.cmcc.dependency.util.ai")
        // clazz.a.overload('[B', '[B').implementation = function (a, b) {
        //     console.log("加密key 和 加密参数", byte2string(a), byte2string(b))
        //     return this.a(a, b)
        // }
        //
        // // hook 调用header中a, b参数生成函数
        // var clazz1 = Java.use("com.cmcc.dependency.b.e")
        // clazz1.a.overload().implementation = function () {
        //     //this.a 生成a和b参数
        //     var ret = this.a()
        //     console.log(ret)
        //     return ret
        // }


        // 拦截发送出去的请求，通过postman自己构造，看能post成功不
        // var clazz2 = Java.use("com.cmcc.dependency.b.b.d")
        // clazz2.b.overload('com.cmcc.dependency.b.n').implementation = function (a) {
        //     var ret = this.b(a)
        //
        //     Java.openClassFile("/data/local/tmp/r0gson.dex").load();
        //     const gson = Java.use('com.r0ysue.gson.Gson');
        //     console.log(gson.$new().toJson(ret))
        //     console.log(JSON.stringify(ret))
        //     // return ret
        // }


        // hook 解密参数的地方
        // var decoder = Java.use("com.cmcc.dependency.b.b.d")
        // decoder.a.overload('java.lang.String',  'java.lang.String').implementation = function(a, b){
        //     console.log("***", a, b)
        //     var ret = this.a(a, b)
        //     console.log("ret = ", ret)
        //     return ret
        // }

        // 查看header中phoneNumber生成过程
        var clazz3 = Java.use("com.cmcc.dependency.util.bj")
        console.log("clazz3.t()", clazz3.t())

        // 加密和解密的key，是根据请求的c参数，和返回的c参数生成的
        var clazz4 = Java.use("com.cmcc.dependency.b.b.d")
        console.log("clazz4.a(0, w)", clazz4.a(0, "MBYBDCVnLjKx3veM1zVemcj5iVdZP2VERICwZTR85Ds="))

        // 查看解密密匙的生成，是根据返回的c字段进行解密的




    })

}




function byte2string(array){
    var result = "";
    for(var i = 0; i < array.length; ++i){
        result+= (String.fromCharCode(array[i]));
    }
   return result;
}



// frida -U zz.dela.cmcc.traffic -l cmcc_key_hook.js
setImmediate(hookai)

