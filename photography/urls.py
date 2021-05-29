from os import name
from django.urls import path
from django.urls.resolvers import URLPattern

from .import views

urlpatterns = [
    path('',views.index, name='index'),
    path('gallery',views.gallery, name='gallery'),
    path('gallery/image/<int:pk>/', views.image, name='image')
]