from django.urls import path
from .views import *

urlpatterns = [
    path('' , index , name = 'index'),
    path('brone/<str:dev_name>/', brone , name = 'brone'),
    path('full' , full , name = 'full'),
    path('placeapi/', Get_place_List.as_view()),
    path('data/', getdata,name='getdata')
]