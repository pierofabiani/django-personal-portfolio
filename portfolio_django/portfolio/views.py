from django.shortcuts import render
from .models import cvelement


def cvsite(request):
    cvelements = cvelement.objects.all()
    return render(request, 'portfolio/homepage.html', {'cvelements': cvelements})
