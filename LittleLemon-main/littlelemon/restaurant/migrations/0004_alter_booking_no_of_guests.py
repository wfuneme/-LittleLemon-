# Generated by Django 5.1.2 on 2024-11-15 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_booking_no_of_guests_alter_menu_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='no_of_guests',
            field=models.PositiveIntegerField(),
        ),
    ]