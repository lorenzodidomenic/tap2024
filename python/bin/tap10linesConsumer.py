# https://towardsdatascience.com/kafka-python-explained-in-10-lines-of-code-800e3e07dad
import os
from kafka import KafkaConsumer
from json import loads

#dal container ci prendiamo  le varibaili d'ambienete che contengono 
# #il nome del topic , il group id e l offset
topic = os.getenv("KAFKA_TOPIC", "tap")
group_id = os.getenv("GROUP_ID", "my-group")
offset = os.getenv("OFFSET", "latest")
print("Paramters are Topic:%s Group id: %s OFFSET: %s " % (topic, group_id, offset))

#startiamo un consumer passandogli topic, kagka server, id del gruppo, e come decodificare il messaggio
consumer = KafkaConsumer(
     topic,
     bootstrap_servers=['kafkaServer:9092'],
     auto_offset_reset=offset,
     enable_auto_commit=True,
     group_id=group_id,
     value_deserializer=lambda x: loads(x.decode('utf-8')))

#per ogni messaggio lo stampiamo
for message in consumer:
    message = message.value
    print('{} read'.format(message))
