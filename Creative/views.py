from django.shortcuts import render, get_object_or_404
from .models import Name

def create(request, id):
    info = get_object_or_404(Name, pk=id )
    num = Name.objects.count()
    return render(request, "Creative/create.html", {'info':info, 'num':num})