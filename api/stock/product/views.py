from rest_framework.generics import CreateAPIView
from product.models import Product
from product.serializers import ProductSerializer
from product.integration.kafka_producer import Kafka


class ProductViewSet(CreateAPIView):
    queryset = Product
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        response = super(ProductViewSet, self).create(request, *args, **kwargs)
        if response.status_code == 201:
            Kafka().send_message(request.data)
        return response
