from django.urls import path
from . import views

app_name = 'pomodoro'

urlpatterns = [
 path('<int:timer_id>/', views.pomodoro_timer, name='pomodoro'),
 path('new', views.new_pomodoro, name='new'),
 path('history', views.history, name='pomodoro_history'),
]
