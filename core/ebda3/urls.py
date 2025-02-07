from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='home'),
    path('gallery/', views.index, name='gallery'),
    path('offers/', views.index, name='offers'),
    path('about-us/', views.index, name='about-us'),
    path('contact-us/', views.index, name='contact-us'),
]
