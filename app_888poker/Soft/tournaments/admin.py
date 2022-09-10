from django.contrib import admin
from .models import Tournaments, Game_Type, Cash_Games, Sit_Go, Spin

admin.site.register(Tournaments)
admin.site.register(Game_Type)
admin.site.register(Cash_Games)
admin.site.register(Sit_Go)
admin.site.register(Spin)

