from django.db import models

# Create your models here.
class Product(models.Model):
    LIVE=1
    DELETE=0
    title=models.CharField(max_length=200)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField()
    priority=models.IntegerField(default=0)
