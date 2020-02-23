from django.shortcuts import render,HttpResponse
from .models import Swim
# Create your views here.
from django.urls import path
def index(request):
    return render(request, 'swim/home.html')

def swimit(request):
    swimmers=Swim.objects
    return render(request,'swim/index.html',{'swim':swimmers,})