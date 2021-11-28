from django.contrib import admin

from .models import *

admin.site.register(BasicInfo)

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    name = 'Album Name'
    hashtags = 'Hashtags'

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    title = 'Tile'
    album = 'Album'
    image_path = 'Upload image'
    feature = 'Feature Image'