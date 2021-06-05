from django.contrib import admin
from django.urls import path, include

from .views import *



urlpatterns = [

    path('pdf/' , GeneratePdf.as_view()),
    
    path('generic-student/' , StudentGeneric.as_view()),
    path('generic-student/<id>/' , StudentGeneric1.as_view()),

    path('student/' ,StudentAPI.as_view()),
    path('get-book/' , get_book),
    path('register/' , RegisterUser.as_view())
    
]
