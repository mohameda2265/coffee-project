from django.db import models


# Create your models here.

class CoffeeMachine(models.Model):
    product_type = models.CharField(max_length=50)
    water_line_compatible = models.BooleanField(default=False)
    coffee_machine_models = models.CharField(max_length=50, default='')
    SKU = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.SKU


class CoffeePod(models.Model):
    product_type = models.CharField(max_length=50)
    coffee_flavor = models.CharField(max_length=50)
    pack_size = models.CharField(max_length=50)
    SKU = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.SKU
