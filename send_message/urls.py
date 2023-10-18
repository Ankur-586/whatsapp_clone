from django.urls import path
from . import views

urlpatterns = [
    path('',views.test),
    path("<str:room_name>/", views.room, name="room")
]