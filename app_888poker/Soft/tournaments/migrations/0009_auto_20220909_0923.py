# Generated by Django 2.1.5 on 2022-09-09 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0008_cash_games_game_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cash_games',
            options={'verbose_name': 'Cash_Games', 'verbose_name_plural': 'Cash_Games'},
        ),
    ]