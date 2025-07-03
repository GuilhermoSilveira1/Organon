from django.shortcuts import render, redirect
from .models import Timers
from django.contrib.auth.models import User
from .forms import PomodoroForm
from django.db.models import Sum, F, ExpressionWrapper, fields

def pomodoro_timer(request):
  timers = Timers.objects.all()
  form = PomodoroForm() 
  
  return render(request, 'pomodromo_timer.html', {
      'form': form,
      'editable': False,
      'timers': timers,
  })

def add(request,id):
    editable = True
    if request.method == "POST":
        editable = False
        form = PomodoroForm(request.POST)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.id = id
            form_instance.save()
            return redirect("pomodoro_timer")
    else:
        form = PomodoroForm()
        timers = Timers.objects.all()
        return render(request, 'pomodromo_timer.html', {
            'form': form,
            "editable": editable,
            'timers': timers
        })

def delete(request, id):
    timers = Timers.objects.get(id=id)
    timers.delete()
    print("Successfully Deleted {{id}}")
    timers = Timers.objects.all()
    form = PomodoroForm()
    if len(timers) == 0:
        return render(request, 'pomodromo_timer.html', {
            'form': form,
            "editable": False,
            'timers': None
        })
    return render(request, 'pomodromo_timer.html', {
        'form': form,
        "editable": False,
        'timers': timers
    })

def history(request):
    return render('pomodoro_history.html')