from django.urls import path
from .views import *

urlpatterns = [
    path('',blog_view,name='blog'),
    path('<slug>', blog_single_view, name="blog-icerik")
]
