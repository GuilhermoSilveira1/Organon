from django.db import models

class Timers(models.Model):
    id = models.IntegerField().primary_key
    date = models.DateField()
    weekday = models.DateField() # necessário fazer um tratamento aqui
    sessions = models.IntegerField()
    focused_time = models.IntegerField()
    break_time = models.IntegerField()
    category = models.CharField(max_length=50)
    notes = models.CharField(max_length=250)