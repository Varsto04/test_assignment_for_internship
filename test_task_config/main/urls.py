from django.urls import path
from . import views


urlpatterns = [
    path('ping/', views.ping, name='ping'),
    path('health/', views.health, name='health'),
    path('list/', views.list_weather, name='list_weather'),
    path('add/', views.add_weather, name='add_weather')
]