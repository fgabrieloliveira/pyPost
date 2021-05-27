
from django.db import models
from django.db.models.deletion import SET_DEFAULT
from  django.utils import timezone

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
    text = models.TextField(max_length=1000)
    author = models.ForeignKey(Reporters, on_delete=SET_DEFAULT, default='desconhecido')
    pub_date = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.title