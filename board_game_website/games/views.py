from django.shortcuts import render
from .models import Games

# Create your views here.
def index(request):
    return render(request, 'index.html')

def games(request):

    games = Games.objects.all()
    return render(request, 'games.html',
    {'games' : games})