from django.contrib import admin
from .models import *


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    name = 'Album Name'
    hashtags = 'Hashtags'
    travel_date = "Travel Date"

    list_display = ['name', 'travel_date']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    title = 'Tile'
    album = 'Album'
    image = 'Upload image'
    feature = 'Feature Image'

    # show a thumbnail of the uploaded image on admin page
    def image_tb(self, obj):
        return html.mark_safe('<img src="%s" width="150" height="150" />' % obj.thumbnail.url)
    image_tb.short_description = "image"

    # List of fields to display
    list_display = ['title', 'pk', 'album', 'genre', 'image_tb']
    list_filter = ['genre', 'album', 'feature']


@admin.register(TravelDiary)
class TravelDiaryAdmin(admin.ModelAdmin):
    name = 'Name'
    title = "Title"
    content = 'Content'
    publish = 'Published'

    # List of fields to display
    list_display = ['name', 'title', 'publish']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    name = 'Name'
    title = "Title"
    content = 'Content'

    # List of fields to display
    list_display = ['name', 'title']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    name = 'Name'


@admin.register(ProfilePhoto)
class ProfilePhotoAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return html.mark_safe('<img src="%s" width="150" height="150" />' % obj.thumbnail.url)
    image_tag.short_description = "image"

    list_display = ['date', 'image_tag', 'active']
    list_filter = ['active']


@admin.register(LandingImage)
class LandingImagesAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return html.mark_safe('<img src="%s" width="150" height="150" />' % obj.thumbnail.url)
    image_tag.short_description = "image"

    list_display = ['date', 'image_tag', 'active']
    list_filter = ['active']
