from django.shortcuts import render
from .models import cvelement


def cvsite(request):
    cvelements = cvelement.objects.all()
    return render(request, 'portfolio/homepage.html', {'cvelements': cvelements})


def contatti(request):
    cvelements = cvelement.objects.all()
    return render(request, 'portfolio/contatti.html', {'cvelements': cvelements})


def curriculum(request):
    cvelements = cvelement.objects.all()
    return render(request, 'portfolio/curriculum.html', {'cvelements': cvelements})
