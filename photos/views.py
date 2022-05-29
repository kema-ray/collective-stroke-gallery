from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from .models import Photos

# Create your views here.
def home(request):
    # date = dt.date.today()
    images = Photos.objects.all()
    return render(request,'home.html',{"images":images})
    # return HttpResponse('Welcome to the photo gallery')
