from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'AdminSide/templates/index.html', {"title": "Royal Travels"})


def packages(request):
    return render(request, 'AdminSide/templates/Packages/Packages.html',
                  {"title": "Royal Travels"})
