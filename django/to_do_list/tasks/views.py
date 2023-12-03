from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'tasks/index.html', context={})

def add_collection(request):
    return HttpResponse("Yolo")
