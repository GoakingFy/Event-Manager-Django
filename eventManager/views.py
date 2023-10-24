from django.shortcuts import render
from .models import Event
from .forms import EventsForm
from django.shortcuts import redirect
# Create your views here.

def indexed(request):
    return render(request, "eventManager/index.html")

def list_events(request):
    evnt = Event.objects.all()
    return render(request, "eventManager/events_list.html" , {"events" : evnt})

def create_events(request):
    if request.method == "POST":
        form = EventsForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            author_event = request.user
            event.save()
            return redirect("events_list")
    else:
        form = EventsForm()
    return render(request, "eventManager/create_events.html" , {"Event_form": form})