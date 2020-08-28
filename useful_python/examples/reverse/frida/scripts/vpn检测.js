
function main() {
    Java.perform(function () {
        // 直接hook网络api，返回值
        var vpn = Java.use("java.net.NetworkInterface")
        vpn.getName.implementation = function(){

            // console.log(this.getName())
            if(this.getName() == "tun0" || this.getName() == "ppp0"){
                console.log(this.getName())
                return "tun0"
            }
            return "tun0"
        };

        var ConManger = Java.use("android.net.ConnectivityManager")
        ConManger.getNetworkCapabilities.implementation = function(arg){
            var result = this.getNetworkCapabilities(arg)
            console.log("vpn", result, typeof result)
            return null
        }

    })
}


setImmediate(main);
