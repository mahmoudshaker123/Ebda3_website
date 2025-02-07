from django.shortcuts import render
from .models import *



def index(request):
    section = request.path.strip('/')  # تحديد القسم بناءً على URL
    home = Home.objects.last()
    offers = Offer.objects.all()
    about = About.objects.last()
    contact_us = ContactUs.objects.last()
    gallery = BusinessGallery.objects.all().order_by('-created_at')[:50]

    context = {
        'home': home,
        'offers': offers,
        'about': about,
        'gallery': gallery,
        'contact_us': contact_us,
        'section': section,  # لإرسال القسم المطلوب للقالب
    }
    return render(request, 'index.html', context)
