from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('task/', include('task.urls', namespace='task')),
    path('auth/', include('authentication.urls', namespace='authentication')),
    path('pomodoro/', include('pomodoro.urls', namespace='pomodoro')),
    path('reward/', include('reward.urls', namespace='reward')),
]