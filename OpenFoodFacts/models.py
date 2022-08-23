from pyexpat import model
from django.db import models

class Produto(models.Model):
    code = models.CharField(max_length=13, unique=True)
    barcode = models.CharField(max_length=13, unique=True)
    status = models.CharField(max_length=100)
    imported_t = models.CharField(max_length=100)
    url = models.URLField()
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    categories = models.CharField(max_length= 100)
    packaging = models.CharField(max_length=100)
    brands = models.CharField(max_length=100)
    image_url = models.URLField()

    def __str__(self):
        return self.product_name
        