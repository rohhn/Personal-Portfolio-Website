from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing_page_view, name='index'),
    path('gallery/', views.gallery_page_view, name='gallery'),
    path('about/', views.about_page_view, name='about'),
    path('travels/<int:diary_id>/', views.single_diary_view, name='travel_diary'),
    path('travels/', views.all_diaries_view, name='travel_diaries'),
    path('projects/<int:project_id>/', views.single_project_view, name='project'),
    path('projects/', views.all_projects_view, name='projects'),
    path('images/', views.gallery_page_view, name="Images")
]
