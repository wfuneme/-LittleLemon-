# Generated by Django 5.1.2 on 2024-11-13 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='no_of_guests',
            field=models.SmallIntegerField(max_length=6),
        ),
        migrations.AlterField(
            model_name='menu',
            name='inventory',
            field=models.SmallIntegerField(max_length=5),
        ),
    ]
