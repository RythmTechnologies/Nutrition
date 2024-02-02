from django.shortcuts import render
from .models import HomeSlider,TopContent
# Create your views here.
def index(request):
    context={}

    sliders = HomeSlider.objects.all()
    Topcontent = TopContent.objects.all()

    context["sliders"]=sliders
    context["Topcontent"]=Topcontent
    

    return render(request, 'index.html',context)