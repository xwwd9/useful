#!/usr/bin/env python
# coding=utf-8
from __future__ import print_function
import frida, sys

hook_code = """
Java.perform(function () {

        var SQLiteDatabase = Java.use('com.tencent.wcdb.database.SQLiteDatabase');
        
        SQLiteDatabase.insertWithOnConflict.implementation = function (a, b, c, d) {
            send('onClick');
            console.log(a, b, c, d)
        };
  
    }
     
)
"""



def on_message(message, data):
    if message['type'] == 'send':
        print(" {0}".format(message['payload']))
    else:
        print(message)


process = frida.get_usb_device(1).attach('com.tencent.mm')

# process = frida.get_usb_device(1).attach('com.example.seccon2015.rock_paper_scissors')

script = process.create_script(hook_code)
script.on('message', on_message)
script.load()
sys.stdin.read()
