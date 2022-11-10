from django.db import models


class Article(models.Model):
    category = models.CharField(max_length=100, default="General")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    thumbnail = models.TextField(default="")
    image_content = models.TextField(default="")
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=30)
    isPublished = models.BooleanField(default=False)