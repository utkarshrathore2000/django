from django.urls import path,include
from django.contrib import admin
from.import views
urlpatterns=[
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('home',views.home,name='home'),
    path('form',views.form,name='form'),
    path('show',views.show,name='show')
]
