from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.diet_app.urls')),
    path('hakkimda/',include('apps.about.urls')),
    path('paketler/',include('apps.packages.urls')),
    path('hizmetler/',include('apps.services.urls')),
    path('iletisim/',include('apps.contact.urls')),
    path('', TemplateView.as_view(template_name='index.html', extra_context={
        "instagram_profile_name": "dytsedanurciray"
    })),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)