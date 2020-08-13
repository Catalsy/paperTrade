from django.contrib.auth.models import AbstractUser
from django.db import models
from computedfields.models import ComputedFieldsModel, computed


# Create your models here.
class User(AbstractUser):
    funds = models.IntegerField(default=100000)
    investing = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.username}"

class Transaction(ComputedFieldsModel):
    stock = models.CharField(max_length=16)
    quantity = models.IntegerField()
    price = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transactions")

    @computed(models.IntegerField(), depends=[['self', ['quantity', 'price']]])
    def total(self):
        return (self.price * self.quantity)
    
    """ Use -> 
    transaction.compute(total)
    transaction.save()
    transaction.total -> output """

    def __str__(self):
        return f"{stock} x{quantity} ${price}"
