from django.urls import  path
from .views import image


urlpatterns = [

   # path('', home, name ='homepage'),

   #path('Advisor/advisor/<str:image>/[name = "image"]', image,name = 'image'),
    path('image/' , image , name = 'image')
]