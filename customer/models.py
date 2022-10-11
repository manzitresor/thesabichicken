from django.db import models

class ChickenItems(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    images = models.ImageField(upload_to = 'chichen_images/')
    price = models.DecimalField(max_digits=5,decimal_places=2)
    category = models.ManyToManyField('Category',related_name='item')

    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class OrderModel(models.Model):
    created_on = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    items = models.ManyToManyField('ChickenItems',related_name='order',blank=True) 

    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %I: %M %p")}'