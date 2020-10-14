from django.db import models
import cv2 as cv

#magic
def modify(image):
    img = cv.imread(image)
    face_cascade = cv.CascadeClassifier('e:\Dokumentumok\IT\Projects\cv\cascade\haarcascade_frontalface_default.xml')
    frame_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame_gray, 1.3, 5)
    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
        cv.ellipse(img, center, (w//2, h//2), 0, 0, 360, (100, 0, 0), 4)
#end of magic

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    image2 = models.ImageField() #magic

    #here comes the magic
    def save(self, *args, **kwargs):
        self.image2 = modify(self.image)

        super().save(*args, **kwargs)
    #end of magic

    def __str__(self):
        return self.title
