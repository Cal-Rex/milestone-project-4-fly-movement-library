# Generated by Django 4.2.2 on 2023-06-23 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movelibrary', '0011_useronerepmax_movement_squashed_0012_remove_useronerepmax_movement'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserOneRepMax',
        ),
    ]