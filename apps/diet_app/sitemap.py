from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from apps.about.models import AboutMe
from apps.blog.models import Blog
from apps.contact.models import Contact
from apps.services.models import Services


#Seo All Models
class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Blog.objects.all().order_by('-created_at')

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return reverse('blog-icerik', args=[obj.slug])

class AboutSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return AboutMe.objects.all().order_by('-created_at')

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return reverse('hakkimizda')


class ContactSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Contact.objects.all().order_by('-created_at')

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return reverse('iletisim')

class ServiceSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Services.objects.all().order_by('-created_at')

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return reverse('hizmetler')