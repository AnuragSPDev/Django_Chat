from django.shortcuts import render
from .models import Rooms

# Create your views here.
def rooms(request):
    all_rooms = Rooms.objects.all()
    return render(request, 'rooms/available_rooms.html', {'all_rooms':all_rooms})