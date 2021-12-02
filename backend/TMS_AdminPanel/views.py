from django.shortcuts import render
from .DBContent import DBContent
# Create your views here.


def index(request):
    return render(request, 'AdminSide/templates/index.html', {"title": "Royal Travels"})


def packages(request):
    data = {"title": "Royal Travels",
            "packages": DBContent.getAllPacakges(), "booking": 700}
    return render(request, 'AdminSide/templates/Packages/Packages.html',
                  data)
