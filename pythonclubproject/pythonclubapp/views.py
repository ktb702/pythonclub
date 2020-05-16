from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.
def index (request):
    return render(request, 'pythonclubapp/index.html')

#View that returns all the resources
def getResources (request):
    resource_list = Resource.objects.all()
    return render(request, 'pythonclubapp/resource.html', {'resource_list' : resource_list})

#View that returns all the meetings
def getMeetings (request):
    meeting_list = Meeting.objects.all()
    return render(request, 'pythonclubapp/meeting.html', {'meeting_list' : meeting_list})

#This view takes parameter int ID and retrieves the meeting with that ID.
def meetingDetails(request, id):
    details=get_object_or_404(Meeting, pk=id)
    #reviews=Review.objects.filter(product=id).count()
    context={
        'meeting' : details,
        #'discount' : discount,
        #'reviews' : reviews,
    }
    return render(request, 'pythonclubapp/details.html', context=context)
