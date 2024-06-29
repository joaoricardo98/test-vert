import json

import requests
from models import Product
from datetime import datetime
import config

import decimal


class StockAPI:
    def __init__(self):
        self.__base_url: str = config.STOCK_BASE_URL

    def __mount_body(self, product: Product) -> dict:
        return {
              'id': product.id,
              'name': product.name,
              'description': product.description,
              'pricing': {
                'amount': float(product.price),
                'currency': product.currency
              },
              'availability': {
                'quantity': product.stock_quantity,
                'timestamp': str(datetime.utcnow())
              },
              'category': product.category
            }

    def send_product(self, product: Product):
        response = requests.post(f'{self.__base_url}/product/', json=self.__mount_body(product))
        if response.status_code != 201:
            raise

