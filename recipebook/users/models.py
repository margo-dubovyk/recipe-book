from django.contrib.auth.models import AbstractUser
from django.db import models


class BotAdmin(AbstractUser):
    username = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.username


class BotUser(models.Model):
    tg_id = models.PositiveBigIntegerField(primary_key=True)  # telegram id
    username = models.CharField(max_length=256, unique=True)
    chosen_name = models.CharField(max_length=256)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    state = models.IntegerField()

    gender_choices = (
        ('f', 'Female'),
        ('m', 'Male'),
        ('o', 'Other'),
    )

    gender = models.CharField(max_length=1, choices=gender_choices)

    def __str__(self):
        return self.username

    def gender_verbose(self):
        return dict(BotUser.gender_choices)[self.gender]
