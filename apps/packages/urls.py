
from django.urls import path
from .views import *
urlpatterns = [
    path('',packages,name="paketler"),
]
