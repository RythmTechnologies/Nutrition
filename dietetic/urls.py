from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from apps.diet_app.sitemap import BlogSitemap, AboutSitemap, ContactSitemap, ServiceSitemap

sitemaps = {
    'blogs': BlogSitemap,
    'abouts': AboutSitemap,
    'contacts': ContactSitemap,
    'services': ServiceSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.diet_app.urls')),
    path('hakkimda/',include('apps.about.urls')),
    path('hizmetler/',include('apps.services.urls')),
    path('blog/',include('apps.blog.urls')),
    path('iletisim/',include('apps.contact.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)