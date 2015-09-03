from django.shortcuts import render
from .models import Item, Getter
from django.http import HttpResponse


def index(request):   
    context = {}
    return render(request, "pull/index.html", context)
    
def GetFeed(request):
    return HttpResponse(Getter.getFeed(request.GET.get("userLastDate","")))