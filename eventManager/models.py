from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()

def publish(self):
        self.save()

def __str__(self):
        return self.title