from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def log_out(request):
    return render(request, 'registration/log_out.html')

def register(request):

    if request.method != 'POST':

        form = UserCreationForm()
    else:

        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()

            login(request, new_user)
            return redirect('board_game_website:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)