# Generated by Django 4.2.2 on 2023-07-14 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movelibrary', '0002_movement_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('thumbnail', models.CharField(max_length=200, unique=True)),
            ],
        ),
    ]