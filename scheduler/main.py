import json

import config
from api import StockAPI
from kafka import KafkaConsumer
from logger import Logger
from models import Product

log = Logger('app')


def run():
    api = StockAPI()
    consumer = KafkaConsumer(
        config.TOPIC_NAME,
        bootstrap_servers=config.BOOTSTRAP_SERVERS,
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    )
    log.info('starting consume')
    for msg in consumer:
        log.info('message received')
        log.info(msg.value)

        product = Product()
        product.fill_from_topic(msg.value)

        log.info('send product to API')
        api.send_product(product)


if __name__ == '__main__':
    run()
