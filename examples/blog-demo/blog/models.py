from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    slug   = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.author + " - " + self.title[0:24]

class Post(models.Model):
    title = models.CharField(max_length=64, unique=True)
    text  = models.TextField()
    blog  = models.ForeignKey(Blog)

    def __str__(self):
        return self.title
