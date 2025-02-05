from django.shortcuts import render
from .models import *

def index(request):
    home = Home.objects.last()
    offers = Offer.objects.all()
    about = About.objects.last()
    contact_us = ContactUs.objects.last()
    gallery = BusinessGallery.objects.all().order_by('-created_at')[:50]  # ترتيب الصور حسب تاريخ الإنشاء
    return render(request, 'index.html', {'home': home, 'offers': offers, 'about': about , 'gallery': gallery , 'contact_us': contact_us})
