from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from movie.managers import CustomUserManager
from django.contrib.auth.models import PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	balance = models.IntegerField(default=0)
	discount = models.IntegerField(default=0)
	phone = models.CharField(max_length=255)
	username = models.CharField(max_length=255, unique=True, null=True)
	password = models.CharField(max_length=255)
	is_staff = models.BooleanField(default=False)
	USERNAME_FIELD = "username"
	REQUIRED_FIELDS = ["first_name", "last_name"]

	objects = CustomUserManager()

	def __str__(self):
		return self.first_name

class Cinema(models.Model):
	title = models.CharField(max_length=255)
	description = models.CharField(max_length=500)
	schedule = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	contacts = models.CharField(max_length=255)

	def __str__(self):
		return self.title

class Genre(models.Model):
	film_genre = models.CharField(max_length=255)
	
	def __str__(self):
		return f"Genre - {self.film_genre}"


class Movie(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=500, null=True)
	year = models.CharField(max_length=255, null=True)
	country = models.CharField(max_length=255, null=True, blank=True)
	genres = models.ManyToManyField(Genre, related_name='movies', blank=True)
	date = models.DateField(auto_now=True)

	def __str__(self):
		return self.name

class Session(models.Model):
	time = models.DateTimeField()
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return f"Time start session - {self.time} Movie - {self.movie}"

class Ticket(models.Model):
	user = models.ForeignKey(User, related_name='payTicket', on_delete=models.CASCADE, null=True)
	session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True)
	seat = models.ForeignKey('Seat', on_delete=models.CASCADE, null=True, blank=True)
	typeticket = models.ForeignKey('TypeTicket', related_name='ticket', on_delete=models.CASCADE, null=True, blank=True)
	book = models.ForeignKey('Book', related_name='ticketbook', on_delete=models.SET_NULL, null=True)
	room = models.ForeignKey('Room', on_delete=models.CASCADE, null=True )

		

	
class TypeTicket(models.Model):
	type_name = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=7, decimal_places=2, null=True)

	def __str__(self):
		return f"Type - {self.type_name} Price - {self.price}"


class Book(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	order = models.IntegerField(null=True, blank=True)

	def __str__(self):
		return f"Booking - {self.user} | Order #{self.order}" 


class Seat(models.Model):
	row = models.CharField(max_length=255)
	place = models.CharField(max_length=255)
	room = models.ForeignKey('Room', on_delete=models.CASCADE, related_name='seats', null=True)

	def __str__(self):
		return f"Ряд - {self.row} Место - {self.place} "



class Room(models.Model):
	name = models.CharField(max_length=255)
	cinema = models.ForeignKey('Cinema', on_delete=models.CASCADE, related_name='room', null=True)
	session = models.ForeignKey(Session,related_name='session_room', on_delete=models.CASCADE, null=True)

	def __str__(self):
		return f"Room - {self.name} | Session - {self.session}"


