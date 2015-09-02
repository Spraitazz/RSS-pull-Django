from django.shortcuts import render
from .models import Item, Getter
from django.http import HttpResponse

# Create your views here.
def index(request):   
    context = {
    "items": Item.objects.all(),
    "getter": Getter
    }
    return render(request, "pull/index.html", context)
    
def GetFeed(request):
    return HttpResponse(Getter.getFeed(request.GET.get("userLastDate","")))