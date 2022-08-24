from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet, basename="products")
router.register(r'carts', views.CartViewSet, basename="carts")
router.register(r'productcart', views.ProductCartViewSet, basename="productcart")
router.register(r'(?P<customer_id>[0-9a-f-]+)/checkorder', views.CheckOrderViewSet, basename="orders")
router.register(r'customer', views.CustomerViewSet, basename="customer")


urlpatterns = [
    path('', include(router.urls))
]


