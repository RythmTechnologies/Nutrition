from django.utils.deprecation import MiddlewareMixin
from .models import Visit

class CountVisitsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        if ip:
            visit, created = Visit.objects.get_or_create(ip_address=ip)
            if not created:
                visit.save()