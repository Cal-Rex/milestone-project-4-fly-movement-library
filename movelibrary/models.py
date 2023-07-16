from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Movement(models.Model):
    movement_name = models.CharField(max_length=200, unique=True)
    vid_link = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    directions = models.TextField(default="")
    bookmarks = models.ManyToManyField(
        User, related_name='bookmarks', blank=True
        )
    thumbnail = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.movement_name}"


class PromoVideo(models.Model):
    promo_name = models.CharField(max_length=200, unique=True)
    vid_link = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)


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
    one_rm = models.BooleanField(default=False)


class UserNonAuthField(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    terms = models.BooleanField(default=False)
    last_movement = models.SlugField(max_length=200, unique=False)


class UserMovementNotes(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    movement = models.ForeignKey(Movement, on_delete=models.CASCADE)
    movement_notes = models.TextField(default="")


class UserOneRepMax(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    movement = models.ForeignKey(Movement, on_delete=models.CASCADE, related_name="one_rm_list")
    one_rep_max = models.IntegerField(unique=False)
    date_recorded = models.DateTimeField(auto_now_add=True)

    class meta:
        ordering = ['date_recorded']

        def __str__(self):
            return f"{self.one_rep_max}KG | recorded on {self.date_recorded}"


class SocialMediaCard(models.Model):
    name = models.CharField(max_length=200, unique=True)
    thumbnail = models.CharField(max_length=200, unique=True)
