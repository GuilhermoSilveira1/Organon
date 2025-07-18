from django import forms
from .models import Task, Subtask

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']
        labels = {
            'title': 'Título',
            'description': 'Descrição',
            'due_date': 'Prazo',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class SubtaskForm(forms.ModelForm):
     class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']
        labels = {
            'title': 'Título',
            'description': 'Descrição',
            'due_date': 'Prazo',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }   