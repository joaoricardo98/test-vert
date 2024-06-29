from django.db.models import Model
from django.db.models.fields import CharField
from django.db.models.fields import DateTimeField
from django.db.models.fields import DecimalField
from django.db.models.fields import PositiveBigIntegerField
from django.utils.timezone import now


class Product(Model):
    CURRENCY_BRAZIL = 'BRL'
    CURRENCIES = (CURRENCY_BRAZIL,)
    CURRENCIES_CHOICES = {CURRENCY_BRAZIL: CURRENCY_BRAZIL}

    id = PositiveBigIntegerField(null=False, primary_key=True, unique=True)
    name = CharField(max_length=255, null=False, blank=False)
    description = CharField(max_length=1024, blank=False, null=False, default='')
    category = CharField(max_length=255, null=False, blank=False)
    price = DecimalField(max_digits=8, decimal_places=2)
    currency = CharField(max_length=3, choices=CURRENCIES_CHOICES)
    stock_quantity = PositiveBigIntegerField()
    stock_record_date = DateTimeField(default=now)
