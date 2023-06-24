from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name
# Create your models here.
class InventoryItem(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT,blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    sold_for = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name
    
class Pricing(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT,blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    sold_for = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name
    

    