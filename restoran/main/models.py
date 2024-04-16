from django.db import models
from django.contrib.auth.models import User

class TableBooking(models.Model):
    id = models.AutoField(primary_key=True, default=None)
    email = models.EmailField(default=None)
    table_number = models.IntegerField(default=None)
    date = models.DateField(default=None)
    time = models.TimeField(default=None)

    def __str__(self):
        return f"Бронирование столика №{self.table_number} для {self.email}"


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default=None)
    email = models.EmailField(default=None)
    password = models.CharField(max_length=50, default=None)
    table = models.OneToOneField(TableBooking, on_delete=models.CASCADE, default=None)

    class Meta:
        app_label = 'main'


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(default=None)
    text = models.TextField(default=None)

    def __iter__(self):
        return iter([self.email, self.text])


class Dish(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='Default Name')
    description = models.TextField(default='Default Description')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    group = models.TextField(default='Default Group')

    def __iter__(self):
        return iter([self.name, self.description, self.price, self.group])
