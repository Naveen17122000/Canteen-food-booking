from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    username = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order for {self.username}: {self.item.name} - {self.quantity} items"

