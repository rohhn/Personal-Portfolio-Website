from django.shortcuts import render
from .models import Image

def index(request):
    images = Image.objects.filter(
        tags__icontains='featured'
    )
    return(render(request, 'landingpage/index.html', {'images':images}))

def gallery(request):
    images = Image.objects.all()
    return(render(request, 'landingpage/gallery.html', {'images':images}))