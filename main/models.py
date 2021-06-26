
from django.db import models
from django.db.models.deletion import CASCADE, SET_DEFAULT
from  django.utils import timezone
from django.contrib.auth.models import User
from myproject.settings import MEDIA_URL

class Reporters(models.Model):
    name = models.CharField(max_length=20)
    birthday = models.CharField(max_length=10)
    nationality = models.CharField(max_length=10)
    bio = models.TextField(max_length=200)

    def __str__(self):
        return self.name

class Articles(models.Model):
    title = models.CharField(max_length=20)
    headline = models.TextField(max_length=50)
    text = models.TextField(max_length=100000)
    author = models.ForeignKey(User, on_delete=CASCADE)
    pub_date = models.DateField(default=timezone.now)
    image = models.ImageField(default='static/images/default.jpeg', upload_to=MEDIA_URL)
    
    def __str__(self):
        return self.title