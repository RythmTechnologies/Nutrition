from django.shortcuts import render, redirect
from apps.diet_app.mixin import HttpRequest, HttpResponse ,RedirectOrResponse
from .models import Services


def services(request: HttpRequest) -> HttpResponse:
    context = {}
    model = Services.objects.all()
    context['services'] = model
    return render(request, 'pages/services.html', context)


def services_spor(request: HttpRequest, slug: str) -> RedirectOrResponse:
    context = {}
    model_filter = Services.objects.filter(slug = slug).first()
    if not model_filter:
        return redirect('services')
    else:
        context['service'] = model_filter
    return render(request, 'pages/services/diets.html', context)


def test():
    pass