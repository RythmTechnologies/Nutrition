from django.shortcuts import render
from .models import AboutMe,Sertifica
# Create your views here.
def about_me(request):
    context = {}


    AboutContent = AboutMe.objects.all()
    AboutSertifica = Sertifica.objects.all().order_by('-created_at')[:1]

    context['AboutContents'] = AboutContent
    context['AboutSertifica'] = AboutSertifica

    return render(request, 'pages/about.html',context )