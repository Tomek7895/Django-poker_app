# Generated by Django 2.1.5 on 2022-09-08 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0007_auto_20220908_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='cash_games',
            name='game_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tournaments.Game_Type'),
        ),
    ]
