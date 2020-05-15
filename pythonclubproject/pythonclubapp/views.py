from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.
def index (request):
    return render(request, 'pythonclubapp/index.html')

#View that returns all the resources
def getResources (request):
    resource_list = Resource.objects.all()
    return render(request, 'pythonclubapp/resource.html', {'resource_list' : resource_list})