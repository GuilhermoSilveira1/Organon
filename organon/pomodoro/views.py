from django.shortcuts import render, redirect, get_object_or_404
from .models import Timers
from .forms import PomodoroForm

def pomodoro_timer(request, timer_id):
    timer = get_object_or_404(Timers, id=timer_id, user=request.user)
    return render(request, 'pomodoro/pomodoro_timer.html', {
        'timer': timer,
    })

def new_pomodoro(request):
    if request.method == "POST":
        form = PomodoroForm(request.POST)
        if form.is_valid():
            timer = form.save(commit=False)
            timer.user = request.user
            form.save()
            return redirect('pomodoro:pomodoro', timer_id=timer.id)

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
