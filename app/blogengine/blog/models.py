from django.db import models
from django.shortcuts import reverse

from django.utils.text import slugify
from time import time
# Create your models here.


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug+'-'+str(int(time()))




class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)  # blank=True означает что это поле модет быть пустым
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    date_pub = models.DateTimeField(auto_now_add=True)  # auto_now_add=True значит будт заполнятся при сохранении в БД

# Метод нужен для того чтобы не запоминать для какой модели какие входные данные
# нужно указывать в html шаблоне, название метода это соглашение в Django
# Метод возвращает ссылку на конкретный объект
    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.title}'
