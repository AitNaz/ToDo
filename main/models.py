from django.db import models

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    creates_ed = models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

