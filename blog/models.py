from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey(to=User,
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    desc = models.TextField()
    image = models.ImageField(upload_to='media/')
    genre = models.ForeignKey(to=Genre, 
                              on_delete=models.CASCADE)
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    desc = models.TextField()
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.desc[:20]