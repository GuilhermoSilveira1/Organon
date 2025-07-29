from django.db import models
from django.contrib.auth.models import User

class Reward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    used = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.description} ({'usada' if self.used else 'pendente'})"
