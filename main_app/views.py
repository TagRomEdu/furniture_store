from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = 
    return render(request, 'main_app/index.html')


def about(request):
    return render(request, 'main_app/about.html')
