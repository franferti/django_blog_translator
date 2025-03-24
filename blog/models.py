from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, 'Draft'),(1, 'Publish'))
# Create your models here.
"""Hemos creado un model llamado post y ahora tenemos que añadirlo a la database, asi que ponemos en la terminal python manage.py makemigrations y luego python 
manage.py migrate y asi es como se mete el model en la database."""
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title #esto se hace para que en la web de admin de django nos salga el nombre de cada post ("Dogs" o "Cats") en lugar de post1, post2...
