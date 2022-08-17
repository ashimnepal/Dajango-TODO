from turtle import title
from unicodedata import name
from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=256)
    contents = models.TextField()

    def __str__(self):
        return self.title
    
    
