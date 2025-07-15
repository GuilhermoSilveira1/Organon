from django import forms
from .models import Timers

class PomodoroForm(forms.ModelForm):
    class Meta:
        model = Timers
        fields = ['sessions', 'focused_time', 'break_time', 'category', 'notes']
        labels = {
            'sessions': 'Sessões',
            'focused_time': 'Tempo de foco (min)',
            'break_time': 'Tempo de pausa (min)',
            'category': 'Categoria',
            'notes': 'Notas',
        }
        widgets = {
            'sessions': forms.NumberInput(attrs={'min': 1}),
            'focused_time': forms.NumberInput(attrs={'min': 1}),
            'break_time': forms.NumberInput(attrs={'min': 1}),
            'category': forms.TextInput(),
            'notes': forms.Textarea(attrs={'rows': 2}),
        }