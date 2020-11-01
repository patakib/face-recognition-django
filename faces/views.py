from django.shortcuts import render
from .forms import ImageForm
import cv2 as cv


# Create your views here.
def image_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance

            #magic
            cv_img = cv.imread(r'media\images\uploaded_img.jpg')
            face_cascade = cv.CascadeClassifier('cascade\haarcascade_frontalface_default.xml')
            frame_gray = cv.cvtColor(cv_img, cv.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(frame_gray, 1.3, 5)
            for (x,y,w,h) in faces:
                center = (x + w//2, y + h//2)
                cv.ellipse(cv_img, center, (w//2, h//2), 0, 0, 360, (100, 0, 0), 4)
            cv.imwrite('media\images\cvimage.jpg', cv_img)
            #end of magic

            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})
