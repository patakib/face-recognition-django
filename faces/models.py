from django.db import models
import os

def imgpath(instance, filename):
    basefilename, file_extension= os.path.splitext(filename)
    return 'images/{basename}{ext}'.format(basename='uploaded_img', ext=file_extension)

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to=imgpath, null=True)

    def __str__(self):
        return self.title
