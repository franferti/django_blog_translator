from . import views
from django.urls import path

urlpatterns = [
    path('<slug:slug>', views.BlogView.as_view(), name='blog_view'),
    path('about/', views.AboutView.as_view(), name='about_view'), #tras crear la página index.html creamos esta linea de código que es la de la homepage. Tras esto vamos a views.
    path('', views.PostList.as_view(), name='home') #aqui unimos el modelo de la homepage con el views
]

"""Cuando hagamos esto tenemos que irnos a la carpeta urls.py que hay dentro de mysite para modificarlo y añadir esta url"""
