from django.contrib import admin
from django.urls import path
from product.views import ProductViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', ProductViewSet.as_view()),
]
