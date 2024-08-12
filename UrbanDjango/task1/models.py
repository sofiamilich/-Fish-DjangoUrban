from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=10)
    age = models.IntegerField

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.TextField(max_length=500)
    cost = models.DecimalField(max_digits=10, decimal_places=10)
    size = models.DecimalField(max_digits=10, decimal_places=10)
    description = models.TextField(max_length=500)
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')
    field_fractional_numbers= models.DecimalField(max_digits=10, decimal_places=10)
    field_boolean_values= models.BooleanField

    def __str__(self):
        return self.title
