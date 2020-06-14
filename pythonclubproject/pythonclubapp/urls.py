from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getResources/', views.getResources, name='resources'),
    path('getMeetings/', views.getMeetings, name='meetings'),
    path('getMeetingDetails/<int:id>', views.meetingDetails, name='details'),
    path('newMeeting/', views.newMeeting, name='newmeeting'),
    path('newResource/', views.newResource, name='newresource'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]