from django.http import JsonResponse
from .models import Reward
import random
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

def generate_reward(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Usuário não autenticado"}, status=401)

    is_big = request.GET.get("big", "false") == "true"

    rewards = [
        "Pode comer 1 docinho 🍬",
        "Assistir 1 episódio curto de série (20 mins) 📺",
        "Tirar um cochilo de 15 minutos 😴",
        "Dar uma volta rápida no quarteirão 🚶",
        "Tomar um café ou chá especial ☕",
        "Jogar 1 partida rápida de algum jogo 🎮",
        "Ler um capítulo de um livro 📖",
        "Ouvir 1 música favorita 🎧",
        "Ficar 10 minutos sem fazer nada 😌",
        "Mandar uma mensagem para alguém querido 💬"
    ]

    big_rewards = [
        "Assistir 1 episódio de série (40 mins) 📺",
        "Comer algo especial (tipo uma sobremesa mais elaborada) 🍰",
        "Fazer uma pausa de 1 hora para lazer 🧘",
        "Sair para tomar um sorvete 🍦",
        "Comprar algo pequeno que você queria 🛍️",
        "Jogar videogame por 1 hora 🎮",
        "Fazer uma caminhada mais longa no parque 🌳",
        "Assistir a um filme 🎬",
        "Fazer uma atividade criativa (desenhar, pintar, escrever) 🎨",
        "Planejar uma pequena saída com amigos ou família 👨‍👩‍👧‍👦"
    ]

    chosen = random.choice(big_rewards if is_big else rewards)

    reward = Reward.objects.create(user=request.user, description=chosen)

    return JsonResponse({"reward": reward.description})

def rewards(request):
    if not request.user.is_authenticated:
        return redirect("login")

    rewards = Reward.objects.filter(user=request.user, used=False).order_by("-created_at")
    return render(request, "rewards/rewards.html", {"rewards": rewards})

@login_required
@require_POST
def used_reward(request, reward_id):
    reward = get_object_or_404(Reward, id=reward_id, user=request.user)
    reward.is_completed = True
    reward.save()
    return redirect('reward:rewards')

@login_required
def history(request):
    rewards = Reward.objects.filter(user=request.user, is_completed=True).order_by('-updated_at')
    return render(request, 'reward/reward_history.html', {
        'rewards': rewards
    })