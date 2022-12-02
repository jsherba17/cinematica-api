from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import *

class UserSerializer(serializers.ModelSerializer):
	balance = serializers.SerializerMethodField()
	discount = serializers.SerializerMethodField()
	class Meta:
		model = User
		fields = 'id','balance','first_name','last_name','username','password','phone','discount'

	def get_balance(self, obj):
		tickets = Ticket.objects.filter(user=obj)
		balance = 0
		for ticket in tickets:
			balance += ticket.typeticket.price
		user = User.objects.get(id=obj.id)
		user.balance = balance
		user.save()
		return balance

	def get_discount(self, obj):
		discount_tickets = TypeTicket.objects.all()
		discount = 0
		user = User.objects.get(id=obj.id)
		if user.balance > 1000.0 and user.balance < 2500.0:
			discount = 3
		elif user.balance > 2500.0 and user.balance < 5000.0:
			discount = 5
		elif user.balance > 5000.0 and user.balance < 10000.0:
			discount = 7
		elif user.balance > 10000.0 and user.balance < 15000.0:
			discount = 10
		user.discount = discount
		user.save()
		
		return discount
	
	def create(self, validated_data):
		user = User.objects.create(
			username=validated_data['username'],
			first_name=validated_data['first_name'],
			last_name=validated_data['last_name']
		)

		user.set_password(validated_data['password'])
		user.save()

		return user

class RegisterSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
	password2 = serializers.CharField(write_only=True, required=True)

	class Meta:
		model = User
		fields = ('username', 'password', 'password2', 'first_name', 'last_name')
		extra_kwargs = {
			'first_name': {'required': True},
			'last_name': {'required': True}
		}

	def validate(self, attrs):
		if attrs['password'] != attrs['password2']:
			raise serializers.ValidationError({"password": "Password fields didn't match."})

		return attrs

	def create(self, validated_data):
		user = User.objects.create(
			username=validated_data['username'],
			first_name=validated_data['first_name'],
			last_name=validated_data['last_name']
		)

		user.set_password(validated_data['password'])
		user.save()

		return user
			
class UserTicket(UserSerializer):
	class Meta(UserSerializer.Meta):
		fields = 'first_name',

class GenreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Genre
		fields = ['film_genre']


class GenreMovie(GenreSerializer):
	class Meta(GenreSerializer.Meta):
		fields = ['movies']


class MovieSerializer(serializers.ModelSerializer):
	genres = GenreSerializer(many=True)

	class Meta:
		model = Movie
		fields = 'id','name','description', 'year', 'genres', 'country',

	def get_or_create_packages(self, packages):
		package_ids = []
		for package in packages:
			genre_instance, _ = Genre.objects.get_or_create(film_genre=package.get('film_genre'))
			package_ids.append(genre_instance.id)
		return package_ids

	def create(self, validated_data):
		package = validated_data.pop('genres', [])
		order = Movie.objects.create(**validated_data)
		order.genres.set(self.get_or_create_packages(package))
		return order

	def update(self, instance, validated_data):
		genres_data = validated_data.pop('genres', instance.genres)
		instance.genres.set(self.get_or_create_packages(genres_data))
		instance.save()

		return instance


class MovieTicket(MovieSerializer):
	class Meta(MovieSerializer.Meta):
		fields = 'name','genres'


class MovieSession(MovieSerializer):
	class Meta(MovieSerializer.Meta):
		fields = 'name',

class MovieCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movie
		fields = 'name', 'description','year','genres','country'


class SessionSerializer(serializers.ModelSerializer):
	movie = MovieSession()
	class Meta:
		model = Session
		fields = 'movie', 'time',


class SessionTicket(SessionSerializer):
	class Meta(SessionSerializer.Meta):
		fields = 'movie', 'time'

class SessionCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Session
		fields = 'movie', 'time',



class RoomSerializer(serializers.ModelSerializer):
	session = SessionTicket()
	class Meta:
		model = Room
		fields = ['id','name','cinema', 'session']


class RoomTicket(RoomSerializer):
	class Meta(RoomSerializer.Meta):
		fields = 'name', 'session'


class RoomCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Room
		fields = ['id', 'name','cinema', 'session',]


class SeatSerializer(serializers.ModelSerializer):

	class Meta:
		model = Seat
		fields = 'row', 'place'


class SeatCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Seat
		fields = ['row', 'place']

class TypeTicketSerializer(serializers.ModelSerializer):
	class Meta:
		model = TypeTicket
		fields = 'type_name', 'price'


class TicketSerializer(serializers.ModelSerializer):
	user = UserTicket()
	typeticket = TypeTicketSerializer(many=False)
	seat = SeatSerializer(many=False)
	
	class Meta:
		model = Ticket
		fields = 'id','user', 'room', 'typeticket','seat',


class TicketCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ticket
		fields = 'user','seat', 'typeticket', 'book','room',


class BookSerializer(serializers.ModelSerializer):
	ticketbook = TicketSerializer(many=True)
	total_price = serializers.SerializerMethodField()

	class Meta:
		model = Book
		fields = 'order','ticketbook','total_price'

	def get_total_price(self, obj):
		user = User.objects.get(id=obj.user.id)
		tickets = Ticket.objects.filter(book=obj)
		total_price = 0
		for ticket in tickets:
			total_price += ticket.typeticket.price
		total_price = total_price - (total_price / 100 * user.discount)
		return total_price


class BookCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = '__all__'

class BookTicket(BookSerializer):
	class Meta(BookSerializer.Meta):
		fields = 'total_price'


class CinemaSerializer(serializers.ModelSerializer):
	room = serializers.StringRelatedField(many=True)

	class Meta:
		model = Cinema
		fields = ['id','title', 'description', 'schedule', 'address', 'contacts', 'room']



# from rest_framework import serializers
# from django.contrib.auth.models import User
# from rest_framework.validators import UniqueValidator
# from django.contrib.auth.password_validation import validate_password


# class RegisterSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(
#             required=True,
#             validators=[UniqueValidator(queryset=User.objects.all())]
#             )

#     password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
#     password2 = serializers.CharField(write_only=True, required=True)

#     class Meta:
#         model = User
#         fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
#         extra_kwargs = {
#             'first_name': {'required': True},
#             'last_name': {'required': True}
#         }

#     def validate(self, attrs):
#         if attrs['password'] != attrs['password2']:
#             raise serializers.ValidationError({"password": "Password fields didn't match."})

#         return attrs

#     def create(self, validated_data):
#         user = User.objects.create(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last_name']
#         )

		
#         user.set_password(validated_data['password'])
#         user.save()

#         return user
