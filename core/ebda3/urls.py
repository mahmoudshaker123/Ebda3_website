from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.home, name='home'),
    path('offers/', offer , name='offers'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),

    ]
