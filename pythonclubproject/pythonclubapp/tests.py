from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
from .views import index, getResources, getMeetings, meetingDetails
from django.urls import reverse
from django.contrib.auth.models import User

# Test case for the Meeting model.
class MeetingTest(TestCase):
    def test_string(self):
        meetingtype = Meeting(meetingtitle="Intro to Pyton")
        self.assertEqual(str(meetingtype), meetingtype.meetingtitle)

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

# Test case for the MeetingMinutes model.
class MeetingMinutesTest(TestCase):
    def test_string(self):
        meetingmintype = MeetingMinutes(minutes="Today")
        self.assertEqual(str(meetingmintype), meetingmintype.minutes)

    def test_table(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')

# Test case for the Resource model.
class ResourceTest(TestCase):
    def test_string(self):
        resourcetype = Resource(resource="Books")
        self.assertEqual(str(resourcetype), resourcetype.resource)

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

# Test case for the Event model.
class EventTest(TestCase):
    def test_string(self):
        eventtype = Event(event="Developer Week")
        self.assertEqual(str(eventtype), eventtype.event)

    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

#Test cases for views
class IndexTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('index'))
       self.assertEqual(response.status_code, 200)
  
class GetResourcesTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('resource_list'))
       self.assertEqual(response.status_code, 200)

class GetMeetingsTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('meeting_list'))
       self.assertEqual(response.status_code, 200)