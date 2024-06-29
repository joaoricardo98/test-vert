from product.models import Product
from rest_framework import serializers


class PricingSerializer(serializers.ModelSerializer):
    amount = serializers.FloatField(source='price')

    class Meta:
        model = Product
        fields = ['amount', 'currency']


class AvailabilitySerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(source='stock_record_date')
    quantity = serializers.IntegerField(source='stock_quantity')

    class Meta:
        model = Product
        fields = ['quantity', 'timestamp']


class ProductSerializer(serializers.ModelSerializer):
    pricing = PricingSerializer(source='*')
    availability = AvailabilitySerializer(source='*')

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'pricing', 'availability', 'category']
