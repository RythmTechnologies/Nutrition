from django.contrib import admin
from .models import Visit
# Register your models here.


class VisitAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'visit_count','created_at')  


# Visit modelini admin paneline kaydedin
admin.site.register(Visit, VisitAdmin)