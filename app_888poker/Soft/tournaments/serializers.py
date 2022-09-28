from rest_framework import serializers
from .models import Tournaments, Cash_Games, Sit_Go, Spin

class TournamentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournaments
        fields = '__all__'

class Cash_GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cash_Games
        fields = '__all__'

class Sit_GoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sit_Go
        fields = '__all__'

class SpinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spin
        fields = '__all__'