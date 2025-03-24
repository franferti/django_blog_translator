from django.shortcuts import render
from .models import Post
from django.views import generic

"""Aqui creamos una view para unir el model blog con el html template blog.html. Tambien crearemos más views como la homepage,..."""
# Create your views here.

class BlogView(generic.DetailView):
    model = Post
    template_name = 'blog.html'

class AboutView(generic.TemplateView): #aqui estaba al principio index pero despues lo cambiamos por about
    template_name = 'about.html'

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-date_created')
    template_name = 'index2.html'