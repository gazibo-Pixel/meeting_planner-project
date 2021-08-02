from django.shortcuts import render, get_object_or_404
from .models import Meeting, Room

def details (request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/details.html", {"meeting": meeting})

def room_list(request):
    return render(request, "meetings/room_list.html", {"r_list":Room.objects.all()})