from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Court, Reservation  # Adjust based on your actual model location
from datetime import timedelta, date
from .forms import CourtForm, ReservationForm


# List all courts
def index(request):
    courts = Court.objects.all()
    return render(request, "courts/index.html", {"courts": courts})


# Detail view for a specific court
def court_detail(request, court_id):
    court = get_object_or_404(Court, id=court_id)
    reservations = Reservation.objects.filter(court=court, date__gte=date.today())
    print("reservations_today_or_greater", reservations)
    for reservation in reservations:
        print(reservation.player.full_name(), reservation.date, reservation.start_time)
    return render(
        request,
        "courts/court_detail.html",
        {"court": court, "reservations": reservations},
    )


def court_add(request):
    if request.method == "POST":
        form = CourtForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("courts:court_add")
    else:
        form = CourtForm()
    return render(request, "courts/courts_add.html", {"form": form})


def court_edit(request, court_id):
    court = get_object_or_404(Court, id=court_id)
    if request.method == "POST":
        form = CourtForm(request.POST, instance=court)
        if form.is_valid():
            form.save()
            return redirect("courts:court_detail", court_id=court.id)
    else:
        form = CourtForm(instance=court)
    return render(request, "courts/court_edit.html", {"form": form, "court": court})


def court_delete(request, court_id):
    court = get_object_or_404(Court, id=court_id)
    if request.method == "POST":
        court.delete()
        return redirect("courts:court_detail")
    return render(request, "courts/delete_court.html", {"court": court})


def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(
        request, "courts/reservation_list.html", {"reservations": reservations}
    )


def reservation_add(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user  # Assuming the user is logged in

            # Set end_time from the cleaned data
            end_time = form.cleaned_data.get("end_time")
            reservation.end_time = end_time  # Save the computed end_time

            reservation.save()
            return redirect("courts:reservation_list")
    else:
        form = ReservationForm()
    return render(request, "courts/reservation_form.html", {"form": form})
