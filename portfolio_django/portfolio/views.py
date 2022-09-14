from django.shortcuts import render

# Create your views here.


def cvsite(request):
    return render(request, 'portfolio/homepage.html')
