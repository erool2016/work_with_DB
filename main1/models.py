from django.db import models
# from django.template.defaultfilters import slugify
# from django.utils.text import slugify
from pytils.translit import slugify


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, primary_key=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='products')
    def __str__(self):
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=50, unique=True)
    addres = models.CharField(max_length=50,)
    notes = models.TextField(blank=True)
    product = models.ManyToManyField(Product, through='OrderItem')
    def __str__(self):
        return f'Заказ N: {self.id}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
