from django.shortcuts import render, redirect
from .models import BoardGame

# Create your views here.

def index(request):
    if request.method == 'GET':
        context = {
            "games": BoardGames.objects.all()
        }
        return render(request, 'boardgames/index.html', context)
    elif request.method == 'POST':
        game = BoardGame()
        game.name  = request.POST["name"]
        game.rating  = request.POST["rating"]
        game.review  = request.POST["review"]
        game.save()
        return redirect(request, f'/boardgames/{game.id}/')

def create(request):
    return render(request, 'boardgames/create_form.html')

def details(request, game_id):
    game = BoardGame.objects.get(pk=game_id)
    context = {
        "game": game
    }
    return render(request, 'boardgsmes/details.html', context)

def edit(request, game_id):
    game = BoardGame.objects.get(pk=game_id)
    context = {
        "game": game
    }
    return render(request, 'boardgames/edit_form/html', context)
