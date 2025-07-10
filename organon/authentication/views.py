from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Usuário já existe.')
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('login')
    return render(request, 'authentication/signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # ou qualquer página principal
        else:
            messages.error(request, 'Credenciais inválidas.')
    return render(request, 'authentication/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
