# Generated by Django 2.1.5 on 2022-09-08 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0002_auto_20220907_0921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
