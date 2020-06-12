

function main(){
    Java.perform(function () {


        Java.openClassFile("/data/local/tmp/r0gson.dex").load();
        const gson = Java.use('com.r0ysue.gson.Gson');



        var clazz = Java.use("com.cmcc.dependency.b.e");

        //具体hook到了5个参数的重载函数
        clazz.a.overload('java.lang.String', 'java.lang.String', 'retrofit2.Callback').implementation = function(a, b, c){
            console.log(a, b)
        };
        clazz.a.overload('java.lang.String','java.lang.String', 'java.lang.String',  'com.cmcc.dependency.b.n', 'retrofit2.Callback', 'int', 'int').implementation = function (a, b, c, d, e) {
            console.log(a, b, c)
        };
        clazz.a.overload('java.lang.String','java.lang.String', 'java.lang.String',  'com.cmcc.dependency.b.n', 'retrofit2.Callback').implementation = function (a, b, c, d, e) {
            printStack()
            console.log("*******************************")
            console.log(a, b, c, d, e)
            console.log(e.toString(), "ok")
            this.a(a, b, c, d, e)
        };




        // new Gson().toJson(d.b(str4, str5, nVar2, str6)) hook d.b函数
        var encoder = Java.use("com.cmcc.dependency.b.b.d")

        encoder.b.overload('java.lang.String', 'java.lang.String', 'com.cmcc.dependency.b.n', 'java.lang.String').implementation = function (a, b, c, d){
            console.log("b = ", a, b, c, d)
            return this.b(a, b, c, d)
        }

        encoder.b.overload('com.cmcc.dependency.b.n').implementation = function (n){
            console.log("n = ", n)
            return this.b(n)
        }

        encoder.e.implementation = function (nVar) {
            // console.log("h(nVar) = ", this.h(nVar))
            // console.log("g(nVar) = ", this.g(nVar))
            // console.log("e params = ", nVar)
            // f2328a 为最终加密的第一个参数

            console.log("f2328a = a(0, str) = ", this.a(0, "MBYBDCVnLjKx3veM1zVemcj5iVdZP2VERICwZTR85Ds="), "key")
            console.log("a", "b")

            // console.log("")
            // 加密的参数
            // {cityCode=111, deviceType=101, ext3=4G, imei=0ZUohZhsuzVz2xyJkowdzQ==, loginPhoneNumber=18200156698, mobileBrand=google, mobileSdkVersion=27, mob
// ileSystemVersion=8.1.0, mobileTime=1591687478123, mobileType=Nexus 6P, moduleId=DynamicLoginActivity, operation=register, phoneNumber=18200156698, requestId=
// a6c8d1a2034611e9edf52df60881aba4, service=esb, staPhoneNumber=18200156698, userAgent=android8.1.0_googleNexus 6P_3.6.6, versionCode=62}

            var ret = this.e(nVar)
            console.log("final result = ", ret)
            // console.log(ret)
            // console.log(encoder.d())

            // return ret
        }


        var classAi = Java.use("com.cmcc.dependency.util.ai")

        classAi.a.overload('[B', '[B').implementation = function(a, b){
            var JString = Java.use("java.lang.String");
            var aa = JString.$new(a)
            var bb = JString.$new(b)
            console.log("aa, bb = ", aa, ", ", bb)
            return this.a(a, b)
        }

        classAi.a.overload('[B').implementation = function(b) {

            //b的内容为cityCode=111&deviceType=101&ext3=4G&imei=0ZUohZhsuzVz2xyJkowdzQ==&loginPhoneNumber=18200159906&mobileBrand=google&mobileSdkVersion=27&mobileSystemVe
            // rsion=8.1.0&mobileTime=1591689159344&mobileType=Nexus 6P&moduleId=DynamicLoginActivity&operation=register&phoneNumber=18200159906&requestId=2c506f49051a78f2d
            // c36e75cc9cbc233&service=esb&staPhoneNumber=18200159906&userAgent=android8.1.0_googleNexus 6P_3.6.6&versionCode=62aP!1@)86*%mgFw0&o9dl， 对b的内容进行最终加密

            console.log("")
            console.log("a(0) = ", this.a(0))
            var ret = this.a(b)
            var JString = Java.use("java.lang.String");
            ret = JString.$new(ret)
            console.log("encoded = ", ret)
            return this.a(b)
            // var JString = Java.use("java.lang.String");
            // b = JString.$new(b)
            // // var result = utilArray.toString(b)
            // console.log("bytes = ", b)
            // // console.log("json = ",  gson.$new().toJson(b))
            //
            //
            // // console.log("a([B) = ", this.a(b))
            // console.log("bj.cw() = ", Java.use("com.cmcc.dependency.util.bj").cw())
            // console.log("a(0) = ", this.a(0))

        }


        // hook 查看requestId的md5加密
        // var class_b_b_d = Java.use("com.cmcc.dependency.b.b.d")
        // class_b_b_d.i.implementation = function (nVar) {
        //     console.log(nVar)
        //     this.i(nVar)
        // }



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


setImmediate(main);



