# Generated by Django 4.2.2 on 2023-07-11 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movelibrary', '0018_delete_usernonauthfield'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserNonAuthField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terms', models.BooleanField(default=False)),
                ('last_movement', models.SlugField(max_length=200, unique=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
