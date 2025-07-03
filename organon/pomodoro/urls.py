from django.urls import path

urlpatterns = [
    path('pomodoro/', 'pomodoro.html', name='pomodoro'),
    path('pomodoro/config', 'pomodoro_config.html', name='pomodoro_config'),
    path('pomodoro/history', 'pomodoro_history.html', name='pomodoro_history')
]