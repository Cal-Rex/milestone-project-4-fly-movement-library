from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Movement(models.Model):
    movement_name = models.CharField(max_length=200, unique=True)
    vid_link = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    bookmarks = models.ManyToManyField(
        User, related_name='bookmarks', blank=True
        )

    def __str__(self):
        return f"{self.movement_name}"


class Tag(models.Model):
    movement = models.ForeignKey(Movement, on_delete=models.CASCADE,)
    upper_body = models.BooleanField(default=False)
    lower_body = models.BooleanField(default=False)
    barbell = models.BooleanField(default=False)
    dumbbell = models.BooleanField(default=False)
    kettlebell = models.BooleanField(default=False)
    olympic = models.BooleanField(default=False)
    power = models.BooleanField(default=False)
    strength = models.BooleanField(default=False)
    arms = models.BooleanField(default=False)
    chest = models.BooleanField(default=False)
    shoulders = models.BooleanField(default=False)
    back = models.BooleanField(default=False)
