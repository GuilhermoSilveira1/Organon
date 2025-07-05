from django.db import models
import datetime

class Timers(models.Model):
    date = models.DateField(auto_now_add=True)
    weekday = models.CharField(max_length=20, editable=False)
    sessions = models.IntegerField()
    focused_time = models.IntegerField(help_text="Tempo de foco em minutos")
    break_time = models.IntegerField(help_text="Tempo de descanso em minutos")
    category = models.CharField(max_length=50)
    notes = models.CharField(max_length=250, blank=True)

    def save(self, *args, **kwargs):
        if not self.weekday:
            self.weekday = self.date.strftime('%A')  # Ex: 'Thursday'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.date} - {self.category}"
