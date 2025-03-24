from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'author') #con esto hacemos que aparezca la fecha y el autor al lado del nombre del post.

# Register your models here.

admin.site.register(Post, PostAdmin) #asi añadimos Post a la página de admin.
