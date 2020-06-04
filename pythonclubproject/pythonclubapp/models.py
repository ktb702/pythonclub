from django.db import models
from django.contrib.auth.models import User

# Python Club Models

# MEETING MODEL #
#This model includes meeting title, meeting date, meeting time, location and agenda.
class Meeting(models.Model):
    meetingtitle = models.CharField(max_length=255)
    meetingdate = models.DateField()
    meetingtime =  models.TimeField()
    meetinglocation = models.CharField(max_length=255)
    meetingagenda = models.TextField(null=True, blank=True)

    #defines what prints when we print 'Meeting'. Default is object1
    def __str__(self):
        return self.meetingtitle
    
    #sub-class that defines metadata of class Meeting.
    class Meta():
        db_table='meeting'


# MEETING MINUTES MODEL #
#This model includes meeting id(FK), attendance(many-to-many field with User)
# and minutes text.
class MeetingMinutes(models.Model):
    meetingid = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    attendance = models.ManyToManyField(User)
    minutes = models.TextField()

    def __str__(self):
        return self.minutes
    
    class Meta():
        db_table='meetingminutes'

# RESOURCE MODEL #
#This model includes resource name, resource type, URL, date entered, 
# user ID (foreign key with User), and description.
class Resource(models.Model):
    resource = models.CharField(max_length=255)
    resourcetype = models.CharField(max_length=255)
    resourceurl = models.URLField(null=True, blank=True)
    resourcedate = models.DateField()
    userid = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    resourcedesc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.resource
    
    class Meta():
        db_table = 'resource'
        verbose_name_plural = 'resources'

# EVENT MODEL #
#This model includes event title, location, date, time, desc, and user ID of member who posted it. 
class Event(models.Model):
    event = models.CharField(max_length=255)
    eventlocation = models.CharField(max_length=255)
    eventdate = models.DateField()
    eventtime = models.TimeField()
    eventdesc = models.TextField()
    userid = models.ForeignKey(User, on_delete=models.DO_NOTHING) 

    def __str__(self):
        return self.event
    
    class Meta():
        db_table = 'event'
        verbose_name_plural = 'events'


