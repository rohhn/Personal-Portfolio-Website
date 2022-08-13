from django.core.files.base import ContentFile
from django.http.response import Http404
from django.shortcuts import render
from django.template import Template, Context
from .models import *


def get_navbar_elements(request):
    travel_diaries = TravelDiary.objects.all() #.order_by("-posted_on")
    response = {
        'travel_diaries': travel_diaries
    }
    return response


def handler404(request):
    response = render(request, 'photography/error_pages/404.html', None)
    response.status_code = 404
    return response


def handler500(request):
    response = render(request, 'photography/error_pages/500.html', None)
    response.status_code = 500
    return response


def index(request):
    context = {
        'navbar_elements': get_navbar_elements(request)
    }
    return render(request, 'photography/index.html', context)


def about(request):
    context = {
        'navbar_elements': get_navbar_elements(request)
    }
    return render(request, 'photography/about.html', context)


def album(request, album_name=None):
    try:
        album = Album.objects.get(name=album_name)
    except Album.DoesNotExist:
        return handler404(request)
    else:
        images = Image.objects.filter(album=album).order_by('-posted_on')

    context = {
        'album': album,
        'images': images,
        'navbar_elements': get_navbar_elements(request)
    }
    return render(request, 'photography/album.html', context)


def genre(request, genre_name=None):
    try:
        genre = Genre.objects.get(name=genre_name)
    except Genre.DoesNotExist:
        return handler404(request)
    else:
        images = Image.objects.filter(genre=genre).order_by('-posted_on')

    context = {
        'genre': genre,
        'images': images,
        'navbar_elements': get_navbar_elements(request)
    }
    return render(request, 'photography/genre.html', context)


def gallery(request):

    genres = Genre.objects.all()

    genre_info = []
    for genre in genres:
        temp = {
            'thumbnail': Image.objects.filter(genre=genre).last(),
            'name': genre.name
        }
        genre_info.append(temp)

    # Randomly list featured images
    featured_images = Image.objects.filter(feature=True).order_by('?')

    context = {
        'genres': genre_info,
        'featured_images': featured_images,
        'navbar_elements': get_navbar_elements(request)
    }

    return render(request, 'photography/gallery.html', context)


def images(request):
    images = Image.objects.all().order_by("-posted_on")
    context = {
        'images': images,
        'navbar_elements': get_navbar_elements(request)
    }

    return render(request, 'photography/all_images.html', context)


def image(request, pk):
    image = Image.objects.get(pk=pk)
    context = {
        'image': image,
        'navbar_elements': get_navbar_elements(request)
    }

    return render(request, 'photography/image.html', context)



def travel_diaries(request):
    pass


def travel_diary(request, diary_name):
    try:
        info = TravelDiary.objects.get(name=diary_name)
    except info.DoesNotExist:
        return handler404(request)
    context = {
        'diary': info,
        'rendered_style': Template(info.style_formats).render(Context()),
        'rendered_content': Template(info.content).render(Context()),
        'navbar_elements': get_navbar_elements(request)
    }
    return render(request, 'photography/travel_diaries/template.html', context)
