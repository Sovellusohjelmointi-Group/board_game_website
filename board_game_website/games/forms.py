from django import forms
from .models import Games

class GameForm(forms.modelForm):
    class Meta:
        model = Games
        fields = ['text']
        labels = {'text':''}