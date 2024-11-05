from django.shortcuts import render
from .forms import MatchForm

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Match  # Adjust based on your actual model location
from datetime import timedelta, date


def index(request):
    matches = Match.objects.all()
    return render(request, "matches/index.html", {"matches": matches})


def match_detail(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    return render(
        request,
        "courts/match_detail.html",
        {"match": match},
    )


def match_add(request):
    if request.method == "POST":
        form = MatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("matches:match_list")
    else:
        form = MatchForm()
    return render(request, "matches/match_add.html", {"form": form})


def match_edit(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    if request.method == "POST":
        form = MatchForm(request.POST, instance=match)
        if form.is_valid():
            form.save()
            return redirect("matches:match_detail", match_id=match.id)
    else:
        form = MatchForm(instance=match)
    return render(request, "matches/match_edit.html", {"form": form, "match": match})


def match_delete(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    if request.method == "POST":
        match.delete()
        return redirect(
            "matches:match_list"
        )  # Redirect to a list or index view of matches
    return render(request, "matches/match_delete.html", {"match": match})
