from django.urls import path
from . import views

app_name = 'board_game_website'

urlpatterns = [
    #home page
path('', views.index, name='index'),

path('games/', views.games, name='games'),

]