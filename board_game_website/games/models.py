from django.db import models

# Create your models here.


class Games(models.Model):
    #Field for the name
    #game name
    name = models.CharField(max_length=200)
    #tää on vaa täs :D

    authors = models.JSONField()
    def __str__(self):
        return self.name

SEMESTER_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
)
  
# declaring a Student Model
  
class Student(models.Model):
      semester = models.CharField(
        max_length = 20,
        choices = SEMESTER_CHOICES,
        default = '1'
        )


