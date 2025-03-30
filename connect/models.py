from django.db import models

# Create your models here.

class Connect(models.Model):
    name = models.CharField(max_length=50)
    conversion = models.CharField(max_length=50)
    mineral = models.CharField(max_length=50)
    price = models.CharField(max_length=12)

    def __str__(self):
        return self.name
