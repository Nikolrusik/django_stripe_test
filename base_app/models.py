from django.db import models
import stripe

# Create your models here.
class Item(models.Model):
    name = models.CharField(name="Name", max_length=255)
    description = models.TextField(name="Description", null=True, blank=True)
    price = models.IntegerField(name="Price", default=100)
