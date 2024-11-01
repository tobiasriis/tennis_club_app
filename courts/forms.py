from django import forms
from .models import (
    Court,
    Reservation,
)
from django.core.exceptions import ValidationError
from datetime import datetime, time, timedelta


class CourtForm(forms.ModelForm):
    class Meta:
        model = Court
        fields = [
            "name",
            "surface_type",
            "location",
        ]  # Adjust fields as per your model

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter court name"}
        )
        self.fields["surface_type"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Select surface type"}
        )
        self.fields["location"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter court location"}
        )


class ReservationForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={"type": "time"}))

    class Meta:
        model = Reservation
        fields = ["court", "player", "date", "start_time"]  # Removed end_time

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        start_time = cleaned_data.get("start_time")

        # Ensure that end_time is exactly one hour after start_time
        if start_time and date:
            end_time = (datetime.combine(date, start_time) + timedelta(hours=1)).time()
            cleaned_data["end_time"] = (
                end_time  # Set end_time in cleaned_data, but not in form fields
            )

            # Optionally check if the end_time is valid
            if end_time < time(9, 0) or end_time > time(
                21, 0
            ):  # Assuming court hours are 9 AM to 9 PM
                raise ValidationError(
                    "Reservation must end between 9:00 AM and 9:00 PM."
                )

        return cleaned_data
