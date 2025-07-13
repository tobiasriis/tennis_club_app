from django.shortcuts import render
from django.conf import settings
from django.urls import reverse, NoReverseMatch
from datetime import date, datetime
from courts.models import Court, Reservation
from users.models import Player
from matches.models import Match


def installed_apps_view(request):
    # Get statistics for dashboard
    courts_count = Court.objects.count()
    players_count = Player.objects.count()
    matches_count = Match.objects.filter(date=date.today()).count()
    reservations_count = Reservation.objects.filter(date__gte=date.today()).count()
    
    # Get recent activity
    today_reservations = Reservation.objects.filter(
        date=date.today()
    ).select_related('court', 'player').order_by('start_time')[:5]
    
    upcoming_matches = Match.objects.filter(
        date__gte=date.today()
    ).select_related('player_1', 'player_2', 'court').order_by('date', 'start_time')[:5]
    
    context = {
        'courts_count': courts_count,
        'players_count': players_count,
        'matches_count': matches_count,
        'reservations_count': reservations_count,
        'today_reservations': today_reservations,
        'upcoming_matches': upcoming_matches,
    }
    
    return render(request, "installed_apps.html", context)
