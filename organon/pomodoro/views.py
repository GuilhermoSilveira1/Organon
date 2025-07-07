from django.shortcuts import render, redirect, get_object_or_404
from .models import Timers
from .forms import PomodoroForm

def pomodoro_timer(request):
    timers = Timers.objects.all().order_by('-date')
    form = PomodoroForm()
    return render(request, 'pomodoro/pomodoro_timer.html', {
        'form': form,
        'editable': False,
        'timers': timers,
    })

def new_pomodoro(request):
    if request.method == "POST":
        form = PomodoroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pomodoro")  # redireciona para a tela do timer
    else:
        form = PomodoroForm()
    
    return render(request, 'pomodoro/new_pomodoro.html', {
        'form': form
    })


def delete(request, id):
    timer = get_object_or_404(Timers, id=id)
    timer.delete()
    return redirect("pomodoro")

def history(request):
    timers = Timers.objects.all().order_by('-date')
    return render(request, 'pomodoro/pomodoro_history.html', {
        'timers': timers
    })
