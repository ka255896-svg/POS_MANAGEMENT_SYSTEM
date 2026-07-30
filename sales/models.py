from products.models import Product
from customers.models import Customer
from django.db import models


class Sale(models.Model):

    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )


    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )


    quantity = models.IntegerField()


    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )


    profit = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )


    sale_date = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return self.product.product_name