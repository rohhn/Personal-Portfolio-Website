from django.core.files.base import ContentFile
from django.shortcuts import render
from .models import Image

def index(request):
    images = Image.objects.filter(
        tags__icontains='featured'
    )

    context = {'images':images}

    return render(request, 'photography/index.html', context)

def gallery(request):
    images = Image.objects.all().order_by('posted_on')

    context = {'all_images':images}

    return render(request, 'photography/gallery.html', context)

def image(request, pk):
    image = Image.objects.get(pk= pk)

    context = {'image':image}
    return render(request, 'photography/image.html', context)