from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE())
    tags = models.JSONField(null=True, blank=True, default=list)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/post/{self.slug}/'

    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)