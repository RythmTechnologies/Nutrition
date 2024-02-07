from django.shortcuts import render, redirect
from apps.diet_app.mixin import HttpRequest, HttpResponse ,RedirectOrResponse
from .models import Services


def services(request: HttpRequest) -> HttpResponse:
    context = {}
    model = Services.objects.all()
    context['services'] = model
    return render(request, 'pages/services.html', context)