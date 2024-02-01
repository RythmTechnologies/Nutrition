
from django.urls import path
from .views import *
urlpatterns = [
    path('',services,name="hizmetler"),
    path('spordiyeti/<id>', services_spor, name="spor-diyeti")
]
