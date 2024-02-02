from django.shortcuts import render
from .models import Packages
# Create your views here.
def packages(request):
    packages = Packages.objects.all()
    return render(request, 'pages/packages.html',{"packages":packages,})