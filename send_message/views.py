from django.shortcuts import render
from django.http import HttpResponse

def test(request):
    return render(request,'send_message/index.html')

def room(request, room_name):
    return render(request, "send_message/room.html", {"room_name": room_name})