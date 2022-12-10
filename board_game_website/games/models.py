from django.db import models
from django import forms

# Create your models here.


RESERVATION_CHOICES = (
    ("NO", "NO"),
    ("YES", "YES")
)
  

  
class Games(models.Model):
        name = models.CharField(max_length=200)
    
        reservation = models.CharField(
            max_length = 20,
            choices = RESERVATION_CHOICES,
            default = 'NO'
        )
        class Modify_reservations(forms.Form):
            Reservation = forms.CharField(widget=forms.Select(choices=RESERVATION_CHOICES))

class Review(models.Model):
    my_review = models.TextField()
    games = models.ForeignKey(Games, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.my_review[:6000]}"







