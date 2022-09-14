from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from tournaments.models import Game_Type
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created. You are now allowed to Log In!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    game_type = Game_Type.objects.all()
    data = {'game_type': game_type,
            'form' : form}
    return render(request, 'users/register.html', data )

@login_required
def profile(request):
    game_type = Game_Type.objects.all()
    data = {'game_type': game_type}
    return render(request, 'users/profile.html', data)

