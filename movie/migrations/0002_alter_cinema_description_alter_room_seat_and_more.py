# Generated by Django 4.1.3 on 2022-11-21 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cinema",
            name="description",
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name="room",
            name="seat",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rooms",
                to="movie.seat",
            ),
        ),
        migrations.AlterField(
            model_name="seat",
            name="place",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="seat",
            name="row",
            field=models.CharField(max_length=255),
        ),
    ]
