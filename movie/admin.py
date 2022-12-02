from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import *

admin.site.register(Room)
admin.site.register(Seat)
admin.site.register(Cinema)
admin.site.register(Ticket)
admin.site.register(TypeTicket)
admin.site.register(Book)
admin.site.register(Session)
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(User)