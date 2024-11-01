from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Player
from .forms import PlayerForm


def index(request):
    players = Player.objects.all()
    return render(request, "users/index.html", {"players": players})


def player_detail(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    return render(request, "users/player_detail.html", {"player": player})


def add_user(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users:index")
    else:
        form = PlayerForm()

    return render(request, "users/add_user.html", {"form": form})


def edit_player(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    if request.method == "POST":
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect("users:player_detail", player_id=player.id)
    else:
        form = PlayerForm(instance=player)
    return render(request, "users/player_edit.html", {"form": form, "player": player})


def delete_player(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    if request.method == "POST":
        player.delete()
        return redirect(
            "users:index"
        )  # Redirect to the players list or any appropriate page
    return render(request, "users/player_delete.html", {"player": player})
