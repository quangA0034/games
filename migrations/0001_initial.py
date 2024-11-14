# Generated by Django 5.1.3 on 2024-11-11 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardGameLibrary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boardgame_name', models.CharField(max_length=100)),
                ('owner_name', models.CharField(max_length=100)),
                ('min_players', models.IntegerField()),
                ('max_players', models.IntegerField()),
                ('available', models.BooleanField(default=True, help_text='Mark if the board game is available to borrow')),
            ],
        ),
        migrations.CreateModel(
            name='BoardGameRental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boardgame_name', models.CharField(max_length=100)),
                ('owner_name', models.CharField(max_length=100)),
                ('min_players', models.IntegerField()),
                ('max_players', models.IntegerField()),
                ('available', models.BooleanField(default=True, help_text='Mark if the board game is available to borrow')),
            ],
        ),
    ]
