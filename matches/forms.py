from django import forms
from .models import Match


class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = [
            "date",
            "start_time",
            "player_1",
            "player_2",
            "court",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Setting form control class and placeholder for each field
        self.fields["date"].widget.attrs.update(
            {"class": "form-control", "type": "date"}
        )
        self.fields["start_time"].widget.attrs.update(
            {"class": "form-control", "type": "time"}
        )
        self.fields["player_1"].widget.attrs.update({"class": "form-control"})
        self.fields["player_2"].widget.attrs.update({"class": "form-control"})
        self.fields["court"].widget.attrs.update({"class": "form-control"})
