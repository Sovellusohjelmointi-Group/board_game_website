from django.shortcuts import render, redirect
from .models import Games, Review
from .forms import GameForm


def index(request):
    return render(request, 'index.html')

def games(request):

    games = Games.objects.all()
    return render(request, 'games.html',
    {'games' : games})

def new_game(request):
    if request.method != 'POST': form = GameForm()
    
    else:
        form = GameForm(data=request.POST) 
        if form.is_valid(): 
            form.save()
            return redirect('board_game_website:games')
    context = {'form' : form}
    return render(request, 'new_game.html', context)


def reviews(request):

    reviews = Review.objects.all()
    return render(request, 'reviews.html',
    {'reviews' : reviews})