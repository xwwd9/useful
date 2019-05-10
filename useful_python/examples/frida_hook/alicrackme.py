#!/usr/bin/env python
# coding=utf-8
from __future__ import print_function
import frida, sys

native_hook_code = """
Java.perform(function(){
    send("Running Script");
 
    var securityCheck = undefined;
    exports = Module.enumerateExportsSync("libcrackme.so");
    for(i=0; i<exports.length; i++){
        if(exports[i].name == "Java_com_yaotong_crackme_MainActivity_securityCheck"){
            securityCheck = exports[i].address;
            send("securityCheck is at " + securityCheck);
            break;
        }
    }
 
    Interceptor.attach(securityCheck,{
        onEnter: function(args){
            send("key is: " + Memory.readUtf8String(Memory.readPointer(securityCheck.sub(0x11a8).add(0x628c))));
            
            //console.log(securityCheck.sub(0x11a8).add(0x628c))
            //console.log(Memory.readCString(ptr(args[2])))
            //console.log(Memory.readCString(args[2]))
            //console.log(Memory.readByteArray(args[2], 10))
            
            var ptr_prompt = args[2];
            Java.perform( function () {
                var String = Java.use("java.lang.String");
                var promt = Java.cast(ptr(ptr_prompt), String);
                //send(promt);
                console.log(promt)
            });
            //send("arg: "+ Memory.readUtf8String(Memory.readPointer(args[2]+676)))
            //send("arg: " + Memory.readUtf8String(Memory.readPointer(securityCheck.sub(0x11a8).add(args[2]))));
            //send("arg: " + Memory.readUtf8String(Memory.readPointer(securityCheck.sub(0x11a8).add(0x628c))));
        }
    });
});
"""

check_hook_code = """
    send("Running Script");
Java.perform(function(){
    MainActivity = Java.use("com.yaotong.crackme.MainActivity");
    MainActivity.securityCheck.implementation = function(v){
        send("securityCheck hooked");
        return true;
    }
});
"""


def on_message(message, data):
    if message['type'] == 'send':

        print(" {0}".format(message['payload']))
    else:
        print(message)


process = frida.get_device_manager().enumerate_devices()[-1].attach(
    "com.yaotong.crackme")
script = process.create_script(native_hook_code)
script.on('message', on_message)
script.load()
sys.stdin.read()
