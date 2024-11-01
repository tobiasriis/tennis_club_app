from django.db import models

# Create your models here.


class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
