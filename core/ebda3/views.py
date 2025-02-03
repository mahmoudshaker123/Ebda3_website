from django.shortcuts import render
from .models import *

# Create your views here.


def home(request):
    home = Home.objects.last()
    return render(request, 'index.html', {'home': home})


def offer(request):
    offers = Offer.objects.all()
    return render(request, 'index.html', {'offers': offers})



def about(request):
    about = About.objects.last()
    return render(request, 'index.html', {'about': about})


def contact(request):
    contact = ContactUs.objects.last()
    return render(request, 'index.html', {'contact': contact})


