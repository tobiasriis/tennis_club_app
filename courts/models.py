from django.db import models


class Court(models.Model):
    name = models.CharField(max_length=100)
    surface_type = models.CharField(max_length=50)  # e.g., clay, grass, hard
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    player = models.ForeignKey(
        "users.Player", on_delete=models.CASCADE
    )  # assuming you have a Player model
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"Reservation for {self.player} on {self.date} from {self.start_time} to {self.end_time}"
