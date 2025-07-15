from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

dias_semana = {
    'Monday': 'Segunda-feira',
    'Tuesday': 'Terça-feira',
    'Wednesday': 'Quarta-feira',
    'Thursday': 'Quinta-feira',
    'Friday': 'Sexta-feira',
    'Saturday': 'Sábado',
    'Sunday': 'Domingo',
}

class Timers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)
    weekday = models.CharField(max_length=20, editable=False)
    sessions = models.IntegerField()
    focused_time = models.IntegerField(help_text="Tempo de foco em minutos")
    break_time = models.IntegerField(help_text="Tempo de descanso em minutos")
    category = models.CharField(max_length=50)
    notes = models.CharField(max_length=250, blank=True)

    def save(self, *args, **kwargs):
        if not self.weekday:
            dia_en = timezone.now().strftime('%A')
            self.weekday = dias_semana.get(dia_en, dia_en)
        super().save(*args, **kwargs)
