from django.urls import path, include
from .views import TournamentViewSet, Cash_GamesViewSet, Sit_GoViewSet, SpinViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('tournament', TournamentViewSet, basename='tournament')
router.register('cash_game', Cash_GamesViewSet, basename='cash')
router.register('sit_go', Sit_GoViewSet, basename='sit_go')
router.register('spin', SpinViewSet, basename='spin')


urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<id>/', include(router.urls)),
    ]