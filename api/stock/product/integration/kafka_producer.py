from kafka import KafkaProducer
from stock.settings import BOOTSTRAP_SERVERS
from stock.settings import TOPIC_NAME
import json


class Kafka:
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS)
        self.topic_name = TOPIC_NAME

    def send_message(self, body):
        self.producer.send(self.topic_name, json.dumps(body).encode('utf-8'))
