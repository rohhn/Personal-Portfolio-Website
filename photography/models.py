import os
from uuid import uuid4
from django.db import models
from PIL import Image as Img
from io import BytesIO, StringIO
from django.core.files.base import ContentFile
from django.utils import timezone, html


class Album(models.Model):
    name = models.CharField(max_length=50)
    hashtags = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower().strip()
        if self.hashtags is not None:
            self.hashtags = self.hashtags.lower().strip().replace("#", "")
        super(Album, self).save(*args, **kwargs)


class Genre(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower().strip()
        super(Genre, self).save(*args, **kwargs)


def rename_image(instance, filename):
    _, extension = os.path.splitext(filename)

    new_file_name = f"{instance.album.name}-{instance.title}-{uuid4().hex}{extension}".replace(" ", "_")

    return os.path.join('images', new_file_name)


def rename_thumbnail(instance, filename):
    _, extension = os.path.splitext(filename)

    new_file_name = f"{instance.album.name}-{instance.title}-{uuid4().hex}{extension}".replace(" ", "_")

    return os.path.join('images/thumbnails/', new_file_name)

class Image(models.Model):

    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    feature = models.BooleanField(default=False)
    posted_on = models.DateTimeField(default=timezone.now, editable=False)
    hashtags = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to=rename_image)
    thumbnail = models.ImageField(upload_to=rename_thumbnail, editable=False)

    def __str__(self) -> str:
        return f"{self.title}-{self.album.name}-{self.feature}"

    def create_thumbnail(self):

        img = Img.open(self.image)
        ratio = round(img.size[0] / img.size[1], 2)
        img.resize((500, round(500 / ratio)))

        # convert extensions to lowercase ex.: .JPEG -> .jpeg
        thumb_name, thumb_extension = os.path.splitext(self.image.name)
        thumb_filename = f"{thumb_name} + {thumb_extension.lower()}"

        if thumb_extension in ['.jpg', '.jpeg']:
            ftype = 'JPEG'
        elif thumb_extension == '.gif':
            ftype = 'GIF'
        elif thumb_extension == '.png':
            ftype = 'PNG'
        else:
            return False

        img_io = BytesIO()
        img.save(img_io, ftype)
        img_io.seek(0)

        self.thumbnail.save(thumb_filename, ContentFile(img_io.read(), False), save=False)
        img_io.close()
        return True

    def save(self, *args, **kwargs):
        """
        Overrides the default save function to perform pre-processing
        """

        self.title = self.title.lower().strip()
        if self.hashtags is not None:
            self.hashtags = self.hashtags.lower().strip().replace("#", "")
        if not self.create_thumbnail():
            raise Exception("Error saving thumbnail.")
        super(Image, self).save(*args, **kwargs)


class TravelDiary(models.Model):
    name = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    style_formats = models.TextField()
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.name.capitalize()

    def save(self, *args, **kwargs):
        self.name = self.name.lower().strip()
        self.title = self.title.lower().strip()

        super(TravelDiary, self).save(*args, **kwargs)
