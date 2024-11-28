from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    price = models.FloatField(default=0.0)
    edition = models.SmallIntegerField(default=1)
    
class Address(models.Model):
    city = models.CharField(max_length=100)
    def __str__(self):
        return self.city

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE)


class Address2(models.Model):
    city = models.CharField(max_length=100)
    def __str__(self):
        return self.city


class Student2(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    addresses = models.ManyToManyField(Address2)