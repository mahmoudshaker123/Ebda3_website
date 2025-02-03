from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ebda3.urls')),  # روابط التطبيق ebda3
]
if settings.DEBUG:  # فقط أثناء التطوير
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)