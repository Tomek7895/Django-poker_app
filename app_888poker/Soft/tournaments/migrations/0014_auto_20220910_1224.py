# Generated by Django 2.1.5 on 2022-09-10 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0013_auto_20220910_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournaments',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
