from django.http import HttpResponse
from django.shortcuts import redirect, render

from tasks.models import Collection

def index(request):
    context = {}
    context["collections"] = Collection.objects.order_by("name")
    return render(request, 'tasks/index.html', context=context)

def add_collection(request):
    print(request.POST)
    collection_name = request.POST.get("collection-name")
    Collection.objects.create(name=collection_name)
    return redirect("home")
