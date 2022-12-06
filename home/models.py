from re import search
from django.db import models

# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=500)
    product_email = models.EmailField(max_length=500)
    product_number = models.IntegerField()
    product_message = models.TextField()
    product_medicine = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.product_name

class Email(models.Model):
    e_email = models.EmailField(max_length=500)

    def __str__(self) -> str:
        return self.e_email

class Search(models.Model):
    searchs = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.searchs