from decimal import Decimal


class Product:
    def __init__(self):
        self.id: str = ''
        self.name: str = ''
        self.description: str = ''
        self.price: Decimal = Decimal()
        self.currency: str = ''
        self.stock_quantity: int = 0
        self.category: str = ''

    def fill_from_topic(self, data: dict):
        self.id = data['productId']
        self.name = data['productName']
        self.description = data['productDescription']
        self.price = Decimal(data['price'])
        self.currency: str = data['currency']
        self.stock_quantity: int = data['stockQuantity']
        self.category: str = data['category']

    def __str__(self):
        return f'{self.id} - {self.name} - {self.stock_quantity}'
