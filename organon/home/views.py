from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def index(request):
    if request.user.is_authenticated:
        return redirect('home')  # ou qualquer view principal
    else:
        return redirect('authentication:login')