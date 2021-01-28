from django.db import models

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class Bookhouse(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.CharField(max_length=7)
    genre =  models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    year = models.DateField(auto_created=True)
    date = models.DateTimeField(auto_now_add=True)
    is_favorite = models.BooleanField(default=False)


