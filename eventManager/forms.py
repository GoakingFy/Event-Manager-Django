from django import forms 
from .models import Event

class EventsForm(forms.ModelForm):
    
    class Meta:
        model = Event
        fields = '__all__'
