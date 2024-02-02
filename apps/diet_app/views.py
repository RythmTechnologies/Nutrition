from django.shortcuts import render
from .models import HomeSlider,TopContent
from apps.blog.models import Blog
# Create your views here.
def index(request):
    context={}

    sliders = HomeSlider.objects.all()
    Topcontent = TopContent.objects.all()
    blogs = Blog.objects.all().order_by('-created_at')[:8]
    context["sliders"]=sliders
    context["Topcontent"]=Topcontent
    context['blogs'] = blogs
    

    return render(request, 'index.html',context)