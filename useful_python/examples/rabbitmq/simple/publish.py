

#!/usr/bin/env python
import pika

username = '***'  # 指定远程rabbitmq的用户名密码
pwd = '***'
user_pwd = pika.PlainCredentials(username, pwd)
connection = pika.BlockingConnection(pika.ConnectionParameters(host='***', port=5010, credentials=user_pwd, virtual_host="my_rabbitmq"))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()