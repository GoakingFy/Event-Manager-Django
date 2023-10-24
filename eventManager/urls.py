from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.indexed, name='index'),
    path("events_list/" , views.list_events , name="events_list"),
    path("create_events/" , views.create_events , name="create_events")
    
]