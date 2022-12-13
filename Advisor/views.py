from django.shortcuts import render
#from django.shortcuts import render
# Create your views here.
from . import form
from .models import Advisor_info
from .form import Advisorform

def home(request):
    return render(request,"templates/homepage/index.html")

def image(request):
    if request.method != "POST":
        Advisorform(request.POST, request.FILES)
        pic = Advisor_info.objects.all()
        return render(request,'advisor/adminphoto.html',context={"pic": pic, "photo": form})
    else:
        photo = Advisorform(request.POST, request.FILES)
        if photo.is_valid():
            photo.save()
            img = photo.instance
            return render(request,'advisor/adminphoto.html',context={'img': img})
