from django.shortcuts import render, redirect
from apps.diet_app.mixin import HttpRequest, HttpResponse, RedirectOrResponse
from .models import Blog


def blog_view(request: HttpRequest) -> HttpResponse:
  context = {}
  blog = Blog.objects.all()
  context["blogs"] = blog

  return render(request, "pages/blog.html", context)


def blog_single_view(request: HttpRequest, slug: str) -> HttpResponse:

  context = {}
  single_blog = Blog.objects.filter(slug = slug).first()
  context["blog"] = single_blog

  return render(request, "pages/blogs/blog.html", context)