"""Soft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tournaments.views import *
from users import views as user_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lobby, name='lobby'),
    path('tournament/<id>/', tournament, name='tournament'),
    path('game_type/<id>/', category, name='game_type'),
    path('cash/<id>/', cash_game, name='cash_game'),
    path('sit_go/<id>/', sit_go, name='sit_go'),
    path('spin/<id>/', spin, name='spin'),
    path('create', tournament_create_view),
    path('game_type/<id>/filter/', filter),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('register/', user_views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('profile/', user_views.profile, name="profile"),
    path('', include('tournaments.urls')),
]
