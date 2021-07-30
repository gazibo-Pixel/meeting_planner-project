from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
def welcome(request):
    return render(request, 'website/welcome.html', {'message':'This is some sort of a message!!!','message2':'Again Some Text'})

def today(request):
    return HttpResponse('This page is serving you some Pho at :' + str(datetime.now))

def about(request):
    return HttpResponse('Written by Mohamed Taha')
