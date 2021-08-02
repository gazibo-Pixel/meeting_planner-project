from django.urls import path
from . import views
urlpatterns = [
    path('<int:id', views.details, name='detail'),
    path('room_list', views.room_list, name='room_list'),
    path ('new', views.new, name='new')
]