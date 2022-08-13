from django.urls import path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/<str:genre_name>', views.genre, name='genre'),
    path('gallery/image/<int:pk>/', views.image, name='image'),
    path('gallery/all', views.images, name='all_images'),
    path('about/', views.about, name='about'),
    # path('travels/spiti/', TemplateView.as_view(template_name='photography/travel_diaries/spiti.html'), name='spiti'),
    path('travels/<str:diary_name>/', views.travel_diary, name='travel_diary'),
    path('test/', TemplateView.as_view(template_name='photography/travel_diaries/test.html'), name='test')
]
