from django.urls import reverse
from model_bakery.baker import make
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Order, Cart, User, ProductCart, Product


class TestShop(APITestCase):

    def test_page_status_code(self):
        response = self.client.get(reverse("products-list"))
        self.assertEquals(response.status_code, 200)


class TestProductList(APITestCase):

    def setUp(self):
        self.product_first = make(Product, name='rose', price=str(1.56))
        self.product_second = make(Product, name='lily', price=str(2.28))

    def _assert_products_fields(self, response_json: list):
        expected_data = [self.product_first, self.product_second]
        self.assertEqual(
            [
                {
                    'name': product.name,
                    'price': str(product.price)
                } for product in expected_data
            ],
            response_json
        )

    def test_get_product_list(self):
        response = self.client.get(reverse('products-list'), follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)
        self._assert_products_fields(response.json())


class TestCartCreation(APITestCase):

    def setUp(self):
        self.cart = make(Cart)

    def test_cart_creation(self):
        customer = make(User)
        response = self.client.post(reverse("carts-list"), {'customer_id': customer.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        existing_cart = Cart.objects.get(customer_id=customer.id)
        self.assertTrue(existing_cart)
        self.assertEqual(existing_cart.customer_id.id, customer.id)

    def test_order_creation(self):
        total_price = 10.50
        response = self.client.post(reverse("order-list"), {'cart_id': self.cart.pk, 'total_price': total_price})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        existing_order = Order.objects.get(cart_id=self.cart.pk)
        self.assertTrue(existing_order)
        self.assertEqual(existing_order.cart_id.pk, self.cart.pk)
        self.assertGreater(existing_order.total_price, 0, "Price can not be negative number")
        self.assertEqual(existing_order.total_price, 10.50)

    def test_products_in_cart(self):
        product = make(ProductCart)
        quantity = 2
        response = self.client.post(reverse("productcart-list"),
                                    {'cart_id': self.cart.pk, 'product_id': product.pk,
                                     'quantity': quantity})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        check_quantity = ProductCart.objects.get(quantity=quantity)
        self.assertEqual(check_quantity.quantity, 2)
        self.assertGreater(check_quantity.quantity, 0, "Quantity has to be positive number")
