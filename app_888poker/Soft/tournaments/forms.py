from django import forms
from .models import Tournaments

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournaments
        fields = [
            'name',
            'date',
            'buy_in',
            'players',
            'prizepool',
            'status',
            'type',
            'game_type'
        ]