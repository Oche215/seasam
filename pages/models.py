from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(max_length=100)

    message = models.CharField(max_length=1900, default='', blank=True, null=True)
    file = models.FileField(upload_to='document/', blank=True, null=True)

    def __str__(self):
        return self.name


class GeoPoliticalRegion(models.Model):
    region = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.region


class NigeriaMineralDeposit(models.Model):
    minerals = models.CharField(max_length=150)
    region = models.ForeignKey(GeoPoliticalRegion, on_delete=models.CASCADE, default=1)
    state = models.CharField(max_length=150, blank=True, null=True)

    note = models.TextField(max_length=1900, default='', blank=True, null=True)
    image = models.ImageField(upload_to='state/', default='state/Topaz-169707.jpg')

    def __str__(self):
        return self.state


class Minerals(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=1900, default='', blank=True, null=True)
    photo = models.ImageField(upload_to='pit/', default='pit/OIP.jpg')

    def __str__(self):
        return self.name

