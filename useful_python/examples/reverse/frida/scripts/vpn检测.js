
function main() {
    Java.perform(function () {
        // 直接hook网络api，返回值
        var vpn = Java.use("java.net.NetworkInterface")
        vpn.getName.implementation = function(){

            console.log(this.getName())
            if(this.getName() == "tun0" || this.getName() == "ppp0"){
                console.log(this.getName())
                return "tun0"
            }
            // console.log("dd")
            // console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()));
            // console.log(this.getName())
            return "tun0"
        }

        //以下需要在apk包中搜索 getNetworkCapabilities 等关键字确定位置
        var vpn3 = Java.use("com.taihebase.activity.utils.SecurityUtil")
        vpn3.hasVpnTransport.implementation = function(){
            return false
        }

    })
}


setImmediate(main);
