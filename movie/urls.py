from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'cinema', CinemaViewSet, basename='cinema')
router.register(r'room', RoomViewSet, basename='room')
router.register(r'seat', SeatViewSet, basename='seat')
router.register(r'ticket', TicketViewSet, basename='ticket')
router.register(r'typeticket', TypeTicketViewSet, basename='typeticket')
router.register(r'book', BookViewSet, basename='book')
router.register(r'session', SessionViewSet, basename='session')
router.register(r'movie', MovieViewSet, basename='movie')
router.register(r'genre', GenreViewSet, basename='genre')
router.register(r'register', RegisterView, basename='register')
 


urlpatterns += router.urls
