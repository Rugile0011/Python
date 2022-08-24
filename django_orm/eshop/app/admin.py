from django.contrib import admin

from .models import Cart, Category, CategoryProduct, User, Order, Product, ProductCart

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(ProductCart)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(CategoryProduct)
