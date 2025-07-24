from django.urls import path
from . import views

app_name = 'task'

urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('new', views.new_task, name='new'),
    path('new-subtask/', views.new_subtask, name='new_subtask'),
    path('<int:task_id>/', views.task_detail, name='task_detail'),
    path('<int:task_id>/complete/', views.complete_task, name='complete_task'),
    path('history', views.history, name='task_history'),
]
