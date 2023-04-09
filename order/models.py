
from django.db import models
from user.models import UserModel
from product.models import Products
# Create your models here.

class Order(models.Model):

    class Meta:
        db_table="orders"

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    order = models.ForeignKey(Products, on_delete=models.CASCADE)
    amount = models.PositiveBigIntegerField()
    code = models.BigAutoField(primary_key=True)
    marker = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.code

