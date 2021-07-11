function hook_dev() {
    try {
        init_dev();
        //imei
        TelephonyManager = Java.use("android.telephony.TelephonyManager");
        TelephonyManager.getDeviceId.overload().implementation = function () {

            ret = this.getDeviceId();
            console.log("getDeviceId before:", ret);
            ret = deviceid;
            return ret;
        }
        //imsi
        TelephonyManager.getSubscriberId.overload().implementation = function () {

            ret = this.getSubscriberId();
            console.log("getSubscriberId before:", ret);
            ret = deviceid;
            return ret;
        }

        //android_id
        Secure = Java.use("android.provider.Settings$Secure");
        Secure.getString.overload('android.content.ContentResolver', 'java.lang.String').implementation = function (resolver, setting) {

            ret = this.getString(resolver, setting);
            if (setting == "android_id") {
                ret = android_id;
            }

            return ret;
        }


        SystemProperties = Java.use("android.os.SystemProperties");
        SystemProperties.get.overload('java.lang.String', 'java.lang.String').implementation = function (property, setting) {
            console.log("key:", property);
            ret = this.get(property, setting);
            if (property == "ro.product.brand") {
                ret = brand;
            } else if (property == "ro.product.model") {
                ret = model;
            } else if (property == "ro.serialno") {
                ret = searial;
            }
            return ret;
        }

        Build = Java.use("android.os.Build");
        if (Build.SERIAL != undefined)
            Build.SERIAL.value = searial;

        if (Build.BOARD != undefined)
            Build.BOARD.value = board;
        if (Build.BRAND != undefined)
            Build.BRAND.value = brand;
        if (Build.DEVICE != undefined)
            Build.DEVICE.value = device;
        if (Build.MANUFACTURER != undefined)
            Build.MANUFACTURER.value = device;
        if (Build.MODEL != undefined)
            Build.MODEL.value = model;
        if (Build.PROCUCT != undefined)
            Build.PROCUCT.value = product;
        if (Build.VERSION.value.RELEASE != undefined)
            Build.VERSION.value.RELEASE.value = "9.0";
    } catch (e) {

        console.log("JSException:", e);
    }
}