from pykafka import KafkaClient
from pykafka.simpleconsumer import OffsetType
import logging

logging.getLogger("pykafka.broker").setLevel('ERROR') 

client = KafkaClient(hosts="localhost:9092") 
topic = client.topics["service-calls"] 

consumer = topic.get_balanced_consumer(
    consumer_group = b'pytkafka-test-2',
    auto_commit_enable = False,
    auto_offset_reset=OffsetType.EARLIEST,
    zookeeper_connect = 'localhost:2181'
)

#Print out the messages
for message in consumer:
    if message is not None:
        print(message.value.decode('utf-8'))
