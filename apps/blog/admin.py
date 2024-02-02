from django.contrib import admin
from .models import Category, Label, Blog


# Register your models here.
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Label)