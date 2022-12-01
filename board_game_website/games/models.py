from django.db import models


# Create your models here.


RESERVATION_CHOICES = (
    ("N", "NO"),
    ("Y", "YES")
)
  

  
class Games(models.Model):
      name = models.CharField(max_length=200)
    
      reservation = models.CharField(
        max_length = 20,
        choices = RESERVATION_CHOICES,
        default = 'N'
        )

def __str__(self):
    return self.name


