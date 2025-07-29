from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Subtask
from .forms import TaskForm, SubtaskForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.template.loader import render_to_string
from django.http import JsonResponse

@login_required
def tasks(request): 
    tasks = Task.objects.filter(user=request.user, is_completed=False).order_by('-updated_at')
    return render(request, 'task/tasks.html', {
        'tasks': tasks
    })

# View de nova tarefa
@login_required
def new_task(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.user = request.user
            task.save()
    else:
        task_form = TaskForm()

    return render(request, 'task/new_task.html', {
        'form': task_form,
    })

# View de nova subtarefa
@login_required
def new_subtask(request, task_id=None):
    subtask_form = SubtaskForm()
    html = render_to_string('task/partials/subtask_form.html', {'form': subtask_form})
    return JsonResponse({'form_html': html})

@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    return render(request, 'task/task_detail.html', {
        'task': task,
    })

def delete(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect("task:tasks")

@login_required
def history(request):
    tasks = Task.objects.filter(user=request.user, is_completed=True).order_by('-updated_at')
    return render(request, 'task/task_history.html', {
        'tasks': tasks
    })

@login_required
@require_POST
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.is_completed = True
    task.save()
    return redirect('task:tasks')
