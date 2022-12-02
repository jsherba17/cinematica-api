from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from movie.mixins import GetSerializerMixin
from .serializers import *

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class RegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class CinemaViewSet(viewsets.ModelViewSet):
	queryset = Cinema.objects.all()
	serializer_class = CinemaSerializer


class RoomViewSet(GetSerializerMixin, viewsets.ModelViewSet):
	queryset = Room.objects.all()
	serializer_class = RoomSerializer
	create_update_serializer = RoomCreateSerializer


class SeatViewSet(GetSerializerMixin, viewsets.ModelViewSet):
	queryset = Seat.objects.all()
	serializer_class = SeatSerializer
	create_update_serializer = SeatCreateSerializer


class TicketViewSet(GetSerializerMixin ,viewsets.ModelViewSet):
	queryset = Ticket.objects.all()
	serializer_class = TicketSerializer
	create_update_serializer = TicketCreateSerializer


class TypeTicketViewSet(viewsets.ModelViewSet):
	queryset = TypeTicket.objects.all()
	serializer_class = TypeTicketSerializer


class BookViewSet(GetSerializerMixin, viewsets.ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	create_update_serializer = BookCreateSerializer


class SessionViewSet(GetSerializerMixin,viewsets.ModelViewSet):
	queryset = Session.objects.all()
	serializer_class = SessionSerializer
	create_update_serializer = SessionCreateSerializer



class MovieViewSet(GetSerializerMixin, viewsets.ModelViewSet):
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer
	create_update_serializer = MovieCreateSerializer


class GenreViewSet(viewsets.ModelViewSet):
	queryset = Genre.objects.all()
	serializer_class = GenreSerializer
