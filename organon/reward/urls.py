from django.urls import path
from . import views

app_name = 'reward'

urlpatterns = [
    path('', views.rewards, name='rewards'),
    path('generate_reward', views.generate_reward, name='generate_reward'),
    path('used_reward/<int:reward_id>', views.used_reward, name='used_reward'),
    path('reward_history', views.history, name='reward_history')
]
