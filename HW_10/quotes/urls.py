from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'quotes'

urlpatterns = [
    path('test/', views.index, name='index'),
    path('', views.quotes, name='quotes'),
    path('quotes/addauthor', views.add_author, name='add_author'),
    path('quotes/addquotes', views.add_qoute, name='add_quote'),
    path('quotes/author/<int:id>', views.author, name='author'),
    path('quotes/addtag', views.add_tag, name='add_tag')

]