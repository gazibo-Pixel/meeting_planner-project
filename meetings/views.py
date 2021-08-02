from django.shortcuts import render, get_object_or_404
from .models import Meeting, Room
from django.forms import modelform_factory
def details (request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/details.html", {"meeting": meeting})

def room_list(request):
    return render(request, "meetings/room_list.html", {"r_list":Room.objects.all()})

MeetingForm = modelform_factory(Meeting, exclude=[])

def new(request):
    form = MeetingForm()
    return render(request, "meetings/new.html", {'form':form})