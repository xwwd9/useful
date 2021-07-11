// frida -U -f com.ss.android.ugc.aweme -l a.js --no-pause
// objection -g com.ss.android.ugc.aweme explore

function main() {
    Java.perform(function () {
        try {
            // var a = Java.use("com.ss.a.b.a")
            // a.b.implementation = function (x) {
            //     console.log(x)
            //     var ret = this.b(x)
            //     console.log(ret)
            //     return ret
            // }

            var rg = Java.use("com.ss.android.c.b.b$a")
            rg.c.implementation = function (x) {

                var content = JSON.parse(x);
                // content.header.clientudid = "e0e0cb45-85c4-4ca9-aaa0-dceb7a4c6b5b";
                // content.header.build_serial = "ENU7N16322360532"
                // content.header.serial_number = "ENU7N16322360532"
                // content.header._gen_time = 1598955531669
                // content.header.openudid = "bfcg64be78aed7be"
                // content.header.mc = "aa:29:97:87:22:11"

                // console.log(content.c, "ccc")
                x = JSON.stringify(content)
                console.log("111",x);
                // console.log("222",this.c(x));

                console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()));
                return this.c(x)
                // return true
            }


            Java.choose("com.ss.android.c.b.b$a",{
            onMatch : function(instance){
                console.log("found instance :"+ instance);

                // console.log("Result of scerect func:"+instance);
        },
            onComplete : function(){
                console.log("Search Completed!")
            }
        })


        } catch (err) {
            res.status(500).json(err.stack)
            res.end()
        }

    })
};


setImmediate(main);

