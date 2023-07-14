# Generated by Django 4.2.2 on 2023-07-14 08:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movement_name', models.CharField(max_length=200, unique=True)),
                ('vid_link', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('directions', models.TextField(default='')),
                ('bookmarks', models.ManyToManyField(blank=True, related_name='bookmarks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PromoVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promo_name', models.CharField(max_length=200, unique=True)),
                ('vid_link', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserOneRepMax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_rep_max', models.IntegerField()),
                ('date_recorded', models.DateTimeField(auto_now_add=True)),
                ('movement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='one_rm_list', to='movelibrary.movement')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserNonAuthField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terms', models.BooleanField(default=False)),
                ('last_movement', models.SlugField(max_length=200, unique=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserMovementNotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movement_notes', models.TextField(default='')),
                ('movement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movelibrary.movement')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upper_body', models.BooleanField(default=False)),
                ('lower_body', models.BooleanField(default=False)),
                ('barbell', models.BooleanField(default=False)),
                ('dumbbell', models.BooleanField(default=False)),
                ('kettlebell', models.BooleanField(default=False)),
                ('olympic', models.BooleanField(default=False)),
                ('power', models.BooleanField(default=False)),
                ('strength', models.BooleanField(default=False)),
                ('arms', models.BooleanField(default=False)),
                ('chest', models.BooleanField(default=False)),
                ('shoulders', models.BooleanField(default=False)),
                ('back', models.BooleanField(default=False)),
                ('one_rm', models.BooleanField(default=False)),
                ('movement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movelibrary.movement')),
            ],
        ),
    ]
