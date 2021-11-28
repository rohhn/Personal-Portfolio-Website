from os import name
from django.urls import path
from django.views.generic.base import TemplateView

from .import views

urlpatterns = [
    path('',views.index, name='index'),
    path('gallery',views.gallery, name='gallery'),
    path('gallery/album/<str:album_name>',views.album, name='album'),
    path('gallery/image/<int:pk>/', views.image, name='image'),
    path('about/', TemplateView.as_view(template_name='photography/about.html'), name='about'),
]