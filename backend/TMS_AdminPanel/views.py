from django.shortcuts import render
from .DBContent import DBContent
# Create your views here.


def index(request):
    return render(request, 'AdminSide/templates/index.html', {"title": "Dashboard"})


def packages(request):
    data = {
        "title": "Packages", "packages": DBContent.getAllPacakges(),
    }
    print(data)
    return render(request, 'AdminSide/templates/Packages/Packages.html',  data)
