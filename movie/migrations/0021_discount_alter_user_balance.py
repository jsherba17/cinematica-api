# Generated by Django 4.1.3 on 2022-11-28 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0020_user_last_login_alter_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]
