from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('auth/', include('authentication.urls')),
    path('task/', include('task.urls')),
    path('pomodoro/', include('pomodoro.urls')),
    path('reward/', include('reward.urls')),
]