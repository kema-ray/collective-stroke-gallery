from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from .models import Photos,Category

# Create your views here.
def home(request):
    # date = dt.date.today()
    images = Photos.objects.all()
    return render(request,'home.html',{"images":images})
    # return HttpResponse('Welcome to the photo gallery')
def search_category(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Photos.search_by_photo_category(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"message":message,"image":searched_images})

    else:
        message = "You haven't searched for Image Category"
        return render(request,'search.html',{"message":message})

