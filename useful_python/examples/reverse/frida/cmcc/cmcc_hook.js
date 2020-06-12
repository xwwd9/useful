function checkrequestId() {
    Java.perform(function () {
        var class_b_b_d = Java.use("com.cmcc.dependency.b.b.d")

        class_b_b_d.i.implementation = function (nVar) {
            console.log(nVar)
            // {cityCode=111, deviceType=101, ext3=4G, imei=0ZUohZhsuzVz2xyJkowdzQ==, loginPhoneNumber=18200525580, mobileBrand=google, mobileSdkVersion=27, mobileSystemVersion=8.1.0, mobileTime=1591686905916, mobileType=Nexus 6P, moduleId=DynamicLoginActivity, operation=register, phoneNumber=18200525580, service=esb, staPhoneNumber=18200525580, userAgent=android8.1.0_googleNexus 6P_3.6.6, versionCode=62}
        }
    })
}

function callback(){

    Java.perform(function () {

        Java.openClassFile("/data/local/tmp/r0gson.dex").load();
        const gson = Java.use('com.r0ysue.gson.Gson');


        var clazz = Java.use("com.cmcc.dependency.b.k")



        // clazz.a.overload('java.lang.String').implementation = function (a) {
        //     console.log(a)
        //     printStack("10")
        // }

        // ((ac) response.body()).string()
        // clazz.onResponse.implementation = function (a, b) {
        //     console.log(a, b, gson.$new().toJson(b))
        //     console.log("******")
        //     this.onResponse(a, b)
        // }



        var clazz1 = Java.use("com.cmcc.dependency.b.h")
        // clazz1.a.overload('java.lang.String',  'boolean').implementation = function(a, b){
        //     console.log("****")
        //     printStack("9")
        //     console.log(a, b)
        //     this.a(a, b)
        // }

        var decoder = Java.use("com.cmcc.dependency.b.b.d")


        // clazz1.a.overload('java.lang.String',  'java.lang.String').implementation = function(a, b){
        //     // var temp1 = gson.$new().toJson(a)
        //     var content = JSON.parse(a);
        //     console.log(content.content, "ccc");
        //     // console.log("clazz.b(i, barry) = ", decoder.a(0, content.c));
        //     // console.log("b(str) = ", this.b(a));
        //     console.log("decoder.a(str,str) = ", decoder.a("a7e00fbd5d28129f", content.content));
        //     this.a(a, b)
        // }

        decoder.a.overload('java.lang.String',  'java.lang.String').implementation = function(a, b){
            console.log("***", a, b)
            var ret = this.a(a, b)
            console.log("ret = ", ret)
            return ret
        }


    })
}




function printStack(name) {
    Java.perform(function () {
        var Exception = Java.use("java.lang.Exception");
        var ins = Exception.$new("Exception");
        var straces = ins.getStackTrace();
        if (straces != undefined && straces != null) {
            var strace = straces.toString();
            var replaceStr = strace.replace(/,/g, "\\n");
            console.log("=============================" + name + " Stack strat=======================");
            console.log(replaceStr);
            console.log("=============================" + name + " Stack end=======================\r\n");
            Exception.$dispose();
        }
    });
}


// frida -U zz.dela.cmcc.traffic -l cmcc_hook.js
setImmediate(callback)

