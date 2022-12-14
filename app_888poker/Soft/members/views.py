from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from tournaments.models import Game_Type


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('')
        else:
            messages.success(request, ("There Was an Error Loggin In, Try Again..."))
            return redirect('login_user')

    else:
        game_type = Game_Type.objects.all()
        data = {'game_type' : game_type}
        return render (request, 'login.html/', data)

