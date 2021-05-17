from django.db import models
from PIL import Image as Img
import os
from io import BytesIO, StringIO
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

class Image(models.Model):
    title = models.CharField(max_length=100)
    posted_on = models.DateTimeField(auto_now_add= True)
    image_path = models.ImageField(upload_to='images/')
    tags = models.CharField(max_length=100)
    image_thumbnail_path = models.ImageField(upload_to='images/thumbnails/', editable=False)

    def create_thumbnail(self):

        img = Img.open(self.image_path)
        img.thumbnail((400,400))
        
        thumb_name, thumb_extension = os.path.splitext(self.image_path.name)
        thumb_filename = thumb_name + thumb_extension.lower()

        if thumb_extension in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif thumb_extension == '.gif':
            FTYPE = 'GIF'
        elif thumb_extension == '.png':
            FTYPE = 'PNG'
        else:
            return False
        
        img_io = BytesIO()
        img.save(img_io, FTYPE)
        img_io.seek(0)

        self.image_thumbnail_path.save(thumb_filename, ContentFile(img_io.read(), False), save= False)
        img_io.close()
        return True

    def save(self, *args, **kwargs):
        if not self.create_thumbnail():
            raise Exception("SOME ERROR.")
        super(Image, self).save(*args, **kwargs)
