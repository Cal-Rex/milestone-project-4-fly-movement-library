# Generated by Django 4.2.2 on 2023-07-12 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movelibrary', '0019_usernonauthfield'),
    ]

    operations = [
        migrations.CreateModel(
            name='PromoVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promo_name', models.CharField(max_length=200, unique=True)),
                ('vid_link', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
    ]
