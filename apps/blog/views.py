from django.shortcuts import render
from apps.diet_app.mixin import HttpRequest, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Blog
import random

def blog_view(request: HttpRequest) -> HttpResponse:
    context = {}
    blog_list = Blog.objects.all()
    
    
    paginator = Paginator(blog_list, 5)  
    page = request.GET.get('page') 
    
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
      
        blogs = paginator.page(1)
    except EmptyPage:
     
        blogs = paginator.page(paginator.num_pages)

    context["blogs"] = blogs
    return render(request, "pages/blog.html", context)


def blog_single_view(request: HttpRequest, slug: str) -> HttpResponse:
  context = {}
  all_blogs=Blog.objects.all()
  if all_blogs.count() > 5:
    randomized_blogs = random.sample(list(all_blogs), 5)
    random_5_blogs = randomized_blogs[:5]
    context["blogs"] = random_5_blogs
  else:
     context["blogs"] = all_blogs

  single_blog = Blog.objects.filter(slug = slug).first()

  context["blog"] = single_blog

  return render(request, "pages/blogs/blog.html", context)