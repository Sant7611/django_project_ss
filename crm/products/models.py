from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    barcode =models.CharField(max_length=20)
    stock_quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name