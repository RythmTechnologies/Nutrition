from django.shortcuts import render
from .models import TopContent
from apps.blog.models import Blog
from apps.social.models import SocialMedia
from apps.google_comment.models import GoogleComment
# Create your views here.
def index(request):
    context={}

    Topcontent = TopContent.objects.all()
    blogs = Blog.objects.all().order_by('-created_at')[:8]

    comments = GoogleComment.objects.all()
    context["Topcontent"]=Topcontent
    context['blogs'] = blogs
    context['google_comments'] = comments


    return render(request, 'index.html',context)

def footer_context(request):
    socialmedia=SocialMedia.objects.all()

    context = {}
    context['socialmedia'] = socialmedia

    return context