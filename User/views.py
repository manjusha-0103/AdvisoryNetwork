from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse


def register_user(request):
    pass

    if request.method == "POST":
        form = UserCreationForm()
        if request.is_valid():

            return render(request,'user/register.html',contest = {'form':form})


