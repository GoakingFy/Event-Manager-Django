from django.shortcuts import render

# Create your views here.

def indexed(request):
    return render(request, "eventManager/index.html")

def list_events(request):
    return render(request, "eventManager/events_list.html")