from django.utils import timezone
from django.db import models
from django.urls import reverse

from shop.settings import AUTH_USER_MODEL

# Create your models here.
"""
Product
- Nom
- Prix
- Quantité en stock
- Description
- Image
"""

class Product(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})
    

class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default = 1)
    is_ordered = models.BooleanField(default = False)
    date = models.DateField(blank = True, null = True)

    def __str__(self):
        return f"{self.product.name} (x{self.qty})"

class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    

    def __str__(self):
        return self.user.username
    
    def delete(self, *args, **kwargs):
        for order in self.orders.all():
            order.is_ordered = True
            order.date = timezone.now()
            order.save()

        self.orders.clear()
        
        super().delete(*args, **kwargs)
