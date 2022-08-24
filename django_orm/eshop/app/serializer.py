from django.db.models import Sum
from rest_framework import serializers

from .models import Product, Cart, ProductCart, User, Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['customer_id']


class ProductCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCart
        fields = ['product_id', 'cart_id', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'cart_id', 'total_price']

    def get_total_price(self, order):
        final_price = order.cart_id.products.aggregate(total_price=Sum('price'))[
                          'total_price'] * ProductCart.objects.filter(cart_id=order.cart_id).first().quantity
        return final_price
