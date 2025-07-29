from django.urls import path
from . import views

app_name = 'reward'

urlpatterns = [
    path('', views.rewards, name='rewards'),
    path('generate_reward', views.generate_reward, name='generate_reward'),
    path('used_reward', views.used_reward, name='used_reward'),
    path('history', views.history, name='history')
]
