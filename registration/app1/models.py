from django.db import models

class Pet(models.Model):
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    location = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.breed

# Create your models here.
