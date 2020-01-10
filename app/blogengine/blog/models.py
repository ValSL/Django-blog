from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)# blank=True означает что это поле модет быть пустым
    date_pub = models.DateTimeField(auto_now_add=True)# auto_now_add=True значит будт заполнятся при сохранении в БД

    def __str__(self):
        return f'{self.title}'
