from django.shortcuts import render
from .models import AboutMe,Sertifica
# Create your views here.
def about_me(request):
    context = {}


    AboutContent = AboutMe.objects.all()
    AboutSertifica = Sertifica.objects.all()

    context['AboutContents'] = AboutContent
    context['AboutSertifica'] = AboutSertifica

    return render(request, 'pages/about.html',context )