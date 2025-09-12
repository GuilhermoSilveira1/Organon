from django.shortcuts import render, redirect
from task.models import Task

def home(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user, is_completed=False).order_by('-created_at')[:5]
        return render(request, 'home/home.html', {'tasks': tasks})
    else:
        return redirect('authentication:login')