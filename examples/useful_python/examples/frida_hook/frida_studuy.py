import sys

import frida


def on_message(message, data):
    if message['type'] == 'send':

        print(" {0}".format(message['payload']))
    else:
        print(message)


thread_backtracer = """
//打印lib线程调用的堆栈，显示堆栈地址成功，map名字失败
Java.perform(function(){

    var f = Module.findExportByName('libcrackme.so', 'Java_com_yaotong_crackme_MainActivity_securityCheck');
    
    Interceptor.attach(f, {
        onEnter: function(args){
            console.log(Thread.backtrace(this.context, Backtracer.ACCURATE))
            console.log(Thread.backtrace(this.context, Backtracer.ACCURATE).map(DebugSymbol.fromaddress))
        }
    })
    



});


"""

if __name__ == '__main__':
    process = frida.get_device_manager().enumerate_devices()[-1].attach(
        "com.yaotong.crackme")
    script = process.create_script(thread_backtracer)
    script.on('message', on_message)
    script.load()
    sys.stdin.read()
