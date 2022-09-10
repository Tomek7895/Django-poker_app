from django.http import HttpResponse
from django.shortcuts import render
from .models import Tournaments, Game_Type, Cash_Games, Sit_Go, Spin

# def start(request):
#     tournament = Tournaments.objects.all()
#     data = {'tournament' : tournament}
#     return render(request, 'szablon.html', data)

def lobby(request):
    game_type = Game_Type.objects.all()
    all_tournaments = Tournaments.objects.all()
    data = {'game_type' : game_type,
            'all_tournaments' : all_tournaments}
    return render(request, 'szablon.html', data)

def category(request, id):
    all_tournaments = Tournaments.objects.all()
    category_type = Game_Type.objects.get(pk=id)
    game_type = Game_Type.objects.all()
    tournament_user = Tournaments.objects.get(pk=id)
    all_cashes = Cash_Games.objects.all()
    all_sit_go = Sit_Go.objects.all()
    all_spins = Spin.objects.all()
    data = {'category_type' : category_type,
            'game_type': game_type,
            'all_tournaments' : all_tournaments,
            'tournament_user' : tournament_user,
            'all_cashes' : all_cashes,
            'all_sit_go' : all_sit_go,
            'all_spins' : all_spins}
    return render(request, 'category_type.html', data)


def tournament(request, id):
    tournament_user = Tournaments.objects.get(pk=id)
    game_type = Game_Type.objects.all()
    data = {'tournament_user' : tournament_user,
            'game_type' : game_type}
    return render(request, 'tournament.html', data)
    # return HttpResponse(tournament_user.name)

def cash_game(request,id):
    cash_type = Cash_Games.objects.get(pk=id)
    game_type = Game_Type.objects.all()
    data = {'cash_type' : cash_type,
            'game_type' : game_type}
    return render (request, 'cash.html', data)

def sit_go(request,id):
    sit_go_type = Sit_Go.objects.get(pk=id)
    game_type = Game_Type.objects.all()
    data = {'sit_go_type' : sit_go_type,
            'game_type' : game_type}
    return render (request, 'sit_go.html', data)

def spin(request,id):
    spin_type = Spin.objects.get(pk=id)
    game_type = Game_Type.objects.all()
    data = {'spin_type' : spin_type,
            'game_type' : game_type}
    return render (request, 'spin.html', data)

def tournament_filers(request):
    all_tournaments = Tournaments.objects.all()
    data ={'all_tournaments' : all_tournaments}
    return render(request, 'szablon_filters.html', data)