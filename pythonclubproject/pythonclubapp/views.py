from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import MeetingForm, ResourceForm
from django.contrib.auth.decorators import login_required

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

#create view for new meeting form 
@login_required
def newMeeting(request):
    meeting_form = MeetingForm
    if request.method == 'POST':
        meeting_form = MeetingForm(request.POST)
        #if form is valid, save it and load the empty form. It's also possible to redirect to another page.
        if meeting_form.is_valid():
            post = form.save(commit=True)
            post.save()
            meeting_form = MeetingForm()
    else: #if it isn't a POST or form is not valid, load empty form
        meeting_form = MeetingForm()
    return render(request, 'pythonclubapp/newmeeting.html', {'meeting_form': meeting_form})

#create view for new resource form 
@login_required
def newResource(request):
    resource_form = ResourceForm
    if request.method == 'POST':
        resource_form = ResourceForm(request.POST)
        #if form is valid, save it and load the empty form. It's also possible to redirect to another page.
        if resource_form.is_valid():
            post = form.save(commit=True)
            post.save()
            resource_form = ResourceForm()
    else: #if it isn't a POST or form is not valid, load empty form
        resource_form = ResourceForm()
    return render(request, 'pythonclubapp/newresource.html', {'resource_form': resource_form})

#create view for the login
def loginmessage(request):
    return render(request, 'pythonclubapp/loginmessage.html')

#create view for logout
def logoutmessage(request):
    return render(request, 'pythonclubapp/logoutmessage.html')