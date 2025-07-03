from django import forms
from .models import Timers

class PomodoroForm(forms.ModelForm):
  class Meta:
      model = Timers
      fields = ['id','date', 'weekday', 'sessions', 'focused_time','break_time', 'category', 'notes']
      widgets = {
          'sessions': forms.NumberInput(attrs={'required': 'required'}),
          'focused_time': forms.NumberInput(attrs={'required': 'required'}),
          'break_time': forms.NumberInput(attrs={'required': 'required'}),
          'category': forms.TextInput(attrs={'required': 'required'}),
          'notes': forms.TextInput(attrs={'required': 'required'}),
      }