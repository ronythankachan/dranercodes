"""Home page for the website"""
from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name="home")

]
