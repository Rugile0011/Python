from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        abstract = True


class User(BaseModel):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.pk} Name: {self.name}, Email: {self.email}, Address: {self.address}, Joined: {self.created_at}'


class Product(BaseModel):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.pk} Name: {self.name}, Price: {self.price}'


class Cart(BaseModel):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Product, through='ProductCart', related_name='carts')

    def __str__(self):
        return f'{self.pk} Customer ID: {self.customer}'


class ProductCart(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.pk} Product ID: {self.product}, Cart ID: {self.cart}, Quantity: {self.quantity}'


class Order(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pk} Cart ID: {self.cart}'


class Category(BaseModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, null=True)
    products = models.ManyToManyField(Product, through='app.CategoryProduct', related_name='categories')

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f'{self.pk} Name: {self.name}, Description: {self.description}'


class CategoryProduct(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pk} Product: {self.product.name}, Category: {self.category.name}'
