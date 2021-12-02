from django.core.files.base import ContentFile
from django.http.response import Http404
from django.shortcuts import render
from .models import *

def index(request):

    images = Image.objects.filter(
        feature=True
    )

    context = {
        'images':images
    }

    return render(request, 'photography/index.html', context)

def album(request, album_name=None):
    
    try:
        album = Album.objects.get(name=album_name)
    except Album.DoesNotExist:
        return Http404
    else:
        images = Image.objects.filter(album = album).order_by('posted_on')

    context = {
        'album':album,
        'images':images
    }
    return render(request, 'photography/album.html', context)

def gallery(request):

    albums = Album.objects.all()
    out = []
    for album in albums:
        temp = {
            'album_thumbnail': Image.objects.filter(album=album).last(),
            'name': album.name
        }
        out.append(temp)
        
    images = Image.objects.filter(feature=True).order_by('posted_on')

    context = {
        'albums': out,
        'featured_images': images
    }

    return render(request, 'photography/gallery.html', context)

def images(request):

    images = Image.objects.all().order_by("-posted_on")
    context = {'images':images}

    return render(request, 'photography/all_images.html', context)

def image(request, pk):

    image = Image.objects.get(pk=pk)
    context = {'image':image}

    return render(request, 'photography/image.html', context)