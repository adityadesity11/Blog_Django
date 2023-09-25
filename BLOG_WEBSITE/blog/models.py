from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import admin
from datetime import datetime as dt

# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='authors', null=True)
    def __str__(self):
        return self.name




class Post(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    created_at = models.DateTimeField(default=dt.now, blank=True)
    def __self__(self):
        return self.title
