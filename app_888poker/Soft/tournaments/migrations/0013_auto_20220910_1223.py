# Generated by Django 2.1.5 on 2022-09-10 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0012_spin_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournaments',
            name='date',
            field=models.DateTimeField(blank=True),
        ),
    ]
