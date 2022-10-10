from django.shortcuts import render
from .models import cvelement

# Import mimetypes module
import mimetypes
# import os module
import os
# Import HttpResponse module
from django.http.response import HttpResponse


def cvsite(request):
    cvelements = cvelement.objects.all()
    return render(request, 'portfolio/homepage.html', {'cvelements': cvelements})


def contatti(request):
    cvelements = cvelement.objects.all()
    return render(request, 'portfolio/contatti.html', {'cvelements': cvelements})


def curriculum(request):
    cvelements = cvelement.objects.all()
    return render(request, 'portfolio/curriculum.html', {'cvelements': cvelements})

# File downlaoder


def download_file(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'sample.pdf'
    filepath = BASE_DIR + '/download/' + filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response
