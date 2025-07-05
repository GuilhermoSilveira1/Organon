from django.urls import path
from . import views

urlpatterns = [
 path('pomodoro/', views.pomodoro_timer, name='pomodoro'),
 path('pomodoro/config', views.add, name='pomodoro_config'),
 path('pomodoro/history', views.history, name='pomodoro_history'),
]
