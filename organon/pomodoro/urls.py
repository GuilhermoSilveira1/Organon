from django.urls import path
from . import views

app_name = 'pomodoro'

urlpatterns = [
# Caminho para a tela home, que o usuário usa para encontrar as outras telas
 path('home', views.home, name='home'),
 path('new', views.new_pomodoro, name='new'),
 path('history', views.history, name='history'),
# Esse é o caminho que mostra na tela para o usuário o timer que ele acabou de criar
 path('<int:timer_id>/', views.pomodoro_timer, name='pomodoro'),
# Esse é o caminho que envia os dados do último timer para o front, para mostrar na tela
 path('api/<int:timer_id>', views.pomodoro_api, name='pomodoro_api'),
]