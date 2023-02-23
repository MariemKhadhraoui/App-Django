from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def homePage(request):
    return HttpResponse('<h1>Title Here</h1>')

def homePage1(request):
    return render(
        request,
        'events/homePage.html'
    )

def listEventsStatic(request):
    #affichage statique 
    list = [ {
            'title': 'Event1',
            'description': 'description2'
        },
        {
            'title': 'Event2',
            'description': 'description2'
        },
        {
            'title': 'Event3',
            'description': 'description3'
        }]
    return render(
        request, 
        'events/listEvents.html',
        {
        'events': list
        }

    )
def listEvents(request):
    #pour afficher les objet dynamique 
    list = Event.objects.all()
    return render(request, 
        'events/listEvents.html',
        {
        'events': list
        })
