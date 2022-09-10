# Generated by Django 2.1.5 on 2022-09-08 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0005_auto_20220908_1007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cash_Games',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prices', models.DecimalField(decimal_places=2, max_digits=12)),
                ('players', models.IntegerField(blank=True, null=True)),
                ('min_buy_in', models.DecimalField(decimal_places=2, max_digits=12)),
                ('max_buy_in', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
    ]