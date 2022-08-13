from django.contrib import admin
from .models import *


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    name = 'Album Name'
    hashtags = 'Hashtags'


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    title = 'Tile'
    album = 'Album'
    image = 'Upload image'
    feature = 'Feature Image'

    # show a thumbnail of the uploaded image on admin page
    def image_tag(self, obj):
        return html.mark_safe('<img src="%s" width="150" height="150" />' % obj.thumbnail.url)
    image_tag.short_description = "image"

    # List of fields to display
    list_display = ['title', 'album', 'genre', 'image_tag']
    list_filter = ['genre', 'album', 'feature']


@admin.register(TravelDiary)
class TravelDiaryAdmin(admin.ModelAdmin):
    name = 'Name'
    title = "Title"
    style_formats = 'Style tag'
    content = 'Content)'

    # List of fields to display
    list_display = ['name', 'title', 'album']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    name = 'Name'
