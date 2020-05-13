#!/usr/bin/env python
import pika

username = 'fs'  # 指定远程rabbitmq的用户名密码
pwd = '***'
user_pwd = pika.PlainCredentials(username, pwd)
connection = pika.BlockingConnection(pika.ConnectionParameters(host='101.200.73.195', port=5010, credentials=user_pwd, virtual_host="my_rabbitmq"))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


a = channel.consume(queue='hello', auto_ack=True)
for i in a:
    print(i)
print(a)
channel.basic_consume(on_message_callback=callback,queue='hello', auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()