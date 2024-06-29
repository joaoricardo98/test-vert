from os import environ

TOPIC_NAME: str = environ['TOPIC_NAME']
BOOTSTRAP_SERVERS: [str] = environ['BOOTSTRAP_SERVERS'].split(',')
STOCK_BASE_URL: str = environ['STOCK_BASE_URL']
