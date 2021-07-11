//frida -U -f com.ss.android.ugc.aweme -l c.js --no-pause

function main() {
    Java.perform(function () {

        // var serialNo = "ENU7N42454434999";
        var rom = "EMUI-5023456";

        var module = "PCLM10";
        var rom_version = "OPM7.184206.222";
        var FINGERPRINT = "google/angler/angler:8.1.0/OPM7.184206.222/5023456:user/release-keys";
        var device_manufacturer = "OPPO";

        var serialNo = "32407dcdeed80";
        var IMEI = "376339673888788";
        var imsi = "";
        var mc = "33:15:bb:45:5a:42";
        var androidId = "c06e1c5c0bb51eb0";
        var udid = "718185715550958";

        var Build = Java.use("android.os.Build");
        // var Version = Java.use("android.os.Build.VERSION");
        Build.SERIAL.value = serialNo;
        Build.ID.value = rom_version;
        Build.FINGERPRINT.value = FINGERPRINT;
        Build.DISPLAY.value = rom_version
        Build.MODEL.value = module
        Build.MANUFACTURER.value = device_manufacturer

        console.log("SERIAL******", Build.SERIAL.value);
        console.log("HARDWARE******", Build.HARDWARE.value);
        console.log("HOST******", Build.HOST.value);
        console.log("PRODUCT******", Build.PRODUCT.value);
        console.log("TIME*d*****", Build.TIME.value);
        console.log("MODEL******", Build.MODEL.value);
        console.log("MANUFACTURER******", Build.MANUFACTURER.value);
        console.log("BOARD******", Build.BOARD.value);
        console.log("ID******", Build.ID.value);
        console.log("FINGERPRINT******", Build.FINGERPRINT.value);
        console.log("TYPE******", Build.DISPLAY.value);
        console.log("BOOTLOADER******", Build.BOOTLOADER.value);
        console.log("TYPE******", Build.DISPLAY.value);
        console.log("RADIO******", Build.BOARD.value);
        // console.log("RADIO******", Build.BOARD.value);
        // console.log("Version******", Build.VERSION.value.RELEASE);

        // var Build2 = Java.use("android.os.Build");
        // console.log("asdfasdf***", Build2.SERIAL.value)

        var TelephonyManager = Java.use("android.telephony.TelephonyManager");

        //IMEI hook
        TelephonyManager.getDeviceId.overload().implementation = function () {
            var temp1 = this.getDeviceId();
            console.log("[*]Called - getDeviceId()");
            console.log("real IMEI: " + IMEI);
            return IMEI;
        };

        // muti IMEI
        TelephonyManager.getDeviceId.overload('int').implementation = function (p) {
            console.log("[*]Called - getDeviceId(int) param is" + p);
            var temp = this.getDeviceId(p);
            console.log("real IMEI " + p + ": " + temp);
            return IMEI;
        };


        //IMSI hook
        TelephonyManager.getSimSerialNumber.overload().implementation = function () {
            var temp2 = this.getSimSerialNumber();
            console.log("[*]Called - getSimSerialNumber(String)");
            console.log("real IMSI: " + temp2);
            return imsi;
        };
        //////////////////////////////////////
        //ANDOID_ID hook
        var Secure = Java.use("android.provider.Settings$Secure");
        Secure.getString.implementation = function (p1, p2) {
            if (p2.indexOf("android_id") < 0) return this.getString(p1, p2);
            console.log("[*]Called - get android_ID, param is:" + p2);
            var temp = this.getString(p1, p2);
            console.log("real Android_ID: " + temp, androidId);
            return androidId
        }



        //android的hidden API，需要通过反射调用
        var SP = Java.use("android.os.SystemProperties");
        SP.get.overload('java.lang.String').implementation = function (p1) {
            var tmp = this.get(p1);
            console.log("[*]SP" + p1 + " : " + tmp);
            return "67676787676"
            // return tmp;
        };

        SP.get.overload('java.lang.String', 'java.lang.String').implementation = function (p1, p2) {
            var tmp = this.get(p1, p2)
            console.log("[*]SP" + p1 + "," + p2 + " : " + tmp);
            return "67676787676"
            // return tmp;
        };







        // hook MAC
        var wifi = Java.use("android.net.wifi.WifiInfo");
        wifi.getMacAddress.implementation = function () {
            var tmp = this.getMacAddress();
            console.log("[*]real MAC: " + tmp);
            return mc;
            // return tmp;
        }


        //douyin hook
        var rg = Java.use("com.ss.android.c.b.b$a");
        rg.c.implementation = function (x) {

            var content = JSON.parse(x);
            content.header.build_serial = serialNo;
            content.header.rom = rom;
            // content.header.serial_number = serialNo;
            // content.header.mc = mc;
            // content.header.udid = udid;
            // content.header.openudid = androidId;


            x = JSON.stringify(content);
            console.log("111",x);
            console.log("222",this.c(x));
            console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()));
            return this.c(x)
        };

        var se = Java.use("com.ss.android.c.b.b.a")
        se.d.implementation = function () {
            var temp = this.d()
            console.log("se", temp)
            return serialNo
        }

        se.e.implementation = function () {
            var temp = this.e()
            console.log("serial_number", temp)
            return temp
        }

        se.b.implementation = function () {
            var temp = this.b()
            console.log("androidid", temp)
            return androidId
        }







    })
}


setImmediate(main);
