from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    text = models.TextField(verbose_name='Контент')
    slug = models.SlugField(max_length=250, unique=True, verbose_name="Слаг", blank=True, null=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="Автор", related_name="posts", default=None, null=True)
    tags = models.JSONField(null=True, blank=True, default=list)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0, verbose_name="Просмотры")
    category = models.CharField(max_length=100, verbose_name='Категория', default=None, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/post/{self.slug}/'

    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)