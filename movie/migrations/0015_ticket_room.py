# Generated by Django 4.1.3 on 2022-11-23 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0014_seat_room_alter_room_session"),
    ]

    operations = [
        migrations.AddField(
            model_name="ticket",
            name="room",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="movie.room"
            ),
        ),
    ]