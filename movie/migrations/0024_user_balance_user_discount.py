# Generated by Django 4.1.3 on 2022-11-28 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0023_remove_user_balance_remove_user_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='balance',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='discount',
            field=models.IntegerField(default=0),
        ),
    ]
