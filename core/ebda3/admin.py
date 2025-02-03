from django.contrib import admin
from .models import *

class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'office', 'users', 'projects', 'workers', 'intro_content', 'main_content', 'img']

admin.site.register(Home)
admin.site.register(Offer)
admin.site.register(ContactUs)
admin.site.register(About, AboutAdmin)
