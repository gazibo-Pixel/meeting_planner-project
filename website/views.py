from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting
from Creative.models import Name

def welcome(request):
    return render(request, 'website/welcome.html', 
    {
    'meetings':Meeting.objects.all(), 
    'create':Name.objects.all()})

def today(request):
    return HttpResponse('This page is serving you some Pho at :' + str(datetime.now))

def about(request):
    return HttpResponse('Written by Mohamed Taha')
