from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.diet_app.urls')),
    path('hakkimda/',include('apps.about.urls')),
    path('hizmetler/',include('apps.services.urls')),
    path('iletisim/',include('apps.contact.urls')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)