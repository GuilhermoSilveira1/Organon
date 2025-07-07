from django.urls import path
from . import views

urlpatterns = [
 path('', views.pomodoro_timer, name='pomodoro'),
 path('new', views.new_pomodoro, name='new_pomodoro'),
 path('history', views.history, name='pomodoro_history'),
]
