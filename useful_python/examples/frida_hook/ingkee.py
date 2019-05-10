import frida, sys

def on_message(message, data):
    if message['type'] == 'send':
        # print("data = ", data.split(b'\x00')[0].decode())
        print("data = ", data)
        print("[*] {0}".format(message['payload']))
    else:
        print(message)







jscode = """
Java.perform(function () {
    // Function to hook is defined here
    var InkeURLBuilder = Java.use('com.meelive.ingkee.mechanism.http.build.InkeURLBuilder');
    // Whenever button is clicked
    InkeURLBuilder.urlEncryption.implementation = function (v) {
        // Show a message to know that the function got called
        if(v.indexOf('follow') != -1){
            //send(v)
        }
        return this.urlEncryption(v)
    };
    
    
    var secret_a = Java.use('com.meelive.ingkee.mechanism.secret.a');
        
    secret_a.a.overload('java.lang.String').implementation = function(v){
        if(v.indexOf('follow') != -1){

            //send(this.i)
            
            var ret = this.a(v)
            
            send(ret)
            return ret
        }
        else{
            return this.a(v)
        }
        
    }
    
    
    var secret = Module.findExportByName("libsecret.so","Java_com_meelive_ingkee_seven_Secret_encryUrl");
    Interceptor.attach(secret, {
    
            onEnter: function (args) {
                //Memory.protect(args[2], 10, 'rw-')
                //Memory.readUtf8String(args[2], size = 10)
                //Memory.readByteArray(ptr(args[2]), size=10)
                //send('asdfasdf')
                
                var ptr_prompt = args[2];
                Java.perform( function () {
                    var String = Java.use("java.lang.String");
                    var promt = Java.cast(ptr(ptr_prompt), String);
                    //send(promt);
                    console.log(promt)
                });
                
                //console.log(Memory.readCString(ptr(args[1])))
                //console.log(Memory.readUtf8String(args[2]))
                //send("key is: " + Memory.readUtf8String(args[2]));
                //send("key is: " + Memory.readCString(args[2]));
                //console.log(hexdump(args[2], { length: 10, ansi: true }))
            },
            
            onLeave: function (result) {
                //console.log('----------')
                // Show argument 1 (buf), saved during onEnter.
                //numBytes = result.toString();
                //send( Memory.readUtf8String(result));
                //console.log(hexdump(result, { length: 200, ansi: true }))
               // console.log(Memory.readUtf8String(result))
            }
        }

    )
    }
)
"""
process = frida.get_usb_device().attach('com.meelive.ingkee')
script = process.create_script(jscode)
script.on('message', on_message)
print('[*] Running CTF')
script.load()
sys.stdin.read()





