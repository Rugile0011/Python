from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSetMixin

from .models import Product, Cart, ProductCart, Order, User
from .serializer import ProductSerializer, CartSerializer, ProductCartSerializer, OrderSerializer, CustomerSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """ A simple ViewSet for viewing products """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """ A simple ViewSet for viewing cart """
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CustomerViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """ A simple ViewSet for viewing customers """
    queryset = User.objects.all()
    serializer_class = CustomerSerializer


class ProductCartViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = ProductCart.objects.all()
    serializer_class = ProductCartSerializer


class CheckOrderViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = Order.objects.filter(cart_id__customer_id=int(self.kwargs['customer_id']))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
